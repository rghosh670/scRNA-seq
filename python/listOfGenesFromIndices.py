for j in range(0,16):
    f = open('muscle_clusters/cluster' + str(j) + '.txt', 'r') # read in indices of 37000 cells
    indexList = f.read().splitlines()
    indexList = [int(i) for i in indexList]
    f.close()

    f = open('data/geneAndTimeData/noUnexpressedGenes.txt', 'r') # read in indices of 37000 cells
    geneList = f.read().splitlines()
    f.close()

    clusterGenes = [geneList[i] for i in indexList]
    print(clusterGenes)
    print(len(clusterGenes))

    with open('muscle_clusters/cluster' + str(j) + '.txt', 'w') as f: # write out results to text file
        for item in clusterGenes:
            f.write("%s\n" % item)

    f.close()
