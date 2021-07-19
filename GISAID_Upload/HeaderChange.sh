#!/bin/bash

###Arguments
while getopts f:g: flag
do
    case "${flag}" in
        f) input_file=${OPTARG};;
	g) gisaid_date=${OPTARG};;
    esac
done


###Virus_Name pieces
#Seq= seq 1 98      #sequence of sample #'s given in fastas (write them manually)
Prefix=">hCoV-19\/USA\/CA-OC-"    #Prefix for GISAID virus name
Suffix="\/2021"


###Finding Sample Numbers
Numba=$(sed -n -e 's/[A-Z]*_[A-Z][0-9][0-9]*//g; /[0-9]*/ s/[A-Z]*//g; s/^>[A-Za-z]*//p' $input_file)   #Extracting the sample number programmatically
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




Fasta_name="Fixed_Fasta_$NewNumba.fasta"
echo $Fasta_name
sed "1 s/.*/$Virus_Name/" $input_file > ~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/$gisaid_date/Fixed_Fasta/$Fasta_name

