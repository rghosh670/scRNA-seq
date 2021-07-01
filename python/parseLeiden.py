import pandas as pd

leiden = pd.read_csv('data/leiden2.csv', index_col = [0])
genes = leiden.index.tolist()
clusters = leiden['leiden'].tolist()

for index, value in enumerate(clusters):
    f = open('leidenClusters/cluster' + str(value) + '.txt', 'a+')
    f.write(genes[index] + '\n')
    f.close()