import scipy
from scipy.cluster.hierarchy import fcluster
from scipy import stats
import scipy.cluster.hierarchy as hac
import statistics
from statistics import mode
from math import floor
import random
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import matplotlib

dist = pd.read_csv('squareformDistance.csv', header = [0], index_col = [0])
print(dist)
dist = dist.to_numpy(dtype=None, copy=True)
print(dist)


condensedCompleteDistMatrix = scipy.spatial.distance.squareform(dist)
np.savetxt('condensedCompleteDistMatrix.csv', condensedCompleteDistMatrix, delimiter = ',')

print(condensedCompleteDistMatrix)
exec(open('sendEmail.py').read())