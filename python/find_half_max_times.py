import pandas as pd
import json

f = open('data/geneAndTimeData/de_analysis_part2/all_up.txt', 'r')
all_up = f.read().splitlines()
f.close()

genes = pd.read_csv('data/geneAndTimeData/de_analysis_part2/impulse_de2_input.csv', index_col=0).index.tolist()

all_up_idx = [i+1 for i, val in enumerate(genes) if val in all_up]
all_up_idx.insert(0,0)

impulse_input = pd.read_csv('data/geneAndTimeData/de_analysis_part2/impulse_de2_input.csv', index_col=0, skiprows=lambda x:x not in all_up_idx)
print(impulse_input)


df = pd.DataFrame(index=impulse_input.index)
bins = impulse_input.columns.tolist()

def get_time_from_bin(bin):
    b1 = bin[:bin.find('_')]
    b2 = bin[bin.find('_')+1:]

    if b1 != 'gt':
        return (int(b1) + int(b2))/2
    else:
        return 690

def parse_bin(bin):
    for i in range(len(bins)):
        if bins[i] == bin:
            return (get_time_from_bin(bins[i]) + get_time_from_bin(bins[i-1]))/2
    
    return None
 

half_max_times = []

for index, row in impulse_input.iterrows():
    half_max = row.max()/2

    for i in range(len(row.tolist())):
        if row.tolist()[i] >= half_max:
            half_max_times.append(parse_bin(bins[i]))
            break

df['half_max'] = half_max_times
df.to_csv('data/geneAndTimeData/de_analysis_part2/half_max_times.csv')