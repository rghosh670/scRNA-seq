from pathlib import Path
import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

dirpath = './lineage_plots'

files = os.listdir(dirpath)
files.sort(key=natural_keys)

f = open('final_tfs/final_tfs.txt', 'r')
tfs = f.read().splitlines()
f.close()

for i in range(len(files)):
    os.rename('lineage_plots/' + files[i], 'lineage_plots/' + tfs[i] + '.png')