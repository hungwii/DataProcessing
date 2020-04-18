from extract import single_column
'''这是从数据中挑出是新冠蛋白的，需要修改的参数就是下面三行文件路径代码'''
#下面第一行是新冠蛋白词典路径、第二行是数组路径、第三行是输出的文件名（文件会保存在代码所在文件夹）
filepath_covid19_dic = 'C:\\Users\\hw\\Desktop\\VirusProject\\hw\\data\\Covs-protein_dict127.txt'
filepath_list = 'C:\\Users\\hw\\Desktop\\test\\test_list.txt'
file_output = 'C:\\Users\\hw\\Desktop\\test\\list_only_covid19.txt'





#载入数据
covid19_dic = single_column(filepath_covid19_dic, 0, removetitle=True)
proteins = single_column(filepath_list, 1, removetitle=False)

print(len(covid19_dic))
print(len(proteins))
#记录是新冠蛋白的行数
locs = []
for key, value in enumerate(proteins):
    if value in covid19_dic:
        locs.append(key)
# 保留新冠对应行，并把数据写入新文件
contents = []
with open(filepath_list, 'r', encoding='utf-8') as f:
    l_temp = f.readlines()
    for r in locs:
        temp = l_temp[r].strip('\n').split()
        contents.append(temp)
#这里是统计最后结果中有多少个1
cc_num = 0
for cc in contents:
    if cc[3] == '1':
        cc_num += 1
print('最后的结果中1的个数为：', cc_num)

#把数据写入文件
with open(file_output, 'w', encoding='utf-8') as output:
    for content in contents:
        rowtext = '{} {} {} {}'.format(content[0], content[1], content[2], content[3])
        output.write(rowtext)
        output.write('\n')

print('end')





