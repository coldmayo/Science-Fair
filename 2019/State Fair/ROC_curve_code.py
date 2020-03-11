test_labels=[]
for i in df2['TRUE']:
    if i=='Class_A':
        test_labels.append(0)
    else:
        test_labels.append(1)
from sklearn.metrics import roc_auc_score

y_pree=[]
for j in y_pred:
    if j=='Class_A':
        y_pree.append(0)
    else:
        y_pree.append(1)

# Calculate roc auc
roc_value = roc_auc_score(test_labels, y_pree)
base_fpr, base_tpr, _ = roc_curve(test_labels, [1 for _ in range(len(test_labels))])
model_fpr, model_tpr, _ = roc_curve(test_labels, test_labels)

plt.figure(figsize = (8, 6))
plt.rcParams['font.size'] = 16
    
    # Plot both curves
plt.plot(base_fpr, base_tpr, 'b', label = 'baseline')
plt.plot(model_fpr, model_tpr, 'r', label = 'model')
plt.legend();
plt.xlabel('False Positive Rate'); 
plt.ylabel('True Positive Rate'); plt.title('ROC Curves');
plt.show();
