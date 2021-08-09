from matplotlib.colors import Normalize
import pandas as pd
from anndata import AnnData
import scanpy as sc

norm = False

df = pd.read_csv('L2/L2_tf_bwm_eset.csv', index_col=0)
cols = df.columns.tolist()

# cols = [i[:i.rfind('.')] for i in cols]
for count in range(len(cols)):
    i = cols[count]
    if '.' in i:
        cols[count] = i[:i.find('.')]

index = df.index

gene_dict = {}
df.columns = cols

if norm:
    df = df.T
    adata = AnnData(df)
    df = sc.pp.normalize_total(adata, inplace=False, exclude_highly_expressed = True)['X']

    df = pd.DataFrame(df)
    df = df.T

    df.columns = cols
    df.index = index

cell_count = {x:cols.count(x) for x in cols}

for index, row in df.iterrows():
    gene_dict[index] = {}
    for cell, val in row.iteritems():
        x = gene_dict[index].setdefault(cell,0)
        x += val
        gene_dict[index][cell] = x

for key, val in gene_dict.items():
    for i in val.keys():
        gene_dict[key][i] /= cell_count[i] * 100


result = pd.DataFrame(index = df.index, columns=gene_dict['nhr-256'].keys())


for i in result.index.tolist():
    result.loc[i] = list(gene_dict[i].values())




result.to_csv('L2/L2_eset_by_muscle_subtype.csv')

