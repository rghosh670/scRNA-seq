import pandas as pd
import statistics
from cellNames import getCellName

NUM_CELLS = 37148
MEDIAN_TIME = 405.0

f = open('data/usefulTimes.txt', 'r')
timeList = f.read().splitlines()
timeList = [int(i) for i in timeList]
f.close()

result_list = []
for i in timeList:
    result_list.append(1 if i <= MEDIAN_TIME else 2)

with open('group.txt', 'w') as f: # write out results to text file
    for item in result_list:
        f.write("%s\n" % item)

f.close()
