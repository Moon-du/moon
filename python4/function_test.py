# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/15 下午 03:29
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : function_test.py
# @Software : PyCharm

# 函数
# 执行特定功能的代码块

# 1.函数的定义
def add(a, b):  # def 函数名(形参列表)：
    c = a + b  # 函数体
    return c  # 返回语句,结束函数的调用
    print('return 之后')  # return语句之后的语句不会被执行，是多余的


# 2.函数的调用:通过函数名调用
print(add(1, 99))  # 1,99：实参


# 饮料机一：
# 只吐出可口可乐
def drink_machine1():
    print('可口可乐')


drink_machine1()


# 饮料机二：
# 选择可乐各类
# 可以吐出可口可乐、芬达、百事可乐
def drink_machine2(drink):
    if drink == '可口可乐':
        print('可口可乐')
    elif drink == '芬达':
        print('芬达')
    else:
        print('百事可乐')


drink_machine2('水')
drink_machine2('可口可乐')


# 3函数的参数传递的方式
# 3.1.按位置传递，关键字参数
def foo1(a, b):
    print(f'a={a}')
    print(f'b={b}')


foo1(1, 2)


# 3.2同名传递，根据参数名字传递参数值
def foo2(a, b):
    print(f'a={a}')
    print(f'b={b}')


foo2(b=1, a=2)  # 实参列表中，使用赋值语句，按照参数名字来传递


# 3.3 默认值参数
def foo3(a, b=10):
    print(f'a={a}')
    print(f'b={b}')


foo3(1, 2)  # 如果传入参数，优先使用传入的值
foo3(1)  # 如果不传，使用默认值

# 4.局部和全局变量
# 4.1：理解变量的作用域
# 4.2：global的用法
print('----------------------------------------')
num = 100  # 在定义之后整个py文件都有作用，称为全局变量


def foo4():
    global num  # 将变量定义为全局
    num = 1  # 函数内定义的变量称为局部变量，只在函数内有作用
    print(f'函数内的局部变量num:{num}')


foo4()
print(f'函数外的全局变量num:{num}')

# 5.函数的返回
# return语句实现函数的返回，结束函数的调用
# 函数必有return语句，如果不写，程序自动添加return None到末尾
print('------------------------------------')


def foo5(a, b):
    c = a + b


print(foo5(1, 2))

# 小练习：编写一个函数，必须参数a,b,c，函数计算a的平方、b的立方、c三者的和，并返回。
print('------------------------------------')


def foo6(a, b, c):
    return a ** 2 + b ** 3 + c


a = foo6(1, 2, 3)
print(a)
