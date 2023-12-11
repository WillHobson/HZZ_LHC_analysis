import sys
import matplotlib.pyplot as plt

#adding shared volume to path
sys.path.insert(1, '/storage')

#dictionary which allows analysis to read in each file by name
samples2 = {'data': {'list' : ['data_A','data_B','data_C','data_D']}}
samples3 = {r'Background $Z,t\bar{t}$' : { # Z + ttbar
        'list' : ['Zee','Zmumu','ttbar_lep'],
        'color' : "#6b59d3" # purple
    }}
samples4 = {    r'Background $ZZ^*$' : { # ZZ
        'list' : ['llll'],
        'color' : "#ff0000" # red
    }}

samples5 = {r'Signal ($m_H$ = 125 GeV)' : { # H -> ZZ -> llll
        'list' : ['ggH125_ZZ4lep','VBFH125_ZZ4lep','WH125_ZZ4lep','ZH125_ZZ4lep'],
        'color' : "#00cdff" # light blue
    }}
individ_2 = []
for i in range(len(samples2['data']['list'])):
    individ_2.append(dict({'data':samples2['data']['list'][i]}))

individ_3 = []
key = list(samples3.keys())[0]
for i in range(len(samples3[key]['list'])):
    individ_3.append(dict({key:samples3[key]['list'][i]}))

individ_4 = []
key = list(samples4.keys())[0]
for i in range(len(samples4[key]['list'])):
    individ_4.append(dict({key:samples4[key]['list'][i]}))

individ_5 = []
key = list(samples5.keys())[0]
for i in range(len(samples5[key]['list'])):
    individ_5.append(dict({key:samples5[key]['list'][i]}))

files_to_do = [individ_2,individ_3,individ_4,individ_5]




# #iterate through samples keys
# for i in range(len(list(samples.items()))):
#     #make a file to store each value and key
#     fname = 'storage/generated'+str(i)+'.py'
#     #slice the dictionary for relevant part
#     data = dict(list(samples.items())[i: i+1]) 
#     #write to file in shared directory
#     with open(fname, 'w') as f:
#         f.write('data = {}'.format(data))
print('HERE!!!!!!')
count = 0
for i in range(4):
    for j in range(len(files_to_do[i])):
        fname = 'storage/generated'+str(count)+'.py'
        data = files_to_do[i][j]
        with open(fname, 'w') as f:
                f.write('data = {}'.format(data))
        print(f'just written {fname} to volume')
        count+=1
#
# 
#fname = 'storage/generated0.py'
#data = dict(list(samples.items())) 
#with open(fname, 'w') as f:
 #   f.write('data = {}'.format(data))