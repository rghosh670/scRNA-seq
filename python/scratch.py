import pandas as pd

df = pd.read_csv('data/de_analysis_part2/impulse_de2_input.csv', index_col = 0)
df += 1
df.to_csv('plus_one_input.csv')