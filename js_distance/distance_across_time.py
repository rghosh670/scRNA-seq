import numpy as np
import pandas as pd
from scipy.spatial import distance
import itertools

use_tfs = True

f = open('data/muscleTFStuff/muscle_tfs.txt', 'r')
tf = f.read().splitlines()
f.close()

muscles = ['bwm_anterior', 'bwm_far_posterior', 'bwm_head_row_1', 'bwm_head_row_2', 'bwm_posterior']

genes = pd.read_csv('data/geneAndTimeData/bwm_csv/bwm_anterior_time_bins.csv', index_col=0, skiprows=lambda x:x not in [0]).columns.tolist()

idx = []

for i, v in enumerate(genes):
    if v in tf:
        idx.append(i+1)

idx.insert(0,0)

if not use_tfs:
    idx = list(range(genes))

for muscle in muscles:
    df = pd.read_csv('data/geneAndTimeData/bwm_csv/' + muscle + '_time_bins.csv', index_col=0, usecols=idx)
    df = df.drop('mean')
    print(df)

    index = df.index.tolist()
    result = pd.DataFrame(index = index, columns = index)
    for a, b in itertools.combinations(index, 2):
        dist = distance.jensenshannon(df.loc[a], df.loc[b])
        result.at[a,b] = dist

    print(result)
    outfile = 'js_distance/across_time/' + muscle + '_distance.csv' if not use_tfs else 'js_distance/across_time/tf_' + muscle + '_distance.csv'
    result.to_csv(outfile)