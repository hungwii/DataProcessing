from extract import single_column
filepath = 'C:\\Users\\hw\\Desktop\\drug_wrong.txt'

f = single_column(filepath, 0, removetitle=False)
f.sort()
with open('hahahaha.txt', 'w', encoding='utf-8') as l:
    for i in f:
        l.write(i)
        l.write('\n')
