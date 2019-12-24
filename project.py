import csv
import pandas as pd
from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob

training_corpus = []
test_corpus = []
test_tweets = []
y_pred= []
y_true= []
with open('train.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        training_corpus.append((row['tweets'], row['Classification']))

with open('train2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_corpus.append((row['tweets'], row['Classification']))
        
with open('test_tweets.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_tweets.append((row['tweets']))    
        y_true.append((row['TRUE']))
model = NBC(training_corpus)
for tweet in test_tweets:
    pred=model.classify(tweet)
    print(pred)
    y_pred.append(pred)
print((model.accuracy(test_corpus))*100,'percent')
