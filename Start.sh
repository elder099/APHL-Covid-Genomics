#!/bin/bash


###Arguments
while getopts d:L: flag
do
    case "${flag}" in
        d) date_path=${OPTARG};;  #here's where you put the path to your date folder
	L) LAB=${OPTARG};;
    esac
done

###Make useful shortcuts and defaults
LAB=${LAB:-"CA-OC-"}  #Make default LAB variable if no input given
uploads="/home/staphb/GISAID_Uploads"


#Make the Fixed directory
mkdir -p $uploads/$date_path/Fixed_Fasta



for file in $uploads/$date_path/Fasta_Pieces/*.fa*
do
  ./GISAID_Upload/HeaderChange.sh -f "$file" -g $date_path -L $LAB
done


#Make GISAID fasta file
cat $uploads/$date_path/Fixed_Fasta/*.fasta > $uploads/$date_path/All_good.fasta
rm $uploads/$date_path/Fixed_Fasta/*


#Make Aspen fasta file
cat $uploads/$date_path/Fasta_Pieces/* > $uploads/$date_path/All_good_Aspen.fasta #Create Aspen-compatible file






#####Python section
#Set up conda environment
#. /Users/Gawdcomplex/opt/anaconda3/etc/profile.d/conda.sh
. /home/staphb/miniconda3/etc/profile.d/conda.sh

#Start conda environment
conda activate Fulgent


#Set up file for Python scripts
mv $uploads/$date_path/*.csv $uploads/$date_path/${date_path}_metadata.csv


#Run Assembly_QC
mkdir -p $uploads/$date_path/Assembly_QC  #Make sure directory is there
python ../Assembly_QC/PercentCoverage.py -d $date_path

#Run Metadata cleaning
python ../Fix_Fulgent/Fix_metadata.py -d $date_path

#Run Fasta cleaning
python ../Fix_Fulgent/Fix_FUL_fastas.py -d $date_path



sed -n -e 's/>//p' $uploads/$date_path/All_good.fasta #Print out virus names for GISAID metadata
