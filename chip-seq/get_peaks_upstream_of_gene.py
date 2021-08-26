import pandas as pd
import scanpy as sc
import os

input_folder = 'chip-seq/genes_downstream_of_peak/'
input_files = os.listdir(input_folder)

result_dict = {}

for i in input_files:
    f = open(input_folder + i, 'r')
    input_genes = f.read().splitlines()
    f.close()

    for gene in input_genes:
        result_dict.setdefault(gene, set()).add(i[:i.find('.txt')])
    

output_folder = 'chip-seq/peaks_upstream_of_gene/'

for key in result_dict.keys():
    result_dict[key] = list(result_dict[key])
    print(result_dict[key])
   
    with open(output_folder + key + '.txt', 'w') as f:
        for item in result_dict[key]:
            f.write('%s\n' % item)

        f.close()
