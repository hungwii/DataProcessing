def match(list1, list2, list3):
    '''输入是三个列表，第一个是词典，第二个是和词典同一属性的，第三个是匹配的，主要是根据词典对数据进行去渣及排序'''

    ans = []
    useless = []
    for k, v in enumerate(list1):
        if v in list2:
            i = list2.index(v)
            temp = v + ' ' + list3[i]
            ans.append(temp)
        else:
            useless.append(k) #记录没有用的下标.

    print(len(useless))
    return ans