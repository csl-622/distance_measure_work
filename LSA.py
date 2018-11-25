from numpy import zeros, transpose, asarray, sum,  diag, dot, arccos
from numpy.linalg import norm
import numpy
from scipy.linalg import svd, inv
from pattern.web import Wikipedia
import re, random, pylab
import time
from math import *
import requests
import sys
import math
import wikipedia
from operator import itemgetter
from pattern.web import URL, Document, plaintext

# stopwords, retreived from http://www.lextek.com/manuals/onix/stopwords1.html

stopwords = ['a', 'about', 'above', 'across', 'after', 'again', 'against', 
'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 
'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 
'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 
'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 
'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 
'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 
'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 
'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 
'down', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 
'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 
'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 
'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 
'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 
'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 
'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 
'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 
'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 
'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 
'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 
'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer',
'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 
'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 
'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer',
'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 
'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on',
'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 
'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 
'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point',
'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 
'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 
'really', 'right', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 
'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 
'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 
'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 
'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 
'still', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 
'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 
'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 
'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 
'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 
'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 
'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 
'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 
'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 
'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 
'yours', 'z']


ignore_characters = ''',:'!'''


def compare(query1, query2): # core comparison function. 
    
    lsa = LSA(stopwords, ignore_characters)
    queries = [lsa.search_wiki(query1), lsa.search_wiki(query2)]
    if(queries[0]==-5 or queries[1]==-5):
        return -5
    elif('ReStArT' == queries[0] or queries[1]=='ReStArT'):
        return 'ReStArT'
    for q in queries:
        lsa.parse(q)
    lsa.build()
    if(len(lsa.keys)<2):
        return -5
    lsa.calc()
    Vt = lsa.Vt
    S = diag(lsa.S)
    vectors =[(dot(S,Vt[:,0]),dot(S,Vt[:,i])) for i in range(len(Vt))]
    angles = [arccos(dot(a,b)/(norm(a,2)*norm(b,2))) for a,b in vectors[1:]]
    return str(abs(1 - float(angles[0])/float(math.pi/2)))

class LSA(object):
    def __init__(self, stopwords, ignore_characters):
        self.stopwords = stopwords
        self.ignore_characters = ignore_characters
        self.wdict = {}
        self.dcount = 0        
    def parse(self, doc):
        words = doc.split();
        for w in words:
            w = w.lower().translate(str.maketrans('','',self.ignore_characters))
            if w in self.stopwords:
                continue
            elif w in self.wdict:
                self.wdict[w].append(self.dcount)
            else:
                self.wdict[w] = [self.dcount]
        self.dcount += 1      
    def build(self): # Create count matrix
        self.keys = [k for k in self.wdict.keys() if len(self.wdict[k]) > 1]
        self.keys.sort()
        self.A = zeros([len(self.keys), self.dcount])
        for i, k in enumerate(self.keys):
            for d in self.wdict[k]:
                self.A[i,d] += 1

    def calc(self): # execute SVD
        self.U, self.S, self.Vt = svd(self.A, full_matrices =False)

    def S(self):
        return self.S
    def U(self):
        return -1 * self.U
    def Vt(self):
        return -1 * self.Vt

    def search_wiki(self, k): # scrape query's wikipedia article
        article = Wikipedia().search(k)
        if(article==None):
            try:
                ny = wikipedia.page(k)
            except requests.exceptions.ConnectionError as e:
                return 'ReStArT'
#            except wikipedia.exceptions.HTTPTimeoutError as e:
#                print('here1')
#                print(str(e))
#            except requests.exceptions.ConnectTimeout as e:
#                print('here2')
#                print(str(e))
            except wikipedia.exceptions.DisambiguationError as e:
                try:
                    ny = wikipedia.page(e.options[0])
                except requests.exceptions.ConnectionError as e:
                    return 'ReStArT'
                except wikipedia.exceptions.DisambiguationError as e:
                    return -5    
            except wikipedia.exceptions.PageError as e:
                return -5
            article = Wikipedia().search(ny.title)

        contents = [section.content for section in article.sections]
        kk=0
        for content in contents:
            if(len(content)==0):
                kk=kk+1
        if(contents==[] or kk==len(contents)):
            try:
                ny = wikipedia.page(k)
            except requests.exceptions.ConnectionError as e:
                return 'ReStArT'
            except wikipedia.exceptions.DisambiguationError as e:
                try:
                    ny = wikipedia.page(e.options[0])
                except requests.exceptions.ConnectionError as e:
                    return 'ReStArT'
                except wikipedia.exceptions.DisambiguationError as e:
                    return -5    
            content=ny.content
            if(len(content)==0):
                return -5
            else:
                contents=[]
                contents.append(content)
        d = []
        for content in contents:
            a = content.split()
            d.append(a)
        content = [j for i in d for j in i if re.match("^[a-zA-Z_-]*$", j) and len(j) > 1] # take only meaningful content
        self.content = ' '.join(content)
        return self.content



if __name__ == "__main__": 
    files=['Altenburg/alt_books_last_50_and_pairs.txt','Frank_Bladin/frank_books_last_50_and_pairs.txt']
    for fil in files:
        file=open(fil,'r',encoding='utf-8')
        lines=[line[0:-1] for line in file]
        file.close()
        file=open(fil[0:-4]+'_LSA.txt','w',encoding='utf-8')
        for b in lines:
            a=b.split(' AND ')
            ans=compare(a[0],a[1]);
            if(ans =='ReStArT'):
                while(ans=='ReStArT'):
                    time.sleep(8)
                    print('RESTARTED DUE TO EXCEEDING OF QUERIES')
                    ans=compare(a[0],a[1]);
            if(ans==-5):
                continue
            string=b+' '+str(ans)
            file.write('%s\n'%string)
        file.close()