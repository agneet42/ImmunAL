setwd('C:\\Users\\USER\\Desktop\\agneet\\New')
source("https://bioconductor.org/BiocInstaller.R")
biocLite("IlluminaHumanMethylation27k.db")

library("IlluminaHumanMethylation450k.db")

a=read.delim('methyl_test.txt', header= FALSE, sep='\n');
d=dim(a)
i=d[1]
b<-NULL
for (j in (1:i)){
  
  probeId = toString(a[j,1])
  j=j+1
  
  b[j] <- unlist(mget(x = probeId,envir = IlluminaHumanMethylation450kSYMBOL))
  
  write.csv(b, "data1.csv")
}
