# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:24:54 2018

@author: nittin pc
"""
import requests
import json
import pickle
import numpy
import  sys 

api_key = ['AIzaSyCaJbAelOedWC8f4lk17gPanog5_YTXDyA',
'AIzaSyA9iMKZwrGSELu66ZAjwn9fVJcvluekrQo',
'AIzaSyAW2RGeDJWdRWwGz5RuXm8LzK7Kbndr2rc',
'AIzaSyCL1OO8neD-VHqPH7-60IgQwv3ODg2NZwE',
'AIzaSyAycDSbkYMF3pMLfisD1u65Nr32oNxeMYU',
'AIzaSyAO5mXyhJjCT9pU2fi213-qA964a75AZEw',
'AIzaSyCCaNbuRJWtNJz0FYx7R2GsYh-6lNjjCgY',
'AIzaSyCP1DXm9lxihlq4Gk5qtb_1f5gULQddxWI',
'AIzaSyA6vLcGvbUD6CGMWqQSe1vQ8EhZUl12kDg',
'AIzaSyBn6GJyLEJx0jrkeYZjWFcD5v8Oo47xNfQ',
'AIzaSyCyWBodfdxauqMVGsxE74ABMq1ddXps_H0',
'AIzaSyCd5D0aU7UtWcjbyc0X1Yry15dmzJXdpLY',
'AIzaSyDgeE2D01JTMDBcgGtoEemjfw61FIGOHcI',
'AIzaSyDQErebV11rNq26pm1zryP9Qob3rHcTPDw',
'AIzaSyD4EPfyueJOmn2FjO_W01Wp1rIV_-PrVGQ',
'AIzaSyCVqPFhUzunrPzmxnjmecHwg9j_8IpDNnU',
'AIzaSyDSUPY_K5h9yYCfuy0-MBJRC7RM5qa5A6w',
'AIzaSyAvFkfQFr738jzNa4yKjNxYeB1MVSd9Qvk',
'AIzaSyBmZ4CCKj5dqphHXIfTTwvlA04SMPDnQDI',
'AIzaSyDpRNMLTHQDuyUaOme1Pb-2WmiGyJkdLZ8',
'AIzaSyCSKFktA4ZP7IjvtG_DVwhq99Vog2q1fdg',
'AIzaSyD7muOwHdHq0VtcmHl30-R4k3H3ncNA2tk',
'AIzaSyAmC0ZA9ygaE1yAyxVCDVWAieYg7RMLUNE',
'AIzaSyBHhl1kj90iY7uocKlbFQf_MKZ6_gmxm_E',
'AIzaSyDwiCToVx2FzrmhOXoJ1VcCof4h__GBswo',
'AIzaSyCeojpsPVJNO3DHfjfY4Ba7n9jAImrpVHA',
'AIzaSyB4jHAkg19FDTDsbrbJWB6aByT8kBuA-xU',
'AIzaSyB4jHAkg19FDTDsbrbJWB6aByT8kBuA-xU',
'AIzaSyD-CKJyqWXpamvJB_eN8KisaSd0J2nNINI',
'AIzaSyDPcxEWZmH-C4EAWwa2oUzSKMJtIUBUjqs',
'AIzaSyCbhsTO7k8fcgWUNe5LCz6U1cWat9Qc1oc']
# the list contains all the API keys

c_id = '013458429740006344042:-qhtvauob0s'
#custom search engine ID 
file = open(r'SAMPLE_FILE.txt','r')
# takes input the file name where pairs are written 
pairs = []
for line in file:
    if('AND' in line):
        line = line.rstrip('\n')
        s = line.split(' AND ')
        pairs.append(s)
        
file.close()
k = 0
print('Using App no', k)
file = open(r'single_count_results.txt','w')
queries = set([x[0] for x in pairs])
queries = queries.union(set([x[1] for x in pairs]))
queries = list(queries)
query1_results = {}
for query1 in queries:
    if k >= len(api_key):
        print("Keys Exhausted")
        sys.exit(1)
    url = 'https://www.googleapis.com/customsearch/v1?key='+api_key[k]+'&cx='+c_id+'&q='+query1
    response = requests.get(url)
    if (response.ok):
        jData = json.loads(response.content)
        query1_results[query1] = jData['queries']['request'][0]['totalResults']
        s = query1+' '+  query1_results[query1] 
        file.write('%s\n' % s)
    else:
        print('Not good response')
        k = k+1
        print('Using App no', k)
        while k < len(api_key):
            url = 'https://www.googleapis.com/customsearch/v1?key='+api_key[k]+'&cx='+c_id+'&q='+query1
            response = requests.get(url)
            if (response.ok):
                jData = json.loads(response.content)
                query1_results[query1] = jData['queries']['request'][0]['totalResults']
                s = query1+' '+  query1_results[query1] 
                file.write('%s\n' % s)
                break
            k=k+1
    

file.close()      
         
print('finding for pairs')  
       
file = open(r'pairs_count_results.txt','w')
joined_results = {}        
for query in pairs: 
    if k >= len(api_key):
        print("Keys Exhausted")
        file.close()
        sys.exit(1)    
    url = 'https://www.googleapis.com/customsearch/v1?key='+api_key[k]+'&cx='+c_id+'&q='+query[0]+' AND '+query[1]
    response = requests.get(url)
    if (response.ok):
        jData = json.loads(response.content)
        joined_results[query[0]+' AND '+query[1]] = jData['queries']['request'][0]['totalResults']
        s = query[0]+' AND '+query[1]+' '+  joined_results[query[0]+' AND '+query[1]] 
        file.write('%s\n' % s)
    else:
        print('Not good response')
        k = k+1
        print('Using App no', k)
        while k < len(api_key):
            url = 'https://www.googleapis.com/customsearch/v1?key='+api_key[k]+'&cx='+c_id+'&q='+query[0]+' AND '+query[1]
            response = requests.get(url)
            if (response.ok):
                jData = json.loads(response.content)
                joined_results[query[0]+' AND '+query[1]] = jData['queries']['request'][0]['totalResults']
                s = query[0]+' AND '+query[1]+' '+  joined_results[query[0]+' AND '+query[1]] 
                file.write('%s\n' % s)
                break
            k=k+11

file.close()    
print("calculating NGD values")
ngd_values = {}
# calculating ngd values
N = 25270000000000
keys = [x[0] for x in joined_results.items() ]
for k in keys:
    s = k.split(' AND ')
    a = s[0] 
    b = s[1]
    if (a!= b):
            ngd_values[a+' AND '+b] = (max(numpy.log(int(query1_results[a])+1),numpy.log(int(query1_results[b])+1)) - numpy.log(int(joined_results[k])+1))/(numpy.log(int(N)) - min(numpy.log(int(query1_results[a])+1),numpy.log(int(query1_results[b])+1)))
            
# saving the ngd values with pairs as keys and ngd as the value  
pickle_out = open(r"ngd_results.pickle","wb")
pickle.dump(ngd_values, pickle_out)
pickle_out.close()