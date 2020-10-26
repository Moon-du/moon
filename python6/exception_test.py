# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

# 异常
# 什么是异常？比代码错误更第一级的错误情况，在不运行代码时难以发现的代码错误
# 异常会中断程序的执行
def foo1():
    for i in range(-5, 6):
        print(50 / i)
        print('除法之后的语句')


# 异常的处理方式：try -except：
# try-except
def foo2():
    for i in range(-5, 6):
        try:  # 可能出异常的代码块
            print(50 / i)
        except Exception as e:  # 出现异常之后执行的语句
            print('除零异常', e)
        print('除法之后的语句')


# try-except-else
# except和else同时只会执行一个，取决于try的代码是否有异常
def foo3():
    for i in range(-5, 6):
        try:  # 可能出异常的代码块
            print(50 / i)
        except Exception as e:  # 出现异常之后执行的语句
            print('除零异常', e)
        else:  # 没有出现异常执行的语句
            print('没有异常')
        print('除法之后的语句')
        print('--------------')


# try-except-else-finally
def foo4():
    for i in range(-5, 6):
        try:  # 可能出异常的代码块
            print(50 / i)
        except Exception as e:  # 出现异常之后执行的语句
            print('除零异常', e)
        else:  # 没有出现异常执行的语句
            print('没有异常')
        finally:  # 一定会执行的语句
            print('不管有没有异常都要执行')
        print('除法之后的语句')
        print('--------------')


if __name__ == "__main__":
    # foo1()
    # foo2()
    # foo3()
    foo4()