import pandas as pd

bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']

cols = pd.read_csv('pca/more_tf/more_tf_' + '270_330' + ':pca.csv', index_col=0).columns.tolist()
df = pd.DataFrame(index = bins, columns = cols)

for bin in bins:
    comp = pd.read_csv('pca/more_tf/more_tf_' + bin + ':pca.csv', index_col=0).iloc[0].tolist()
    df.loc[bin] = comp

print(df)