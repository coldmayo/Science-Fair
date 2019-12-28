# Science-Fair
This is the Repository for all my 2019 Science Fair Project

## Problem statement:
Will the neural network be able to predict whether or not a twitter user could be a potential mass shooter?

## Hypothesis:
If the program is trained with data from mass killer’s manifesto then, the program will find users that might be at risk.

## Abstract:
The purpose of this experiment is to find potential mass murderers using Twitter data, mass murders’ manifestos, and machine learning. 

The procedures were: 1st- Analyze the manifestoes for threatening statements and hate speech as defined by Cambridge dictionary. 
2nd-Put the data found from the manifestos into “train.csv”. If the statement is offensive put “Class_B” next to it and if it is not put “Class_A” next to the statement.
3rd-Extract the tweets from the Twitter API (Application Program Interface) and put the tweets into a csv called “test_tweets.csv”.
4th-Train the neural network with “train.csv” and test if the selected tweets are hate speech/ threatening or not with “test_tweets.csv”.
5th-Save the results into the text file “Predictions.txt” and record results.
  
  After recording the data the neural network was right 10 out of the 11 times it was tested. Which makes the accuracy 0.91. The accuracy of positive predictions was 0.93. The amount of positives identified correctly was 0.90. There were 6 true positives, 0 false positives, 4 true negatives, and 1 false negative.
  
  In conclusion, the neural network was able to tell the difference between a regular user and a potential mass shooter. Although the predictions were not 100% right the confidence interval was statistically sound.
  
## Definitions:
true positive (TP) - outcome where the model correctly predicts the positive class.\n
true negative (TN) - outcome where the model correctly predicts the negative class.
false positive (FP) - outcome where the model incorrectly predicts the positive class. 
false negative (FN) - outcome where the model incorrectly predicts the negative class.
Accuracy - fraction of predictions our model got right. The equation for that is: TP+TNTP+FP+FN+TN
Precision - the proportion of positive identifications that were correct. The equation for that is: TPTP+FP
Recall - the amount of positives identified correctly. The equation is TPTP+FN 
F1 score - a weighted harmonic mean of precision and recall such that the best score is 1.0 and the worst is 0.0.
Macro average - the average of the precision and recall of the system on different sets
Weighted average - an average resulting from the multiplication of each component by a factor reflecting its importance
Manifesto - a public declaration of policy and aims
Hate speech - public speech that expresses hate or encourages violence towards a person or group based on something such as race,   religion, sex, or sexual orientation
Confidence Interval - a type of estimate computed from the statistics of the observed data
Neural network - a set of algorithms, modeled loosely after the human brain, that are designed to recognize patterns
API (Application Program Interface) - a set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service.
Mass shooting - three or more killings in a single incident
Mass murderer - a person who commits mass murder
