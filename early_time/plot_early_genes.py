import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from sklearn.preprocessing import Normalizer

df = pd.read_csv('num_cells_data.csv', index_col=0)
print(df)

to_remove = []

for i in range(0, len(df), 4):
    to_remove.append(df.index.tolist()[i])

df = df.drop(to_remove)
# df = df.iloc[0:len(df)//8]

sns.set(font_scale=0.5)

df.iloc[:,:] = Normalizer(norm='l1').fit_transform(df)
ax = sns.heatmap(df, yticklabels=3, xticklabels=1)

plt.rcParams['ytick.major.size'] = 20
plt.rcParams['ytick.major.width'] = 4
plt.rcParams['xtick.bottom'] = True
plt.rcParams['ytick.left'] = True
plt.show()
plt.savefig('im_tired.png')