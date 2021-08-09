import numpy as np
import pandas as pd

result = pd.read_csv('more_tfs/more_tfs.csv', index_col=0)
genes = result.index.tolist()

x = result.columns.tolist()

for i in range(5):
    x[i] = 'PC_' + x[i]

result.columns = x

gene_list = pd.read_csv('gene_fits.csv', index_col=0).index.tolist()

idx = []

for i,v in enumerate(gene_list):
    if v in genes:
        idx.append(i+1)

idx.insert(0,0)

gene_fits = pd.read_csv('gene_fits.csv', index_col=0, skiprows = lambda x:x not in idx)


result['slope_e5'] = np.nan
result['std_err_e5'] = np.nan


for index, row in gene_fits.iterrows():
    result.at[index, 'slope_e5'] = row['estimate']
    result.at[index, 'std_err_e5'] = row['std_err']

gene_list = pd.read_csv('more_tfs_linear_fit.csv', index_col=0).index.tolist()

idx = []

for i,v in enumerate(gene_list):
    if v in genes:
        idx.append(i+1)

idx.insert(0,0)

linear_fit = pd.read_csv('more_tfs_linear_fit.csv', index_col=0, skiprows = lambda x:x not in idx)

print(linear_fit)

result['pca_slope_e5'] = np.nan
result['pca_r^2'] = np.nan


for index, row in linear_fit.iterrows():
    result.at[index, 'pca_slope_e5'] = row['slope_e5']
    result.at[index, 'pca_r^2'] = row['r^2']


for index, row in gene_fits.iterrows():
    result.at[index, 'slope_e5'] = row['estimate']
    result.at[index, 'std_err_e5'] = row['std_err']

gene_list = pd.read_csv('pca/pca_markers/max_pca_marker_time_bin_270_330.csv', index_col=0).index.tolist()

idx = []

for i,v in enumerate(gene_list):
    if v in genes:
        idx.append(i+1)

idx.insert(0,0)

bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']
df_dict = {}

for bin in bins:
    df = pd.read_csv('pca/pca_markers/max_pca_marker_time_bin_' + bin + '.csv', index_col=0)
    df_dict[bin] = df
    print(df)

result['specificity_cell'] = [""] * len(result)
result['specificity'] = np.nan

for index, row in result.iterrows():
    if index in df_dict[row['time_bin']].index.tolist():
        result.at[index, 'specificity_cell'] = df_dict[row['time_bin']].at[index, 'cell_group']
        result.at[index, 'specificity'] = df_dict[row['time_bin']].at[index, 'specificity']


print(result)
exit()
result.to_csv('more_tfs.csv')
