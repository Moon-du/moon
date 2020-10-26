# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/16 上午 10:57
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : recursion_test.py
# @Software : PyCharm

# 递归函数
# 特殊的函数调用方式，函数自己调用自己
# 作用类似于循环，为了实现代码的反复执行
# 思路是：将一个未知或者庞大的问题，逐渐变小，直到有一个确定的答案
# 变量必须越来越小

# 1-100累加：
# 1-100累加=100+99-1累加
# 99-1累加=99+98-1的累加

def foo1(n):  # 必须有形参
    # 必有分支语句
    if n == 1:  # 停止递归
        return 1
    else:  # 将问题逐渐变小
        return n + foo1(n - 1)


# 最大的递归层次
num = 0

def foo2():
    global num
    num += 1
    print(num)
    return foo2()


if __name__ == '__main__':
    # print(foo1(100))
    # print(foo1(1000))#递归有最大递归次数：995
    foo2()
