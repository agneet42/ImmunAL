library(csbl.go)
set.prob.table(organism=TAXONOMY.HUMAN, type="similarity")
ent <- entities.from.text("C:/Users/USER/Desktop/agneet/results/layer2/modifiedGO.txt")
n<-entity.sim.many(ent, "MF", "Resnik");
write.csv(n,"C:/Users/USER/Desktop/agneet/results/layer2/test1.csv")
