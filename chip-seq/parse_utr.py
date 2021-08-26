import pandas as pd

chr = ['I', 'II', 'III', 'IV', 'V', 'X']

for i in chr:
    count = 0
    df = pd.read_csv('chip-seq/gff3/chr' + i + '.gff3', sep='\t', header=None)
    result = pd.DataFrame(columns = df.columns)

    for index, row in df.iterrows():
        if 'five' in str(row[2]) or 'three' in str(row[2]):
            result.loc[count] = row
            count += 1

    idx = [str(i)[str(i).rfind(':')+1:] for i in result.iloc[:,8].tolist()]
    result.index = idx
    result = result.sort_values(by=3)
    print(result)
    
    result.to_csv('chip-seq/utr/utr_chr' + i + '.csv')