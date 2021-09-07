###GenBank and GISAID IDs w/in-house sample names
db_id<-read.csv("~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/resubs/CAOC_DB_IDs.csv",header=TRUE)
###Samples that are baseline surveillance w/in-house smaple names
bs_id<-read.csv("~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/resubs/Baseline_IDs.csv",header=TRUE) 
db_id
bs_id

bs_id[!(bs_id$OCPHL %in% db_id$miseq_specimen_id),]; dim(bs_id[!(bs_id$OCPHL %in% db_id$miseq_specimen_id),])[1]
#49 unsubmitted or already labeled samples
db_id[!(db_id$miseq_specimen_id %in% bs_id$OCPHL),]; dim(db_id[!(db_id$miseq_specimen_id %in% bs_id$OCPHL),])[1]
#57 samples are not baseline surveillance



############
###Making database ID dataset from only baseline surveillance samples
bl_surveil_ids<-inner_join(bs_id,db_id,by=c("OCPHL" = "miseq_specimen_id"))

bl_surveil_ids
dim(db_id)[1]-57   #309 samples are surveillance
sum(bl_surveil_ids$genbank_accession=="") #After removing non-surveillance samples, 12 were not accepted to Genbank


############
###These are known GenBank IDs from BioProject PRJNA748084
gb_ids<-read.csv("~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/resubs/AddKeyword_OC_20210907.csv",header=TRUE)

db_id[!(db_id$genbank_accession %in% gb_ids$Accession.ID),]; dim(db_id[!(db_id$genbank_accession %in% gb_ids$Accession.ID),])[1] 
#14 uploaded samples do not have a genbank accession
gb_ids[!(gb_ids$Accession.ID %in% db_id$genbank_accession),] #no missing accessions

###Merging all database IDs w/known GenBank IDs
gb_id_merge<-inner_join(db_id,gb_ids,by=c("genbank_accession" = "Accession.ID"))
dim(gb_id_merge); dim(db_id)[1]; 366 - 14  #This works out


############
###Merging baseline surveillance data w/known GenBank IDs
Mix<-inner_join(bl_surveil_ids,gb_id_merge,by=c("genbank_accession")) #This is like removing 12 non-surveillance samples
Mix; dim(Mix); 309 - 12 #this matches 309 baseline samples excluding 12 that were not accepted to GenBank

###Final dataset only includes GenBank IDs and new Keyword
Fin<-data.frame(genbank_accession=Mix$genbank_accession,Keyword=Mix$Keyword)
Fin
write.csv(Fin,"~/Desktop/Covid_Genomics_APHL/GISAID_Uploads/resubs/CAOC_Keywords_GenBank.csv",row.names=FALSE)


