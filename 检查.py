from extract import single_column

filepath_list = 'C:\\Users\\hw\\Desktop\\test\\list_only_314gene.txt'
filepath_pos =  'H:\\Data\\eps_new0417\\Treatment_38drugs.txt'
a = single_column(filepath_list, 0)
b = single_column(filepath_pos, 0, removetitle=True)

print(len(set(a)))
print(len(set(b)))
print(len(set(a) & set(b)))