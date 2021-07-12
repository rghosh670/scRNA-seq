import pandas as pd

time_bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']

for bin in time_bins:
    df = pd.read_csv('marker_genes/marker_time_bin_' + bin + '.csv', index_col=1)

    df = df.drop('Unnamed: 0', axis = 1)
    df = df.sort_values(by = 'specificity', ascending=False)
    df.to_csv('marker_genes/marker_time_bin_' + bin + '.csv')
    print(df)