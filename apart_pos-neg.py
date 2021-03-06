from extract import single_column
'''从某个文档中,根据正样本词典。分隔出正样本和负样本,这个忘记当时留着干嘛了，先保留着'''
filepath_list = 'C:\\Users\\hw\\Desktop\\list_only_covid19.txt'
filepath_pos = 'C:\\Users\\hw\\Desktop\\positive.txt'

line_0 = single_column(filepath_list, 0, removetitle=False)
line_2 = single_column(filepath_list, 2, removetitle=False)
line_pos = single_column(filepath_pos, 0, removetitle=False)


pos_name, neg_name = [], []
pos_score, neg_score = [], []
for loc, drug in enumerate(line_0):
    if drug in line_pos:
        pos_name.append(drug)
        pos_score.append(line_2[loc])
    else:
        neg_name.append(drug)
        neg_score.append(line_2[loc])


with open('C:\\Users\\hw\\Desktop\\数据\\positive_data2.txt', 'w', encoding='utf-8') as f:
    for i, j in zip(pos_name, pos_score):
        rowtext = '{} {}'.format(i, j)
        f.write(rowtext)
        f.write('\n')

with open('C:\\Users\\hw\\Desktop\\数据\\negative_data2.txt', 'w', encoding='utf-8') as ll:
    for k, l in zip(neg_name, neg_score):
        r = '{} {}'.format(k, l)
        ll.write(r)
        ll.write('\n')

print('end')
