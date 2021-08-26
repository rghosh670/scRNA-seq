import os

dir = 'chip-seq/transcripts_downstream_of_peak/'

files = os.listdir(dir)

transcript_set = set()

for file in files:
    f = open(dir + file, 'r')
    transcripts = f.read().splitlines()
    f.close()

    transcript_set.update(transcripts)

transcript_list = list(transcript_set)

with open('data/muscleTFStuff/all_transcripts.txt', 'w') as f:
    for item in transcript_list:
        f.write('%s\n' % item)

    f.close()