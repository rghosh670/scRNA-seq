import pandas as pd

f = open('data/listOfGenes.txt', 'r')
genes = f.read().splitlines()
f.close()

f = open('data/listOfAllGenes.txt', 'r')
allGenes = f.read().splitlines()
f.close()

uGenes = list(set(allGenes) - set(genes))

eset = pd.read_csv('data/t6.csv',index_col=[0], usecols=uGenes)
sum = eset.sum(axis = 1).tolist()

print(sum)

