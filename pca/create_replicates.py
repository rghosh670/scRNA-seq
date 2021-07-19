import numpy as np
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('lib_size_norm.csv', index_col = 0)

# print(pd.Series((np.random.rand(1,len(df))[0]))+0.5)
# exit()

cols = df.columns.tolist() * 3

for i in range(len(cols)):
    cols[i] = cols[i] + '_rep' + str(i // (len(df.columns)) + 1)

result = pd.DataFrame(index = df.index, columns = cols)
print(result)

z = 0
for index, col in df.iteritems():
    result[cols[z]] = col
    z += 1

for k in range(len(result.columns)):
    if k >= len(df.columns):
        x = k % len(df.columns)
        rand = pd.Series((np.random.rand(1,len(df))[0]))+0.5
        rand.index = df.index
        result[cols[k]] = df.iloc[:,x].multiply(rand)
 
result = result.astype(int)

result.to_csv('input_with_replicates.csv')