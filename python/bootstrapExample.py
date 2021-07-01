import pandas as pd

# scikit-learn bootstrap
from sklearn.utils import resample
# # data sample
# data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# # prepare bootstrap sample
# boot = resample(data, replace=True, n_samples=4, random_state=1)
# print('Bootstrap Sample: %s' % boot)
# # out of bag observations
# oob = [x for x in data if x not in boot]
# print('OOB Sample: %s' % oob)

raw_reads = pd.read_csv('data/geneAndTimeData/bwm_raw_reads.csv', index_col = 0, usecols = list(range(20)), skiprows = lambda x: x not in list(range(20)))
print(raw_reads)

boot = resample(raw_reads, replace=True, n_samples=5, random_state=1)
print(boot)