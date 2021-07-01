import pandas as pd

t6 = pd.read_csv('~/Downloads/t6.csv', usecols = ['gene', 'cell.bin', 'bootstrap.median.tpm'])

cellBinList = t6['cell.bin'].tolist()
geneList = t6['gene'].tolist()
tpm = t6['bootstrap.median.tpm'].tolist()

genes = list(dict.fromkeys(geneList))
cellBins = list(dict.fromkeys(cellBinList))

df = pd.DataFrame(index = cellBins, columns = genes)

for i in range(len(tpm)):
    df.at[cellBinList[i], geneList[i]] = tpm[i]

df.to_csv('data/t6.csv')
exec(open('python/sendEmail.py').read())