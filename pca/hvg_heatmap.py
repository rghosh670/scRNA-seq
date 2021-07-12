import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
import matplotlib

norm = 'raw'

df = pd.read_csv('pca/' + norm + '/' + norm + '_HVGs.csv', index_col=0)
# df = df.drop(['pat-10', 'lev-11', 'act-4'])
# df['mean'] = df.mean(axis=1)
# df = df.sort_values(by = 'mean')
# df = df.drop('mean', axis = 1)
# normalized_df=(df-df.mean())/df.std()
# normalized_df=(df-df.min())/(df.max()-df.min())

sns.set(font_scale=0.5)
g = sns.clustermap(df, norm = LogNorm(), xticklabels=1, col_cluster=False)
plt.show()
plt.savefig(norm + '_heatmap.png')