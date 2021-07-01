import magic
import scprep

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/home/rohit/Desktop/rawReadsWithoutUnexpressedGenes.csv')
data = scprep.filter.filter_library_size(data, cutoff = 420)

for i in range(1, 14, 2):
    magic_operator = magic.MAGIC(t = i)
    magic_output = magic_operator.fit_transform(data, genes="all_genes")
    magic_output.to_csv('~/Desktop/magicWithoutNormalization' + str(i) + '.csv', index = False)