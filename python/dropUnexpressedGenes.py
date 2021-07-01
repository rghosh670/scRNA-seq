import pandas as pd

data = pd.read_csv("~/Desktop/rawReads.csv")
data = data.loc[:, (data != 0).any(axis=0)]

data.to_csv('~/Desktop/rawReadsWithoutUnexpressedGenes.csv', index = False)