# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

# 模块module
# 模块是什么？模块指的就是.py文件

# 模块要经过导入之后，才可以使用模块里面函数、变量

# 模块导入的格式：
# 1.import导入
import random


def foo1():
    print(random.randint(1, 10))  # 调用格式：模块名.函数名（）


# 2. from-import
from random import randint  # from 模块 import 函数名


def foo2():
    print(randint(1, 10))  # 直接通过函数名调用


# 自定义模块的导入
import python5.db_test  # 从项目下的第一层.第二层.文件
def foo3():
    rs = python5.db_test.db('select * from students;')
    print(rs)

from python5.db_test import db
def foo4():
    rs = db('select * from students;')
    print(rs)

if __name__ == "__main__":
    foo1()
    foo2()
    foo3()
    foo4()