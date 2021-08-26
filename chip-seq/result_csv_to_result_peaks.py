import pandas as pd
import numpy as np

chr = ['I', 'II', 'III', 'IV', 'V', 'X']
comparison = ['in_between', 'greater_than', 'less_than']

for chr_num in chr:
    for comp in comparison:
        df = pd.read_csv('chip-seq/result_csv/chr' + chr_num + '_' + comp + '_five_prime.csv', index_col=0)

        peak_dict = {}

        for index, row in df.iterrows():
            peak_dict.setdefault(row['peak'],[]).append(row['five_prime_transcript'])

for key in peak_dict.keys():
    peak_dict[key] = list(set(peak_dict[key]))
    with open('chip-seq/transcripts_downstream_of_peak/' + key + '.txt', 'w') as f:
        for item in peak_dict[key]:
            f.write("%s\n" % item)

        f.close()
