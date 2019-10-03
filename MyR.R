num.csv <- read.csv("Eloit Rodger.csv", header=True, sep=";")
install.packages("ggplot2"); #ggplot2 is not part of the standard install...
library(ggplot2);
qplot(X, Y, data=num.csv);