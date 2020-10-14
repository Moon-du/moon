# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/12 下午 02:31
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : prac.py
# @Software : PyCharm

# 1.练习数据的抓换，一次把所有的数据转换为其它数据类型并打印输出
import random

num = random.randint(1, 10)
print(num)

a = 123
print(str(a))
print(int(a))
print(float(a))
print(bool(123))

# 2.使用input函数，输出类似"我是xxx，我今天xx岁"
# name = input('请输入你的名字')
# age = str(input('请输入你的年龄'))
# print(f'你的名字是:{name}你的年龄是:{age}')
# 3.画三种图，解释一下程序的内存分配
# a = 'a'
# b = a
# a = 'b'
# 1.a指向a
# 2.b指向a
# 3.a指向b
# 4.获取多个用户输入的名字、年龄、身高和体重，连成一句话打印出来。要求：用几种不同的字符串格式化方式打印，并且要求对齐。
name = input('请输入你的名字')
age = (input('请输入你的年龄'))
high = float(input('请输入你的身高'))
weight = float(input('请输入你的体重'))

print(f'你的名字是:{name}\t你的年龄是:{age}\t你的身高是:{high}\t你的体重是:{weight} ')
print(f'你的名字是:{name:<5},你的年龄是:{age:<5},你的身高是:{high:<5.1f},你的体重是:{weight:<5.1f} ')
print('你的名字是:%s你的年龄是:%s你的身高是:%5.1f你的体重是:%5.1f' % (name, age, high, weight))
