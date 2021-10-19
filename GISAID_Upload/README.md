# How to Use GISAID Header Converter
Use the Start.sh within ~/Tools/APHL_Covid_Genomics/GISAID_Uploads   (though it shouldn't matter)

For Orange County:
  -**d** Date filepath in the form "YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-OC-" (no input default is "CA-OC-")

**Ex.** ./Start.sh -d 2021-08-31 -L "CA-OC-" OR ./Start.sh -d 2021-08-31


For San Luis Obispo:
  -**d** Date filepath in the form "SLO_YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-SLOPH-"

**Ex.** ./Start.sh -d SLO_2021-07-20 -L "CA-SLOPH-"

For San Luis Obispo ClearLabs
  -**d** Date filepath in the form "SLO_YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-SLOPH-"
  -**s** Sequencing technology -- any input indicates clearlabs
**Ex.** ./Start.sh -d SLOC_2021-10-05 -L "CA-SLOPH-" -s


For Fulgent:
  -**d** Date filepath in the form "FUL_YYYY-MM-DD"
  -**L** Shorthand name of the Lab "CA-CDC-FG-"

**Ex.** ./Start.sh -d FUL_2021-08-12 -L "CA-CDC-FG-"
