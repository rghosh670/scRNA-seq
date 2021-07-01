import cellNames
from cellNames import getCellName
import statistics
import csv

f = open('data/usefulTimes.txt', 'r')
times = [int(x) for x in f.read().splitlines()]
f.close()

cellDict = {}

medianTime = statistics.median(times)

for i in range(cellNames.NUM_CELLS):
    cellDict.setdefault(getCellName(i, False), []).append(1 if times[i] <= medianTime else 2)

print(cellDict)

with open('test.csv', 'w') as f:
    for key in cellDict.keys():
        f.write("%s,%i\n"%(key,', '.join(cellDict[key])))