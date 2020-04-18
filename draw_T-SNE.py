from extract import single_column
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


file_dic = 'H:\\Data\\dict\\Covs-protein_dict127.txt'
file_protein = 'H:\\Data\\dict\\protein5390_dict.txt'
dic_temp = single_column(file_dic, 0, removetitle=True)
pro = single_column(file_protein, 0, removetitle=True)
#去除字典中的重复
dic = list(set(dic_temp))

locs = []
for loc, name in enumerate(dic):
    if name in pro:
        locs.append(pro.index(name))

#保存新冠蛋白的向量
data_pro = []
file_protein = 'C:\\Users\\hw\\Desktop\\all_protein.txt'
with open(file_protein, 'r', encoding='utf-8') as f:
    contents = f.readlines()
    for loc in locs:
        data_pro.append(contents[loc].split())

#把116个向量中的字符串转换为数字
data_protein = []
for li in data_pro:
    temp = list(map(float, li))
    data_protein.append(temp)

#下面处理药物数据

# file_dic_drug = 'H:\\Data\\dict\\drug2953_dict.txt'
file_rank_drug = 'C:\\Users\\hw\\Desktop\\drug_dict_top_number.txt'
file_drug = 'C:\\Users\\hw\\Desktop\\all_drug_600.txt'
top = 200

nums_drug = single_column(file_rank_drug, 0, removetitle=True)[0:top]
locs_drug = list(map(int, nums_drug))
data_drug = []
with open(file_drug, 'r', encoding='utf-8') as ff:
    lines = ff.readlines()
    for loc_drug in locs_drug:
        data_drug.append(lines[loc_drug].split())

#建立标签
label_drug = [1 for i in range(top)]
label_pro = [0 for j in range(116)]

########################################################################################################################
#对数据进行预处理
def plot_embedding(data, label, title):
    """
    :param data:数据集
    :param label:样本标签
    :param title:图像标题
    :return:图像
    """
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)		# 对数据进行归一化处理
    fig = plt.figure()		# 创建图形实例
    ax = plt.subplot(111)		# 创建子图
    # 遍历所有样本
    for i in range(data.shape[0]):
        # 在图中为每个数据点画出标签
        plt.text(data[i, 0], data[i, 1], str(label[i]), color=plt.cm.Set1(label[i] / 1),
                 fontdict={'weight': 'bold', 'size': 7})
    plt.xticks()		# 指定坐标的刻度
    plt.yticks()
    plt.title(title, fontsize=14)
    # 返回值
    return fig
#准备数据
data = data_drug + data_protein
label = label_drug + label_pro

print('Starting compute t-SNE Embedding...')
#设置好参数
ts = TSNE(n_components=2, init='pca', random_state=0)
# t-SNE降维
reslut = ts.fit_transform(data)
# 调用函数，绘制图像
fig = plot_embedding(reslut, label, 't-SNE Embedding of digits')
# 显示图像
plt.show()


