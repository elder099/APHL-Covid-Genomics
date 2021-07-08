#!/bin/bash

#Found=$(find OCPH_pass -name "OCPH[1-3].fasta" -print) #Small subset for testing

for file in ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/2021-07-08/Fasta_Pieces/*.fa
do
	./HeaderChange.sh -f "$file"
done


cat ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/2021-07-08/Fixed_Fasta/*.fasta > ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/2021-07-08/All_good.fasta
rm ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/2021-07-08/Fixed_Fasta/*
