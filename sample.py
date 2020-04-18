import random
from extract import single_column
'''这里的预测结果有两列，一列是max，一列是ave.需要修改的参数就是return部分'''


def sample(filepath_pos, filepath_neg, seed, proportion=1):
    '''这是一个对负样本随机采样的函数'''
    random.seed(seed)
    pos_name = single_column(filepath_pos, 0, removetitle=False)
    pos_max = single_column(filepath_pos, 1, removetitle=False)
    pos_ave = single_column(filepath_pos, 2, removetitle=False)

    neg_name = single_column(filepath_neg, 0, removetitle=False)
    neg_max = single_column(filepath_neg, 1, removetitle=False)
    neg_ave = single_column(filepath_neg, 2, removetitle=False)

    pos_num = len(pos_name)
    neg_num = pos_num * proportion

    #下面用随机函数进行采样
    neg_max_sample = []
    neg_ave_sample = []
    neg_name_sample = random.sample(neg_name, neg_num)
    for i in neg_name_sample:
        loc = neg_name.index(i)
        neg_max_sample.append(neg_max[loc])
        neg_ave_sample.append(neg_ave[loc])

    temp1 = [1 for i in range(len(pos_name))]
    temp2 = [0 for j in range(len(neg_name_sample))]
    temp1.extend(temp2)
    pos_max.extend(neg_max_sample)
    pos_ave.extend(neg_ave_sample)
    return neg_name_sample, temp1, pos_max