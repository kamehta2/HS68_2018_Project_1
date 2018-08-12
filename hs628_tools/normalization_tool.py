
import numpy as np
from sklearn import preprocessing


class NormCheck:
    """
    The class NormCheck takes two arguments from the user.
    1. dataset: The user should provide data set as a numpy array without any categorical variables
                and missing values.
    2. cutoff: As per the data set, users should choose a cutoff value that is optimal based on the
                distribution of their data. This cutoff value will be used to decide if the data set
                needs normalization or not based on calculating the mean ratio and the range ratio
                of the provided data. If the user does not put any value for the cutoff, then the
                default value of cutoff = 0.3.

    There are three functions in the class NormCheck.
    1. find_mean_ratio, which returns mean_ratio
    2. find_range_ratio, which returns range_ratio
    3. decide_normalization, which returns an array containing normalized data or "None"

    Note: For the cutoff value, there is no one thumb rule that is expected to work for all types of
            data sets. The default value of 0.3 was determined based on findings made on sample data
            sets that I had chosen, such as checking the range and distribution of data values of
            these data sets, and coming up with a threshold which indicates an unbalanced distribution,
            and hence making a case for normalization.
    """

    def __init__(self, dataset, cutoff=0.3):
        self.dataset = dataset
        self.cutoff = cutoff
        self.mean_ratio = None
        self.range_ratio = None

    def find_mean_ratio(self):
        """
        This function takes data set as nd.array as input from the user. It will calculate mean of each column,
        then it will find minimum and maximum value of the mean and return the mean_ratio.
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
        This function takes data set as nd.array as input from the user. It will calculate minimum and
        maximum value of each column, find out range of each column and return the range_ratio.
        """
        min = self.dataset.min(axis=0)
        max = self.dataset.max(axis=0)
        range = max - min
        rangemin = range.min()
        rangemax = range.max()
        if rangemax != 0:
            range_ratio = rangemin * 100 / float(rangemax)
            self.range_ratio = range_ratio
        else:
            self.range_ratio = 1E10
        return self.range_ratio

    def decide_normalization(self):
        """
        This function uses input of mean_ratio and range_ratio from above functions, checks with user's input
        of cutoff value or the default value of 0.3. If the mean_ratio and range_ratio are less than the cutoff
        value, the function returns an array containing normalized data or None otherwise.
        """
        if self.mean_ratio < self.cutoff:
            if self.range_ratio < self.cutoff:
                dataset_normalized = preprocessing.normalize(self.dataset)
                return dataset_normalized
            else:
                return None
        else:
            return None


if __name__ == '__main__':

    data = np.genfromtxt('College.csv', delimiter=',', skip_header=1)
    # The sample data set can be downloaded from below link.
    # http://www-bcf.usc.edu/~gareth/ISL/College.csv
    rowwise_missing_entries = len(data) - np.sum(data == data, axis=0)
    data_nocategory_columns = rowwise_missing_entries < len(data)
    modified_data = data[:, data_nocategory_columns]

    normalization = NormCheck(modified_data, 0.2)
    # normalization = NormCheck(modified_data, 0.1)
    # normalization = NormCheck(modified_data)

    percent_mean_ratio = normalization.find_mean_ratio()
    print percent_mean_ratio
    percent_range_ratio = normalization.find_range_ratio()
    print percent_range_ratio
    normalized_data = normalization.decide_normalization()
    print normalized_data
