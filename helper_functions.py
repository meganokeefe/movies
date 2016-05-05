#Helper Functions for Movies Project
#Megan O, 5/4/16

import pickle
from collections import Counter
import numpy as np

#Converts pickle file into indexed dictionary
def from_pickle(fn):
    pkl_file = open(fn, 'rb')
    mydict = pickle.load(pkl_file)
    pkl_file.close()
    return mydict.items()

def search_by_title(searchtitle, ditems):
    return [d for d in ditems if searchtitle in d[1]['title']]

#gets a list of the unique
def get_flat_unique(element_name, ditems):
    hier = [item[1][element_name] for item in ditems]
    hs = [item for sublist in hier for item in sublist]
    return [x[0] for x in Counter(hs).items()]

#gets a list of movies under the specified genre name
def get_by_genre(gname, ditems):
    return [f for f in ditems if gname in f[1]['genres']]

#given a list of movies, returns a counter of the release years
def get_years_count(subset):
    dates = [item[1]['date'] for item in subset]
    cleandates = []
    for d in dates:
        if d!="":
            cleandates.append(d[:4])
    return Counter(cleandates)

#given ditems and a genre game, get
def get_num_films(ditems, gname, startDate, endDate):
    genall = get_by_genre(gname, ditems)
    dts = get_years_count(genall)
    dates = xrange(startDate, endDate)
    counts = []
    for d in dates:
        if dts[str(d)]:
            counts.append(dts[str(d)])
        else:
            counts.append(0)
    return counts

#revenue by year
def get_median_revenue(ditems, gname):
    genall = get_by_genre(gname, ditems)
    revs = [item[1]['revenue'] for item in genall]
    revs = [int(i) for i in revs if i!=""]
    return np.median(revs)

diadem = from_pickle('films.pkl')

#get revenues
# genres = get_flat_unique('genres', diadem)
# gup = [(x) for x in genres]
# for tup in gup:
#     gup.append(get_median_revenue(diadem, tup[0]))
# print gup
