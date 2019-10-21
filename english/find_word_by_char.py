# Developed by Wannaphong Phatthiyaphaibun
from nltk.corpus import words
import collections
wordlist = words.words()

def find(s):
 word=[]
 p=collections.Counter(list(s))
 for i in wordlist:
  if len(i)==len(s):
   t=False
   if collections.Counter(list(i))==p:
    t=True
   if t:
    word.append(i)
 return word

# Use
find('tca') # ['act', 'cat', 'act', 'cat']
