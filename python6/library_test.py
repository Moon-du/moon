# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/19 下午 03:13
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : library_test.py
# @Software : PyCharm

# 标准库

# sys模块：获取python系统的设置和修改python设置
import sys

print(sys.argv)

# os模块：获取操作系统的设置，操作os
import os

print(os.getcwd())

# math模块：提供一些数学函数
import math

print(math.factorial(5))
print(math.fabs(-5))

# time模块：提供系统时间和对时间进行处理
import time

t = time.time()  # 系统当前时间：以秒记的从1970年1月1月0时0点0分0秒开始经过的时间
print(t)
print(time.gmtime(t))  # 将时间转换为标准时区时间以年-月-日：时-分-秒的格式输出
print(time.localtime(t))  # 将时间转换为本地时区时间以年-月-日：时-分-秒的格式输出

#type模块：获取对象的类型
print(type(-1))
print(type(False))
print(type("123"))
print(type(12.12))