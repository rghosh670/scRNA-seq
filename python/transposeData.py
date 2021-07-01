import pandas as pd

data = pd.read_csv('data/rawReadsWithCellNames.csv', index_col=0)
data = data.transpose()
data.to_csv('data/transposedRawReadsWithCellNames.csv')
print(data)