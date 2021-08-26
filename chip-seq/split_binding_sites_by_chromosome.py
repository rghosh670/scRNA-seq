import pandas as pd

chr = ['I', 'II', 'III', 'IV', 'V', 'X']

df = pd.read_csv('chip-seq/peaks/full_binding_sites.csv', index_col=[0])
# print(df)

print(set(df['Chromosome']))

# exit()
df_dict = {}

for i in chr:
    df_dict[i] = df.loc[df['Chromosome'] == i]
    print(df_dict[i])
    df_dict[i].to_csv('chip-seq/peaks/chromosome_' + i +'.csv')


