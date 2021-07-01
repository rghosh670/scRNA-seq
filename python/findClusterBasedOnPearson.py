import pandas as pd
import json
import numpy as np

df = pd.read_csv('data/muscleTFStuff/overall_correlationBetweenTFAndCluster.csv', index_col=0)

for cluster in df.columns:
    df[cluster] = df[cluster].apply(lambda x: int(-2) if '*' in x else x)
    df[cluster] = pd.to_numeric(df[cluster])

max = df.idxmax(axis=1).tolist()
genes = df.index

finalDict = {}
for index, value in enumerate(max):
    max[index] = value.replace('ward_cluster', '')
    finalDict[genes[index]] = max[index]

# with open('data/muscleTFStuff/clusterBasedOnPearson.txt', 'w') as f: # write out results to text file
#     for item in max:
#         f.write("%s\n" % item)

# f.close()

with open('data/muscleTFStuff/clusterBasedOnPearson.txt', 'w') as outfile:
    json.dump(finalDict, outfile)

outfile.close()