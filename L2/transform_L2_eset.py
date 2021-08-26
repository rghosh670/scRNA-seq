from matplotlib.colors import Normalize
import pandas as pd
from anndata import AnnData
import scanpy as sc

norm = True

def normalize(df, cols, index):
    df = df.T
    df = df + 1
    adata = AnnData(df)

    df = sc.pp.normalize_total(adata, inplace=False, exclude_highly_expressed = True)['X']

    df = pd.DataFrame(df)
    df = df.T

    df.columns = cols
    df.index = index
    return df

df = pd.read_csv('L2/L2_tf_bwm_eset.csv', index_col=0)
cols = df.columns.tolist()

# cols = [i[:i.rfind('.')] for i in cols]
for count in range(len(cols)):
    i = cols[count]
    if '.' in i:
        cols[count] = i[:i.find('.')]

index = df.index
df = normalize(df, cols, index)

gene_dict = {}
df.columns = cols

cell_count = {x:cols.count(x) for x in cols}

for index, row in df.iterrows():
    gene_dict[index] = {}
    for cell, val in row.iteritems():
        x = gene_dict[index].setdefault(cell,0)
        x += val
        gene_dict[index][cell] = x

index = df.index
cols = gene_dict['nhr-256'].keys()
result = pd.DataFrame(index = df.index, columns=cols)

for i in result.index.tolist():
    result.loc[i] = list(gene_dict[i].values())

result.to_csv('L2/L2_eset_by_muscle_subtype.csv')

