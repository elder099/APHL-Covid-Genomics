#!/bin/bash

Seq= seq 1 98      #sequence of sample #'s given in fastas
Prefix="hCoV-19\/USA\/UCI-"    #Prefix for GISAID virus name
Suffix='/2021'



echo $Seq
echo $Prefix
echo $Suffix

grep '^>[A-Za-z]' OCPH_Pass/OCPH1.fasta
Numba=$(sed -n -e 's/^>[A-Za-z]*//p' OCPH_Pass/OCPH11.fasta)   #Extracting the sample number programmatically
NumbaSize=${#Numba}

echo $Numba
echo $NumbaSize

#Prepping for the while loop
n=$NumbaSize
NewNumba="$Numba"

#While loop to prepend enough 0 digits
#Each loop prepends a 0
while [ $n -lt 3 ]
do
	NewNumba="0$NewNumba"
	echo $NewNumba
	n=$(( $n + 1 ))
	echo $n
done

echo break

Virus_Name="$Prefix$NewNumba$Suffix"
echo $Virus_Name



