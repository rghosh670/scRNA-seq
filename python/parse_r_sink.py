import pandas as pd

f = open('hello.txt', 'r')
sink = f.read().splitlines()
f.close()

gene_list = []
t1_list = []
t2_list = []
avg_list = []

for i in range(len(sink)):
    if 't1' and 't2' in sink[i]:
        gene_line = sink[i-1]

        if '`' in gene_line:
            gene = gene_line[gene_line.find('`')+1:gene_line.rfind('`')]
        else:
            gene = gene_line[gene_line.find('$case$')+6:gene_line.rfind('$lsImp')]

        gene_list.append(gene)
        time_line = sink[i+1].split()
        t1_list.append(time_line[-2])
        t2_list.append(time_line[-1])
        avg_list.append((float(time_line[-2]) + float(time_line[-1]))/2)

df = pd.DataFrame(index=gene_list)
df['t1'] = t1_list
df['t2'] = t2_list
df['avg'] = avg_list
df.to_csv('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis_part2/state_transition_times.csv')