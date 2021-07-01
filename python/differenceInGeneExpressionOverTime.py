import pandas as pd
import numpy as np
from scipy import stats, mean
import matplotlib.pyplot as plt

cluster_type = 'ward'
num_clusters = 16

for k in range(num_clusters):
    f = open(cluster_type + 'clusters/cluster' + str(k) + '.txt', 'r')
    genes = f.read().splitlines()
    genes.insert(0, 'cell')
    f.close()

    t6 = pd.read_csv('data/t6.csv', index_col=0, usecols=genes)
    combined_t6 = pd.read_csv('data/combined_t6.csv', index_col=0, usecols=genes)


    cellNames = []
    timeBins = []
    for i in range(len(t6.index)):
        cell = t6.index[i][0:t6.index[i].index(':')] if t6.index[i].find(':') != -1 else t6.index[i]
        timeBin = t6.index[i][t6.index[i].index(':') + 1:] if t6.index[i].find(':') != -1 else t6.index[i]
        cellNames.append(cell)
        timeBins.append(timeBin)

    differenceDF = pd.DataFrame(columns = t6.columns)

    for i in range(1, len(cellNames)):
        if(cellNames[i] == cellNames[i-1]):
            differenceDF.loc[cellNames[i] + ':' + timeBins[i] + '-' + timeBins[i-1]] = abs(t6.loc[t6.index[i]] - t6.loc[t6.index[i-1]])#/combined_t6.loc[cellNames[i]]

    differenceDF.fillna(0, inplace=True)

    differenceDF.loc['sum'] = differenceDF.sum(axis = 0)
    sum = [round(i) for i in differenceDF.loc['sum'].tolist()]

    differenceDF.loc['sum'].plot(kind = 'bar')
    differenceDF.to_csv('data/geneDifferenceOverTime/' + cluster_type + 'Cluster' + str(k) + '.csv')