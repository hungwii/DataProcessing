import numpy as np
from extract import single_column
from tomatrix import tomatrix
from check import check
'''这个主要是调用写好的函数（主要是tomatrix）,把一个矩阵，根据字典，去除无用的行和列'''


#文件路径,file_1表示字典，file_2表示需要修改的矩阵
file_1 = 'C:\\Users\\hw\\Desktop\\Data20200324\\Data\\dict\\drug2953_dict.txt'
file_2 = 'C:\\Users\\hw\\Desktop\\Data20200324\\Data\\drug similarity\\Therapeutic_Similarity.txt'

#提取出词典
file_1_title = single_column(file_1, 0, removetitle=True)

##把剩下的数据转换成矩阵的形式,第一个参数为词典，第二个参数为根据词典修改的矩阵，第三个为是否去掉矩阵的第一行，第四个为是否去掉矩阵第一列
pure_mat = tomatrix(file_1_title, file_2, removetitle=True, removefirstcol=True)

#检查输出的矩阵的格式
check(pure_mat)

#如果矩阵不是0/1矩阵，把所有元素进行转化，然后求和，就可以清楚看出有几个非零元素
repeat_mat = pure_mat.copy()
repeat_mat[(repeat_mat < 0)] = 0
repeat_mat[repeat_mat > 0] = 1
num = np.sum(repeat_mat)
print("非0个数", num)

#输出结果到txt文件
np.savetxt('C:\\Users\\hw\\Desktop\\Data20200324\\Data\\drugnewsim\\Therapeutic_Similarity.txt', pure_mat, fmt="%f")

print('end')

