# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/13 上午 11:23
# @Author   : Moon-du
#  @Site    : https://www.ysbzc.com/
# @File     : if_test.py
# @Software : PyCharm


# 程序的执行结构：顺序、分支(选择)、循环


# 1.顺序：从上往下，依次执行

# 2.分支：if语句
# 2.1基本if语句
money = 5

if money >= 5:
    print('吃豆浆和包子')
print('去上课')

# 小练习：用户输入年龄，请大于25岁的站到右边去！
# age = int(input('请输入年龄:'))
# if age > 25:
#     print('请站在右边')

# 2.2 if-else结构
# age = int(input('请输入年龄:'))
# if age > 25:
#     print('请站在右边')
# else:
#     print('请站在左边')

# 用户输入一个数，判断这个数是偶数还是奇数？将结果打印出来。
# num = int(input('请输入一个数：'))
# if num % 2 == 0:
#     print(f'{num}是偶数')
# else:
#     print(f'{num}是奇数')

# 2.3 if-elif-else结构
score = 61
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('合格')
else:
    print('不合格')

# if语句嵌套
hasMelon = False
print('程序员出门买西瓜')
if hasMelon:
    isMelonFresh = False
    if isMelonFresh:
        print('买两个番茄和一个西瓜')
    else:
        print('买两个番茄和一个哈密瓜')
else:
    print('买两个番茄')

x = 0
if x:
    print('x is not zero')
