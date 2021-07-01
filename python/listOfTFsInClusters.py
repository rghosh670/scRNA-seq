f = open('data/muscleTFStuff/transcriptionFactors.txt', 'r')
tf = f.read().splitlines()
f.close()

f = open('data/muscleTFStuff/clusterOfTranscriptionFactors.txt', 'r')
clusterList = f.read().splitlines()
indices = [i for i, x in enumerate(clusterList) if x == '-1']
tf = [i for j, i in enumerate(tf) if j not in indices]
f.close()

with open('data/muscleTFStuff/listOfTFsInClusters.txt', 'w') as f: # write out results to text file
    for item in tf:
        f.write("%s\n" % item)

f.close()