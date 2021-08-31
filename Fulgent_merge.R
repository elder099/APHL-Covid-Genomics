library(tidyverse)

#options(scipen=999)  #Change options so no scientific notation
Gender=read.csv("~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-08-12/Gender_meta.csv",header=TRUE,stringsAsFactors = T)
Gender

Other=read.csv("~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-08-12/FUL_meta.csv",header=TRUE); Other
colnames(Other)
colnames(Gender)

Meta=inner_join(Other,Gender,by=c("External.Accession" = "Accession.Number"));Meta

write.csv(Meta,"~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/FUL_2021-08-12/Complete_FUL_meta.csv")
?merge
