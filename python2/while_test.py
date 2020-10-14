# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/13 下午 02:32
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : while_test.py
# @Software : PyCharm

import random

# 3.循环结构:反复执行相同的代码
# while循环、for循环
# 1-100:1+2+3+4+5+...+100累加
a = 1
sum = 0

sum = sum + a
a += 1

sum = sum + a
a += 1

sum = sum + a
a += 1

# 3.1 while语句
# 1-100的累加

a = 1  # 初始化语句
sum = 0
while a <= 100:  # 循环条件
    sum = sum + a  # 循环体
    a = a + 1  # 迭代语句
print(sum)

# 2.猜数字：系统给出一个1-10之间的整数，用户输入猜测的数字，系统给出相应的提示
# num = random.randint(1, 10)
# n = int(input('请输入一个数字(1-10):'))
# if n > num:
#     print('大了')
# elif n < num:
#     print('小了')
# elif n == num:
#     print('对了')
# else:
#     pass

# 3.猜数字游戏，增加游戏次数限制，最多只能猜5次。如果5次都没猜正确，给出提示，游戏结束
time = 1
num = random.randint(1, 10)
isRight = False
while time <= 5:

    n = int(input('请输入一个数字(1-10):'))
    if n > num:
        print('大了')
    elif n < num:
        print('小了')
    elif n == num:
        print('对了')
        isRight = True
        time = 5
    else:
        pass
    time += 1
if isRight == False:
    print('5次都不对，太笨了')
