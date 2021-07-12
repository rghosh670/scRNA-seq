import pandas as pd

norm = 'raw'

df  = pd.read_csv('pca/' + norm + '/' + norm + '_first_components.csv', index_col=0)
df = df.abs()
df.to_csv('pca/' + norm + '/' + norm + '_first_components_abs.csv')