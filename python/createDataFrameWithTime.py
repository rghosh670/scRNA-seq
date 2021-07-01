import pandas as pd
import numpy as np
from cellNames import getCellName
import statistics
from statistics import mean

NUMCELLS = 37148

cellList = []
for i in range(NUMCELLS):
    cellList.append(getCellName(i))

userCell = input('Enter cell name: ').strip()

if userCell =='all_cells':
    rowList = [*range(1, NUMCELLS+1)]
else:
    rowList = [i + 1 for i, value in enumerate(cellList) if (value == userCell or userCell in value and type(value) is tuple)]

if not rowList:
    print('Not a valid cell')
    exit()

rowList.insert(0, 0)

f = open('data/usefulTimes.txt', 'r')
timeList = f.read().splitlines()
timeList = [timeList[i-1] for i in rowList[1:]]
f.close()

f = open('data/listOfGenes.txt', 'r')
geneList = f.read().splitlines()
f.close()

eset = pd.read_csv('data/rawReads.csv', index_col = None, skiprows = lambda x : x not in rowList, header = 0)

timeListWithoutDuplicates = list(dict.fromkeys(timeList))

df = pd.DataFrame(index=geneList,
                  columns=timeListWithoutDuplicates)

for i in df.columns:
    df[i]=  np.empty((len(df), 0)).tolist()


for row, expressionSeries in eset.iterrows():
    for i in range(len(expressionSeries.index)):
        if expressionSeries.values[i] != 0.0:
            try:
                df.at[expressionSeries.index[i], timeList[row]] = df.at[expressionSeries.index[i], timeList[row]] + [float(expressionSeries.values[i])]
            except:
                print(expressionSeries.index[i], timeList[row])

for i in df.columns:
    df[i] = df[i].apply(lambda y: 1e-10 if len(y)==0 else y)
    df[i] = df[i].apply(lambda y: mean(y) if type(y) == list else y)

df = df.reindex(sorted(df.columns), axis=1)

df = df[(df.T != 1e-10).any()]

df.to_csv('data/averagedExpressionOverTime.csv')
exec(open('python/sendEmail.py').read())

