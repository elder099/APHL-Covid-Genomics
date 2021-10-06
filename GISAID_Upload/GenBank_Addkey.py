#!/usr/bin/env python
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
                        help='Input a date in form 2021-10-05')
    return parser.parse_args(cmdline_params)
###Parsing command line prompts###


if __name__ == '__main__':
    #grab command line input
    opts = parse_cmdline_params(sys.argv[1:])
    date = opts.date_path #input date of run


    #Set up input file name shortcuts
    path = "/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/" + date
    base_path = path + "/BaselineSamples.csv"
    Asp_path = path + "/All_good_Aspen.fasta"
    new_GB_path = path + "/All_good_GB_Final.fasta"


    #####
    #####CREATE GENBANK FASTA FILE W/BASELINE TAGS
    #####


    Baseline=pd.read_csv(base_path) #dataframe of baseline metadata
    Baselist=pd.DataFrame(Baseline['CAOC Number'][Baseline['Type of Specimen'].notnull()]) #list of only baseline samples
    print(Baselist)
    NewGB=open(new_GB_path,"w")
    n=0
    q=0

    ###Loop through original Aspen file to create New GenBank fasta
    for record in SeqIO.parse(Asp_path,"fasta"):

        if record.id in Baselist['CAOC Number'].to_list():  #append keyword only if in list of baseline samples
            print(record.id+' [keyword=purposeofsampling:baselinesurveillance]')
            NewGB.writelines([">",record.id,' [keyword=purposeofsampling:baselinesurveillance]',"\n",str(record.seq),"\n"])
            q=q+1
        else:
            print(record.id)
            NewGB.writelines([">",record.id,"\n",str(record.seq),"\n"])


        n=n+1
    print(n) #336 unfiltered
    print(q) #77 of them were Baseline
