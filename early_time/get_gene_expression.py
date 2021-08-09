import pandas as pd
import numpy as np

muscles = ['bwm_anterior', 'bwm_far_posterior', 'bwm_head_row_1', 'bwm_head_row_2', 'bwm_posterior']
bins = ['210_270', '270_330', '330_390', '390_450']

df = pd.read_csv('num_cells.csv', index_col=0)

df = df[df['num_cells'] > 4]

index = []
for i in df.index.tolist():
    for bin in bins:
        index.append(i + '/' + bin)

muscle_dict = {}

for muscle in muscles:
    muscle_dict[muscle] = pd.read_csv('data/geneAndTimeData/bwm_csv/' + muscle + '_time_bins.csv', index_col=0)

result = pd.DataFrame(index = index, columns = muscles)

bins = []

for i in result.index.tolist():
    bin = i[i.find('/')+1:]
    gene = i[:i.find('/')]


    for muscle in muscles:
        if bin in muscle_dict[muscle].index.tolist():
            print(bin,gene)
            result.at[i, muscle] = muscle_dict[muscle].at[bin, gene]

print(result)
result.to_csv('num_cells_data.csv')