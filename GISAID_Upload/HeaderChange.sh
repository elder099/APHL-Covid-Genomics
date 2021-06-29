#!/bin/bash

###Arguments
while getopts "f:y:" flag
do
    case "${flag}" in
        f) input_file=${OPTARG};;
	y) year=${OPTARG};;   #Collection year
    esac
done


###Virus_Name pieces
#Seq= seq 1 98      #sequence of sample #'s given in fastas (write them manually)
Prefix=">hCoV-19\/USA\/SLOPH-"    #Prefix for GISAID virus name
Suffix="\/$year"

###Finding Sample Numbers
Numba=$(sed -n -e 's/^>[A-Za-z]*//p' $input_file)   #Extracting the sample number programmatically
NumbaSize=${#Numba}




###Adjusting Sample # Format
#Prepping for the while loop
n=$NumbaSize
NewNumba="$Numba"

##While loop to prepend enough 0 digits
##Each loop prepends a 0
while [ $n -lt 3 ]
do
	NewNumba="0$NewNumba"
	n=$(( $n + 1 ))
done


Virus_Name="$Prefix$NewNumba$Suffix"




Fasta_name="Fixed_Fasta/2021_0621_SLO/${year}_Fixed/Fixed_Fasta_$NewNumba.fasta"
echo $Fasta_name
sed "1 s/.*/$Virus_Name/" $input_file > $Fasta_name

