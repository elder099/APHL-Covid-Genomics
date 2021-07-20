#!/bin/bash

#Found=$(find OCPH_pass -name "OCPH[1-3].fasta" -print) #Small subset for testing

###Arguments
while getopts d:L: flag
do
    case "${flag}" in
        d) date_path=${OPTARG};;  #here's where you put the path to your date folder
	L) LAB=${OPTARG};;
    esac
done

#Make the Fixed directory
mkdir -p ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/$date_path/Fixed_Fasta

for file in ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/$date_path/Fasta_Pieces/*.fa*
do
	./HeaderChange.sh -f "$file" -g $date_path -L $LAB
done

cat ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/$date_path/Fixed_Fasta/*.fasta > ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/$date_path/All_good.fasta
rm ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/$date_path/Fixed_Fasta/*
