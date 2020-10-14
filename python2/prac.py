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

# print(True and False)
# print(False and True)
# print(False and False)
# print(True and True)
#
# print(True or False)
# print(False or True)
# print(False or False)
# print(True or True)
#
# print(not True)
# print(not False)


# 2、闰年问题（输入一个年份，判断是否为闰年）
# 能被4整除 不能被100整除
# 或者能被400整除
# 4年一闰，百年不闰，400年又闰

# year = int(input('输入一个年份'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('闰年')
# else:
#     print('不是闰年')


# 3、小明身高1.75，体重80kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# （1）低于18.5：过轻
# （2）18.5-25：正常
# （3）25-28：过重
# （4）28-32：肥胖
# （5）高于32：严重肥胖
# h = 1.78
# w = 55
# BMI = w / (h * h)
# if BMI < 18.5:
#     print('过轻')
# elif 18.5 <= BMI < 25:
#     print('正常')
# elif 25 <= BMI < 28:
#     print('过重')
# elif 28 <= BMI <= 32:
#     print('肥胖')
# elif BMI >= 32:
#     print('正常')
# else:
#     pass
# print(BMI)
#
# h = 1.78
# w = 55
# BMI = w / (h * h)
# if BMI < 18.5:
#     print('过轻')
# elif BMI > 18.5 and BMI <= 25:
#     print('正常')
# elif BMI > 25 and BMI <= 28:
#     print('过重')
# elif BMI > 28 and BMI <= 32:
#     print('肥胖')
# elif BMI > 32:
#     print('正常')
# else:
#     pass
# print(BMI)
# 4.打印以下图形
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# for i in range(5):
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(i + 1, 6):
#         print('*', end=' ')
#     print()
# 5.打印以下图形
# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(5):
#     for j in range(i + 1, 6):
#         print('*', end=' ')
#     print()
# 6.打印以下图形
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# for i in range(5):
#     for j in range(i, 5):
#         print(' ', end=' ')
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()
# 7.打印以下图形
#       *               3空 1*
#     * * *             2空 3*
#   * * * * *           1空 5*
# * * * * * * *         0空 7*
#   * * * * *
#     * * *
#       *
# for i in range(5):
#     for j in range(i + 1, 5):
#         print(' ', end=' ')
#     for j in range(2 * i - 1):
#         print('*', end=' ')
#     print()
# for i in range(4):
#     for j in range(0, i + 1):
#         print(' ', end=' ')
#     for j in range(5 - 2 * i):
#         print('*', end=' ')
#     print()
