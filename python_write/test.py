import sys
import matplotlib.pyplot as plt
sys.path.insert(1, '/storage')

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

#print(dict(list(samples.items())[1: 2]))

##fname = 'storage/generated.py'
#data = dict(list(samples.items())[1: 2]) 

#with open(fname, 'w') as f:
    #f.write('data = {}'.format(data))

for i in range(len(list(samples.items()))):
    fname = 'storage/generated'+str(i)+'.py'
    data = dict(list(samples.items())[i: i+1]) 
    with open(fname, 'w') as f:
        f.write('data = {}'.format(data))
#
# 
#fname = 'storage/generated0.py'
#data = dict(list(samples.items())) 
#with open(fname, 'w') as f:
 #   f.write('data = {}'.format(data))