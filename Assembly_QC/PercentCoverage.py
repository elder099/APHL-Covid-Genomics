import os
import sys
import gzip
import pandas as pd
import argparse
import random
import numpy
from Bio import SeqIO  #requires biopython

###Parsing command line prompts###
def parse_cmdline_params(cmdline_params):
    info = "Input vcf files and known SNP file"
    parser = argparse.ArgumentParser(description=info)
    parser.add_argument('-d', '--date_path', required=True,
                        help='Input a date in form FUL_2021-09-14')
    return parser.parse_args(cmdline_params)
###Parsing command line prompts###



#####
#####MAIN SECTION
#####

if __name__ == '__main__':
    CountOut=pd.DataFrame()

    opts = parse_cmdline_params(sys.argv[1:])
    date = opts.date_path #input where to do assembly QC
    date = "/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/" + date
    fasta_path = date + "/All_good_Aspen.fasta"
    print(fasta_path)



    for record in SeqIO.parse(fasta_path,"fasta"):

        #print(record.id)
        Seq=record.seq #This is the ACTG


        Seqlist=list(Seq)
        consec=1          #counter of consecutive bases
        conseclist=[]
        for i in range(1,len(Seqlist)):      #start from range 1 to not hit end of list
            if Seqlist[i-1] in ["A","C","T","G"] and Seqlist[i] in ["A","C","T","G"]:  #check that nuc is consecutive
                consec+=1
            else:
                conseclist.append(consec)
                consec=1



        #####
        #####ACTG counter
        #####
        counter = str(Seq).count('A')+str(Seq).count('G')+str(Seq).count('T')+str(Seq).count('C') #Count unambiguous bases

        Countdict={"ID":[record.id], "BaseCount":[counter],"CoveragePercent":counter/29903,"Num_Consecutive": max(conseclist)} #Make dictionary
        Countframe=pd.DataFrame.from_dict(Countdict)        #Make dataframe from dictionary
        CountOut = pd.concat([CountOut, Countframe])        #Add to running table

    #print(CountOut.to_string())
    QCRep=list(CountOut["ID"][CountOut["CoveragePercent"]>0.90])  #List of samples that pass
    QCframe=pd.DataFrame(QCRep,columns=["Passing_IDs"]) #Make dataframe for csv file

    ###Write out samples that pass in format that seqtk can read
    HC_path = date + "/Assembly_QC/HighCoverage.csv"
    print(HC_path)

    QCframe.to_csv(HC_path,index=False)


    ###Write out QC metric report
    pass_path = date + "/Assembly_QC/PCoverage.csv"
    print(pass_path)
    CountOut.to_csv(pass_path,index=False)
