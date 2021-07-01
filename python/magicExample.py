import magic
import pandas as pd
import matplotlib.pyplot as plt

X = pd.read_csv('/home/rohit/Desktop/MAGIC-master/data/test_data.csv')
magic_operator = magic.MAGIC()
X_magic = magic_operator.fit_transform(X, genes='all_genes')
# plt.scatter(X_magic['VIM'], X_magic['CDH1'], c=X_magic['ZEB1'], s=1, cmap='inferno')
# plt.show()
# magic.plot.animate_magic(X, gene_x='VIM', gene_y='CDH1', gene_color='ZEB1', operator=magic_operator)

X_magic.to_csv('~/Desktop/exampleOutput.csv', index = False)
