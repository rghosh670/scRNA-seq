import magic
import pandas as pd
import matplotlib.pyplot as plt
from cellNames import getCellColor

geneList = ['unc-62', 'ceh-20', 'mps-2']

rawData = pd.read_csv("~/Desktop/rawReads.csv", usecols = geneList)
magicWithNormalization = pd.read_csv('~/Desktop/magicOutput/magicWithNormalization17.csv', usecols = geneList)

cellColors = []
for i in range(len(rawData.index)):
    cellColors.append(getCellColor(i))


# plot1 = plt.figure(num = 'Raw Data')
# plt.scatter(rawData[geneList[0]], rawData[geneList[1]], c=rawData[geneList[2]], s=1, cmap='inferno')

plot3 = plt.figure(num = geneList[0] + ' vs. ' + geneList[1])
plt.scatter(magicWithNormalization[geneList[0]], magicWithNormalization[geneList[1]], c=cellColors, s=1, cmap='inferno')


# plots = []
# csv = []
# for i in range(1, 20, 2):
#     plots.append(plt.figure(num = geneList[0] + ' vs. ' + geneList[1] + ' ' + str(i)))
#     csv.append(pd.read_csv('/home/rohit/Desktop/magicOutput/magicWithNormalization' + str(i) + '.csv', usecols = geneList))
#     plt.scatter(csv[i//2][geneList[0]], csv[i//2][geneList[1]], c = cellColors, s = 1, cmap = 'inferno')

# magic_operator = magic.MAGIC()
# magic_operator.fit_transform(rawData, genes = geneList)
# magic.plot.animate_magic(rawData, gene_x=geneList[0], gene_y=geneList[1], gene_color=geneList[2], operator=magic_operator)._start()

plt.show()
