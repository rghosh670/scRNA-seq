import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import scipy
from scipy.cluster.hierarchy import fcluster
from scipy import stats
import scipy.cluster.hierarchy as hac

df = pd.read_csv('data/geneAndTimeData/de_analysis_part2/bwm_up_tf_avg_expression.csv', index_col=0)

df = df[(df.T != 1e-10).any()]

def my_metric(x, y):
    r = stats.pearsonr(x, y)[0]
    return 1 - r  # correlation to distance: range 0 to 2

def dendrogram(plot):
    Z = hac.linkage(df,  method='single', metric=my_metric)

    plt.figure(figsize=(12.5, 5))
    plt.title('Increasing Transcription Factors in Muscle Cells')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    hac.dendrogram(
        Z,
        labels=df.index,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    if plot:
        plt.show()
        plt.savefig('figures/up_tf_dendrogram_part2.png')
    return Z
Z = dendrogram(plot=True)

def print_clusters(timeSeries, Z, k, plot=False):
    # k Number of clusters I'd like to extract
    results = fcluster(Z, k, criterion='maxclust')

    # check the results
    s = pd.Series(results)
    clusters = s.unique()

    for c in clusters:
        cluster_indices = s[s == c].index
        print(cluster_indices)
        if plot:
            timeSeries.T.iloc[:, cluster_indices].plot()
            plt.show()
    return
# print_clusters(df, Z, 60, plot=False)


