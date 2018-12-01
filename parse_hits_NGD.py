import math
import json
import pickle

dict_NGD = {}

with open('data/Frank_Bladin/frank_whole.json') as f:
    data = json.load(f)

with open('data/Frank_Bladin/pairs_frank_whole.txt') as f:
    lines = f.read().splitlines()
#print(len(lines))
for each_pair in range(159,len(lines)):
	pair = str.split(lines[each_pair],'AND')
	pair[0] = pair[0].strip()
	pair[1] = pair[1].strip()
	left_ind = None
	right_ind = None
	pair_ind = None
	#print(pair[0] + ',,, ' + pair[1])
	#print(each_pair)
	for each in range(0,len(data)):
		if(data[each]["query"] == pair[0]):
			left_ind = each
			#print('left')
		if(data[each]["query"] == pair[1]):
			right_ind = each
			#print('right')
		if(data[each]["query"] == lines[each_pair]):
			pair_ind = each
			#print('pair')
	if(left_ind is not None and right_ind is not None and pair_ind is not None):
		#print(data[left_ind]['num_results_for_query'])
		#print(pair_ind)
		#print(data[pair_ind]['num_results_for_query'])
				
		if(data[left_ind]['num_results_for_query'][0] != 'A'):
			h_left = 1
		else:		
			h_left = int(data[left_ind]['num_results_for_query'].split(' ')[1].replace(',',''))
		if(data[right_ind]['num_results_for_query'][0] != 'A'):
			h_right = 1
		else:		
			h_right = int(data[right_ind]['num_results_for_query'].split(' ')[1].replace(',',''))
		if(data[pair_ind]['num_results_for_query'][0] != 'A'):
			h_both = 1
		else:		
			h_both = int(data[pair_ind]['num_results_for_query'].split(' ')[1].replace(',',''))
		#print((max( math.log(h_left),math.log(h_right)) - math.log(h_both) ) / ( math.log(25270000000) - min( math.log(h_left),math.log(h_right)) ) )
		dict_NGD[lines[each_pair]] = (max( math.log(h_left),math.log(h_right)) - math.log(h_both) ) / ( math.log(25270000000) - min( math.log(h_left),math.log(h_right)) ) 

#print(dict_NGD)
print(len(dict_NGD))
for key in dict_NGD:
	if(dict_NGD[key] < 0):
		print(key +' '+ str(dict_NGD[key]))
with open('data/Frank_Bladin/frank_whole.pkl', 'wb') as f: 
    pickle.dump(dict_NGD, f)
 
		

