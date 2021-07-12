import pandas as pd
import numpy as np
from scipy import stats

norm = 'raw'

genes = pd.read_csv('pca/' + norm + '/' + norm + '_HVGs.csv', index_col=0).index.tolist()

cols = ['slope', 'interecept', 'r', 'p', 'std_err']

result = pd.DataFrame(index = genes, columns = cols)

df  = pd.read_csv('pca/' + norm + '/' + norm + '_first_components_abs.csv', index_col=0, usecols=genes)


x = [300, 360, 420, 480, 545, 615, 690]

for index, col in df.iteritems():
    fit = list(stats.linregress(x,col.tolist()))
    result.loc[index] = fit


r = result['r'].tolist()
r2 = [i ** 2 for i in r]
result['r^2'] = r2

result.to_csv('pca/' + norm + '/' + norm + '_linear_fit.csv')

print(result)