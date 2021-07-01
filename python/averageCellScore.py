import pandas as pd
import numbers

cellScore = pd.read_csv('muscle_clusters2/muscle_clusters2CellScore.csv', index_col = [0])
cellScore = cellScore.groupby(by=cellScore.index, axis=0).apply(lambda g: g.mean() if isinstance(g.iloc[0,0], numbers.Number) else g.iloc[0])

cellScore.to_csv('muscle_clusters2/averageMuscle_clusters2CellScore.csv')
