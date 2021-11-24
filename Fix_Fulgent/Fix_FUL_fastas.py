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

    #grab command line input
    opts = parse_cmdline_params(sys.argv[1:])
    date = opts.date_path #input where to do assembly QC

    #Set up input file name shortcuts
    path = "/home/staphb/GISAID_Uploads/" + date
    pass_Asp_path = path + "/Passing_Samples.csv"        #Input list Aspen-formatted samples
    pass_GIS_path = path + "/Passing_Samples_GIS.csv"    #Input list GISAID-formatted samples
    base_path = path + "/BaselineSamples.csv"            #Input list Baseline surveillance samples

    old_Asp_path = path + "/All_good_Aspen.fasta"        #Input original Aspen-formatted fasta
    old_GIS_path = path + "/All_good.fasta"              #Input original GISAID-formatted fasta

    #Set up output file name shortcuts
    new_Asp_path = path + "/All_good_Aspen_Final.fasta"
    new_GIS_path = path + "/All_good_GIS_Final.fasta"
    new_GB_path = path + "/All_good_GB_Final.fasta"


    #####
    #####EDIT ASPEN FASTA FILE
    #####

    Pass=pd.read_csv(pass_Asp_path)
    NewAspen=open(new_Asp_path,"w")
    n=0
    p=0

    for record in SeqIO.parse(old_Asp_path,"fasta"):
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

    PassGIS=pd.read_csv(pass_GIS_path)
    NewGIS=open(new_GIS_path,"w")
    n=0
    p=0

    for record in SeqIO.parse(old_GIS_path,"fasta"):
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
    Baseline=pd.read_csv(base_path)
    NewGB=open(new_GB_path,"w")
    n=0
    p=0
    q=0

    for record in SeqIO.parse(old_Asp_path,"fasta"):

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
