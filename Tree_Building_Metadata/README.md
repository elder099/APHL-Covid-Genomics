# Tree-Building Metadata Workflow

1. *Merge_UCI_Metadata.py*: Inner join merging UCI_list.csv & ALL_OCPHL_metadata.csv -> UCI_metadata.csv
   - Take only metadata from UCI samples
2. *UCI_Terra_metadata.csv*: Filter UCI_metadata.csv -> UCI_Terra_metadata.csv
   - Take only metadata needed for Terra upload
3. *Merge.py*: Inner join merging UCI_Terra_metadata.csv & UCI_Pango_Results.csv -> UCI_metadata_Pango.csv
   - Match UCI_specimen_id's & append pangolin result data
4. *UCI_Complete_Metadata*: Edit UCI_metadata_Pango.csv to prepare for upload to Terra
