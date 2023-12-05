import sys
import matplotlib.pyplot as plt

#adding shared volume to path
sys.path.insert(1, '/storage')

#dictionary which allows analysis to read in each file by name
samples = {

    'data': {
        'list' : ['data_A','data_B','data_C','data_D'],
    },


   r'Background $Z,t\bar{t}$' : { # Z + ttbar
       'list' : ['Zee','Zmumu','ttbar_lep'],
        'color' : "#6b59d3" # purple
    },


    r'Background $ZZ^*$' : { # ZZ
        'list' : ['llll'],
        'color' : "#ff0000" # red
    },

    r'Signal ($m_H$ = 125 GeV)' : { # H -> ZZ -> llll
        'list' : ['ggH125_ZZ4lep','VBFH125_ZZ4lep','WH125_ZZ4lep','ZH125_ZZ4lep'],
        'color' : "#00cdff" # light blue
    },

}

#iterate through samples keys
for i in range(len(list(samples.items()))):
    #make a file to store each value and key
    fname = 'storage/generated'+str(i)+'.py'
    #slice the dictionary for relevant part
    data = dict(list(samples.items())[i: i+1]) 
    #write to file in shared directory
    with open(fname, 'w') as f:
        f.write('data = {}'.format(data))
#
# 
#fname = 'storage/generated0.py'
#data = dict(list(samples.items())) 
#with open(fname, 'w') as f:
 #   f.write('data = {}'.format(data))