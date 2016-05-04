#Created: 30 April 2016
#Last update: 3 May 2016
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

    #get characters
    with open('data/cmd.txt') as infile:
        rawc = infile.readlines()
    allc = [item.decode('unicode_escape').encode('ascii','ignore').split("\t") for item in rawc]
    #hashable structure
    uchars = {}
    for x in allc:
        mov_id = x[0]
        if mov_id in uchars:
            uchars[mov_id].append([x[3], x[5], x[8], x[9]])
        else: #new init
            uchars[mov_id] = [[x[3], x[5], x[8], x[9]]]


    #get plot summaries & parse them into a hashable dict
    with open('data/plot_summaries.txt') as infile:
        rawsum = infile.readlines()
    sums = [t.split("\t") for t in rawsum]
    sums2 = {id: sum.decode('unicode_escape').encode('ascii','ignore').strip() for (id,sum) in sums}

    #TIME TO COMPILE THE DATA SOURCES
    base = {} #the set of movies and all associated data!
    #index by wiki movie ID
    for i, item in enumerate(allt):
        if i%100==0:
            print "on movie #" + str(i)
        item = item.decode('unicode_escape').encode('ascii','ignore')
        item = item.split("\t")
        #Clean languages, countries, genres of punctuation / ID information
        m_id = item[0]
        languages = ast.literal_eval(item[6]).values()
        countries = ast.literal_eval(item[7]).values()
        genres = ast.literal_eval(item[8]).values()
        if m_id in uchars:
            chars = uchars[m_id]
        else:
            chars = []
        #only about half the films have summaries...
        if m_id in sums2:
            summary = sums2[m_id]
        else:
            summary = ""
        #clean up the chars
        base[m_id] = {'title': item[2], 'date': item[3], 'revenue': item[4], 'runtime': item[5], 'languages': languages, 'countries': countries, 'genres': genres, 'chars': chars, 'summary': summary}
    #print base['15401493']
    return base

d = read_data()
to_pickle(d, "films.pkl")
