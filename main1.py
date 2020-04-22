from extract import single_column
from combine import combine
import numpy as np
from check import check, precheck

'''这个文件主要是调用几个写好的函数，把表示交互反应的文件，根据字典中的顺序，转换成一个邻接矩阵（只有0/1）'''

#输入两个词典和一个交互信息的数据文件路径，file_1，file_2是file_1x2中两个属性的字典
file_1 = 'H:\\Data\\data422\\data\\dict\\gene_dict.txt'
file_2 = 'H:\\Data\\data422\\data\\dict\\gene_dict.txt'
file_1x2 = 'H:\\Data\\data422\\data\\interaction\\PPI.txt'

#调用column中的single_column,分离出某个数据文件的某一列。
#第一个参数是文件，第二个参数是想要第几列，第三个参数是决定是否要去掉首行（标题）
file_1_list = single_column(file_1, 0, removetitle=True)
file_2_list = single_column(file_2, 0, removetitle=True)
file_1x2_list1 = single_column(file_1x2, 0, removetitle=True)
file_1x2_list2 = single_column(file_1x2, 1, removetitle=True)


#对于分离出来的几个列进行检查，就是检查数据有没有问题
#从check中调用precheck,第1,3个参数是字典，第2,4个参数是交互数据的两列
precheck(file_1_list, file_1x2_list1, file_2_list, file_1x2_list2)


# 拼接矩阵并检查
hello = combine(file_1_list, file_1x2_list1, file_2_list, file_1x2_list2)
check(hello)

#输出为txt格式
np.savetxt('C:\\Users\\hw\\Desktop\\protein_protein_mat.txt', hello, fmt="%d")

print("end")