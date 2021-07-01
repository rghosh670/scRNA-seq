import pandas as pd
from listOfIndicesFromGenes import get_indices
from scipy import stats
import math

f = open('data/muscleTFStuff/transcriptionFactors.txt', 'r')
tf = f.read().splitlines()
f.close()

tf.append('cell')

t6 = pd.read_csv('data/t6Stuff/t6.csv', index_col = 0, usecols=tf)
t6 = t6['BWM_anterior:210_270':'BWM_posterior:gt_650']
t6 = t6.loc[:, (t6 != 0).any(axis=0)]

cellScore = pd.read_csv('wardClusters/wardCellBinScore.csv', index_col=0)
cellScore = cellScore['BWM_anterior:210_270':'BWM_posterior:gt_650']
cellScore = cellScore.loc[:, (cellScore != 0).any(axis=0)]

df = pd.DataFrame(index=t6.columns, columns=cellScore.columns)

for gene in t6.columns:
    for cluster in cellScore:
        correlation, p_value = stats.pearsonr(t6.loc[:,gene], cellScore.loc[:,cluster])
        correlation = correlation if p_value < 0.5 else '*' + str(correlation)
        df.at[gene, cluster] = correlation

df.to_csv('data/muscleTFStuff/overall_correlationBetweenTFAndCluster.csv')