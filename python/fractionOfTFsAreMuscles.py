import pandas as pd

f = open('data/muscleTFStuff/transcriptionFactors.txt', 'r')
tf = f.read().splitlines()
f.close()

t6 = pd.read_csv('data/t6Stuff/mean_t6.csv', index_col=[0])
muscle_t6 = t6['BWM_anterior' : 'BWM_posterior']

# fractions = []
# for factor in tf:
#     if (t6[factor] != 0).sum():
#         fractions.append((muscle_t6[factor] != 0).sum() / (t6[factor] != 0).sum())

# with open('data/fractionOfTFsAreMuscles.txt', 'w') as f: # write out results to text file
#     for item in fractions:
#         f.write("%s\n" % item)

# f.close()

fractions = []
for factor in tf:
    fractions.append((muscle_t6[factor] != 0).sum() / 5)

with open('data/muscleTFStuff/tfFractionWithinMuscles', 'w') as f: # write out results to text file
    for item in fractions:
        f.write("%s\n" % item)

f.close()