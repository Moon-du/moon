# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/13 下午 03:36
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : for_test.py
# @Software : PyCharm

# 3.2 for循环语句
# 3.2.1 range()：产生一个序列
a = list(range(10))  # 一个参数是终点，默认起点从0开始，包左不包右
b = list(range(10, 20))  # 两个参数，一个是起点，一个是终点，包左不包右
c = list(range(1, 101, 2))  # 第三个参数是步长，控制从起点到重点的每次增加值
print(a)
print(b)
print(c)

# 1-100累加
# for是对序列的遍历，依次讲序列的中元素值赋值给临时变量i
# 循环次数由序列的元素个数决定
sum = 0
for i in range(1, 101):
    print(i, end=' ')
    sum += i
print(sum)

# 1-100累乘：100！阶乘
# 5!=5x4x3x2x1
sum = 1
for i in range(1, 101):
    sum = sum * i
print(sum)

# 打印出以下图形
# *
# *
# *
# *
# *
print('----------------------------------------')
for i in range(5):
    print('*')

print('----------------------------------------')
# * * * * *
for i in range(5):
    print('*', end=' ')

print()
print('----------------------------------------')
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()

# 循环嵌套结构：
# 外层循环先执行，再执行内层循环
# 外层循环变化为1，内层循环遍历一遍

print('----------------------------------------')
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(5):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# 打印出以下9x9乘法表
# 1x1=1
# 1x2=2 2x2=4
# 1x3=3 2x3=6 3x3=9
# ....
# 1x9=9 ... 9x9=81

print('----------------------------------------')
for i in range(1, 10):
    for j in range(1, i + 1):
        sum = i * j
        print(f'{j}x{i}={sum:2d}', end=' ')
    print()