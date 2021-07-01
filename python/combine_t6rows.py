import pandas as pd
import numpy as np
from scipy import stats, mean
import matplotlib.pyplot as plt

t6 = pd.read_csv('data/t6.csv', index_col=0)

cellNames = []
indexDict = {}
for i in range(len(t6.index)):
    cell = t6.index[i][0:t6.index[i].index(':')] if t6.index[i].find(':') != -1 else t6.index[i]
    cellNames.append(cell)
    indexDict.setdefault(cell, []).append(i)


sumDF = pd.DataFrame(0, index = list(dict.fromkeys(cellNames)), columns = t6.columns)

for key, indexList in indexDict.items():
    for value in indexList:
        sumDF.loc[key] = sumDF.loc[key] + t6.iloc[value]

sumDF.to_csv('data/combined_t6.csv')