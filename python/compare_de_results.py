import numpy as np
import pandas as pd
import json

# with open('data/geneAndTimeData/de_analysis/tfs_before_func_genes.txt') as json_file:
#     tf_dict = json.load(json_file)
# json_file.close()

# for i in tf_dict.values():
#     print(len(i))


# f = open('data/geneAndTimeData/de_analysis/14116_genes.txt', 'r')
# genes_14116 = f.read().splitlines()
# f.close()

f = open('data/geneAndTimeData/de_analysis/muscle_functional_genes.txt', 'r')
func_genes = f.read().splitlines()
f.close()

# # genes_in_func_not_14116 = np.setdiff1d(func_genes, genes_14116)

# func_genes = [x for x in func_genes if x not in genes_in_func_not_14116]

my_list = ['amphid', 'hyp_tail_amphid_nonamphid', 'hypodermis', 'nonamphid', 'tail_hyp']

diff_list_of_lists = []

for i in my_list:
    f = open('data/geneAndTimeData/de_analysis/bwm_vs_' + i + '.txt', 'r')
    de_result = f.read().splitlines()
    f.close()

    diff_list = np.setdiff1d(func_genes, de_result)
    # diff_list_of_lists.append(diff_list)
    print(diff_list)
    print(len(diff_list))

exit()
res = list(set.intersection(*map(set, diff_list_of_lists)))
print(len(res))

with open('data/geneAndTimeData/de_analysis/genes_in_func_not_de_result.txt', 'w') as f: # write out results to text file
    for item in res:
        f.write("%s\n" % item)

f.close()
