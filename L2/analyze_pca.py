import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
import matplotlib
from sklearn.preprocessing import Normalizer

def detect_outlier(data_1):
    outliers=[]
    threshold=1
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for index, y in enumerate(data_1):
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(index)
    return outliers

df = pd.read_csv('L2/mean_subtract_pca.csv', index_col=0)
first_component = df.iloc[0].tolist()
first_component = [abs(i) for i in first_component]

indices = set()
outlier_datapoints = detect_outlier(first_component)
indices.update(outlier_datapoints)

indices = list(indices)

df = df.iloc[:,indices]

genes = df.columns.tolist()

index = pd.read_csv('L2/L2_eset_by_muscle_subtype.csv', index_col=0).index.tolist()

genes_idx = [i+1 for i, val in enumerate(index) if val in genes]
genes_idx.insert(0,0)

df = pd.read_csv('L2/L2_eset_by_muscle_subtype.csv', index_col=0, skiprows=lambda x:x not in genes_idx)
print(df)

sns.set(font_scale=1)
df.iloc[:,:] = Normalizer(norm='l1').fit_transform(df)
g = sns.clustermap(df, xticklabels=1, col_cluster=False, cbar=False, dendrogram_ratio=0.001, figsize=(4,10))
g.ax_row_dendrogram.set_visible(False)

plt.show()
plt.tight_layout()
g.cax.set_visible(False)

outfile = 'L2/heatmap.png'
plt.ylim(bottom=0.5)

plt.savefig(outfile, bbox_inches='tight', pad_inches=.25)