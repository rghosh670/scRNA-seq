import pandas as pd
import numpy as np

raw_reads = pd.read_csv('data/geneAndTimeData/bwm_raw_reads.csv', index_col=0)
cells = raw_reads.index.tolist()

f = open('data/geneAndTimeData/bwm_times.txt', 'r')
times = [int(i) for i in f.read().splitlines()]
f.close()

bins = [(200, 270), (270, 330), (330, 390), (390, 450), (450, 510), (510, 580), (580, 650), (650, 840)]

def return_bin(i):
    for bin in bins:
        if bin[0] <= i < bin[1]:
            return bin

    print(i)


bwm_anterior_dict = {}
bwm_far_posterior_dict = {}
bwm_head_row_1_dict = {}
bwm_head_row_2_dict = {}
bwm_posterior_dict = {}

bwm_list = [bwm_anterior_dict, bwm_far_posterior_dict, bwm_head_row_1_dict, bwm_head_row_2_dict, bwm_posterior_dict]

for i in range(len(cells)):
    if 'BWM_anterior' in cells[i]:
        temp_df = bwm_anterior_dict.setdefault('BWM_anterior' + str(return_bin(times[i])), pd.DataFrame()).append(raw_reads.iloc[i])
        bwm_anterior_dict['BWM_anterior' + str(return_bin(times[i]))] = temp_df

    if 'BWM_far_posterior' in cells[i]:
        temp_df = bwm_far_posterior_dict.setdefault('BWM_far_posterior' + str(return_bin(times[i])), pd.DataFrame()).append(raw_reads.iloc[i])
        bwm_far_posterior_dict['BWM_far_posterior' + str(return_bin(times[i]))] = temp_df

    if 'BWM_head_row_1' in cells[i]:
        temp_df = bwm_head_row_1_dict.setdefault('BWM_head_row_1' + str(return_bin(times[i])), pd.DataFrame()).append(raw_reads.iloc[i])
        bwm_head_row_1_dict['BWM_head_row_1' + str(return_bin(times[i]))] = temp_df

    if 'BWM_head_row_2' in cells[i]:
        temp_df = bwm_head_row_2_dict.setdefault('BWM_head_row_2' + str(return_bin(times[i])), pd.DataFrame()).append(raw_reads.iloc[i])
        bwm_head_row_2_dict['BWM_head_row_2' + str(return_bin(times[i]))] = temp_df

    if 'BWM_posterior' in cells[i]:
        temp_df = bwm_posterior_dict.setdefault('BWM_posterior' + str(return_bin(times[i])), pd.DataFrame()).append(raw_reads.iloc[i])
        bwm_posterior_dict['BWM_posterior' + str(return_bin(times[i]))] = temp_df

for dictionary in bwm_list:
    for key, val in dictionary.items():
        val.to_csv('data/geneAndTimeData/bwm_csv/' + str(key) + '.csv')