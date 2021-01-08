setwd('C:\\Users\\USER\\Desktop\\agneet\\New')
library("illuminaHumanv4.db")
a=read.delim('full test.txt', header= FALSE, sep='\n')
d=dim(a)
i=d[1]
b<-NULL
for (j in (1:i)){
  
  probeId = toString(a[j,1])
  j=j+1
  b[j] <- unlist(mget(x = probeId,envir = illuminaHumanv4SYMBOL))
  
 write.csv(b, "data.csv")
}

