#!/bin/bash

nextflow run czbiohub/sc2-illumina-pipeline -profile artic,docker \
    --reads '../Basespace/Projects/20210514_SLO/Samples/SLOPH2/Files/*_R{1,2}_001.fastq.gz*' \
    --kraken2_db 'sc2-illumina-pipeline/kraken2_db' \
    --outdir '../sc2-output/20210514_SLO-output/'
