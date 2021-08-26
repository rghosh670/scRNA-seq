import pandas as pd
import os

df = pd.read_csv('data/muscleTFStuff/transcripts_to_genes.txt', sep='\t', index_col=[0])

input_dir = 'chip-seq/transcripts_downstream_of_peak/'
output_dir = 'chip-seq/genes_downstream_of_peak/'

files = os.listdir(input_dir)

for i in files:
    f = open(input_dir + i, 'r')
    transcripts = list(set(f.read().splitlines()))
    f.close()

    genes = [df.loc[i]['Public Name'] for i in transcripts]
    
    with open(output_dir + i, 'w') as f:
        for item in genes:
            f.write("%s\n" % item)

        f.close()
