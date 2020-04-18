from extract import single_column
"这个可以根据文件中的某一列数字，选择出TOP"
top = 100    #这里是设置想要前几
col = 2     #这里是选择第几列数字（由0开始计数）
filepath = 'C:\\Users\\hw\\Desktop\\list_only_covid19.txt'    #文件路径,注意，这里的数据不是在data文件夹，而是在result文件夹。因为该文件是之前的函数运行的结果
filepath_dic = 'C:\\Users\\hw\\Desktop\\VirusProject\\hw\\data\\Covs-protein_dict127.txt' #新冠蛋白质词典
output_path = 'C:\\Users\\hw\\Desktop\\top100_list.txt'  #设置输出结果路径

covid19_protein_dic = single_column(filepath_dic, 0, removetitle=True)
only_procol = single_column(filepath, 1, removetitle=False)

#首先把每一行转换成列表，并且提前把要比较数字的那一列由字符串转换为数字
contents = []
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        content = line.strip('\n').split()
        a = float(content[col])
        content[col] = a
        contents.append(content)

results = []
for protein in covid19_protein_dic:
    temps = []
    while protein in only_procol:
        loc = only_procol.index(protein)
        temps.append(contents[loc])
        only_procol[loc] = 'X'

    #排序
    temps.sort(key=lambda x: x[col], reverse=True)
    #保存top的结果
    results.extend(temps[:top])

with open(output_path, 'w', encoding='utf-8') as output:
    for result in results:
        rowtext = '{} {} {} {}'.format(result[0], result[1], result[2], result[3])
        output.write(rowtext)
        output.write('\n')

print("end")








