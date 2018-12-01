# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:25:37 2018

@author: nittin pc
"""

import pickle
import random

import msvcrt
f = open(r'frank_whole.pkl','rb')
dict1 = pickle.load(f)
f.close()
dictionary = {}
for items in dict1.items():
    dictionary[tuple(set(items[0].split(' AND ')))] = items[1]
#### K means for the dictionary
# no of clusters
N = 30
queries  = []
for item in dictionary.items():
    queries = queries + list(item[0])
    
queries = list(set(queries))

# choosing initial N random centers

initial_centers = [queries[x] for x in random.sample(range(0,len(queries)),N)]
clusters_with_center = {}
for x in initial_centers:
    clusters_with_center[x] = []   

print('Clusters Initiated')
# no of iterations for k means
max_iterations = 100    
centers = initial_centers
counter = 0
while(True):
    counter = counter + 1
    
    #queries = list(set(queries)-set(centers))
    while (True):
        for factoid in queries:
            distance = []
            flag = False
            for cents in centers:
                if ((tuple(set([factoid,cents]))) in [x[0] for x in dictionary.items()]):
                    distance.append(dictionary[tuple(set([factoid,cents]))])
                    flag = True
            if(not distance):
                print('Empty Neighbourhood')
            if flag :
                clusters_with_center[centers[distance.index(min(distance))]].append(factoid)
                        
#        for n in centers:
#            print('Center*****',n, clusters_with_center[n] )    
        p = 0               
        for n in clusters_with_center:
            if n[1]:
                p+=1
        print('No of groups ',p) 
        break
#        if p == N:
#            break
#        else: # for recentering the new centers
#            print('Recentering!!')
#            centers = [queries[x] for x in random.sample(range(0,len(queries)),N)]
#            clusters_with_center = {}
#            for x in centers:
#                clusters_with_center[x] = [] 
            
    
    clusters = []
    #ch = input()
    #type(ch)
    for items in clusters_with_center.items():
        clusters.append(list(set([items[0]]).union(set(items[1]))))
    new_centers = []
    for items in clusters:
        arr =[]
        for x in items:
            summ = 0
            for y in items:
                if ((tuple(set([x,y]))) in [it[0] for it in dictionary.items()]):
                    summ += abs(dictionary[tuple(set([x,y]))])
        arr.append(summ) 
        new_centers.append(items[arr.index(min(arr))])
        #new_centers.append(items[arr.index(min([sum([abs(dictionary[tuple(set([x,y]))]) for y in items]) for x in items]))])
    if (centers == new_centers or counter >= max_iterations ):
        print('Current Centers', new_centers)
        if (counter == max_iterations):
            print('Unable to converge')
            break
        print('After ',counter,' iterations, clusters converged!')
        break
    else :
        clusters_with_center = {}
        for x in new_centers:
            clusters_with_center[x] = []   
        centers = new_centers
