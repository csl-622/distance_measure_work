import json
from collections import defaultdict

with open('data/Frank_Bladin/1.json') as f:
    dict_1 = json.load(f)


with open('data/Frank_Bladin/2.json') as f:
    dict_2 = json.load(f)

with open('data/Frank_Bladin/3.json') as f:
    dict_3 = json.load(f)


dict_whole = {}
list_dict1 = []

for each_rev in dict_1:
	dict_whole[each_rev['revid']] = each_rev['links']
	list_dict1.extend(each_rev['links'])

list_dict2 = []
for each_rev in dict_2:
	dict_whole[each_rev['revid']] = each_rev['links']
	list_dict2.extend(each_rev['links'])

list_dict3 = []
for each_rev in dict_3:
	dict_whole[each_rev['revid']] = each_rev['links']
	list_dict3.extend(each_rev['links'])

dict_whole['425778683'] = list(set(dict_whole['425778683']) - set(list_dict1))
dict_whole['451073584']	= list(set(dict_whole['425778974']) - set(list_dict2)) 

for ind in range(0,len(dict_2)):
	if(dict_2[ind]['revid'] == '425778683'):
		dict_2[ind]['links'] = dict_whole['425778683']
	
for ind in range(0,len(dict_3)):
	if(dict_3[ind]['revid'] == '451073584'):
		dict_3[ind]['links'] = dict_whole['451073584']
	
with open('data/Frank_Bladin/2.json', 'w') as fp:
    json.dump(dict_2, fp)

with open('data/Frank_Bladin/3.json', 'w') as fp:
    json.dump(dict_3, fp)


new_dict = []
new_dict.extend(dict_1)
new_dict.extend(dict_2)
new_dict.extend(dict_3)

with open('data/Frank_Bladin/whole_dict.json', 'w') as fp:
    json.dump(new_dict, fp)

rev_user_factoid = defaultdict(list)

for each_rev in new_dict:
	for each_link in each_rev['links']:
		each_link = each_link[2:len(each_link)-2].split('|')[0]
		rev_user_factoid[each_link].append([each_rev['revid'],each_rev['userid']])

with open('data/Frank_Bladin/rev_user_fact.json', 'w') as fp:
    json.dump(rev_user_factoid, fp)

print(rev_user_factoid)
print(len(rev_user_factoid))


#425777960 -- first last
#425778683 -- second first
#451071288 -- second last
#451073584 -- third first+

