from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from IPython.display import Image
print(Image(filename='conf.png'))
print ('\nClasification report:\n', classification_report(y_true,y_pred))
print ('\nConfussion matrix:\n',confusion_matrix(y_true,y_pred))
