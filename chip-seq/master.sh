#!/bin/bash

if  [[ $1 = "-1" ]]; then
    echo "Part 1"
    python chip-seq/map_peaks_to_genes.py
    python chip-seq/result_csv_to_result_peaks.py
    python chip-seq/get_all_transcripts.py
fi

if [[ $1 = "-2" ]]; then
    echo "Part 2"
    python chip-seq/convert_transcripts_to_genes.py
    python chip-seq/get_peaks_upstream_of_gene.py
fi

if [[ $1 = "-3" ]]; then
    echo "All"
    python chip-seq/map_peaks_to_genes.py
    python chip-seq/result_csv_to_result_peaks.py
    python chip-seq/get_all_transcripts.py
    python chip-seq/convert_transcripts_to_genes.py
    python chip-seq/get_peaks_upstream_of_gene.py
fi



