#For El Paso Shooter
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
words = re.findall(r'\w+', open("PasoShooter.txt").read().lower())
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
count = Counter(words).most_common(50)
plt.rcParams["figure.figsize"] = (20,8)
df = pd.DataFrame(count, columns = ['Words', 'number of times used'])
df.plot.bar(x='Words',y='number of times used')
plt.title("Most Common words used in the El Paso Shooter's manifesto")

#For Dylann Roof
words = re.findall(r'\w+', open("Dylan Roof.txt").read().lower())
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
count = Counter(words).most_common(50)
plt.rcParams["figure.figsize"] = (20,8)
df = pd.DataFrame(count, columns = ['Words', 'number of times used'])
df.plot.bar(x='Words',y='number of times used')
plt.title("Most Common words used in Dylann Roof's manifesto")

#The rest are the same but using different folders :-)
