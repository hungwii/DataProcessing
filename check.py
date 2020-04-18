import numpy as np
from extract import single_column

def check(a1):
    '''这个函数是为了检查我们最后输出的数组是不是正确的，直接调用就好，函数输入就是数组'''

    print(a1) #输出这个数组
    print('数组所有元素求和: ', np.sum(a1)) #求和，如果数组全是0/1，可以看有多少个1
    print("数据类型", type(a1))  # 打印数组数据类型
    print("数组元素数据类型：", a1.dtype)  # 打印数组元素数据类型
    print("数组形状：", a1.shape)  # 打印数组形状
    print("数组元素总数：", a1.size)  # 打印数组尺寸，即数组元素总数
    print("数组的维度数目", a1.ndim)  # 打印数组的维度数目

def precheck(b1, b2, b3, b4):
    '''主要是为了检查4个列表之间的匹配情况'''
    if len(set(b3)) < len(set(b4)):
        print("字典1过小")
    elif len(set(b3)) > len(set(b4)):
        print("字典1囊括了所有药物，OK的")
    else:
        print("字典1大小刚刚好，OK的")

    if len(set(b3)) < len(set(b4)):
        print("字典2过小")
    elif len(set(b3)) > len(set(b4)):
        print("字典2囊括了所有药物，OK的")
    else:
        print("字典2大小刚刚好，OK的")

    print('从左到右长度分别是：', len(b1), len(b2), len(b3), len(b4))
    print('第1个列表去重后的大小', len(set(b1)))
    print('第2个列表去重后的大小', len(set(b2)))
    print('第3个列表去重后的大小', len(set(b3)))
    print('第4个列表去重后的大小', len(set(b4)))

    print("第一个的集合并第二个的集合", len(set(b1) | set(b2)))
    print("第一个的集合且第二个的集合", len(set(b1) & set(b2)))
    print("第三个的集合并第四个的集合", len(set(b3) | set(b4)))
    print("第三个的集合且第四个的集合", len(set(b4) & set(b4)))

def r_c(filepath):
    '''我们拿到一个矩阵，需要检查行列的标题是否是对应的就可以用这个函数，输入就是文件路径进就行了'''

    col = single_column(filepath, 0, removetitle=True)
    print('第一列长度：', len(col))

    # 检查行列是否相等
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_tempt = lines[0]
        line_1 = line_tempt.split()[1:]
    print('第一行长度： ', len(line_1))
    print("并集的个数", len(set(col) | set(line_1)))
    print('交集的个数', len(set(col) & set(line_1)))
    # 匹配两列看下情况
    yes = 0
    for v, k in enumerate(col):
        if k == line_1[v]:
            yes += 1
        else:
            print('行和列从第：' + str(v + 1) + '个数开始不匹配')
            print('连续匹配的个数', yes)
            break
