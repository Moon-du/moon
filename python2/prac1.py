# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/13 上午 10:36
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : prac.py
# @Software : PyCharm

# 1.算出下图的and ，or ，not的结果

# A	    B 	    A and B	A or B	not A
# true	false	false	true	false
# false	true	false	true	true
# false	false	false	false	true
# true	true	true	true	false
print(True and False)
print(False and True)
print(False and False)
print(True and True)

# 2、闰年问题（输入一个年份，判断是否为闰年）
# 能被4整除 不能被100整除
# 或者能被400整除
# 4年一闰，百年不闰，400年又闰
year = 2000
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year}年是闰年')
else:
    print(f'{year}年不是闰年')

if year % 4 == 0:
    if year % 100 != 0:
        print(f'{year}年是闰年')
    else:
        if year % 400 == 0:
            print(f'{year}年是闰年')
        else:
            print(f'{year}年不是闰年')
else:
    print(f'{year}年不是闰年')

# 3、小明身高1.75，体重80kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# （1）低于18.5：过轻
# （2）18.5-25：正常
# （3）25-28：过重
# （4）28-32：肥胖
# （5）高于32：严重肥胖
# height = float(input('请输入身高:'))
# weight = float(input('请输入体重：'))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print('过轻')
# elif 18.5 <= bmi <= 25:
#     print('正常')
# elif bmi > 25 and bmi <= 28:
#     print('微胖')
# elif bmi > 28 and bmi <= 32:
#     print('肥胖')
# else:
#     print('严重肥胖')


# 5.打印以下图形
# * * * * *
# * * * *
# * * *
# * *
# *
print('---------------------------------------')
for i in range(5):
    for j in range(5 - i):
        print('*', end=' ')
    print()

# 4.打印以下图形
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
print('---------------------------------------')
for i in range(5):
    # 打印空格
    for j in range(i):
        print('  ', end='')

    # 打印*号
    for k in range(5 - i):
        print('*', end=' ')
    print()

# 6.打印以下图形
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
print('---------------------------------------')
for i in range(5):
    # 打印空格
    for j in range(5 - i - 1):
        print('  ', end='')

    # 打印*号
    for k in range(i + 1):
        print('*', end=' ')
    print()

# 7.打印以下图形
#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *
print('---------------------------------------')
num = 51
for i in range(num):
    # 空格打印
    if i <= num // 2 - 1:
        for j in range(num // 2 - i):
            print(' ', end=' ')
    elif i > (num // 2 - 1):
        for j in range(i - num // 2):
            print(' ', end=' ')

    # *号打印
    if i <= num//2:
        for k in range(2 * i + 1):
            print('*', end=' ')

    elif i > num//2:
        for k in range(num - 2 * (i - num//2)):
            print('*', end=' ')
    print()
