from scipy.cluster.hierarchy import fcluster
from scipy import stats
from scipy.spatial.distance import squareform
import scipy.cluster.hierarchy as hac
import statistics
from statistics import mode
from math import floor
import random
import numpy as np; np.random.seed(0)
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import matplotlib
from cellNames import getCellName
import seaborn as sns

dist = pd.read_csv('IL1_squareform.csv', index_col = [0])
print(dist)

ax = sns.heatmap(dist)
fig = ax.get_figure()
fig.savefig('IL1_heatmap.png')

dist = pd.read_csv('smallNeurons.csv', index_col = [0])
print(dist)

ax = sns.heatmap(dist)
fig = ax.get_figure()
fig.savefig('all_neurons_heatmap.png')
