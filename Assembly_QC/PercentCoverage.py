import os
import sys
import gzip
import pandas as pd
import argparse
import random
import numpy
from Bio import SeqIO  #requires biopython





#####
#####MAIN SECTION
#####

if __name__ == '__main__':
    CountOut=pd.DataFrame()

    for record in SeqIO.parse("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-08-12/All_good.fasta","fasta"):

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
    CountOut["ID"][CountOut["CoveragePercent"]>0.89].to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-08-12/Assembly_QC/HighCoverage.csv",index=False)
    CountOut.to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-08-12/Assembly_QC/PCoverage.csv",index=False)
