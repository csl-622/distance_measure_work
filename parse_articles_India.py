from xml.dom import minidom
import re
import glob

file_list = glob.glob("data/India/*.xml")
#filename=r'data/Ace_Books/11.xml'
b = 1
for filename in file_list:
	print(b)
	b +=1
	mydoc = minidom.parse(filename)
	revs = mydoc.getElementsByTagName('rev')

	p = re.compile('\[\[[^\[\]:]*\]\]')
	p_data = re.compile('[^\=]\={1}\={1}[^\=]')

	#file = open('/home/shubham/Desktop/Books/Sem 7/CSL622/project/wikipedia articles mail/Ace_Books/links_4.txt','w')
	list_of_dict = []       # list of dictionaries of each revision 
	links_prior = []
	file  = open(filename[0:-3]+'txt' ,"w",encoding='utf-8')
	#a = 1;
	for each_rev in revs:
		if(each_rev.childNodes==[]):
			continue
		diction = {}					# dictionary for each revision	
		links_added = []        			# list of links added in revision without brackets
		#para = each_rev.childNodes[0].data.split("External links")[0].split("Bibliography")[0].split("References")[0].split("Notes")[0].split("See also")[0]
		para_list = p_data.split(each_rev.childNodes[0].data)
		if(len(para_list) < 5):
			continue
		para = para_list[4]
		#l = p.findall(each_rev.childNodes[0].data)	# total links with brackets
		l = p.findall(para)	
		l_added = list(set(l) - set(links_prior))	# links added with brackets
		l_add_rem = list( (l_added) + (list(set(links_prior) - set(l))))
		links_prior = l					# prior links with brackets for next iteration
		#if a == 38:
		#	print(l_added)
		for each_link in l_added:
			#if a == 38:
			#	print(each_link[2:len(each_link)-2])
			linkk = each_link[2:len(each_link)-2].split('|')[0]
			file.write("%s\n" % linkk)
			links_added.append(each_link[2:len(each_link)-2])
		diction['revid'] = each_rev.attributes['revid'].value
		diction['parentid'] = each_rev.attributes['parentid'].value
		diction['user'] = each_rev.attributes['user'].value
		diction['userid'] = each_rev.attributes['userid'].value
		diction['timestamp'] = each_rev.attributes['timestamp'].value
		diction['size'] = each_rev.attributes['size'].value
		diction['links'] = l_add_rem  			# links added + removed in this revision 
		list_of_dict.append(diction)
		#a+=1

	file.close()
	import json

	with open(filename[0:-3]+'json', 'w') as fp:
	    json.dump(list_of_dict, fp)

