import pandas as pd
import json
from scipy import stats
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

with open('muscle_clusters2/gene_cluster_dict.txt') as json_file:
    gene_cluster_dict = json.load(json_file)
json_file.close()

usecols = list(gene_cluster_dict.keys())
usecols.insert(0, 'cell')

userows = [0]
T6_BWM_ANTERIOR_BOUNDS = (116, 124)
userows.extend([*range(T6_BWM_ANTERIOR_BOUNDS[0], T6_BWM_ANTERIOR_BOUNDS[1])])

t6 = pd.read_csv('data/t6Stuff/t6.csv', index_col=[0], skiprows = lambda x:x not in userows, usecols=usecols)

userows = [0]
CELL_SCORE_BWM_ANTERIOR_BOUNDS = (1, 9)
userows.extend([*range(CELL_SCORE_BWM_ANTERIOR_BOUNDS[0], CELL_SCORE_BWM_ANTERIOR_BOUNDS[1])])

cell_score = pd.read_csv('muscle_clusters2/muscle_clusters2CellBinScore.csv', index_col=[0], skiprows = lambda x:x not in userows)

# def my_metric(x, y):
#     r = stats.pearsonr(x, y)[0]
#     return 1 - r  # correlation to distance: range 0 to 2

r_values = []
final_genes = []

for gene in t6.columns:
    cluster = str(gene_cluster_dict[gene])

    x = t6[gene].tolist()
    y = cell_score['cluster' + cluster].tolist()
    r = stats.pearsonr(x, y)[0]

    if not math.isnan(r) and -0.1 < r < 0.1 and 'a' <= gene[0] <= 'c':
        final_genes.append(gene)
        r_values.append(r)

        print(gene, cluster, r)


# n, bins, patches = plt.hist(x=r_values, bins='auto', color='#0504aa',
#                             alpha=0.7, rwidth=0.85)
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.text(23, 45, r'$\mu=15, b=3$')
# maxfreq = n.max()
# # Set a clean upper y-axis limit.
# plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
# # plt.show()
