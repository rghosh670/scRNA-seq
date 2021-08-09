import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from sklearn.preprocessing import Normalizer

genes = pd.read_csv('more_tfs/more_tf_hvgs.csv', index_col=0).index.tolist()

df = pd.read_csv('more_tfs/more_tf_hvgs.csv', index_col=0)

f = open('data/muscleTFStuff/tfs_over_500_cells.txt', 'r')
over_500 = f.read().splitlines()
f.close()


tfs = []
for index, row in df.iterrows():
   if 'head_row_1' not in row.idxmax() and 'far_posterior' not in row.idxmax() and index in over_500:
       print(row)
       tfs.append(index)

idx = []
for i,v in enumerate(genes):
    if v in tfs:
        idx.append(i+1)

idx.insert(0,0)

df = pd.read_csv('more_tfs/more_tf_hvgs.csv', index_col=0, skiprows=lambda x:x not in idx)
print(df)

df.to_csv('non_extermity.csv')
exit()

to_remove = []

for i in range(0, len(df), 4):
    to_remove.append(df.index.tolist()[i])

df = df.drop(to_remove)
# df = df.iloc[0:len(df)//8]

sns.set(font_scale=0.5)

df.iloc[:,:] = Normalizer(norm='l1').fit_transform(df)
ax = sns.heatmap(df, yticklabels=3, xticklabels=1)
plt.show()
plt.savefig('im_tired.png')