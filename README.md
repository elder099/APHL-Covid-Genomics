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
  

**Examples to Copy/Pasta**

For Orange County:
  -**d** Date filepath in the form "YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-OC-" (no input default is "CA-OC-")

**Ex.** ./Start.sh -d 2021-08-31 -L "CA-OC-" 
OR 
**Ex.** ./Start.sh -d 2021-08-31


For San Luis Obispo:
  -**d** Date filepath in the form "SLO_YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-SLOPH-"

**Ex.** ./Start.sh -d SLO_2021-07-20 -L "CA-SLOPH-"


For Fulgent:
  -**d** Date filepath in the form "FUL_YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-CDC-FG-"

**Ex.** ./Start.sh -d FUL_2021-08-12 -L "CA-CDC-FG-" 
