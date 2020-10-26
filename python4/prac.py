# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/15 下午 05:00
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : prac.py
# @Software : PyCharm

# 1.# 求 1-100以内所有含6的数
# def fool1():
#     for i in range(1, 101):
#         if i % 10 == 6 or i // 10 == 6:
#             print(i)
#
#
# fool1()
# 2、Chuckie Lucky赢了100W美元，
# 他把它存入一个每年盈利8%的账户。
# 在每年的最后一天，Chuckie取出10W美元。
# 编写一个程序，计算需要多少年Chuckie就会清空他的账户。
# def fool2():
#     zh = 1000000
#     for i in range(1, 99):
#         zh = zh * (1 + 0.08) - 100000
#         if zh < 0:
#             break
#     print(i)
# 
#
# fool2()

# 3、题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 程序分析：采取逆向思维的方法，从后往前推断。
# def fool3():
#     t = 1
#     for i in range(9):
#         t = (t + 1) * 2
#     print(t)
#
#
# fool3()

# 4、不使用自带函数，写一个函数，用于返回一个数的绝对值
# def fool4(a):
#     if a > 0:
#         print(a)
#     else:
#         print(a * -1)
#
#
# fool4(99)

# 5、写一个函数，用来求三个数的最大值
# def fool5(a, b, c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     elif c > a and c > b:
#         print(c)
#
#
# fool5(1, 2, 3)
# 提升：
# 6、写一个函数，返回输入整数（大于999小于10000）的每位数的数字之和。
# def fool6(num):
#     g = (num % 10)
#     s = (num // 10 % 10)
#     b = (num // 100 % 10)
#     q = (num // 1000 % 10)
#     print(g + s + b + q)
#
#
# fool6(9998)
