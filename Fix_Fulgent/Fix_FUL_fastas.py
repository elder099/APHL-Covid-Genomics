import sys
import argparse
import io
import os
import pandas as pd
import numpy as np
from Bio import SeqIO  #requires biopython


###Parsing command line prompts###
def parse_cmdline_params(cmdline_params):
    info = "Date path to Fulgent sample set"
    parser = argparse.ArgumentParser(description=info)
    parser.add_argument('-d', '--date_path', required=True,
                        help='Input a date in form FUL_2021-09-14')
    return parser.parse_args(cmdline_params)
###Parsing command line prompts###



if __name__ == '__main__':

    #####
    #####EDIT ASPEN FASTA FILE
    #####

    Pass=pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Passing_Samples.csv")
    OldAspen="/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/All_good_Aspen.fasta"
    NewAspen=open("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/All_good_Aspen_Final.fasta","w")
    n=0
    p=0

    for record in SeqIO.parse(OldAspen,"fasta"):
        if record.id in Pass['Public ID'].to_list():
            print(record.id)
            NewAspen.writelines([">",record.id,"\n",str(record.seq),"\n"])

            p=p+1

        n=n+1
    print(n)
    print(p)



    #####
    #####EDIT GISAID FASTA FILE
    #####

    PassGIS=pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Passing_Samples_GIS.csv")
    OldGIS="/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/All_good.fasta"
    NewGIS=open("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/All_good_GIS_Final.fasta","w")
    n=0
    p=0

    for record in SeqIO.parse(OldGIS,"fasta"):
        if record.id in PassGIS['Public GIS ID'].to_list():
            print(record.id)
            NewGIS.writelines([">",record.id,"\n",str(record.seq),"\n"])

            p=p+1

        n=n+1
    print(n)
    print(p)




    #####
    #####CREATE GENBANK FASTA FILE W/BASELINE TAGS
    #####

    ###Reuse Pass and OldAspen to create New GenBank fasta
    #Pass=pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Passing_Samples.csv")
    #OldAspen="/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/All_good_Aspen.fasta"
    Baseline=pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/BaselineSamples.csv")
    NewGB=open("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/All_good_GB_Final.fasta","w")
    n=0
    p=0
    q=0

    for record in SeqIO.parse(OldAspen,"fasta"):

        if record.id in Pass['Public ID'].to_list():
            if record.id in Baseline['Public ID'].to_list():
                print(record.id+' [keyword=purposeofsampling:baselinesurveillance]')
                NewGB.writelines([">",record.id,' [keyword=purposeofsampling:baselinesurveillance]',"\n",str(record.seq),"\n"])
                q=q+1
            else:
                print(record.id)
                NewGB.writelines([">",record.id,"\n",str(record.seq),"\n"])

            p=p+1

        n=n+1
    print(n) #336 unfiltered
    print(p) #165 pass QC
    print(q) #77 of them were Baseline

    NewAspen.close()
    NewGIS.close()
    NewGB.close()
