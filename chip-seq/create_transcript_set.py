import os

output_directory = 'chip-seq/result_peaks_to_genes'
files = os.listdir(output_directory)

master_set = set()

for i in files:
    f = open(output_directory + '/' + i, 'r')
    t = f.read().splitlines()
    f.close()

    master_set.update(t)

master_list = list(master_set)

with open('data/muscleTFStuff/all_transcripts.txt', 'w') as f:
    for item in master_list:
        f.write('%s\n'%item)
    
    f.close()

