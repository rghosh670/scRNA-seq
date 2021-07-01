import pandas as pd

df = pd.read_csv('data/geneAndTimeData/bwm_csv/.csv', index_col=[0])
print(df)

"""
new_cols = []

for i in df.columns:
    new_cols.append(int(i[i.find('_')+1:]) - 30)

new_cols[-1] += 60
df.columns = new_cols

result = []

for index, val in df.iterrows():
    numerator = 0
    denominator = 0
    for i, v in enumerate(val):
        numerator += v*df.columns[i]
        denominator += v
    
    result.append(numerator/denominator)

df['center'] = result

print(df)

"""