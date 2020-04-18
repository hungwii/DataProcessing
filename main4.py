from extract import single_column
#这是排序

filepath = 'H:\\PyCharm_Projects\\DataProcessing\\test_list.txt'
nums = []
count_1 = 0
count_05 = 0
list = single_column(filepath, 2, removetitle=False)
for i in list:
    temp = float(i)
    nums.append(temp)
nums.sort(reverse=True)
for num in nums:
    if num >= 1:
        count_1 += 1
    if num >= 0.5 and num < 1:
        count_05 += 1
print(count_05)
print(count_1)
print(nums[0:20])