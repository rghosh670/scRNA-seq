import pandas as pd


f = open('data/listOfGenes.txt', 'r')
genes = f.read().splitlines()
genes.append('cell')
f.close()

t6 = pd.read_csv('data/t6.csv', index_col = [0], usecols=genes)
sum = t6.sum(axis = 1).tolist()

t6sum = pd.DataFrame(index = t6.index)
t6sum['sum'] = sum

t6sum.to_csv('data/t6sum.csv')