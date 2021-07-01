import pandas as pd

ward = pd.read_csv('wardClusters/wardCellBinScore.csv', index_col = 0)
leiden = pd.read_csv('leidenClusters/leidenCellBinScore.csv', index_col = 0)

df = ward.copy(deep = True)

for i in leiden.columns:
    df[i] = leiden[i]

df.to_csv('data/combinedCellBinScore.csv')
print(df)


