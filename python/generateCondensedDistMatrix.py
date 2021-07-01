import pandas as pd
from scipy import stats
from scipy.spatial.distance import pdist
import numpy as np

def my_metric(x, y):
    r = stats.pearsonr(x, y)[0]
    return 1 - r  # correlation to distance: range 0 to 2

df = pd.read_csv('data/averagedExpressionOverTime.csv', index_col=[0])
dist = pdist(df, my_metric)

np.savetxt('data/betterCondensedDistance.csv', dist, delimiter = ',')
print(dist)
