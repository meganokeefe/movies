from helper_functions import *
from do_pygal import *
import csv
import string

"""
Want to know how genres connect to each other.
For movies with more than one genre listed, what are the top intersections?

Build a matrix of all the genres
For every time they co-occur, add a weight

"""

def write_labels():
    genres = get_flat_unique('genres', diadem)
    writer = csv.writer(open('labels.csv', 'wb'))
    for i, gname in enumerate(genres):
       writer.writerow([gname, unicode(str(i+1)).encode("utf-8")])

#Weights: Source, Target, Weight

def write_weights(diadem):
    genres = get_flat_unique('genres', diadem)
    weights = {}
    #get genre lists for all the films
    glists = [item[1]['genres'] for item in diadem]
    for i, glist in enumerate(glists):
        if i%100==0:
            print "On genre list ", i
        for s in glist:
            for t in glist:
                if s!=t:
                    sid = genres.index(s)+1
                    tid = genres.index(t)+1
                    if (sid, tid) in weights:
                        weights[(sid, tid)] = weights[(sid, tid)] + 1
                    else: #pair already in weights
                        weights[(sid, tid)] = 1
    #out
    writer = csv.writer(open('weights.csv', 'wb'))
    for key, value in weights.items():
            writer.writerow([unicode(key[0]).encode("utf-8") , unicode(key[1]).encode("utf-8"), unicode(value).encode("utf-8")])

diadem = from_pickle('films.pkl')
write_weights(diadem)
