import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob

training_corpus = []
test_corpus = []

with open('train.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        training_corpus.append((row['tweets'], row['Classification']))

with open('train2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_corpus.append((row['tweets'], row['Classification']))

model = NBC(training_corpus) 
print(model.classify(""))
print(model.accuracy(test_corpus))
