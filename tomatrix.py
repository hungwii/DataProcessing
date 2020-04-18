import numpy as np
from check import check
from extract import single_column
import copy


def tomatrix(file_dic, filepath, removetitle=False, removefirstcol=False):
    '''把数据转换为矩阵，其中行标题和列标题是否要去掉可以通过最后两个参数决定，第一个参数是文件路径，第二个参数是矩阵的长度'''

    dic_1 = file_dic
    col_1 = single_column(filepath, 0, removetitle=True)

    #创建全0矩阵
    long_mat = len(dic_1)
    mat_a = np.zeros((long_mat, long_mat))

    #打开文件读取数据
    with open(filepath, 'r', encoding='utf-8') as file:
        final_list = []    #用来记录最后剩下的行
        lines = file.readlines()  #把文件的每一行读取进一个列表，列表中每一个元素就是矩阵的一行
        if removetitle == True:  #决定是否删除第一行
            del lines[0]
        if removefirstcol == True: #决定是否删除第一列
            yes1 = 0
            for line in lines:
                tempt_list = line.strip('\n').split() #把每一行拆分成一个列表
                del tempt_list[0]   #对于每一行数据删除第一个，想当于删除了第一列

                #用0去替换列表中的缺失值"NA"
                for miss in tempt_list:
                    try:
                        tempt_list[tempt_list.index(miss)] = float(miss)
                    except ValueError:
                        tempt_list[tempt_list.index(miss)] = float(0)

                # 检查是否清除干净了
                for r, ring in enumerate(tempt_list):
                    if type(ring) != float:
                        print(type(ring))
                        print(ring)
                        print("行数", lines.index(line))
                        print("这个位置出错了:", r)
                        break
                    else:
                        yes1 += 1
                final_list.append(tempt_list)
            print("正确的元素的个数", yes1)

        else:
            yes1 = 0
            for line in lines:
                tempt_list = line.strip('\n').split()
                for miss in tempt_list:
                    try:
                        tempt_list[tempt_list.index(miss)] = float(miss)
                    except ValueError:
                        tempt_list[tempt_list.index(miss)] = float(0)
                #检查是否清除干净了
                for r, ring in enumerate(tempt_list):
                    if type(ring) != float:
                        print("行数", lines.index(line))
                        print("这个位置出错了:", r)
                        break
                    else:
                        yes1 += 1

                final_list.append(tempt_list)
            print("正确的元素的个数", yes1)
    #检查final_list:
    print('总的行数', len(final_list))

    #遍历所有行，删除无用的行以及对应的列
    for drug_name in col_1:
        if drug_name not in dic_1:
            drug_loc = col_1.index(drug_name)
            final_list[drug_loc] = 'XX'
            #删除列
            for pp in final_list:
                if pp != 'XX':
                    pp[col_1.index(drug_name)] = 'X'
                else:
                    continue

    #把标记了要删除的统一删除
    while 'XX' in final_list:
        final_list.remove('XX')
    for undel_col in final_list:
        while 'X' in undel_col:
            undel_col.remove('X')

    #补删除col_1
    for drug0, drug in enumerate(col_1):
        if drug not in dic_1:
            col_1[drug0] = 'XXX'
    while 'XXX' in col_1:
        col_1.remove('XXX')

    #检查删除后的结果
    print('*****删除后的行数：', len(final_list))
    for cccc in final_list:
        if len(cccc) != len(final_list):
            print('删除个数不对')
            print('------------------------')
            break

    #检查数据中0的个数，方便核对
    ehe_num = 0
    for ehes in final_list:
        # print(ehes)
        for ehe in ehes:
            if ehe == float(0):
                ehe_num += 1
    print('*****最后数据中有' + str(ehe_num) + '个0')

    #遍历列表，把列表的值一个一个插入到矩阵中,由于是对称的，所以用双循环来实现
    for drug_1 in col_1:
        a = dic_1.index(drug_1)
        aa = col_1.index(drug_1)
        for drug_2 in col_1:
            c = dic_1.index(drug_2)
            cc = col_1.index(drug_2)
            mat_a[a][c] = final_list[aa][cc]

    return mat_a
