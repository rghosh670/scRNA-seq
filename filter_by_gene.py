import pandas as pd

# genes = pd.read_csv('controlled_replicates.csv', index_col=0).index.tolist()

f = open('final_tfs/final_tfs.txt', 'r')
final_tfs = f.read().splitlines()
f.close()


f = open('data/muscleTFStuff/tfs_over_500_cells.txt', 'r')
tfs = f.read().splitlines()
f.close()

final_tfs = [i for i in final_tfs if i in tfs]
print(len(final_tfs))

with open('final_tfs/final_tfs.txt', 'w') as f: # write out results to text file
    for item in final_tfs:
        f.write("%s\n" % item)

f.close()


# idx = []
# for i,v in enumerate(genes):
#     if v in tfs:
#         idx.append(i+1)

# idx.insert(0,0)

# df = pd.read_csv('controlled_replicates.csv', index_col=0, skiprows=lambda x:x not in idx)
# print(df)

# for index, row in df.iterrows():
#     if 'gt' not in row.idxmax():
#         if int(row.idxmax()[:row.idxmax().find('_')]) <= 270:
#             print(index)
