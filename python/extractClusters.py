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
from numpy import genfromtxt

df = pd.read_csv('muscle_ward_distance.csv', header = None, index_col = None)
Z = df.to_numpy(dtype=None, copy=True)

def dendrogram(plot):
    plt.figure(figsize=(12.5, 5))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    hac.dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    if plot:
        # plt.show()
        plt.savefig('dendrogram_muscle.png')
    return

# dendrogram(True)
# exit()

def print_clusters(Z, k, plot=False):
    # k Number of clusters I'd like to extract
    results = fcluster(Z, k, criterion='maxclust')

    # check the results
    s = pd.Series(results)
    clusters = s.unique()

    counter = 0
    for c in clusters:
        cluster_indices = s[s == c].index
        print(cluster_indices)

        with open('muscle_clusters2/cluster' + str(counter) + '.txt', 'w') as f: # write out results to text file
            for item in cluster_indices:
                f.write("%s\n" % item)

        f.close()
        counter = counter + 1

    return

print_clusters(Z, 16)