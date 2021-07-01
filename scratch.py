import pandas as pd
from anndata import AnnData
import scanpy as sc

df = pd.read_csv('data/de_analysis_part2/impulse_de2_input.csv', index_col=[0])
# print(df)


adata = AnnData(df)
X_norm = sc.pp.normalize_total(adata, target_sum=1, inplace=False)['X']
print(X_norm)

df = pd.DataFrame(X_norm, index = df.index, columns = df.columns)
df *= 100
df = df.astype(int)
print(df)

df += 1
df.to_csv('normalized_input.csv')