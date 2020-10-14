# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 上午 11:15
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : data_struct.py
# @Software : PyCharm

# 数据结构
# 多个变量的集合，理解为以一排杯子或者一排柜子
# 列表list，元祖tuple，字典dictionary
a1 = 1
a2 = 2
# ...
a100 = 100

# 1.列表list
# 1.1列表的定义
list1 = [1, 1.1, 'abc', True]
# 下标/索引：从0开始，最后一个元素的下标是长度-1
print(list1[0])
print(list1[3])

# 操作列表的函数
# max(list)：返回列表的最大值，只能对数值类型的列表使用
list2 = [1, -99, 100, 5]
print(max(list2))

# min(list)：返回列表的最小值，只能对数值类型的列表使用
print(min(list2))

# len(list):返回列表的元素个数/长度
print(len(list2))

# 1.2列表的主要操作：增，删，改，查
# 1.2.1 新增元素
# list.append(元素):默认从末尾增加一个元素到列表
list2.append(100)
print(list2)

# list.insert(index,元素)：在指定index位置插入元素，index之后的元素下标依次+1

# 1.2.2 删除元素
# list.pop([index]):index删除指定索引位置的元素，如果不写，默认删除最后一个元素
list2.pop()
print(list2)
list2.pop(0)
print(list2)

# del list[index]：删除list中指定index的元素
del list2[1]
print(list2)

# 1.2.3 修改元素
# 对指定index位置重新赋值
list2[0] = 99
print(list2)

# 1.2.4 查询列表
list3 = [6, 5, 4, 3, 2, 1]
# 遍历查询
for i in list3:
    i = i + 1
    print(i)
print(list3)

for i in range(len(list3)):  # 通过index遍历，可以修改原有列表
    list3[i] += 1
    print(list3[i])
print(list3)

# 深复制和浅复制
list4 = list3  # 浅复制
list4[0] = 8
print(list4)
print(list3)
list4 = [5, 4, 3, 2, 1]
print(list4)
print(list3)

# 深复制
list4 = []
for i in list3:
    list4.append(i)
print(list4)
print(list3)
list4[0] = 8
print(list4)
print(list3)
