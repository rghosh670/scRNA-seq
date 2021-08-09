import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


def detect_outlier(data_1):
    outliers=[]
    threshold=1
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for index, y in enumerate(data_1):
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(index)
    return outliers


f = open('data/muscleTFStuff/muscle_tfs.txt', 'r')
tfs = f.read().splitlines()
f.close()

muscles = ['bwm_anterior', 'bwm_far_posterior', 'bwm_head_row_1', 'bwm_head_row_2', 'bwm_posterior']

genes = pd.read_csv('data/geneAndTimeData/bwm_csv/' + muscles[0] + '_time_bins.csv', index_col=0).columns.tolist()

idx = []
for i,v in enumerate(genes):
    if v in tfs:
        idx.append(i+1)

idx.insert(0,0)

tf_dict = {}
master_set = set()
for muscle in muscles:
    df = pd.read_csv('data/geneAndTimeData/bwm_csv/' + muscle + '_time_bins.csv', index_col=0, usecols=idx)
    df = df.iloc[0:4]

    df = df.sub(df.mean(axis=0), axis=1)
    pca = PCA(n_components=4)
    pca.fit(df)

    evr = ["{:.7f}".format(i) for i in pca.explained_variance_ratio_.tolist()]
    result = pd.DataFrame(pca.components_, index=evr, columns=df.columns)
    # print(result)

    indices = set()
    data = df.iloc[0].tolist()
    outlier_datapoints = detect_outlier(data)
    indices.update(outlier_datapoints)

    genes = [v for i, v in enumerate(df.columns.tolist()) if i in indices]

    print(genes)
    tf_dict[muscle] = genes
    master_set.update(genes)

num_cell_dict = {}

for gene in master_set:
    num_cell_dict[gene] = 0
    for val in tf_dict.values():
        if gene in val:
            num_cell_dict[gene] += 1

result_df = pd.DataFrame(columns = ['num_cells'])

for k,v in num_cell_dict.items():
    result_df.loc[k] = [v]

result_df.to_csv('num_cells.csv')