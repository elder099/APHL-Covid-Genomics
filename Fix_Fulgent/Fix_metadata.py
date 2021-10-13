#!/usr/bin/env python
import sys
import argparse
import io
import os
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date as dates

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
    today = dates.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))  #age in years
    if age > 0:
        return age
    else:  #Infant ages in months
        month_age = today.month - born.month + 12*(today.year > born.year) - (today.day < born.day) - 1  #+12* because no negatives, -1 because python months add 1
        if month_age == 1:
            return str(month_age) + " month"
        else:
            return str(month_age) + " months"
    #return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#Add GIDAIS name to IDs
def add_GIS(ID):
    GISID = 'hCoV-19/USA/CA-CDC-' + ID + '/2021'
    return(GISID)


if __name__ == '__main__':
    #grab command line input
    opts = parse_cmdline_params(sys.argv[1:])
    date = opts.date_path #input where to do assembly QC

    #Set up input file name shortcuts
    path = "/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/" + date
    meta_path = path + '/' + date + '_metadata.csv'    #Input metadata has name in very standard format
    QC_path = path + "/Assembly_QC/HighCoverage.csv"   #Input list of QC-passing samples


    #####Process metadata
    InMeta = pd.read_csv(meta_path)
    InMetanoNA = InMeta[InMeta[['Date of Birth','Date of Collection','Gender']].notnull().all(1)]   #Remove all incomplete data
    print(InMetanoNA)

    #####Read in samples that passed QC
    PassQC_df = pd.read_csv(QC_path)

    #####Merge for Complete Metadata &&& Passing QC
    PassQC_meta = InMetanoNA.merge(PassQC_df,how='inner',left_on='Public ID',right_on='Passing_IDs')
    #####Edit DOB information
    PassQC_meta['Age'] = PassQC_meta['Date of Birth'].apply(calculate_age)
    #print(PassQC_meta['Age']) #It worked like a charm!


    #####
    #####OUTPUTS
    #####

    #Set up input file name shortcuts
    out_meta_path = path + '/Final_Passing_Metadata.csv'   #Output complete metadata of QC-passing samples
    pass_path = path + "/Passing_Samples.csv"              #Output list of of QC-passing samples
    pass_GIS_path = path + "/Passing_Samples_GIS.csv"
    base_path = path + "/BaselineSamples.csv"


    #####Output metadata for Passing Samples
    PassQC_meta.to_csv(out_meta_path,index=False)

    #####Make a list of Passing Samples
    PassQC_meta['Public ID'].to_csv(pass_path,index=False)

    #####Make a GISAID-friendly list
    PassQC_meta['Public GIS ID'] = PassQC_meta['Public ID'].apply(add_GIS)  #add GISAID prefix and suffix
    PassQC_meta['Public GIS ID'].to_csv(pass_GIS_path,index=False)

    #####Make a list of Baseline Surveillance samples for GenBank tagging
    PassQC_meta['Public ID'][PassQC_meta['Baseline Surveillance'].notnull()].to_csv(base_path,index=False)
