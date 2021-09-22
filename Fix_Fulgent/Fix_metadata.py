#!/usr/bin/env python
import sys
import argparse
import io
import os
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date

###Parsing command line prompts###
def parse_cmdline_params(cmdline_params):
    info = "Date path to Fulgent sample set"
    parser = argparse.ArgumentParser(description=info)
    parser.add_argument('-d', '--date_path', required=True,
                        help='Input a date in form FUL_2021-09-14')
    return parser.parse_args(cmdline_params)
###Parsing command line prompts###



#####HELPER FUNCTIONS
def calculate_age(born):
    born = datetime.strptime(born, "%m/%d/%Y").date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#Add GIDAIS name to IDs
def add_GIS(ID):
    GISID = 'hCoV-19/USA/CA-CDC-' + ID + '/2021'
    return(GISID)



if __name__ == '__main__':
    #grab command line input
    opts = parse_cmdline_params(sys.argv[1:])
    path = opts.date_path #input where to do assembly QC

    #Set up input file name shortcuts
    date = "/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/" + path
    meta_path = date + '/' + date + '_metadata.csv'    #Input metadata has name in very standard format
    QC_path = date + "/Assembly_QC/HighCoverage.csv"   #Input list of QC-passing samples


    #####Process metadata
    InMeta = pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Fulgent_file_for_Jesse_09152021.csv")
    InMetanoNA = InMeta[InMeta[['Date of Birth','Date of Collection','Gender']].notnull().all(1)]   #Remove all incomplete data
    print(InMetanoNA)

    #####Read in samples that passed QC
    PassQC_df = pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Assembly_QC/HighCoverage.csv")

    #####Merge for Complete Metadata &&& Passing QC
    PassQC_meta = InMetanoNA.merge(PassQC_df,how='inner',left_on='Public ID',right_on='Passing_IDs')

    #####Edit DOB information
    PassQC_meta['Age'] = PassQC_meta['Date of Birth'].apply(calculate_age)
    #print(PassQC_meta['Age']) #It worked like a charm!



    #####
    #####OUTPUTS
    #####

    #Set up input file name shortcuts
    out_meta_path = date + '/Final_Passing_Metadata.csv'   #Output complete metadata of QC-passing samples
    pass_path = date + "/Passing_Samples.csv"              #Output list of of QC-passing samples
    pass_GIS_path = date + "/Passing_Samples_GIS.csv"
    base_path = date + "/BaselineSamples.csv"


    #####Output metadata for Passing Samples
    PassQC_meta.to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Final_Passing_Metadata.csv",index=False)

    #####Make a list of Passing Samples
    PassQC_meta['Public ID'].to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Passing_Samples.csv",index=False)

    #####Make a GISAID-friendly list
    PassQC_meta['Public GIS ID'] = PassQC_meta['Public ID'].apply(add_GIS)  #add GISAID prefix and suffix
    PassQC_meta['Public GIS ID'].to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Passing_Samples_GIS.csv",index=False)

    #####Make a list of Baseline Surveillance samples for GenBank tagging
    PassQC_meta['Public ID'][PassQC_meta['Baseline Surveilance'].notnull()].to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/BaselineSamples.csv",index=False)
