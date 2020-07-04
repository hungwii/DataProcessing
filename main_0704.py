from extract import single_column
import random

#参数的

file_path_rel = '/Users/huangwei/Downloads/drug_disease_association.txt'

drug_name_col = single_column(file_path_rel, col_num=0, removetitle=False)
target_name_col = single_column(file_path_rel, col_num=1, removetitle=False)

temp_drug_col = [] #这是没有去重的
for drug_name in drug_name_col:
    drug_num = drug_name.split(':')[0]
    temp_drug_col.append(drug_num)

drug_col = set(temp_drug_col) #这是进行了去重操作的

print('没有去重，药物总共有：' + str(len(temp_drug_col)))
print('去重后， 药物总共有：' + str(len(drug_col)))
print('----------------------------------------------')

temp_target_col = [] #这是没有去重的
for target_name in target_name_col:
    target_num = target_name.split(':')[0]
    temp_target_col.append(target_num)

target_col = set(temp_target_col) #这是进行了去重操作的

print('没有去重，靶点总共有：' + str(len(temp_target_col)))
print('去重后， 靶点总共有：' + str(len(target_col)))
print('----------------------------------------------')

relations = []
with open(file_path_rel, 'r', encoding='utf-8') as f:
    rels = f.readlines()
    for rel in rels:
        relation = rel.strip('\n').split()
        relation[0] = relation[0].split(':')[0]
        relation[1] = relation[1].split(':')[0]
        relation = [relation[0], relation[1]]
        relations.append(relation)
#这个时候relations的数据格式是：[[D,C], [D, C]]

train_rel_num = 5343
val_rel_num = 667
test_rel_num = 667


#创建一个训练集的字典，保证字典里面的每一个key都不为空
random.shuffle(relations)
train = relations[:train_rel_num]
valid = relations[train_rel_num:(train_rel_num+test_rel_num)]
test = relations[(train_rel_num+test_rel_num):]
print('检查分割的数量是否正确：')
print(len(train))
print(len(valid))
print(len(test))
print('------------------------')


all_drug_in_train = []
all_target_in_train = []

for _ in trian:
    all_drug_in_train.append[_[0]]
    all_target_in_train.append[_[1]]



