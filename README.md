# APHL-Covid-Genomics
Scripts developed for Orange and San Luis Obispo County Public Health Laboratories


**To Start:** GISAID_Uploads/Start.sh
  - **Create a new RUN directory** with naming convention "FUL_2021-09-28"
    - Data source (PHL) _ yyyy-mm-dd
  - Enter new RUN directory
  - Add metadata to RUN directory
  - Create new directory **"Fasta_Pieces"**
  - Fill Fasta_Pieces with **individual assemblies**
  - Run **GISAID_Uploads/Start.sh** according to GISAID_Uploads/README.md


**What This Does:**
  - Takes input of Fulgent metadata (in a fairly standardized format)
    - Filters out samples with incomplete metadata (collection date, gender, birth date)
    - Creates list of Baseline surveillance samples
  - Perform Assembly_QC on Samples
    - Checks coverage
    - Checks # of consecutive unambiguous nucleotides (>10k)
    - Creates list of QC-passing samples with GISAID-formatted and normally-formatted IDs
  - Filters out Assemblies lacking metadata or not passing QC
  - Format Assemblies for GISAID
    - Take individual assemblies, change headers to "hCoV-19/USA/CA-{name here}-##/2021"
    - Concatenate files into All_good.fasta
  - Format Assemblies for Aspen
    - Just concatenate files
  - Format Assemblies for GenBank
    - Takes input of Baseline surveillance status
    - Adds keyword to fasta header of surveillance samples
  
 
