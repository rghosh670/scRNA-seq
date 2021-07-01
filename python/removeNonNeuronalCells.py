import pandas as pd

f = open('/home/rohit/Desktop/indicesOfUsefulCells.txt', 'r')
indices = f.read().splitlines()
f.close()

indices = [int(i) + 1 for i in indices]
indices.insert(0, 0)

eset = pd.read_csv('~/Desktop/rawReads.csv',
                   skiprows=lambda x: x not in indices, header = 0)

eset.to_csv('~/Desktop/rawReads2.csv', index = False)
