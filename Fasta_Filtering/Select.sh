#!/bin/bash

###Search fasta file for specific samples
awk '
BEGIN {
	printing = 0;
}
/^>/ {
	printing = 0;
}
/^>OCPHL[0-9]$/ {  #Sample 0-9
	printing = 1;
	printf("%s\n", $0);
	next;
}
/^>OCPHL[1-9][0-9]$/ {  #Sample 10-99
	printing = 1;
	printf("%s\n", $0);
	next;
}
/^>OCPHL2[1-9][0-9][0-9]$/ {  #Samples >2100
	printing = 1;
	printf("%s\n", $0);
	next;
}
/^>UCI_[0-9]$/ {  #UCI Samples 0-9
        printing = 1;
        printf("%s\n", $0);
        next;
}
/^>UCI_[0-9][0-9]$/ {  #UCI Samples 0-99
        printing = 1;
        printf("%s\n", $0);
        next;
}

/^[A-Z][A-Z]*/ {  #Also print data
	if (printing)  #Only print if correct sample name
		printf("%s\n", $0);
	next;
}
{
	next;
}' < OCPHL_Complete_fastas/Fasta_Pieces/CZBio_OC_all.fasta \
   > OCPHL_Complete_fastas/CZ_OCPHL_Filter.fasta  #Output into own file


###Grab only UCI Samples, output into own file
sed -n -e '/UCI_[1-9].*/,/^>OCPH/{/^>OCPH/!p;}' ./OCPHL_Complete_fastas/Fasta_Pieces/CZBio_OC_all.fasta > OCPHL_Complete_fastas/CZ_UCI_Filter.fasta

###Concatenate CZBio filtered fasta & OCPHL fastas
cat OCPHL_Complete_fastas/CZ_OCPHL_Filter.fasta OCPHL_Complete_fastas/Fasta_Pieces/OCPHL*.fasta > OCPHL_Complete_fastas/CZ_OCPHL_Merge.fasta
