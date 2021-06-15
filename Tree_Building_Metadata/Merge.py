import os
import sys
import gzip
import gzip
import csv
import pandas as pd

UCI_Pango=pd.read_csv("~/Desktop/Covid_Genomics_APHL/Tree_Building/UCI_Pango_Results.csv")
UCI_meta=pd.read_csv("~/Desktop/Covid_Genomics_APHL/Tree_Building/UCI_Terra_metadata.csv")

UCI_meta=pd.merge(UCI_meta,UCI_Pango,how="inner",on="entity:UCI_specimen_id")


UCI_meta.to_csv("~/Desktop/Covid_Genomics_APHL/Tree_Building/UCI_metadata_Pango.csv")
