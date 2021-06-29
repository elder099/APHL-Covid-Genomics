#!/bin/bash

#Found=$(find OCPH_pass -name "OCPH[1-3].fasta" -print) #Small subset for testing

#Frances note to self:use this to change header for batch upload to GISAID
for file in ~/workspace/SARS-CoV-2/20210621_SLO/consensus.fasta/2020_Fastas/*.fasta
do
	~/APHL-Covid-Genomics/GISAID_Upload/HeaderChange.sh -y 2020 -f "$file"
done


for file1 in ~/workspace/SARS-CoV-2/20210621_SLO/consensus.fasta/2021_Fastas/*.fasta
do
	~/APHL-Covid-Genomics/GISAID_Upload/HeaderChange.sh -y 2021 -f "$file1"
done

#Make each year separately just becaause
cat Fixed_Fasta/2021_0621_SLO/2020_Fixed/*.fasta > Fixed_Fasta/2021_0621_SLO/Run4_2020.fasta
cat Fixed_Fasta/2021_0621_SLO/2021_Fixed/*.fasta > Fixed_Fasta/2021_0621_SLO/Run4_2021.fasta

#Merge the two years for a complete picture
cat Fixed_Fasta/2021_0621_SLO/Run4_202[01].fasta > Fixed_Fasta/2021_0621_SLO/All_Run4.fasta     
