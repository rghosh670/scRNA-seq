import pandas as pd
import re

from pandas.core.arrays.categorical import factorize_from_iterables

t7 = pd.read_csv('data/t7Stuff/t7.csv', index_col=[0], usecols=[1,3,6])

result_dict = {}
gene_list = []
lineage_list = ['^MSxppp','^MSxappp','^Cxp','^D']


def is_useful_lineage(lineage):
    for i in lineage_list:
        if re.search(i, lineage):
            return True
    
    return False

for index, row in t7.iterrows():
    lineage = row['lineage']

    if not is_useful_lineage(lineage):
        continue

    expression = row['bootstrap.median.tpm']
    gene = index
    
    result_dict.setdefault(lineage, []).append(expression)

    if gene not in gene_list:
        gene_list.append(gene)

df = pd.DataFrame(columns=gene_list)

for key in result_dict.keys():
    df.loc[key] = result_dict[key]

print(df)
df.to_csv('data/t7Stuff/parsed_muscle_t7.csv')