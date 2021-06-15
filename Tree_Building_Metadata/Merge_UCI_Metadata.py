import os
import sys
import gzip
import gzip
import csv
import pandas as pd

UCI_IDs=pd.read_csv("~/Desktop/Covid_Genomics_APHL/Tree_Building/UCI_list.csv")
All_meta=pd.read_csv("~/Desktop/Covid_Genomics_APHL/Tree_Building/ALL_OCPHL_metadata.csv")


UCI_meta=pd.merge(UCI_IDs,All_meta,how="inner",on="covv_virus_name")


UCI_meta.to_csv("~/Desktop/Covid_Genomics_APHL/Tree_Building/UCI_metadata.csv")
