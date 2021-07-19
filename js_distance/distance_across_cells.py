import numpy as np
import pandas as pd
from scipy.spatial import distance
import itertools

use_tfs = True

f = open('data/muscleTFStuff/muscle_tfs.txt', 'r')
tf = f.read().splitlines()
f.close()

muscles = ['bwm_anterior', 'bwm_far_posterior', 'bwm_head_row_1', 'bwm_head_row_2', 'bwm_posterior']
bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']

genes = pd.read_csv('data/geneAndTimeData/bwm_csv/bwm_anterior_time_bins.csv', index_col=0, skiprows=lambda x:x not in [0]).columns.tolist()

idx = []

for i, v in enumerate(genes):
    if v in tf:
        idx.append(i+1)

idx.insert(0,0)

if not use_tfs:
    idx = list(range(len(genes)))

df_dict = {}
for muscle in muscles:
    df_dict[muscle] = pd.read_csv('data/geneAndTimeData/bwm_csv/' + muscle + '_time_bins.csv', index_col=0, usecols=idx)
    df_dict[muscle] = df_dict[muscle].drop('mean')


for bin in bins:
    result = pd.DataFrame(index = muscles, columns = muscles)

    for a, b in itertools.combinations(muscles, 2):
        dist = distance.jensenshannon(df_dict[a].loc[bin], df_dict[b].loc[bin])
        result.at[a,b] = dist

    print(result)
    outfile = 'js_distance/across_cells/' + bin + '_distance.csv' if not use_tfs else 'js_distance/across_cells/tf_' + bin + '_distance.csv'
    result.to_csv(outfile)