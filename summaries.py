#Exploration of the plot summaries
from helper_functions import *
import string
from collections import Counter
import math
import pprint as pp

#get lists of tuples... [summary, revenue] - only do this once
def transform():
    count = 1
    ditems = from_pickle('films.pkl')
    sums = {}
    for film in ditems:
        if film[1]['summary'] != '' and film[1]['revenue'] != '':
            sums[count] = [film[1]['summary'], film[1]['revenue']]
            count = count + 1
    output = open('summaries.pkl', 'wb')
    pickle.dump(sums, output)
    output.close()

#remove stopwords, etc
def clean(summaries):
    tk = []
    with open("stopwords.txt") as inf:
        stopwords = [i.strip() for i in inf.readlines()]
    for item in summaries:
        s = item[1][0].lower()
        exclude = set(string.punctuation)
        raw2 = ''.join(ch for ch in s if ch not in exclude)
        spl = raw2.split(" ")
        spl2 = [w for w in spl if not w in stopwords]
        tk.append((" ".join(spl2), item[1][1]))
    return tk

#Returns a weighted ranking of words assoc. w/ top-selling films
#given cleaned list of tuples, return a ranked list
def blockbuster_words(sums):
    allCounts = {}
    for i, item in enumerate(sums):
        if i%100==0:
            print "on film ", i, "of", len(sums)
        summary = item[0]
        rev = float(item[1])
        counts = Counter(summary.split(" "))
        #increment allCounts with
        for tup in counts.items():
            word = tup[0]
            unweightedCount = tup[1]
            if word in allCounts:
                allCounts[word] = allCounts[word] + unweightedCount*rev
            else:
                allCounts[word] = unweightedCount*rev
    output = open('block_weights.pkl', 'wb')
    pickle.dump(block, output)
    output.close()
    return allCounts

#Does the same thing but with bigrams
def blockbuster_bigrams(sums):
    allCounts = {}
    for i, item in enumerate(sums):
        if i%100==0:
            print "on film ", i, "of", len(sums)
        summary = item[0]
        summary.replace("  ", " ") #double space bug
        rev = float(item[1])
        #build bigrams
        spl = summary.split(" ")
        bigrams = []
        index = 0
        while index < len(spl)-3: #last version uses trigrams 
            bigrams.append((spl[index], spl[index+1], spl[index+2]))
            index = index + 1
        #continue.
        counts = Counter(bigrams)
        #increment allCounts with
        for tup in counts.items():
            word = tup[0]
            unweightedCount = tup[1]
            if word in allCounts:
                allCounts[word] = allCounts[word] + unweightedCount*rev
            else:
                allCounts[word] = unweightedCount*rev
    output = open('block_trigram_weights.pkl', 'wb')
    pickle.dump(allCounts, output)
    output.close()
    return allCounts

#Normalizes the weighted counts becuase they're huge numbers (multiplied by revenue
#vals in the millions)
def normalize(weights):
    norms = {}
    orig = [i[1] for i in weights]
    maxVal = max(orig) #all the weighted counts
    print "Max val is ", maxVal
    for item in weights:
        normValue = float(item[1])/maxVal
        norms[item[0]] = math.log(normValue, 2) #take the log. small values are the worst
    return Counter(norms).most_common(100)

#transform()
#sums = from_pickle("summaries.pkl")
#cleaned = clean(sums) #tokenize
#blockbuster_bigrams(cleaned)

weights = from_pickle("block_trigram_weights.pkl")
pp.pprint(normalize(weights))
