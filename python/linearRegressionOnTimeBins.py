import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('data/combinedCellBinScore.csv', index_col=0)

cellNames = []
indexDict = {}
timeBinMidpoints = {}

for i in range(len(df.index)):
    if df.index[i].find(':') != -1 and 'pseudotime' not in df.index[i]:
        cell = df.index[i][0:df.index[i].index(':')]
        timeBinMidpoint = df.index[i][df.index[i].index(':') + 1:]
        timeBinMidpoint = (float(timeBinMidpoint[:timeBinMidpoint.index('_')]) + float(timeBinMidpoint[timeBinMidpoint.index('_')+1:]))/2 if timeBinMidpoint[:timeBinMidpoint.index('_')] != 'gt' else float(timeBinMidpoint[timeBinMidpoint.index('_')+1:])
        cellNames.append(cell)
        timeBinMidpoints.setdefault(cell, []).append(timeBinMidpoint)
        indexDict.setdefault(cell, []).append(i)

indexDict = {k: v for k, v in indexDict.items() if len(v) > 1}
timeBinMidpoints = {k: v for k, v in timeBinMidpoints.items() if len(v) > 1}


result_df = pd.DataFrame(index = list(indexDict.keys()), columns = df.columns)
result_df = result_df.astype('object')

for i in range(len(df.columns)):
    for cell, indexList in indexDict.items():
        x = df.iloc[:,i][indexList]
        y = timeBinMidpoints[cell]
        result = list(stats.linregress(x,y))
        result_df[df.columns[i]][cell] = result

result_df.fillna(0, inplace=True)
result_df.to_csv('data/linearRegressionOnTimeBins.csv')
