# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 下午 03:00
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : prac.py
# @Software : PyCharm

import random

# 1. 练习：将列表[45,23,2,5,3,2,6,45,43,21,66,2,3,2]进行从小到大排序，不能用sort()函数，


# 2、求 100-200以内同时能被7、8整除的数
for i in range(100, 201):
    if i % 7 == 0 and i % 8 == 0:
        print(i, end=' ')

# 3.找出一个列表中，只出现了一次的数字，并且保持原来的次序，例如[1,2,1,3,2,5]结果为[3,5]
print('\n----------------------------------------------')
list1 = [1, 2, 1, 3, 2, 5]
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)

# 提升
# 4、求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100
print('----------------------------------------------')
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
    else:
        sum -= i
print(sum)

# 5.求100以内的素数：>1整数，只能被1和自己整除
print('----------------------------------------------')
prime = []
for i in range(2, 101):
    num = 0  # 整除次数
    for j in range(1, i + 1):  # 计算被整除次数，从1到数自己
        if i % j == 0:
            num += 1
    if num == 2:
        prime.append(i)
print(prime)

# 6. 水仙花数：水仙花数是指一个 n 位数 ( n 大于等于 3 )，它的每个位上的数字的 n 次幂之和等于它本身。
# # （例如：1的3次方 + 5的三次方 + 3三次方 = 153）。根据这个要求，打印所有三位数的水仙花数。
print('----------------------------------------------')
list3 = []
for i in range(100, 1000):
    # 拆出数的每一位
    a = i // 100
    b = (i - a * 100) // 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        list3.append(i)
print(list3)

list3 = []
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if a * 100 + b * 10 + c == a ** 3 + b ** 3 + c ** 3:
                list3.append(a * 100 + b * 10 + c)
print(list3)

# 7.一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# # 再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？
print('----------------------------------------------')
height = 100
sum = height
for i in range(9):
    height = height / 2
    sum += 2 * height
    print(sum, height)

print(f'第10次落地，经过{sum}米，第10次的反弹高度是{height / 2}')

# 8. 随机产生20个100-200之间的正整数存放到列表中，
# 并求列表中的所有元素最大值、最小值、平均值，然后将各元素的与平均值的差组成一个列表
print('----------------------------------------------')
# 产生随机数列表
list4 = []
for i in range(20):
    num = random.randint(100,200)
    list4.append(num)
print(list4)

# 计算最大、最小、平均值
max1 = max(list4)
min1 = min(list4)
sum = 0
for i in list4:
    sum +=i
avg = sum/len(list4)
print(f'最大值:{max1},最小值:{min1},平均值:{avg}')

# 计算差值列表
for i in range(len(list4)):
    list4[i] = list4[i] - avg
print(list4)
