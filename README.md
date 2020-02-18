# Science-Fair
This is the Repository for all my 2019 Science Fair Project

## Problem statement:
Can a classification model predict whether or not a twitter user could be a potential mass shooter?

## Hypothesis:
If the program is trained with data from a mass killer’s manifesto then, the program will find users that might be at risk.

## Abstract:
The purpose of this experiment is to find potential mass murderers using Twitter data, mass murders’ manifestos, and machine learning. 

The procedures were: 1st- Analyze the manifestoes for threatening statements and hate speech as defined by Cambridge dictionary. 
2nd-Put the data found from the manifestos into “train.csv”. If the statement is offensive put “Class_B” next to it and if it is not put “Class_A” next to the statement.
3rd-Extract the tweets from the Twitter API (Application Program Interface) and put the tweets into a csv called “test_tweets.csv”.
4th-Train the neural network with “train.csv” and test if the selected tweets are hate speech/ threatening or not with “test_tweets.csv”.
5th-Save the results into the text file “Predictions.txt” and record results.
  
  After recording the data the neural network was right 10 out of the 11 times it was tested. Which makes the accuracy 0.91. The accuracy of positive predictions was 0.93. The amount of positives identified correctly was 0.90. There were 6 true positives, 0 false positives, 4 true negatives, and 1 false negative.
  
  In conclusion, the neural network was able to tell the difference between a regular user and a potential mass shooter. Although the predictions were not 100% right the confidence interval was statistically sound.
  
## Background Reasurch
  Mass shootings have been in the news a lot in the past few years. That’s because of the rate at which they are happening. In 2019 there were more mass shootings than days in the year. But, what is a mass shooting? The Congressional Research Service defines it as events where more than four people are killed with a firearm, and in one or more locations nearby. One way to combat this is to use patterns made by previous mass shooters to find potential offenders. Most mass shooters have a few traits in common. These traits can include: being motivated by revenge, desire fame or glory, and show dangerous warning signs.<br/><br /> 
	How can we accurately find potential killers using the common traits previously stated? Machine Learning is a subset of AI that gives computers the ability to learn and improve from training without explicit instructions. Using Machine Learning, it is possible to determine if someone is a potential mass shooter using a sufficiently large dataset. To do this, my experiment would have to use a classification model. A classification model attempts to draw conclusions from observed values. In other words, it has an output resembling a category. An example of a classification model output would be rain or no rain.<br/><br/> 
In this project, I used the Naive Bayes classifier, which uses the Bayes Theorem to make predictions. It is called naive because it assumes that the variables are independent of each other. It's called Bayes or Bayesian because it uses the Bayes Theorem to make classifications. The Bayes Theorem can determine the probability of two classes based on training data. The formula is P(a | b)=P(b | a)P(a)P(b). P(a | b) represents the probability that a and b are true, the same is true for P(b | a). P(a) is the probability that a is true; similarly, P(b) is the probability that b is true. Other applications of Naive Bayes are spam detection, sentiment analysis, recommendation systems, etc.<br/><br />
  Artificial Intelligence uses a variety of languages, but Python is the most popular and the one used in this project. Google does a lot of AI projects, most of which are done in Python. A recent example is called Automated mechanism design via neural networks. They made a neural network that learns to design revenue mechanisms. Another commonly used programming language is R. According to analyticstraining.com R features more than the typical bar charts and line plots, but also many ways to represent multidimensional data.<br/><br />

  
## Definitions:
true positive (TP) - outcome where the model correctly predicts the positive class.<br />
true negative (TN) - outcome where the model correctly predicts the negative class.<br />
false positive (FP) - outcome where the model incorrectly predicts the positive class.<br /> 
false negative (FN) - outcome where the model incorrectly predicts the negative class.<br />
Accuracy - fraction of predictions our model got right.<br />
Precision - the proportion of positive identifications that were correct.<br /> 
Recall - the amount of positives identified correctly.<br />  
F1 score - a weighted harmonic mean of precision and recall such that the best score is 1.0 and the worst is 0.0<br />
Macro average - the average of the precision and recall of the system on different sets<br />
Weighted average - an average resulting from the multiplication of each component by a factor reflecting its importance<br />
Manifesto - a public declaration of policy and aims<br />
Hate speech - public speech that expresses hate or encourages violence towards a person or group based on something such as race,   religion, sex, or sexual orientation<br />
Confidence Interval - a type of estimate computed from the statistics of the observed data<br />
Neural network - a set of algorithms, modeled loosely after the human brain, that are designed to recognize patterns<br />
API (Application Program Interface) - a set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service.<br />
Mass shooting - three or more killings in a single incident<br />
Mass murderer - a person who commits mass murder<br />
