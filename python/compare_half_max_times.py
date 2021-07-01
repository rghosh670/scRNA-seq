import pandas as pd
import numpy as np
import json

genes = pd.read_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/half_max_times.csv', index_col=0).index.tolist()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/up_tf.txt', 'r')
up_tf = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/up_func_gene.txt', 'r')
up_func_gene = f.read().splitlines()
f.close()

up_tf_idx = [i+1 for i, val in enumerate(genes) if val in up_tf]
func_genes_idx = [i+1 for i, val in enumerate(genes) if val in up_func_gene]

up_tf_idx.insert(0,0)
func_genes_idx.insert(0,0)

up_tf_times = pd.read_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/half_max_times.csv', index_col=0, header=0, skiprows = lambda x:x not in up_tf_idx)
func_genes_times = pd.read_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/half_max_times.csv', index_col=0, header=0, skiprows = lambda x:x not in func_genes_idx)

result = {}

func_genes_times = func_genes_times.sort_values(by = 'half_max', ascending=False)

for tf in up_tf_times.iterrows():
    tf_gene = tf[0]
    tf_avg = tf[1][0]

    
    for func_gene_row in func_genes_times.iterrows():
        func_gene = func_gene_row[0]
        func_gene_avg = func_gene_row[1][0]
        
        if func_gene_avg <= tf_avg:
            break
        
        result.setdefault(tf_gene, []).append(func_gene)
        
with open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/tfs_before_func_genes_by_half_max.txt', 'w') as outfile:
    json.dump(result, outfile)

outfile.close()