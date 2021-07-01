import pandas as pd
from listOfIndicesFromGenes import get_indices
from scipy import stats
import math

f = open('data/muscleTFStuff/transcriptionFactors.txt', 'r')
tf = f.read().splitlines()
tf.append('cell')
f.close()

t6 = pd.read_csv('data/t6Stuff/t6.csv', index_col = 0, usecols=tf)
t6 = t6['BWM_anterior:210_270':'BWM_posterior:gt_650']

t6_dict = {}
for i in t6.index:
    t6_dict[i[:i.index(':')]] = t6_dict.setdefault(i[:i.index(':')], pd.DataFrame(columns=t6.columns)).append(t6.loc[i])

cellScore = pd.read_csv('wardClusters/wardCellBinScore.csv', index_col=0)
cellScore = cellScore['BWM_anterior:210_270':'BWM_posterior:gt_650']

cellScore_dict = {}
for i in cellScore.index:
    cellScore_dict[i[:i.index(':')]] = cellScore_dict.setdefault(i[:i.index(':')], pd.DataFrame(columns=cellScore.columns)).append(cellScore.loc[i])

for i in t6_dict.keys():
    t6_dict[i] = t6_dict[i].loc[:, (t6_dict[i] != 0).any(axis=0)]
    cellScore_dict[i] = cellScore_dict[i].loc[:, (cellScore_dict[i] != 0).any(axis=0)]

df = pd.DataFrame(index=t6.columns, columns=t6_dict.keys())
for i in t6_dict.keys():
    isna = df[i].isna()
    df.loc[isna, i] = pd.Series([[]] * isna.sum()).values


for cell in t6_dict.keys():
    for index, gene in enumerate(t6_dict[cell].columns):
        for cluster in cellScore:
            correlation, p_value = stats.pearsonr(t6_dict[cell].loc[:,gene], cellScore_dict[cell].loc[:,cluster])
            df.at[gene, cell] = df.at[gene, cell] + [correlation]

df.to_csv('data/muscleTFStuff/muscle_correlationBetweenTFAndCluster.csv')