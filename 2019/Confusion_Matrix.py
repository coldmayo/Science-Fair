from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from IPython.display import Image
print(Image(filename='conf.png'))
print ('\nClasification report:\n', classification_report(y_true,y_pred))
print ('\nConfussion matrix:\n',confusion_matrix(y_true,y_pred))
with open("ConfusionMat+ClassRep.txt", 'w') as f:
    f.write('Confusion Matrix:')
    f.write('\n')
    f.write(np.array2string(confusion_matrix(y_true, y_pred), separator=', '))
    f.write('\n')
    f.write('Classification Report:')
    f.write('\n')
    f.write(classification_report(y_true,y_pred))
f.close()
