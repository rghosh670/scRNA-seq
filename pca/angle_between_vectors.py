import pandas as pd
import numpy as np
import itertools

types = ['raw',  'mean_subtract', 'normalized_by_cell', 'normalized_by_cell_and_gene', 'normalized_by_gene']
time_bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']

for bin in time_bins:
    result = pd.DataFrame(index = types, columns = types)
    for a, b in itertools.combinations(types, 2):
        vector_1 = pd.read_csv('pca/' + a + '/' + a + '_' + bin + ':pca.csv', index_col=0).iloc[0].tolist()
        vector_2 = pd.read_csv('pca/' + b + '/' + b + '_' + bin + ':pca.csv', index_col=0).iloc[0].tolist()
        unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
        unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        angle = np.arccos(dot_product)

        result.at[a,b] = angle
        print(angle)
    
    result.to_csv('pca/angle_between_vectors_' + bin + '.csv')