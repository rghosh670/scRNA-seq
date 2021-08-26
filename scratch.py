import pandas as pd
import scanpy as sc
import os

chr = ['II', 'III', 'IV', 'V', 'X']

result_df  = pd.read_csv('chip-seq/utr/utr_chr' + 'I' + '.csv', index_col=0)
for chr_num in chr:
    df = pd.read_csv('chip-seq/utr/utr_chr' + chr_num + '.csv', index_col=0)
    result_df = result_df.append(df)


print(result_df)
result_df.to_csv('chip-seq/utr/full_utr.csv')