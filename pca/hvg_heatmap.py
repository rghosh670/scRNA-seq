import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
import matplotlib
from sklearn.preprocessing import Normalizer



df = pd.read_csv('more_tf_hvgs.csv', index_col=0)
sns.set(font_scale=1)
df.iloc[:,:] = Normalizer(norm='l1').fit_transform(df)
g = sns.clustermap(df, xticklabels=1, col_cluster=False, cbar=False, dendrogram_ratio=0.001, figsize=(20,35.6))
g.ax_row_dendrogram.set_visible(False)

plt.show()
plt.tight_layout()
g.cax.set_visible(False)

outfile = 'background.png'
plt.ylim(bottom=0.5)

plt.savefig(outfile, bbox_inches='tight', pad_inches=.25)

"""
norm_types = ['mean_subtract', 'raw', 'normalized_by_cell', 'normalized_by_gene', 'normalized_by_cell_and_gene', 'transcription_factor']

norm_by_row = True

for norm in norm_types:
    df = pd.read_csv('pca/' + norm + '/' + norm + '_HVGs.csv', index_col=0)
    # df = df.drop(['pat-10', 'lev-11', 'act-4', 'mlc-3'])
    sns.set(font_scale=0.5)
    if norm_by_row:
        df.iloc[:,:] = Normalizer(norm='l1').fit_transform(df)
        g = sns.clustermap(df, xticklabels=1, col_cluster=False)
    else:
        g = sns.clustermap(df, norm = LogNorm(), xticklabels=1, col_cluster=False)

    plt.show()


    outfile = 'row_norm_' + norm +'_heatmap.png'if norm_by_row else norm +'_heatmap.png'
    plt.savefig(outfile)

"""