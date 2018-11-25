# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:51:54 2018

@author: Narotam
"""

files=['1.txt','2.txt','3.txt','4.txt','5.txt','6.txt','7.txt','8.txt','9.txt','10.txt','11.txt']
a=set()
for filename in files:
    with open(filename,'r',encoding='utf8') as out:    
        for line in out:
            a.add(line)
            
a=set(i.lower() for i in a)

with open('final.txt','w',encoding='utf-8') as out:
    for b in a:
        out.write(b)
        
import itertools
file=open('final.txt','r',encoding='utf-8')
lines=[line.strip('\n') for line in file]
#lines=lines[-40:]
file.close()
file=open('all_pairs_Ace_Books.txt','w',encoding='utf-8')
i=0
#for line in lines:
#    file.write('%s\n'%line)
for pair in itertools.combinations(lines,2):
    strng = ' AND '.join(pair)
    i=i+1
    file.write('%s\n'% strng)
file.close()