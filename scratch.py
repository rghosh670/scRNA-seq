import pandas as pd

df = pd.read_csv('controlled_replicates.csv', index_col=0)


for index, col in df.iteritems():
    rep = index[-1]

    if rep == '2':
        df[index] = df[index[:-1] + '1'] + 1

    if rep == '3':
        df[index] = df[index[:-1] + '1'] - 1


df[df < 0] = 0
df = df + 1
df.to_csv('20_input.csv')