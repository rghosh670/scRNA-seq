import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib
from sklearn.decomposition import PCA
from anndata import AnnData
import scanpy as sc


normalize_by_cell = False
normalize_by_gene = True
mean_subtract = False

def get_adjustment():
    if mean_subtract:
        return 'mean_subtract'

    if normalize_by_gene and normalize_by_cell:
        return 'normalized_by_cell_and_gene'
    if normalize_by_cell:
        return 'normalized_by_cell'
    if normalize_by_gene:
        return 'normalized_by_gene'

    return ''

f = open('/home/rohit/Documents/scRNA-seq/data/muscleTFStuff/muscle_tfs.txt')
tf = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/muscle_functional_genes.txt')
func_genes = f.read().splitlines()
f.close()

genes = tf + func_genes
index = pd.read_csv('~/Documents/scRNA-seq/data/de_analysis_part2/impulse_de2_input.csv', index_col=0).index.tolist()

genes_idx = [i+1 for i, val in enumerate(index) if val in genes]
genes_idx.insert(0,0)

input = pd.read_csv('~/Documents/scRNA-seq/data/de_analysis_part2/impulse_de2_input.csv', index_col=0, skiprows=lambda x:x not in genes_idx).T
num_components = len(input.index)
cols = input.columns
print(input)

if mean_subtract:
    input = input.sub(input.mean(axis=0), axis=1)

if normalize_by_gene:
    input = (input-input.mean())/input.std()
    input = input.fillna(0)

if normalize_by_cell:
    # input +=1 
    adata = AnnData(input)
    input = sc.pp.normalize_total(adata, inplace=False, exclude_highly_expressed = True)['X']

pca = PCA(n_components=num_components)
pca.fit(input)

evr = ["{:.7f}".format(i) for i in pca.explained_variance_ratio_.tolist()]

df = pd.DataFrame(pca.components_, index=evr, columns=cols)
print(df)

adjustment = get_adjustment()

outfile = adjustment + '_' + 'pca_across_times.csv'
df.to_csv('pca/' + outfile)