# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/15 下午 05:00
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : prac.py
# @Software : PyCharm

# 1.# 求 1-100以内所有含6的数
def foo1():
    list1 = []
    for i in range(1, 101):
        i = str(i)
        if i.count('6') >= 1:
            list1.append(i)
    return list1


# 2、Chuckie Lucky赢了100W美元，
# 他把它存入一个每年盈利8%的账户。
# 在每年的最后一天，Chuckie取出10W美元。
# 编写一个程序，计算需要多少年Chuckie就会清空他的账户。
def foo2():
    money = 100
    year = 0
    while money >= 0:
        money = money * 1.08
        money = money - 10
        year += 1
        # print(money)
    return year


# 3、题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 程序分析：采取逆向思维的方法，从后往前推断。
def foo3():
    # y=x/2-1
    # y+1=x/2
    # 2*(y+1)=x
    # peach = 1
    # for i in range(9):
    #     peach = 2*(peach+1)
    # return peach

    peach = [1]
    for i in range(9):
        peach_second = 2 * (peach[i] + 1)
        peach.append(peach_second)
    peach.reverse()
    return peach


# 4、不使用自带函数，写一个函数，用于返回一个数的绝对值
def foo4(a):
    # return (a**2)**0.5
    if a >= 0:
        return a
    else:
        return a * -1


# 5、写一个函数，用来求三个数的最大值
def foo5(a, b, c):
    # if a > b:
    #     if a > c:
    #         return a
    #     else:
    #         return c
    # else:
    #     if b > c:
    #         return b
    #     else:
    #         return c
    list1 = [a, b, c]
    return max(list1)


# 提升：
# 6、写一个函数，返回输入整数（大于999小于10000）的每位数的数字之和。
def foo6(num):
    a = num // 1000
    b = (num - a * 1000) // 100
    c = (num - a * 1000 - b * 100) // 10
    d = num % 10
    return a + b + c + d


def foo7(num):
    num = str(num)  # '9876'
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum


def foo8(num):
    sum = 0
    num = foo4(num)
    while num > 10:
        n = num % 10
        sum += n
        num = num // 10
    sum += num
    return sum

if __name__ == '__main__':  # 判断模块名是否是本模块
    print(foo1())
    print(foo2())
    print(foo3())
    print(foo4(-7))
    print(foo5(1, 2, 3))
    print(foo5(1, 3, 2))
    print(foo5(3, 2, 1))
    print(foo6(9876))
    print(foo7(9876))
    print(foo7(876))
    print(foo7(76))
    print(foo8(-9876))
    print(foo8(876))
    print(foo8(76))
