import numpy as np
import sklearn as sk
from sklearn import preprocessing


class NormCheck:
    def __init__(self, csv_file, cutoff=0.3, alldata1=None):
        self.csv_file = csv_file
        self.cutoff = cutoff
        self.alldata1 = alldata1

    def find_percent_diff(self):
        alldata = np.genfromtxt(self.csv_file, delimiter=',', skip_header=1)
        rowwise_missing_entries = len(alldata) - np.sum(alldata == alldata, axis=0)
        data_nocategory_columns = rowwise_missing_entries < len(alldata)
        self.alldata1 = alldata[:, data_nocategory_columns]
        allmean = self.alldata1.mean(axis=0)
        allmeanmin = allmean.min()
        allmeanmax = allmean.max()
        percent_diff = allmeanmin * 100 / float(allmeanmax)
        return percent_diff

    def get_input(self, percent_diff):
        if percent_diff < self.cutoff:
            rescale = raw_input ("This dataset should be normalized. Do you want to proceed with normalization?"+"\n"+"YES/NO"+"\n")
            return rescale
        else:
            return "This dataset may not need normalization."

    def compare(self, rescale):
        if rescale.upper() == "YES":
            alldata_normalized = preprocessing.normalize(self.alldata1)
            alldata_normalized = alldata_normalized
            return alldata_normalized
        else:
            return "You have selected not to normalize your dataset."


if __name__ == '__main__':

    Normalization = NormCheck("College.csv",0.3)
    #Normalization = NormCheck(College.csv)
    #Normalization = NormCheck(heart.csv, 0.4)
    #Normalization = NormCheck(data.csv)

    percentage = Normalization.find_percent_diff()
    rescale_input = Normalization.get_input(percentage)
    normalized_data = Normalization.compare(rescale_input)
    print normalized_data
