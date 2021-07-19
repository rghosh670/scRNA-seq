import pandas as pd
import numpy as np
from scipy import stats

norm = 'transcription_factor'

# genes = pd.read_csv('pca/' + norm + '/' + norm + '_HVGs.csv', index_col=0).index.tolist()
genes = pd.read_csv('more_tfs.csv', index_col=0).index.tolist()

cols = ['slope_e5', 'interecept', 'r', 'p', 'std_err']

result = pd.DataFrame(index = genes, columns = cols)

df  = pd.read_csv('pca/' + norm + '/' + norm + '_first_components_abs.csv', index_col=None, usecols=genes)

df = df.replace(0,1e-10)

x = [300, 360, 420, 480, 545, 615, 690]

for index, col in df.iteritems():
    y = col.tolist()
    fit = list(stats.linregress(x,y))
    result.loc[index] = fit


r = result['r'].tolist()
r2 = [i ** 2 for i in r]
result['r^2'] = r2

result['slope_e5'] = [i *10000 for i in result['slope_e5']]
# result.to_csv('pca/' + norm + '/' + norm + '_linear_fit.csv')
result.to_csv('more_tfs_linear_fit.csv')



print(result)