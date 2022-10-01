# 5-letter word count
import math
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphanums

# initiate list for counts
lettercount = [0]*(26*5)

# open/read 5-ltr words - count letters per location in word
with open("5-ltr-words.txt", "r+") as f:
    for word in f:
        for ltr in word:
            if ltr != '\n':
                x = ord(ltr) - 96
                lettercount[x+(word.index(ltr))*26-1]+=1

# give stats on letters
finaltotal = 0

letterposperc = [0]*26*5
lettertotcount = [0]*26
lettertotperc = [0]*26

for ltrcount in lettercount:
    lettertotcount[lettercount.index(ltrcount) % 26] += ltrcount
    finaltotal += ltrcount

for tot in lettertotcount:
    lettertotperc[lettertotcount.index(tot)] = (tot/finaltotal)*100

for ltrperc in lettercount:
    letterposperc[lettercount.index(ltrperc)] = (ltrperc/(lettertotcount[lettercount.index(ltrperc) % 26]))*100

ind = np.arange(26)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
plt.xlabel('Frequency')
plt.ylabel('Letter')
plt.title('Frequencies of letters in 5-Letter words')
plt.xticks(ind, alpha)
plt.yticks(np.arange(0, 10, 1))
plt.bar(alpha, lettertotperc)
plt.savefig('frequency.png')


