import numpy as np
from sklearn import preprocessing


class NormCheck:
    def __init__(self, dataset, cutoff=0.3):
        self.dataset = dataset
        self.cutoff = cutoff
        self.mean_ratio = None
        self.range_ratio = None

    def find_mean_ratio(self):
        """
        takes dataset as nd.array as an input from user and then it will calculate mean of each columns and
        return mean_ratio.
        """
        mean = self.dataset.mean(axis=0)
        meanmin = mean.min()
        meanmax = mean.max()
        if meanmax != 0:
            self.mean_ratio = meanmin * 100 / float(meanmax)
        else:
            self.mean_ratio = 1E10
        return self.mean_ratio

    def find_range_ratio(self):
        """
        takes dataset as nd.array as an input from user and then it will calculate range of each columns and
        return range_ratio
        """
        col_min = self.dataset.min(axis=0)
        col_max = self.dataset.max(axis=0)
        col_range = col_max - col_min
        rangemin = col_range.min()
        rangemax = col_range.max()
        if rangemax != 0:
            self.range_ratio = rangemin * 100 / float(rangemax)
        else:
            self.range_ratio = 1E10
        return self.range_ratio

    def decide_normalization(self):
        """
        takes input of mean_ratio and range_ratio, check with the user's input of cutoff or
        the default value of 0.3.
        """
        if self.mean_ratio < self.cutoff:
            dataset_normalized = preprocessing.normalize(self.dataset)
            return dataset_normalized
        else:
            return None


if __name__ == '__main__':

    data = np.genfromtxt('College.csv', delimiter=',', skip_header=1)
    rowwise_missing_entries = len(data) - np.sum(data == data, axis=0)
    data_nocategory_columns = rowwise_missing_entries < len(data)
    modified_data = data[:, data_nocategory_columns]

    normalization = NormCheck(modified_data, 0.2)
    # normalization = NormCheck(modified_data, 0.1)
    # normalization = NormCheck(modified_data)

    mean_ratio = normalization.find_mean_ratio()
    print mean_ratio
    range_ratio = normalization.find_range_ratio()
    print range_ratio
    normalized_data = normalization.decide_normalization()
    print normalized_data
