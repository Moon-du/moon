# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 上午 10:53
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : __init__.py.py
# @Software : PyCharm

# def add(a, b):
#     c = a + b
#     return c
#
#
# print(add(1, 99))


# def add(a, b):
#     c = a + b
#
#
#
# add(1, 2)
# 饮料机一：
# 只吐出可口可乐
# def drink(a):
#     a = input('内容')
#     print(a)
#
#
# drink(1)

# 饮料机二：
# 选择可乐各类
# 可以吐出可口可乐、芬达、百事可乐
# 小练习：编写一个函数，必须参数a,b,c，函数计算a的平方、b的立方、c三者的和，并返回。

# def lf(a, b, c):
#     print(a * a + b ** 3 + c)
#
#
# lf(1, 2, 3)
def lf(a, b, c):
    n = a * a + b ** 3 + c
    return n


print(lf(1, 2, 3))
