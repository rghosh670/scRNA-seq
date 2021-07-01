import magic
import scprep

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

data = scprep.io.load_csv('/home/rohit/Desktop/rawReadsWithoutUnexpressedGenes.csv', cell_names=False)
data = scprep.filter.filter_library_size(data, cutoff = 420)

data = scprep.normalize.library_size_normalize(data)
data = scprep.transform.sqrt(data)

for i in range(1, 20, 2):
    magic_op = magic.MAGIC(t = i)
    magic_output = magic_op.fit_transform(data, genes='all_genes')
    magic_output.to_csv('~/Desktop/magicWithNormalization' + str(i) + '.csv', index = False)