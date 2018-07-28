import numpy as np
import sklearn as sk
from sklearn import preprocessing


class NormCheck:
    def __init__(self, csv_file, cutoff=0.3, alldata1=None):
        self.csv_file = csv_file
        self.cutoff = cutoff
        self.alldata1 = alldata1

    def find_percent_diff(self):
        """ 
        This function reads the data from .csv file as a numpy.ndarray. It calculates mean for each column.
        It further processes this data to return the percentage difference.
        """
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
        """
        This function presents user to provide an input, if it determines that data will benefit from normalization.
        The user input gives choice to user if they want to proceed with normalization or not.
        If data does not need normalization, the function returns with an informative message reflecting the same.
        """
        if percent_diff < self.cutoff:
            rescale = raw_input ("This dataset should be normalized. Do you want to proceed with normalization?"+"\n"+"YES/NO"+"\n")
            return rescale
        else:
            return "This dataset may not need normalization."


    def compare(self, rescale):
        """
        This function checks if user decided to proceed with normalization, and if so, goes ahead and performs normalization
        and returns normalized dataset as a numpy.ndarray. Else, it reflects a message that the user has not selected to normalize the dataset,
        even though the recommendation was provided to the user.
        """
        if rescale.upper() == "YES":
            alldata_normalized = preprocessing.normalize(self.alldata1)
            alldata_normalized = alldata_normalized
            return alldata_normalized
        else:
            return "This dataset may not need normalization or you have selected not to normalize your dataset."


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    normalization = NormCheck("College.csv",0.1)
    #normalization = NormCheck(College.csv)
    #normalization = NormCheck(heart.csv, 0.4)
    #normalization = NormCheck(data.csv)

    percentage = normalization.find_percent_diff()
    rescale_input = normalization.get_input(percentage)
    normalized_data = normalization.compare(rescale_input)
    print normalized_data
