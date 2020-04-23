from extract import single_column
'''这是从数据中挑出大于阈值的'''
filepath_list = 'C:\\Users\\hw\\Desktop\\test\\list_only_cov.txt'
file_output = 'C:\\Users\\hw\\Desktop\\test\\list_only_morethan0.txt'
door_num = 0



#载入数据
nums = single_column(filepath_list, 2, removetitle=False)

#记录大于阈值的位置
locs = []
count = 0
for key, value in enumerate(nums):
    if float(value) > door_num:
        locs.append(key)
        count += 1
print("大于阈值的个数为：", count)

#保留大于阈值的行
contents = []
with open(filepath_list, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for loc in locs:
        content = lines[loc].strip('\n').split()
        contents.append(content)

#把数据写入文件
with open(file_output, 'w', encoding='utf-8') as output:
    for content in contents:
        rowtext = '{} {} {} {}'.format(content[0], content[1], content[2], content[3])
        output.write(rowtext)
        output.write('\n')

print('end')



