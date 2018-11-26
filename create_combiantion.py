# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:32:08 2018

@author: nittin pc

"""
import itertools
f = open(r'LIST_OF_SERACH_PHRASES.txt','r')

lis  = [x.rstrip('\n') for x in f]

f.close()
new_pairs = []

for p in itertools.combinations(lis,2):
    new_pairs.append(p[0]+' AND '+p[1])
    
f =open(r'pairs.txt','w')
    
for r in new_pairs:
    f.write('%s\n'%r)
f.close()