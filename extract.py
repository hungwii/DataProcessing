def single_column(filepath, col_num=0, removetitle=False):
    '''这个函数用来提取文件中某一列的数据,注意文件是以utf-8格式打开，以空格分开的，
    其中第一个参数是文件绝对路径，第二个参数(col_num)是提取第几列, 第三个参数（removetitle）确定是否去掉第一行'''


    ans = []
    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.readlines()
        for content in contents:
            a = content.split()[int(col_num)]
            ans.append(a)

    if removetitle == True:
        del ans[0]

    return ans

def single_row(filepath, rownum, removetitle=False):
    '''这个函数是为了提取出某一行，基本设置和single_row是一致的'''
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ans = lines[0].strip('\n').split()
        if removetitle == True:
            del ans[0]
    return ans
