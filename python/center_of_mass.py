import pandas as pd

df = pd.read_csv('data/de_analysis_part2/impulse_de2_input.csv', index_col=[0])
new_cols = [125, 185, 240, 300, 360, 420, 480, 540, 610, 690]

# for i in df.columns:
#     new_cols.append(int(i[i.find('_')+1:]) - 30)

# new_cols[-1] += 60

df.columns = new_cols

result = []

for index, val in df.iterrows():
    numerator = 0
    denominator = 0
    for i, v in enumerate(val):
        numerator += v*df.columns[i]
        denominator += v
    
    result.append(numerator/denominator)

df['center'] = result

print(df)