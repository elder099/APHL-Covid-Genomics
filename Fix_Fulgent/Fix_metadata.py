#!/usr/bin/env python
import sys
import argparse
import io
import os
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date

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

    InMeta = pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Fulgent_file_for_Jesse_09152021.csv")
    InMetanoNA = InMeta[InMeta[['Date of Birth','Date of Collection','Gender']].notnull().all(1)]
    print(InMetanoNA)

    PassQC_df = pd.read_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Assembly_QC/HighCoverage.csv")

    ###Merge for Complete Metadata &&& Passing QC
    PassQC_meta = InMetanoNA.merge(PassQC_df,how='inner',left_on='Public ID',right_on='Passing_IDs')

    #print([i for i in PassQC_df['Passing_IDs'].to_list() if i not in PassQC_meta['Public ID'].to_list()])  #Confirmed to have worked

    ###Edit DOB information
    PassQC_meta['Age'] = PassQC_meta['Date of Birth'].apply(calculate_age)
    #print(PassQC_meta['Age']) #It worked like a charm!


    ###Output metadata for Passing Samples
    PassQC_meta.to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Final_Passing_Metadata.csv",index=False)

    ###Make a list of Baseline Surveillance samples for GenBank tagging
    PassQC_meta['Public ID'][PassQC_meta['Baseline Surveilance'].notnull()].to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/BaselineSamples.csv",index=False)

    ###Make a list of Passing Samples
    PassQC_meta['Public ID'].to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Passing_Samples.csv",index=False)

    ###Make a GISAID-friendly list
    PassQC_meta['Public GIS ID'] = PassQC_meta['Public ID'].apply(add_GIS)
    PassQC_meta['Public GIS ID'].to_csv("/Users/Gawdcomplex/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-09-21/Passing_Samples_GIS.csv",index=False)
