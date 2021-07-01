import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

genes = pd.read_csv('data/t6Stuff/bwm_t6.csv', index_col=0, skiprows=lambda x: x not in [0]).columns.tolist()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/up_tf.txt', 'r')
up_tf = f.read().splitlines()
f.close()

up_tf_idx = [i+1 for i, val in enumerate(genes) if val in up_tf]

up_tf_idx.insert(0,0)

muscles = ['anterior', 'far_posterior', 'head_row_1', 'head_row_2', 'posterior']
mean_dict = {}

for i in muscles:
    temp_df = pd.read_csv('data/geneAndTimeData/bwm_csv/bwm_' + i + '_time_bins.csv', index_col=0, usecols=up_tf_idx)
    mean_dict[i] = temp_df.loc['mean'].tolist()

col_names = pd.read_csv('data/geneAndTimeData/bwm_csv/bwm_anterior_time_bins.csv', index_col=0, usecols=up_tf_idx).columns.tolist()
df = pd.DataFrame(columns = col_names)

for key, val in mean_dict.items():
    df.loc[key] = val

df = df.T
df = df.reindex(df.mean(axis=1).sort_values().index, axis=0)

df.to_csv('data/geneAndTimeData/de_analysis_part2/bwm_up_tf_avg_expression.csv')

# l = []
# for i in range(len(df.index)):
#     for j in range(len(df.columns)):
#         l.append(df.iloc[i,j])
        
# l = np.array(l)
# l = l[(l>np.quantile(l,0.05)) & (l<np.quantile(l,0.95))].tolist()
# l.sort()
# print(l)

ax = sns.heatmap(df, vmin=0, vmax = 30)
plt.show()

plt.savefig('figures/up_tf_heatmap_part2.png')

