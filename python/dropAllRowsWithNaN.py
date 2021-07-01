import pandas as pd

df = pd.read_csv('data/variance_t6.csv', index_col=0)
df.dropna(axis = 0, how = 'all', inplace = True)

df.to_csv('data/variance_t6.csv')