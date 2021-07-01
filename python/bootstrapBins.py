import pandas as pd
from sklearn.utils import resample
import multiprocessing as mp

pool = mp.Pool(5)
pool.close()

f = open('data/geneAndTimeData/listOfGenes.txt', 'r')
genes = f.read().splitlines()
genes.insert(0, 'time')
f.close()

bins = [(200, 270), (270, 330), (330, 390), (390, 450), (450, 510), (510, 580), (580, 650), (650, 840)]

bwm_list = ['BWM_anterior', 'BWM_far_posterior', 'BWM_head_row_1', 'BWM_head_row_2', 'BWM_posterior']

for cell in bwm_list:
    df = pd.DataFrame(columns=genes)
    for bin in bins:
        try:
            bwm_csv = pd.read_csv('data/geneAndTimeData/bwm_csv/' + cell + str(bin) + '.csv', index_col=0)
            samples = 200
            for i in range(3):
                boot = resample(bwm_csv, replace=True, n_samples=samples)
                mean = [round(100*i) for i in boot.mean(axis=0).tolist()]
                mean.insert(0, str(bin)+'_rep'+str(i))
                df.loc[len(df.index)] = mean
                print(df)
        except:
            pass

    df.set_index('time', inplace=True)
    df.to_csv('data/geneAndTimeData/bwm_bootstrap/' + cell + '.csv')

