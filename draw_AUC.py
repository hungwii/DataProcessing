from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sample import sample
'''调用采样函数进行采样，调用sklearn的函数计算fpr,tpr,计算auc,然后画图'''

#参数设置
proportion = 1 #正样本是负样本的多少倍？
filepath_pos = 'H:\\Data\\eps_new0417\\p-n-data\\positive_data.txt' #正样本文件
filepath_neg = 'H:\\Data\\eps_new0417\\p-n-data\\negative_data.txt' #负样本文件
seed = 6306 #设置随机种子的大小





#采样(这里注意不同方法对应不同数量的参数)
neg_name, drug_label, max_score = sample(filepath_pos, filepath_neg, seed, proportion=proportion)
#调用函数计算ROC, AUC
fpr, tpr, threshold = roc_curve(drug_label, list(map(float, max_score)))
roc_auc = auc(fpr, tpr)


#画ROC图
plt.figure()
lw = 2
plt.figure(figsize=(10, 8))
plt.plot(fpr, tpr, color='darkorange',
lw = lw, label = 'AUROC = %0.3f' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# plt.title('Roc Curve')
plt.legend(loc="lower right")
plt.savefig('H:\\Data\\eps_new0417\\'+str(roc_auc)+'ave.eps', dpi=1200, format='eps')
plt.show()

print('此时auc大小为', roc_auc)
print('随机种子的大小', seed)


print('end')


