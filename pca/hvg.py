import pandas as pd
import numpy as np
import itertools

time_bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']


def detect_outlier(data_1):
    outliers=[]
    threshold=2
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for index, y in enumerate(data_1):
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(index)
    return outliers


norm = 'raw'

df = pd.read_csv('pca/' + norm + '/' + norm + '_' + 'first_components.csv', index_col=0)

indices = set()
for index, row in df.iterrows():
    outlier_datapoints = detect_outlier(row.tolist())
    indices.update(outlier_datapoints)

indices = list(indices)
print(indices)

df = df.iloc[:,indices]

muscles = ['head_row_1', 'head_row_2', 'anterior', 'posterior', 'far_posterior']
muscle_dict = {}

for muscle in muscles:
    muscle_dict[muscle] = pd.read_csv('data/geneAndTimeData/bwm_csv/bwm_' + muscle + '_time_bins.csv', index_col=0)


result = pd.DataFrame(index = df.columns, columns = muscles)

for index, col in df.iteritems():
    col = col.abs()
    bin = col.idxmax()

    for muscle in muscles:
        result.at[index, muscle] = muscle_dict[muscle].at[bin, index]
    
print(result)
# exit()
result.to_csv('pca/' + norm + '/' + norm + '_HVGs.csv')