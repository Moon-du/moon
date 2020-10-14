# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 下午 02:31
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : sort_test.py
# @Software : PyCharm

# 排序算法
# 练习：将列表[45,23,2,5,3,2,6,45,43,21,66,2,3,2]进行从小到大排序，不能用sort()函数，

# 1.冒泡排序：通过对相邻的两个数比较大小，较大(较小)数和后一个数交换位置，实现列表的整体有序
list1 = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]
# 升序
for i in range(len(list1) - 1):  # 外层循环决定找多少次最大值
    for j in range(len(list1) - i - 1):  # 内层循环决定每次比较哪些数
        # 比较相邻两个数，如果前一个数较大和后一个数交换位置
        # print(j)
        if list1[j] > list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp
print(list1)

# 降序
for i in range(len(list1) - 1):  # 外层循环决定找多少次最小值
    for j in range(len(list1) - i - 1):  # 内层循环决定每次比较哪些数
        # 比较相邻两个数，如果前一个数较小和后一个数交换位置
        # print(j)
        if list1[j] < list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1)

# python独有交换值的形式
a = 1
b = 2
a, b = b, a
print(a, b)

# 2.用列表的sort()方法排序
list1.sort()
print(list1)

list1.reverse()  # 翻转列表
print(list1)

# 3.用max()/min()函数，依次找出最大/最小值，将它从原来列表删掉，添加到一个新空列表当中
list2 = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]
list3 = []
for i in range(len(list2)):
    temp = min(list2)
    list3.append(temp)
    index = list2.index(temp)
    list2.pop(index)
print(list3)
