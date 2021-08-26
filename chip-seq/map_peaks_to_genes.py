import pandas as pd
import numpy as np
import multiprocessing as mp

def largest_within_delta(X, k):
    X = np.asarray(X)
    right_idx = X.searchsorted(k,'right')-1
    return right_idx


def smallest_larger_than(arr, val):
    try:
        return list(map(lambda i: i> val, arr)).index(True)
    except:
        return None

def list_find_in_between(arr, val_1, val_2):
    return np.where((arr > val_1) & (arr < val_2))[0]

chr = ['I', 'II', 'III', 'IV', 'V', 'X']

for chr_num in chr:
    peak = pd.read_csv('chip-seq/peaks/chromosome_' + chr_num + '.csv', index_col=0)
    peak_idx = peak.index.tolist()
    peak.index = peak['End']

    utr = pd.read_csv('chip-seq/utr/utr_chr' + chr_num + '.csv', index_col=0)
    utr_idx = utr.index.tolist()

    peak_starts = peak['Start'].tolist()
    peak_ends = peak['End'].tolist()

    less_than_cols = ['five_prime_transcript', 'peak', 'five_prime_start', 'peak_start (used to compare)', 'peak_end', 'nearest_three_prime_end', 'three_prime_transcript']
    less_than_manager = mp.Manager().list()

    greater_than_cols = ['five_prime_transcript', 'peak', 'five_prime_end', 'peak_start', 'peak_end (used to compare)', 'nearest_three_prime_start', 'three_prime_transcript']
    greater_than_manager = mp.Manager().list()

    in_between_cols = ['five_prime_transcript', 'peak', 'five_prime_start', 'five_prime_end', 'peak_start', 'peak_end']
    in_between_manager = mp.Manager().list()

    def find_less_than(utr_index):
        utr_row = utr.iloc[utr_index]

        if 'five' in utr_row[2]:
            five_start = utr_row[3]
            three_index = utr_index
            three_end = five_start

            while three_index > 0:
                three_index -= 1

                if 'three' in utr.iloc[three_index][2]:
                    three_end = utr.iloc[three_index][4]
                    break
            
            peak_index = largest_within_delta(peak_starts, five_start)
            peak_start = peak.iloc[peak_index]['Start']
            peak_end = peak.iloc[peak_index]['End']
            
            while peak_start > three_end and peak_index > 0:
                new_row_list = [utr_idx[utr_index], peak_idx[peak_index], five_start, peak_start, peak_end, three_end, utr_idx[three_index]]
                new_row = pd.Series(new_row_list, index = less_than_cols)
                less_than_manager.append(new_row)
                peak_index -= 1
                peak_start = peak.iloc[peak_index]['Start']
                peak_end = peak.iloc[peak_index]['End']

    def find_greater_than(utr_index):
            utr_row = utr.iloc[utr_index]

            if 'five' in utr_row[2]:
                five_end = utr_row[4]
                three_index = utr_index
                three_start = five_end

                while three_index < len(utr) - 1:
                    three_index += 1

                    if 'three' in utr.iloc[three_index][2]:
                        three_start = utr.iloc[three_index][3]
                        break

                
                peak_index = smallest_larger_than(peak_ends, five_end)
                peak_start = peak.iloc[peak_index]['Start']
                peak_end = peak.iloc[peak_index]['End']


                while peak_end < three_start and peak_index < len(peak):
                    peak_end = peak.iloc[peak_index]['End']
                    peak_start = peak.iloc[peak_index]['Start']
                    new_row_list = [utr_idx[utr_index], peak_idx[peak_index], five_end, peak_start, peak_end, three_start, utr_idx[three_index]]
                    new_row = pd.Series(new_row_list, index = greater_than_cols)
                    greater_than_manager.append(new_row)
                    peak_index += 1


    def find_in_between(utr_index):
        utr_row = utr.iloc[utr_index]

        if 'five' in utr_row[2]:
            five_start = utr_row[3]
            five_end = utr_row[4]

            peak_start_index = list_find_in_between(peak_starts, five_start, five_end)

            if len(peak_start_index) > 0:
                for i in peak_start_index:
                    peak_start = peak.iloc[i]['Start']
                    peak_end = peak.iloc[i]['End']
                    new_row_list  = [utr_idx[utr_index], peak_idx[i], five_start, five_end, peak_start, peak_end]
                    new_row = pd.Series(new_row_list, index=in_between_cols)
                    in_between_manager.append(new_row)


            peak_end_index = list_find_in_between(peak_ends, five_start, five_end)
            if len(peak_end_index) > 0:
                for i in peak_start_index:
                    peak_start = peak.iloc[i]['Start']
                    peak_end = peak.iloc[i]['End']
                    new_row_list  = [utr_idx[utr_index], peak_idx[i], five_start, five_end, peak_start, peak_end]
                    new_row = pd.Series(new_row_list, index=in_between_cols)
                    in_between_manager.append(new_row)

    pool_one = mp.Pool(10)
    pool_two = mp.Pool(10)
    pool_three = mp.Pool(10)

    for utr_index in range(len(utr)):
        plus = utr.iloc[utr_index][6] == '+'
        
        if plus:
            pool_one.apply_async(find_less_than, args = (utr_index,))
        else:
            pool_two.apply_async(find_greater_than, args = (utr_index,))
        pool_three.apply_async(find_in_between, args = (utr_index,))

    pool_one.close()
    pool_one.join()

    pool_two.close()
    pool_two.join()

    pool_three.close()
    pool_three.join()

    less_than = pd.concat(less_than_manager, ignore_index=False,axis=1).T
    greater_than = pd.concat(greater_than_manager, ignore_index=False,axis=1).T
    in_between = pd.concat(in_between_manager, ignore_index=False,axis=1).T

    print(less_than)
    less_than.to_csv('chip-seq/result_csv/chr' + chr_num + '_less_than_five_prime.csv')

    print(greater_than)
    greater_than.to_csv('chip-seq/result_csv/chr' + chr_num + '_greater_than_five_prime.csv')

    print(in_between)
    in_between.to_csv('chip-seq/result_csv/chr' + chr_num + '_in_between_five_prime.csv')