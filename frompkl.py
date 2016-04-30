import pickle

def from_pickle(fn):
    pkl_file = open(fn, 'rb')
    mydict = pickle.load(pkl_file)
    pkl_file.close()
    return mydict

d = from_pickle('protest.pkl')
