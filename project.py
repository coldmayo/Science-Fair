import re
from collections import Counter
from nltk.corpus import stopwords
def counter(numb,doc,namee):
    words = re.findall(r'\w+', open(doc).read().lower())
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    count = Counter(words).most_common(numb)
    print(namee,"\n")
    return(count)
#El Paso Shooter numb=110
print(counter(110,'El Paso Shooter.txt', 'El Paso Shooter'))
#Elliot Rodger numb=200
print(counter(200,'Eloit Rodger.txt', 'Eloit Rodger'))
#Jim David Adkisson numb=120
print(counter(120,'Jim David Adkisson.txt', 'Jim David Adkisson'))
#Dylann Roof numb=150
print(counter(150,'Dylann Roof.txt', 'Dylann Roof'))
#Seuong Cho
print(counter(140,'Sueong Cho.txt', 'Seuong Cho'))
