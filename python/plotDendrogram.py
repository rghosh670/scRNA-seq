import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import genfromtxt


Z = genfromtxt('muscle_ward_distance.csv', delimiter=',')

def dendrogram(Z, plot):
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
        plt.savefig('muscle_ward_dendrogram.png')
    return Z

dendrogram(Z, True)