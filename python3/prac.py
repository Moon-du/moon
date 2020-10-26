# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 下午 03:00
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : prac.py
# @Software : PyCharm

# 1. 练习：将列表[45,23,2,5,3,2,6,45,43,21,66,2,3,2]进行从小到大排序，不能用sort()函数，
# list1 = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]
# for i in range(len(list1)):
#     for j in range(len(list1) - i - 1):
#         if list1[j] < list1[j + 1]:
#             temp = list1[j]
#             list1[j] = list1[j + 1]
#             list1[j + 1] = temp
# print(list1)

# 2、求 100-200以内同时能被7、8整除的数
# for i in range(100, 201):
#     if i % 7 == 0 and i % 8 == 0:
#         print(i)

# 3.找出一个列表中，只出现了一次的数字，并且保持原来的次序，例如[1,2,1,3,2,5]结果为[3,5]
# list2 = [1, 2, 1, 3, 2, 5]
# for i in list2:
#     if list2.count(i) == 1:
#         print(i)

# 4、求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100

# sum = 0
# for i in range(101):
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
# print(sum)

# 5.求100以内的素数
# n = 100
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')
# for i in range(2, n):
#     num = 0
#     for j in range(2, i):
#         if i % j == 0:
#             num += 1
#     if num < 1:
#         print(i, end=' ')

# 6. 水仙花数：水仙花数是指一个 n 位数 ( n 大于等于 3 )，它的每个位上的数字的 n 次幂之和等于它本身。
# # （例如：1的3次方 + 5的三次方 + 3三次方 = 153）。根据这个要求，打印所有三位数的水仙花数。

# for num in range(100, 1000):
#     g = (num % 10)
#     s = (num // 10 % 10)
#     b = (num // 100 % 10)
#     # print(f'{b}{s}{g}')
#     if g ** 3 + s ** 3 + b ** 3 == num:
#         print(num)

# l6 = list(range(100, 1000))
# for i in l6:
#     x = tuple(str(i))
#     if int(x[0]) ** 3 + int(x[1]) ** 3 + int(x[2]) ** 3 == i:
#         print(i)
# 7.一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# # 再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？
# h = 100
# sum = h
# for i in range(9):
#     h /= 2
#     sum += h * 2
# print(sum, h/2)

# 8. 随机产生20个100-200之间的正整数存放到列表中，
# 并求列表中的所有元素最大值、最小值、平均值，然后将各元素的与平均值的差组成一个列表
# list3 = []
# list4 = []
# sum = 0
# import random
#
# for i in range(20):
#     num = random.randint(100, 200)
#     list3.append(num)
# for i in list3:
#     sum += i
# print(max(list3), min(list3), sum / len(list3))
# for i in range(len(list3)):
#     diff = list3[i] - sum / len(list3)
#     list4.append(diff)
# print(list4)
