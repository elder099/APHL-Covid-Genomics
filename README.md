# APHL-Covid-Genomics
Scripts developed for Orange and San Luis Obispo County Public Health Laboratories


**To Start:** GISAID_Uploads/Start.sh
  - **Create a new RUN directory** in ~/Assembly_QC with naming convention "SLO_2021-10-05"
    - Data source (PHL) _ yyyy-mm-dd
  - Enter new RUN directory
  - Add metadata to RUN directory
  - Create new directory **"Fasta_Pieces"**
  - Fill Fasta_Pieces with **individual assemblies**
  - Run **Start.sh** according to next section

## How to Use GISAID Header Converter)
Use the Start.sh within ~/Tools/APHL_Covid_Genomics/ 
(complete examples in GISAID_Upload/README.md)

For San Luis Obispo:
  -**d** Date filepath in the form "SLO_YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-SLOPH-"

**Ex.** ./Start.sh -d SLO_2021-07-20 -L "CA-SLOPH-"

For San Luis Obispo ClearLabs
  -**d** Date filepath in the form "SLO_YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-SLOPH-"
  -**s** Sequencing technology -- any input indicates clearlabs
**Ex.** ./Start.sh -d SLOC_2021-10-05 -L "CA-SLOPH-" -s asdf



**What This Does:**
  - Format Assemblies for GISAID
    - Take individual assemblies, change headers to "hCoV-19/USA/CA-{name here}-##/2021"
    - Concatenate files into All_good.fasta
  - Format Assemblies for Aspen
    - Just concatenate files
  - Format Assemblies for GenBank (optional, not implemented)
    - Takes input of Baseline surveillance status
    - Adds keyword to fasta header of surveillance samples
  - Perform Assembly_QC on Samples
    - Checks coverage
    - Checks # of consecutive unambiguous nucleotides (>10k)
  
 
