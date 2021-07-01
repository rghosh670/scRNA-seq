import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('pca/pca_part1/270_330:pca.csv', index_col=[0])
print(df)

plt.scatter(df.iloc[1], df.iloc[2], s=5)
plt.xlabel('PC1 (' + str(df.index[0]) + '%)')
plt.ylabel('PC2 (' + str(df.index[1]) + '%)')
plt.show()