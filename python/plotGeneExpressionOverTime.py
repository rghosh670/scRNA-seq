import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import random

NUMCELLS = 37148

cellList = []
for i in range(NUMCELLS):
    cellList.append(getCellName(i))

f = open('data/listOfGenes.txt', 'r')
geneList = f.read().splitlines()
f.close()

userCell = input('Enter cell name: ').strip()

if userCell =='all_cells':
    rowList = [*range(1, NUMCELLS+1)]
else:
    rowList = [i + 1 for i, value in enumerate(cellList) if (value == userCell or userCell in value and type(value) is tuple)]

rowList.insert(0, 0)

df = pd.read_csv('~/Desktop/rawDF.csv', index_col=[0])

def plot(indicesOfGenesToPlot, label = False):
    genes = [geneList[i] for i in indicesOfGenesToPlot]

    genePlot = plt.figure(num = 'Gene Expression in ' + userCell)
    ax1 = genePlot.add_subplot()

    for row, series in df.iterrows():
        if row in genes:
            ax1.scatter(df.columns, series, s = 1, color = [random.random(), random.random(), random.random()], cmap = 'inferno')

    plt.show()
    return
