#!/bin/bash

cat Fasta_Pieces/* > All_good_pre_Aspen.fasta
sed -n -e "/>CAOC[0-9]*/ s/$/ \[keyword\=purposeofsampling\:baselinesurveillance\]/p ; /[ACTGN][ACTGN][ACTGN][ACTGN]*/p" All_good_pre_Aspen.fasta > All_good_Aspen.fasta
rm All_good_pre_Aspen.fasta
