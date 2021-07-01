import magic
import pandas as pd
import matplotlib.pyplot as plt

geneList = ['unc-10', 'rab-3', 'mps-2']

rawData = pd.read_csv("~/Desktop/transposedEset.csv", usecols = geneList)

plot1 = plt.figure(num = 'Raw Data')
plt.scatter(rawData[geneList[0]], rawData[geneList[1]], c=rawData[geneList[2]], s=1, cmap='inferno')

plt.show()
