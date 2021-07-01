import pandas as pd

bwm_t6 = pd.read_csv('data/t6Stuff/bwm_t6.csv', index_col=0)
bwm_t6.loc['BWM_head_row_1:210_270'] = bwm_t6.loc['BWM_head_row_1:270_330']
bwm_t6.loc['BWM_head_row_2:210_270'] = bwm_t6.loc['BWM_head_row_2:270_330']

muscle_t7 = pd.read_csv('data/t7Stuff/parsed_muscle_t7.csv', index_col=0)
muscle_t7 = muscle_t7[muscle_t7['time'] < 210]

genes = bwm_t6.columns.tolist()

bins = ['90_160', '160_210', '210_270', '270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']

def find_bin(input):
    if type(input) != str:
        for bin in bins:
            bound_1 = int(bin[:bin.find('_')])
            bound_2 = int(bin[bin.find('_')+1:])
            if(bound_1 <= input <= bound_2):
                return bin

        return None

    for bin in bins:
        if bin in input:
            return bin
    
    return None
    
df_dict = {}

for bin in bins:
    df_dict[bin] = pd.DataFrame(columns = genes)

for index, row in bwm_t6.iterrows():
    df_dict[find_bin(index)].loc[index] = bwm_t6.loc[index]

for index, row in muscle_t7.iterrows():
    df_dict[find_bin(row['time'])].loc[index] = muscle_t7.loc[index]

final_df = pd.DataFrame(columns=genes)

for key in df_dict.keys():
    sum = df_dict[key].sum(axis=0).tolist()

    multiplier = 1 if len(df_dict[key]) == 5 else (5/len(df_dict[key]))
    sum = [round(i*multiplier) for i in sum]

    final_df.loc[key] = sum

final_df = final_df.loc[:, (final_df != 0).any(axis=0)]
final_df = final_df.T
final_df.to_csv('data/geneAndTimeData/de_analysis/impulse_de2_input.csv')