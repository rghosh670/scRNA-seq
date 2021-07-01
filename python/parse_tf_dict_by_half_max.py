import pandas as pd
import json

with open('data/geneAndTimeData/de_analysis_part2/tfs_before_func_genes_by_half_max.txt') as json_file:
    tf_dict = json.load(json_file)
json_file.close()

half_max_times = pd.read_csv('data/geneAndTimeData/de_analysis_part2/half_max_times.csv', index_col=0)

l = ['m_up', 'm_down', 't_up', 't_down']
l_dict = {}

gene_dict = {}

for i in l:
    f = open('data/geneAndTimeData/de_analysis_part2/' + i + '.txt', 'r')
    l_dict[i] = f.read().splitlines()
    f.close()


for key in tf_dict.keys():
    for gene in tf_dict[key]:
        if gene not in gene_dict:
            for gene_list in l_dict.keys():
                if gene in l_dict[gene_list]:
                    gene_dict[gene] = gene_list

writer = pd.ExcelWriter('excel_files/tfs_before_functional_genes_by_half_max.xlsx', engine='xlsxwriter')

for key in tf_dict.keys():
    df = pd.DataFrame(index = tf_dict[key])
    gene_group = [gene_dict[i] for i in tf_dict[key]]
    half_max = [half_max_times.loc[i]['half_max'] for i in tf_dict[key]]
    df['gene_group'] = gene_group
    df['half_max'] = half_max
    df.to_excel(writer, sheet_name = key + ' ' + str(half_max_times.loc[key]['half_max']))
    
writer.save()