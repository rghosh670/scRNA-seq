import pandas as pd
import json

f = open('data/muscleTFStuff/transcriptionFactors.txt', 'r')
tf = f.read().split()
f.close()

listOfGeneLists = []
for j in range(0,16):
    f = open('wardClusters/cluster' + str(j) + '.txt', 'r')
    geneList = f.read().splitlines()
    f.close()
    listOfGeneLists.append(geneList)

tfCluster = {}
for i in range(len(tf)):
    found = False
    for geneListIndex, geneList in enumerate(listOfGeneLists):
        if tf[i] in geneList:
            tfCluster[tf[i]] = geneListIndex
            found = True
            break

    if not found:
        tfCluster[tf[i]] = -1

# with open('data/muscleTFStuff/muscleClusterList.txt', 'w') as f: # write out results to text file
#     for item in tfCluster:
#         f.write("%s\n" % item)

# f.close()

with open('data/muscleTFStuff/wardClusterDict.txt', 'w') as outfile:
    json.dump(tfCluster, outfile)

outfile.close()