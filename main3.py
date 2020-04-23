from extract import single_column
'''这是一个把交互矩阵转换成列表，第一列药物，第二列蛋白，第三列数字'''
# 需要注意两个位置的参数：1、第11行filepath的路径 2、39行输出的路径

results = []
contents = []
count = 0  # 记录最后一共有几个交互信息，方便核对
# 把字典，矩阵数据载入
filepath_drug_dic = 'H:\\Data\\dict\\drug2953_dict.txt'
filepath_protein_dic = 'H:\\Data\\dict\\protein5390_dict.txt'
filepath = 'C:\\Users\\hw\\Desktop\\test\\Zscore.txt'
filepath_interaction = 'C:\\Users\\hw\\Desktop\\test\\interaction.txt'

# 把药物和蛋白质词典提取出第一列
drug_list = single_column(filepath_drug_dic, 0, removetitle=True)
protein_list = single_column(filepath_protein_dic, 0, removetitle=True)

# 检查词典数量是否正确
print("药物词典的长度：", len(drug_list))
print("蛋白词典的长度:", len(protein_list))


# 交互数据
rows = []
with open(filepath_interaction, 'r', encoding='utf-8') as f:
    tempts = f.readlines()
    for tempt in tempts:
        row = tempt.strip('\n').split()
        rows.append(row)


# 把矩阵数据，按照字典转换成列表
with open(filepath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        content = line.strip('\n').split()
        contents.append(content)
    for drug, content in enumerate(contents):
        for target, sim in enumerate(content):
            drug_id = drug_list[drug]
            protein_id = protein_list[target]
            interaction = rows[drug][target]
            temp = [drug_id, protein_id, sim, interaction]
            results.append(temp)
            count += 1

# 把结果转换为列表
with open('C:\\Users\\hw\\Desktop\\test\\test_list.txt', 'w', encoding='utf-8') as output:
    for result in results:
        rowtext = '{} {} {} {}'.format(
            result[0], result[1], result[2], result[3])
        output.write(rowtext)
        output.write('\n')

print("end")

