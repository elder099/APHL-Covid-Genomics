#!/bin/bash

#Found=$(find OCPH_pass -name "OCPH[1-3].fasta" -print) #Small subset for testing

for file in OCPH_pass/*.fasta
do
	./HeaderChange.sh -f "$file"
done


cat Fixed_Fasta/*.fasta > All_UCI.fasta
