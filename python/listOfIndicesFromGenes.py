f = open('data/geneAndTimeData/listOfAllGenes.txt', 'r')
geneList = f.read().splitlines()
f.close()

def get_indices(genes):
    indices = [i for i,j in enumerate(geneList) if j in genes]
    return indices
