import pandas as pd
import re

input_file = '~/Downloads/full_binding_sites_table.csv'
cols = ['DB Identifier', 'Score' ,'Chromosome', 'Start', 'End', 'Strand', 'DCC ID', 'Type', 'Name']

df = pd.read_csv(input_file, index_col=[0])

print(df)
df = df.loc[df['Type'] == 'target gene']
df.index = df['Name']
df.to_csv('chip-seq/peaks/full_binding_sites.csv')
print(df)

"""
df.insert(0, 'DB Identifier', df.index)
genes = [i[find_nth(i, '_', 2)+1:find_nth(i, '_', 3)].lower() for i in df.index]
genes = [i[:re.search(r"\d", i).start()] + "-" + i[re.search(r"\d", i).start():]for i in genes]

df.index = genes
df.to_csv(input_file)

"""