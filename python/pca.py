import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib
from sklearn.decomposition import PCA

f = open('/home/rohit/Documents/scRNA-seq/data/muscleTFStuff/muscle_tfs.txt')
tf = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/muscle_functional_genes.txt')
func_genes = f.read().splitlines()
f.close()

genes = tf + func_genes
bwm_t6_columns = pd.read_csv('~/Documents/scRNA-seq/data/geneAndTimeData/bwm_csv/bwm_total_time_bins.csv', index_col=0).columns.tolist()

genes_idx = [i+1 for i, val in enumerate(bwm_t6_columns) if val in genes]
genes_idx.insert(0,0)

bwm_df = pd.read_csv('~/Documents/scRNA-seq/data/geneAndTimeData/bwm_csv/bwm_total_time_bins.csv', index_col=0, usecols=genes_idx)

pca = PCA(n_components=5)
pca.fit(bwm_df)

evr = ["{:.7f}".format(i) for i in pca.explained_variance_ratio_.tolist()]

df = pd.DataFrame(pca.components_, index=evr, columns=bwm_df.columns)
print(df)
df.to_csv('hello.csv')
