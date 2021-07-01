import pandas as pd
import json

transition_times = pd.read_csv('data/geneAndTimeData/de_analysis_part2/state_transition_times.csv', index_col=0)

with open('data/geneAndTimeData/de_analysis_part2/parsed_tfs_before_func_genes.txt') as json_file:
    tf_dict = json.load(json_file)
json_file.close()

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

writer = pd.ExcelWriter('excel_files/tfs_before_functional_genes.xlsx', engine='xlsxwriter')

for key in tf_dict.keys():
    df = pd.DataFrame(index = tf_dict[key])
    gene_group = [gene_dict[i] for i in tf_dict[key]]
    t1 = [transition_times.loc[i]['t1'] for i in tf_dict[key]]
    t2 = [transition_times.loc[i]['t2'] for i in tf_dict[key]]
    avg = [transition_times.loc[i]['avg'] for i in tf_dict[key]]
    df['gene_group'] = gene_group
    df['t1'] = t1
    df['t2'] = t2
    df['avg'] = avg
    df.to_excel(writer, sheet_name = key + ' ' + str(transition_times.loc[key]['avg']))
    
writer.save()