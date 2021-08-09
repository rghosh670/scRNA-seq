import numpy as np
import pandas as pd

df = pd.read_csv('impulse_de2_input.csv', index_col = 0)

cols = df.columns.tolist() * 3

for i in range(len(cols)):
    cols[i] = cols[i] + '_rep' + str(i // (len(df.columns)) + 1)

result = pd.DataFrame(index = df.index, columns = cols)

multipliers = [1,0.9,1.1]

for index, val in enumerate(result.columns):
    x = index % len(df.columns)
    mult_idx = index//len(df.columns)
    result[val] = df.iloc[:,x].multiply(multipliers[mult_idx])

result = result.astype(int)
print(result)
result.to_csv('controlled_replicates.csv')