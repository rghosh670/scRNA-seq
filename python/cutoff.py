import magic
import scprep

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


data = scprep.io.load_csv('/home/rohit/Desktop/rawReadsWithoutUnexpressedGenes.csv', cell_names=False)
print(data)

scprep.plot.plot_library_size(data, cutoff = 420)
plt.show()