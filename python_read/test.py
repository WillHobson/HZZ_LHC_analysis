import uproot # for reading .root files
import awkward as ak # to represent nested data in columnar format
import vector # for 4-momentum calculations
import time # to measure time to analyse
import math # for mathematical functions such as square root
import numpy as np # for numerical calculations such as histogramming
import matplotlib.pyplot as plt # for plotting
from matplotlib.ticker import AutoMinorLocator # for minor ticks
import sys
import infofile
import os
import pickle

#function that checks how many files to analyse there are in volume
def check_file_count():
    files = []
    for file in os.listdir('storage/'):
        if file.startswith('generated'):
            files.append(file)
    return len(files)

#add path to retrieve files from volume
sys.path.insert(1,'/storage')

#find all the files that store generated data to read and analyse
files = []
for file in os.listdir('storage/'):
    if file.startswith('generated'):
        files.append(file)



#if there exists data, proceed with analysing
while check_file_count()>0:

    #find all files for analysing
    files = []
    for file in os.listdir('storage/'):
        if file.startswith('generated'):
            files.append(file)
            
    #find the index of the generated files
    index=[]
    for i in files:
        x = int(i.split('d')[1].split('.')[0])
        index.append(x)

    #choose to analyse the file with the lowest index
    filetouse = np.min(index)
    filetouse = f'generated'+str(filetouse)
    filetodelete = 'storage/'+filetouse+'.py'

    #showing which file will be analysed
    print(f'USING{filetouse}')

    #import the data to read and analyse from file in volume       
    mod = __import__(filetouse)
    samples = mod.data

    #remove the file being analysed so it is not done again
    os.remove(filetodelete)


    #lumi = 0.5 # fb-1 # data_A only
    #lumi = 1.9 # fb-1 # data_B only
    #lumi = 2.9 # fb-1 # data_C only
    #lumi = 4.7 # fb-1 # data_D only
    lumi = 10 # fb-1 # data_A,data_B,data_C,data_D

    fraction = 0.5 # reduce this is if you want the code to run quicker
                                                                                                                                    
    #tuple_path = "Input/4lep/" # local 
    tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/" # web address
    MeV = 0.001
    GeV = 1.0

    def calc_weight(xsec_weight, events):
        return (
            xsec_weight
            * events.mcWeight
            * events.scaleFactor_PILEUP
            * events.scaleFactor_ELE
            * events.scaleFactor_MUON 
            * events.scaleFactor_LepTRIGGER
        )
    def get_xsec_weight(sample):
        info = infofile.infos[sample] # open infofile
        xsec_weight = (lumi*1000*info["xsec"])/(info["sumw"]*info["red_eff"]) #*1000 to go from fb-1 to pb-1
        return xsec_weight # return cross-section weight

    def calc_mllll(lep_pt, lep_eta, lep_phi, lep_E):
        # construct awkward 4-vector array
        p4 = vector.zip({"pt": lep_pt, "eta": lep_eta, "phi": lep_phi, "E": lep_E})
        # calculate invariant mass of first 4 leptons
        # [:, i] selects the i-th lepton in each event
        # .M calculates the invariant mass
        return (p4[:, 0] + p4[:, 1] + p4[:, 2] + p4[:, 3]).M * MeV


    # cut on lepton charge
    # paper: "selecting two pairs of isolated leptons, each of which is comprised of two leptons with the same flavour and opposite charge"
    def cut_lep_charge(lep_charge):
    # throw away when sum of lepton charges is not equal to 0
    # first lepton in each event is [:, 0], 2nd lepton is [:, 1] etc
        return lep_charge[:, 0] + lep_charge[:, 1] + lep_charge[:, 2] + lep_charge[:, 3] != 0

    # cut on lepton type
    # paper: "selecting two pairs of isolated leptons, each of which is comprised of two leptons with the same flavour and opposite charge"
    def cut_lep_type(lep_type):
    # for an electron lep_type is 11
    # for a muon lep_type is 13
    # throw away when none of eeee, mumumumu, eemumu
        sum_lep_type = lep_type[:, 0] + lep_type[:, 1] + lep_type[:, 2] + lep_type[:, 3]
        return (sum_lep_type != 44) & (sum_lep_type != 48) & (sum_lep_type != 52)

    def read_file(path,sample):
        start = time.time() # start the clock
        print("\tProcessing: "+sample) # print which sample is being processed
        data_all = [] # define empty list to hold all data for this sample
        
        # open the tree called mini using a context manager (will automatically close files/resources)
        with uproot.open(path + ":mini") as tree:
            numevents = tree.num_entries # number of events
            if 'data' not in sample: xsec_weight = get_xsec_weight(sample) # get cross-section weight
            for data in tree.iterate(['lep_pt','lep_eta','lep_phi',
                                    'lep_E','lep_charge','lep_type', 
                                    # add more variables here if you make cuts on them 
                                    'mcWeight','scaleFactor_PILEUP',
                                    'scaleFactor_ELE','scaleFactor_MUON',
                                    'scaleFactor_LepTRIGGER'], # variables to calculate Monte Carlo weight
                                    library="ak", # choose output type as awkward array
                                    entry_stop=numevents*fraction): # process up to numevents*fraction

                nIn = len(data) # number of events in this batch

                if 'data' not in sample: # only do this for Monte Carlo simulation files
                    # multiply all Monte Carlo weights and scale factors together to give total weight
                    data['totalWeight'] = calc_weight(xsec_weight, data)

                # cut on lepton charge using the function cut_lep_charge defined above
                data = data[~cut_lep_charge(data.lep_charge)]

                # cut on lepton type using the function cut_lep_type defined above
                data = data[~cut_lep_type(data.lep_type)]

                # calculation of 4-lepton invariant mass using the function calc_mllll defined above
                data['mllll'] = calc_mllll(data.lep_pt, data.lep_eta, data.lep_phi, data.lep_E)

                # array contents can be printed at any stage like this
                #print(data)

                # array column can be printed at any stage like this
                #print(data['lep_pt'])

                # multiple array columns can be printed at any stage like this
                #print(data[['lep_pt','lep_eta']])

                nOut = len(data) # number of events passing cuts in this batch
                data_all.append(data) # append array from this batch
                elapsed = time.time() - start # time taken to process
                print("\t\t nIn: "+str(nIn)+",\t nOut: \t"+str(nOut)+"\t in "+str(round(elapsed,1))+"s") # events before and after
        
        return ak.concatenate(data_all) # return array containing events passing all cuts

    def get_data_from_file(todo):

        data = {} # define empty dictionary to hold awkward arrays
        for s in todo: # loop over samples
            print(f's=={s}')
            frames = [] # define empty list to hold data
            if s == 'data': prefix = "Data/" # Data prefix
            else: # MC prefix
                    prefix = "MC/mc_"+str(infofile.infos[list(todo.values())[0]]["DSID"])+"."
            fileString = tuple_path+prefix+list(todo.values())[0]+".4lep.root"
            temp = read_file(fileString,list(todo.values())[0]) # call the function read_file defined below
            frames.append(temp) # append array returned from read_file to list of awkward arrays
            data[s] = ak.concatenate(frames)

        return data # return dictionary of awkward arrays

    start = time.time() # time at start of whole processing
    data = get_data_from_file(samples) # process all files
    elapsed = time.time() - start # time after whole processing
    print("Time taken: "+str(round(elapsed,1))+"s") # print total time taken to process every file

    print('great success')

    #write the awkward array to a file named answer+index.py
    fname = 'storage/answer'+str(np.min(index))+'.py'
    with open(fname, 'wb') as f:
        pickle.dump(data, f)
        