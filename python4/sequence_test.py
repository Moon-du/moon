# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/15 上午 10:57
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : sequence_test.py
# @Software : PyCharm

# 序列sequence
# 有序的队列
# 列表、元祖、字符串都是序列
# 字典不是序列
str1 = 'abcd'
for i in str1:
    print(i)

# 字符串可以看成是单个字符元素组成的元祖，不能修改元素的值，不能增加和删除元素
for index in range(len(str1)):
    print(str1[index])
# str1[0] = 'e'

# 索引的操作
# 索引/下标一般是整数，或者算术表达式，整数变量
# 索引可以是正数也可以是负数,代表倒数第几个元素
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
str1 = '汇智动力'
print(list1[-1])
print(tuple1[-1])
print(str1[-1])

# 序列的切片：sequence[start:end]
# 切片操作包左不包右

print(list1[1:2])
print(tuple1[:2])
print(str1[1:])

# 切片的练习
# 11:12:11> 001 enter chatroom, level2
str2 = '11:12:11> 001 enter chatroom, level2'
id = str2[10:10 + 3]
print(id)

# 列表生成式
before_tax = [10000, 8000, 5000, 400]
after_tax = [one * 0.9 for one in before_tax]
print(after_tax)

list3 = [1, 2, 3, 2, 1]
list3.remove(1)
print(list3)

# 字符串的分割和拼接
str1 = 'My name is Trump'
# 分割：根据特定字符串将字符串分割为字符串的列表
# 默认根据空格分割
list1 = str1.split()
print(list1)
str2 = 'My,nammme,is,Trump'
list2 = str2.split(',')
print(list2)
list3 = str2.split('m')
print(list3)

# 拼接:将字符串的列表拼接为字符串
# 格式:'拼接字符串'.join(列表)
str4 = ' '.join(list1)
print(str4)

# 字符串的方法
str1 = 'My name is Trump'
print(str1.count(' '))
print(str1.find('is'))
print(str1.replace(' ',';'))

# 去除字符串左右两边的特殊字符
str1 = '....My name ... is Trump........'
# lstrip():去除字符串左边的特殊字符
str2 = str1.lstrip('.')
print(str2)

# rstrip()：去除字符串右边的特殊字符
str3 = str1.rstrip('.')
print(str3)

# strip():同时去除左右两边的特殊字符
str4 = str1.strip('.')
print(str4)
