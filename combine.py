import numpy as np
def combine(dict_l1, l1, dict_l2, l2):
    '''根据字典组合数据，最后形成一个邻接矩阵，第1，3个参数是字典，2,4个参数是交互数据的两列'''
    mylist = []
    count = 0
    #首先遍历第一个字典，为字典中每一个元素创建一个字典2长度的向量。根据情况补1
    for drug in dict_l1:
        #如果药物有交互，则补1
        if drug in l1:
            tempt = [key for key, value in enumerate(l1) if value == drug]
            one = [0 for i in range(len(dict_l2))]
            for t in tempt:
                if l2[t] in dict_l2:
                    one[dict_l2.index(l2[t])] = 1
                    count += 1
            mylist.append(one)
        #如果药物只在字典中出现，但是并没有交互，则创建全0向量
        else:
            one = [0 for i in range(len(dict_l2))]
            mylist.append(one)
    #最后把列表嵌套转换成numpy的矩阵
    mat = np.array(mylist)
    print('count' , count)
    return mat