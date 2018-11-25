# -*- coding: utf-8 -*-

import pickle as pkl
import math
import matplotlib.pyplot as plt
import numpy as np
article_fb='Frank_Bladin'
article_alt='Altenburg'
article_ace='Ace_Books'

st=article_fb

wd='F:/semester_notes/4th year/1st sem/csl622/project/wikipedia articles mail/'
with open(wd+st+'/'+st+'_NGD_40.pkl', "rb") as input_file:
    e = pkl.load(input_file)
    

file=open(wd+st+'/'+st+'_LSA_40.txt','r')

dict2={}
for line in file:
    pair=line.rstrip('\n').split(' AND ')
    val=pair[1].split(' ')
    val1=val[-1]
    val=' '.join(val[0:-1])
    strr=pair[0]+' AND '+val
    if(val1!='nan' and strr in e):
        dict2[strr]=float(val1)
        
file.close()
dict1={}
for pair in e.items():
    if(not math.isnan(pair[1]) and pair[0] in dict2):
        dict1[pair[0]]=pair[1]
        

x=[pair[1] for pair in dict1.items()]

y=[dict2[pair[0]] for pair in dict1.items()]

pcc=-np.corrcoef(x, y)[0,1]
print(pcc)

plt.plot(x,y,'.')