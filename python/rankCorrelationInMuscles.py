import pandas as pd
from scipy import stats
import itertools
from collections import Counter

"""

t6 = pd.read_csv('data/t6Stuff/BWM_t6.csv', index_col=[0])

muscle_cells = [i[:i.find(':')] for i in t6.index]
muscle_cells = list(dict.fromkeys(muscle_cells))
t6_list = []

t6_list.append(t6.iloc[0:8])
t6_list.append(t6.iloc[8:16])
t6_list.append(t6.iloc[16:23])
t6_list.append(t6.iloc[23:30])
t6_list.append(t6.iloc[30:])


final_df = pd.DataFrame(index = t6.columns, columns = muscle_cells)

for gene in t6.columns:
    rank = 0

    for index, df in enumerate(t6_list):
        x = [int(i[i.rindex('_')+1:]) for i in df.index.tolist()]
        y = df[gene]
        r = stats.linregress(x, y)[2]
        final_df.at[gene, muscle_cells[index]] = r

final_df.to_csv('rankCorrelationInMuscles.csv')

"""

df = pd.read_csv('rankCorrelationInMuscles.csv', index_col=[0])

x = []
for i in df.index:
    neg_count = len(list(filter(lambda x: (x < 0), df.loc[i].tolist())))
    x.append(neg_count)

print(Counter(x))