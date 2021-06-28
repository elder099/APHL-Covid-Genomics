#!/bin/bash

#Found=$(find OCPH_pass -name "OCPH[1-3].fasta" -print) #Small subset for testing

#Frances note to self:use this to change header for batch upload to GISAID
for file in ~/workspace/SARS-CoV-2/20210621_SLO/consensus.fasta/2020/*.fasta
do
	~/APHL-Covid-Genomics/GISAID_Upload/HeaderChange.sh -f "$file"
done



cat Fixed_Fasta/*.fasta > run4.fasta
