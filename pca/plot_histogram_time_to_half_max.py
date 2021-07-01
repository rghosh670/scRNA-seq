import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis/14116_genes.txt', 'r')
genes = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis/up_tf.txt', 'r')
up_tf = f.read().splitlines()
f.close()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/muscle_functional_genes.txt', 'r')
functional_genes = f.read().splitlines()
f.close()

up_tf_idx = [i+1 for i, val in enumerate(genes) if val in up_tf]
func_genes_idx = [i+1 for i, val in enumerate(genes) if val in functional_genes]

up_tf_idx.insert(0,0)
func_genes_idx.insert(0,0)

up_tf_times = pd.read_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis/state_transition_times.csv', index_col=0, header=0, skiprows = lambda x:x not in up_tf_idx)
func_genes_times = pd.read_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis/state_transition_times.csv', index_col=0, header=0, skiprows = lambda x:x not in func_genes_idx)

tf_avg = up_tf_times['avg'].tolist()
func_genes_avg = func_genes_times['avg'].tolist()

# print(tf_avg)
# _ = plt.hist(tf_avg, bins='auto')  # arguments are passed to np.histogram
# plt.title("Up Transcription Factor Times to Half Max")
# plt.show()
# plt.savefig('up_tf_times_hist.png')

print(func_genes_avg)
_ = plt.hist(func_genes_avg, bins='auto')  # arguments are passed to np.histogram
plt.title("Funcitonal Genes Times to Half Max")
plt.show()
plt.savefig('functional_genes_times_hist.png')


# for func_gene_row in func_genes_times.iterrows():
#     func_gene_avg = func_gene_row[1][2]
        