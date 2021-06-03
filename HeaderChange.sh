#!/bin/bash

Seq= seq 1 98      #sequence of sample #'s given in fastas
Prename="hCoV-19\/USA\/UCI-"    #Prefix for GISAID virus name
Suffix='/2021'



echo $Seq
echo $Prename
echo $Suffix

grep '^>[A-Za-z]' OCPH_Pass/OCPH1.fasta
Numba= sed -n -e 's/^>[A-Za-z]*//p' OCPH_Pass/OCPH1.fasta   #Extracting the sample number programmatically

echo break
sed -n -e "1 s/^>[A-Za-z]*/$Prename/p" OCPH_Pass/OCPH1.fasta
