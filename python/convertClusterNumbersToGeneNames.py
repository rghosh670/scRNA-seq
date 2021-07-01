import pandas as pd

f = open('data/geneAndTimeData/listOfAllGenes.txt', 'r')
genes = f.read().splitlines()
f.close()

for j in range(16):
    f = open('muscle_clusters2/cluster' + str(j) + '.txt', 'r')
    nums = f.read().splitlines()
    nums = [int(i) for i in nums]
    f.close()

    geneList = [genes[i] for i in nums]

    with open('muscle_clusters2/cluster' + str(j) + '.txt', 'w') as f: # write out results to text file
        for item in geneList:
            f.write("%s\n" % item)

    f.close()


# cellScore.to_csv('wardClusters/wardCellBinScore.csv')
