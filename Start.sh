#!/bin/bash


###Arguments
while getopts d:L:s: flag
do
    case "${flag}" in
        d) date_path=${OPTARG};;  #here's where you put the path to your date folder
	L) LAB=${OPTARG};;
	s) seqtech=${OPTARG};;
    esac
done

LAB=${LAB:-"CA-OC-"}  #Make default LAB variable if no input given


#Make shortcut variables


#Make the Fixed directory
mkdir -p ~/Assembly_QC/$date_path/Fixed_Fasta

if [ ! -z "$seqtech" ]
	then
		echo "Seqtech supplied -- Clearlabs"
fi

###Run HeaderChange.sh on every fasta in date_path
for file in ~/Assembly_QC/$date_path/Fasta_Pieces/*.fa*
do
	./GISAID_Upload/HeaderChange.sh -f "$file" -g $date_path -L $LAB -s $seqtech
done


#Create GISAID-formatted multi-fasta
cat ~/Assembly_QC/$date_path/Fixed_Fasta/*.fasta > ~/Assembly_QC/$date_path/All_good.fasta
rm ~/Assembly_QC/$date_path/Fixed_Fasta/*


#Create Aspen-compatible file
cat ~/Assembly_QC/$date_path/Fasta_Pieces/* > ~/Assembly_QC/$date_path/All_good_Aspen.fasta 

#sed -n -e "/>[FCS][GAL][A-Z]*[0-9]*/ s/$/ \[keyword\=purposeofsampling\:baselinesurveillance\]/p ; /[ACTGN][ACTGN][ACTGN][ACTGN]*/p" ~/Assembly_QC/$date_path/All_good_Aspen.fasta > ~/Assembly_QC/$date_path/All_good_GB.fasta  #Add baseline surveillance tag to make GenBank-compatible file


#####Python section
#Start conda environment
. ~/anaconda3/etc/profile.d/conda.sh
conda activate Assembly_QC


#Create GenBank-compatible multi-fasta
#python ./GISAID_Upload/GenBank_Addkey.py -d $date_path

#Run Assembly_QC
mkdir -p ~/Assembly_QC/$date_path/Assembly_QC  #Make sure directory is there
python ./Assembly_QC/PercentCoverage.py -d $date_path


sed -n -e 's/>//p' ~/Assembly_QC/$date_path/All_good.fasta #Print out virus names for GISAID metadata
