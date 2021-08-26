#!/bin/bash

python chip-seq/map_peaks_to_genes.py
python chip-seq/result_csv_to_result_peaks.py
python chip-seq/get_all_transcripts.py
python chip-seq/convert_transcripts_to_genes.py
python chip-seq/get_peaks_upstream_of_gene.py