from extract import single_column
"这个可以根据文件中的某一列数字，选择出TOP,相比于版本1，这里利用了数字出现的顺序，跑起来会更快。但是要注意几个参数"
top = 20  # 这里是设置想要前几
col = 2  # 这里是选择第几列数字来排序（由0开始计数）
genenum = 116  # 词典和文件匹配的蛋白质数目，用于写文件
drugnum = 2953  # 药物的数量，也就是一个蛋白出现了多少次，用于循环
# 文件路径,注意，这里的数据不是在data文件夹，而是在result文件夹。因为该文件是之前的函数运行的结果
filepath = 'C:\\Users\\hw\\Desktop\\test\\list_only_cov.txt'
filepath_dic = 'H:\\Data\\dict\\Covs-protein_dict127.txt'  # 新冠蛋白质词典
output_path = 'C:\\Users\\hw\\Desktop\\test\\list_top20.txt'  # 设置输出结果路径

# 下面两行注意列的参数的修改
covid19_protein_dic = single_column(filepath_dic, 1, removetitle=True)
only_procol = single_column(filepath, 1, removetitle=False)

# 首先把每一行转换成列表，并且提前把要比较数字的那一列由字符串转换为数字
contents = []
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        content = line.strip('\n').split()
        a = float(content[col])
        content[col] = a
        contents.append(content)
print("------------数据转换为列表阶段结束---------------")
results = []
count = 0
for i in range(genenum):
    temps = []
    # 每个蛋白（temp）都有2953个
    while len(temps) < drugnum:
        temps.append(contents[i])
        i += genenum
    # 排序
    temps.sort(key=lambda x: x[col], reverse=True)
    # 保存top的结果
    results.extend(temps[:top])
    count += 1
    print("the:", count)


with open(output_path, 'w', encoding='utf-8') as output:
    for result in results:
        rowtext = '{} {} {} {}'.format(
            result[0], result[1], result[2], result[3])
        output.write(rowtext)
        output.write('\n')

print("end")
