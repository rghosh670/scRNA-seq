import pandas as pd

eset = pd.read_csv('data/rawReads.csv', index_col=None, header = 0)

f = open('data/namesOfNeuronalCells.txt', 'r')
names = f.read().splitlines()
f.close()

eset.index = names
eset.to_csv('data/rawReadsWithCellNames.csv')