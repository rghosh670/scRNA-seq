import pandas as pd
import numpy as np
import json

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/14467_genes.txt', 'r')
genes = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/up_tf.txt', 'r')
up_tf = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/muscle_functional_genes.txt', 'r')
functional_genes = f.read().splitlines()
f.close()

up_tf_idx = [i+1 for i, val in enumerate(genes) if val in up_tf]
func_genes_idx = [i+1 for i, val in enumerate(genes) if val in functional_genes]

up_tf_idx.insert(0,0)
func_genes_idx.insert(0,0)

up_tf_times = pd.read_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/state_transition_times.csv', index_col=0, header=0, skiprows = lambda x:x not in up_tf_idx)
func_genes_times = pd.read_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/state_transition_times.csv', index_col=0, header=0, skiprows = lambda x:x not in func_genes_idx)

result = {}

func_genes_times = func_genes_times.sort_values(by = 'avg', ascending=False)

for tf in up_tf_times.iterrows():
    tf_gene = tf[0]
    tf_avg = tf[1][2]
    
    for func_gene_row in func_genes_times.iterrows():
        func_gene = func_gene_row[0]
        func_gene_avg = func_gene_row[1][2]
        
        if func_gene_avg <= tf_avg:
            break
        
        result.setdefault(tf_gene, []).append(func_gene)
        
with open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/tfs_before_func_genes.txt', 'w') as outfile:
    json.dump(result, outfile)

outfile.close()