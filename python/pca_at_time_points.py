import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib
from sklearn.decomposition import PCA
from anndata import AnnData
import scanpy as sc


normalize_by_cell = False
normalize_by_gene = False
mean_subtract = True

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


muscles = ['BWM_anterior', 'BWM_far_posterior', 'BWM_head_row_1', 'BWM_head_row_2', 'BWM_posterior']
columns = pd.read_csv('data/geneAndTimeData/bwm_csv/bwm_' + 'anterior' + '_time_bins.csv').columns.tolist()

f = open('/home/rohit/Documents/scRNA-seq/data/muscleTFStuff/muscle_tfs.txt')
tf = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/muscle_functional_genes.txt')
func_genes = f.read().splitlines()
f.close()

genes = tf + func_genes
genes_idx = [i+1 for i, val in enumerate(columns) if val in genes]
genes_idx.insert(0,0)

df_dict = {}
bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']

for i in muscles:
    df_dict[i] = pd.read_csv('data/geneAndTimeData/bwm_csv/' + i.lower() + '_time_bins.csv', index_col=0, usecols=genes_idx)

df_final_dict = {}
for bin in bins:
    df = pd.DataFrame(columns = df_dict['BWM_anterior'].columns)
    for cell, cell_df in df_dict.items():
        df.loc[cell] = cell_df.loc[cell + ':' + bin] 

    df_final_dict[bin] = df 
        
for key, val in df_final_dict.items():
    if mean_subtract:
        val = val.sub(val.mean(axis=0), axis=1)

    if normalize_by_gene:
        val = (val-val.mean())/val.std()
        val = val.fillna(0)

    if normalize_by_cell:
        # val +=1 
        adata = AnnData(val)
        val = sc.pp.normalize_total(adata, inplace=False, exclude_highly_expressed = True)['X']

    pca = PCA(n_components=5)
    pca.fit(val)

    evr = ["{:.7f}".format(i) for i in pca.explained_variance_ratio_.tolist()]

    df = pd.DataFrame(pca.components_, index=evr, columns=df_dict['BWM_anterior'].columns)


    adjustment = get_adjustment()

    outfile = adjustment + '_' + key + ':pca.csv'
    df.to_csv('pca/' + outfile)
