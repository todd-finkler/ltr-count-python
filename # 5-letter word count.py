# 5-letter word count

# initiate list for counts
lettercount = [0]*(26*5)

# open/read 5-ltr words - count letters per location in word
with open("5-ltr-words.txt", "r") as f:
    for word in f:
        for ltr in word:
            x = to_ascii(ltr) - 97
            lettercount[x*5+(word.index(ltr))]+=1

# give stats on letters
finaltotal = 0

letterposperc = [0]*26*5
lettertotcount[0]*26
lettertotperc[0]*26

for ltrcount in lettercount:
    lettertotcount[math.floor(lettercount.index(ltrcount)/5)] += ltrcount
    finaltotal += ltrcount

for ltrperc in lettercount:
    lettposperc[lettercount.index(ltrperc)] = ltrperc/x(lettertotcount[math.floor(lettercount.index(ltrcount)/5)])*100

for tot in lettertotcount:
    lettertotperc[lettertotcount.index(tot)] = tot/finaltotal*100

for pl in lettertotperc:
    print(chr(97+lettertotcount.index(pl)), " = ", pl)

