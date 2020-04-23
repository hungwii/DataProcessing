from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sample import sample
'''调用采样函数进行采样，调用sklearn的函数计算precision,recall,计算auc,然后画图'''

#参数设置
proportion = 1 #正样本是负样本的多少倍？
filepath_pos = 'C:\\Users\\hw\\Desktop\\test\\pn\\positive_data.txt' #正样本文件
filepath_neg = 'C:\\Users\\hw\\Desktop\\test\\pn\\negative_data.txt' #负样本文件
seed = 1710


#采样(这里注意不同方法对应不同数量的参数)
neg_name, drug_label, max_score = sample(filepath_pos, filepath_neg, seed, proportion=proportion)
#调用函数计算ROC, AUC
precision, recall, threshold = precision_recall_curve(drug_label, list(map(float, max_score)))

#计算AUPRC
auprc = 0
long = len(threshold)
#微积分的知识计算曲线下面积
for i in range(0, long-1):
    auprc += (recall[i]-recall[i+1]) * precision[i]
print('prc', auprc)
print(precision)
print("----------------------------")
print(recall)


#画PRC图
plt.figure()
lw = 2 #线条的宽度
plt.figure(figsize=(10, 8)) #图片的尺寸
plt.plot(recall, precision, color='darkorange', lw=lw,
         label = 'AUPR = %0.3f' % auprc) #x,y的数据，线条样式
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--') #对角线
plt.xlim([0.0, 1.0]) #横坐标上下限
plt.ylim([0.0, 1.0])   #纵坐标上下限
plt.xlabel('Recall') #横坐标标题
plt.ylabel('Precision')    #纵坐标标题
# plt.title('PRC Curve')  #图片标题
plt.legend(loc="lower right")
plt.savefig('C:\\Users\\hw\\Desktop\\test\\pn\\pr-max.eps', dpi=1200, format='eps')
plt.show()


print('end')

