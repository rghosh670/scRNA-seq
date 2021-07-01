import scanpy as sc
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/averagedExpressionOverTime.csv', header = [0], index_col = [0])
adata = sc.AnnData(data)

# sc.tl.pca(adata, svd_solver='arpack')
# sc.pl.pca_variance_ratio(adata, log=True)

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=20, use_rep = 'X')
sc.tl.umap(adata)

sc.tl.leiden(adata)

sc.pl.umap(adata, color = ['leiden'], save = 'leiden2.png')
sc.tl.rank_genes_groups(adata, 'leiden', method='wilcoxon')

adata.obs[['leiden']].to_csv('leiden2.csv')
print('done')


