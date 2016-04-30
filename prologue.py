#30 April 2016
#Compiling the three data sources (movies, characters, summaries) in Megan-usable pkl format

import ast
import pickle
import re
import pandas as pd
import pprint as pp
from collections import Counter

def to_pickle(mydict, fn):
    output = open(fn, 'wb')
    pickle.dump(mydict, output)
    output.close()

def read_data():
    #1. MMD.txt is the plain TSV with the movie metadata
    with open('data/mmd.txt') as infile:
        allt = infile.readlines()
    base = {}
    #index by wiki movie ID
    for i, item in enumerate(allt):
        if i%1000==0:
            print "getting metadata for movie #" + str(i)
        item = item.decode('unicode_escape').encode('ascii','ignore')
        item = item.split("\t")
        #Clean languages, countries, genres of punctuation / ID information
        languages = ast.literal_eval(item[6]).values()
        countries = ast.literal_eval(item[7]).values()
        genres = ast.literal_eval(item[8]).values()
        base[item[0]] = {'title': item[2], 'date': item[3], 'revenue': item[4], 'runtime': item[5], 'languages': languages, 'countries': countries, 'genres': genres}
    return base

d = read_data()
to_pickle(d, "protest.pkl")

#CHAR METADATA
"""Cols:
1. Wikipedia movie ID
2. Freebase movie ID
3. Movie release date
4. Character name
5. Actor date of birth
6. Actor gender
7. Actor height (in meters)
8. Actor ethnicity (Freebase ID)
9. Actor name
10. Actor age at movie release
11. Freebase character/actor map ID
12. Freebase character ID
13. Freebase actor ID
"""



#PLOT SUMMARIES (id -> movie.metadata.tsv)
