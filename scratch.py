import pandas as pd
import scanpy as sc
import os

dir = 'chip-seq/peaks_upstream_of_gene/'
files = os.listdir(dir)

my_set = set()
x = 0
for file in files:
    x+=1
    f = open(dir + file, 'r')
    data = f.read().splitlines()
    f.close()

    print(data)

print(x)