from extract import single_column


'''根据正样本词典分离正负样本，并计算最大值和平均值'''
filepath_list = 'C:\\Users\\hw\\Desktop\\test\\list_only_cov.txt'
filepath_pos = 'H:\\Data\\eps_new0417\\Treatment_38drugs.txt'
list_0 = single_column(filepath_list, 0, removetitle=False)
list_2 = single_column(filepath_list, 2, removetitle=False)
list_pos = single_column(filepath_pos, 0, removetitle=True)

left, right = 0, 115
step = 116
long = 342547

# 计算平均值的函数


def cal_aver(list):
    total = 0
    for numbers in list:
        total += float(numbers)jia shi
    return total / len(list)


# 获取药物列表
result_name = []
result_max = []
result_ave = []
while right <= long:
    temp = []
    for i in range(left, right + 1):
        temp.append(list_2[i])
    result_max.append(max(map(float, temp)))  # 记下最大值
    result_ave.append(cal_aver(temp))  # 记下平均值
    result_name.append(list_0[left])  # 记下名字
    left += step
    right += step


# for i in range(2953):
#     temp = []
#     while len(temp) < 312:
#         temp.append(list_2[i])
#         i += 312
#     result_max.append(max(map(float, temp)))  # 记下最大值
#     result_ave.append(cal_aver(temp))  # 记下平均值
#     result_name.append(list_0[i])  # 记下名字


# 分离正负样本
pos_name = []
neg_name = []
pos_score_max = []
pos_score_ave = []
neg_score_max = []
neg_score_ave = []
for key, value in enumerate(result_name):
    if value in list_pos:
        pos_name.append(value)
        pos_score_ave.append(result_ave[key])
        pos_score_max.append(result_max[key])
    else:
        neg_name.append(value)
        neg_score_ave.append(result_ave[key])
        neg_score_max.append(result_max[key])


with open('C:\\Users\\hw\\Desktop\\test\\pn\\positive_data.txt', 'w', encoding='utf-8') as f:
    for n, nm, na in zip(pos_name, pos_score_max, pos_score_ave):
        rowtext_pos = '{} {} {}'.format(n, nm, na)
        f.write(rowtext_pos)
        f.write('\n')

with open('C:\\Users\\hw\\Desktop\\test\\pn\\negative_data.txt', 'w', encoding='utf-8') as l:
    for nn, nnm, nna in zip(neg_name, neg_score_max, neg_score_ave):
        rowtext_neg = '{} {} {}'.format(nn, nnm, nna)
        l.write(rowtext_neg)
        l.write('\n')

print('end')
