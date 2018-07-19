import numpy as np
import sklearn as sk
from sklearn import preprocessing

#alldata = np.genfromtxt('heart.csv', delimiter=',', skip_header=1)
#alldata = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
alldata = np.genfromtxt('college.csv', delimiter=',', skip_header=1)

rowwise_missing_entries = len(alldata) - np.sum(alldata==alldata, axis=0)

data_nocategory_columns = rowwise_missing_entries < len(alldata)
alldata1 = alldata[:, data_nocategory_columns]

allmean = alldata1.mean(axis=0)

allmeanmin = allmean.min()
allmeanmax = allmean.max()
allmeanrange = allmeanmax - allmeanmin
percent_diff = allmeanmin * 100/ float(allmeanmax)

def getinput():
    if percent_diff < 0.3:
        rescale = raw_input ("This dataset should be normalized. Do you want to proceed with normalization?"+"\n"+"Yes/No"+"\n")
        return rescale
    else:
        print "This dataset may not need normalization."

normalization_input = getinput()

def compare():
    if normalization_input.upper() == "YES":
        alldata_normalized = preprocessing.normalize(alldata1)
        return alldata_normalized
    else:
        print "You have selected not to normalize your dataset."

normalized_data = compare()
normalized_data
