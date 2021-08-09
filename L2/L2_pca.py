import pandas as pd
import json
from sklearn.decomposition import PCA
from anndata import AnnData
import scanpy as sc

mean_subtract = True

def get_adjustment():
    if mean_subtract:
        return 'mean_subtract'
    return ''


input = pd.read_csv('L2/L2_eset_by_muscle_subtype.csv', index_col=0).T
num_components = len(input.index)
cols = input.columns
print(input)

if mean_subtract:
    input = input.sub(input.mean(axis=0), axis=1)

pca = PCA(n_components=num_components)
pca.fit(input)

evr = ["{:.7f}".format(i) for i in pca.explained_variance_ratio_.tolist()]

df = pd.DataFrame(pca.components_, index=evr, columns=cols)
print(df)

adjustment = get_adjustment()

outfile = adjustment + '_' + 'pca_across_times.csv'
df.to_csv('L2/' + outfile)