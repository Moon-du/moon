# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/19 下午 04:36
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : prac.py
# @Software : PyCharm

import random


# 1、日期计算：输入1970年-2049年范围内的日期，判断这一天是这一年的第几天？
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def foo1(year, month, day):
    if isLeapYear(year):
        if month == 1:
            return day
        elif month == 2:
            return 31 + day
        elif month == 3:
            return 31 + 29 + day
        elif month == 4:
            return 31 + 29 + 31 + day
        elif month == 5:
            return 31 + 29 + 31 + 30 + day
        elif month == 6:
            return 31 + 29 + 31 + 30 + 31 + day
        elif month == 7:
            return 31 + 29 + 31 + 30 + 31 + 30 + day
        elif month == 8:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + day
        elif month == 9:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + day
        elif month == 10:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
        elif month == 11:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
        elif month == 12:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
        else:
            print(f'输入月份不合法:{month}')
    else:
        if month == 1:
            return day
        elif month == 2:
            return 31 + day
        elif month == 3:
            return 31 + 28 + day
        elif month == 4:
            return 31 + 28 + 31 + day
        elif month == 5:
            return 31 + 28 + 31 + 30 + day
        elif month == 6:
            return 31 + 28 + 31 + 30 + 31 + day
        elif month == 7:
            return 31 + 28 + 31 + 30 + 31 + 30 + day
        elif month == 8:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + day
        elif month == 9:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day
        elif month == 10:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
        elif month == 11:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
        elif month == 12:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
        else:
            print(f'输入月份不合法:{month}')


def foo2(year, month, day):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for i in range(month - 1):
        days += days_of_month[i]
    days = days + day
    if isLeapYear(year) and month > 2:
        days += 1
    return days


# 2.用函数编程实现点球大战，
# 实现了最简单的5轮比赛循环
user_attack_dir = 0
robot_attack_dir = 0

user_score = 0
robot_score = 0

turn = 1


# 用户进攻
def user_attack():
    global user_attack_dir
    user_attack_dir = int(input('请输入你要进攻的方向(1-左，2-中，3-右)：'))


# 用户防守
def robot_defense():
    global user_score
    global user_attack_dir
    dir = random.randint(1, 3)
    print(dir)
    if dir == user_attack_dir:
        print('电脑防守成功')
    else:
        user_score += 1
        print('电脑防守失败，用户得一分')


# 电脑进攻
def robot_attack():
    global robot_attack_dir
    robot_attack_dir = random.randint(1, 3)
    print(robot_attack_dir)


# 用户防守
def user_defense():
    global robot_attack_dir
    global robot_score
    dir = int(input('请输入你要防守的方向(1-左，2-中，3-右)：'))
    if dir == robot_attack_dir:
        print('用户防守成功')
    else:
        print('用户防守失败，电脑得一分')
        robot_score += 1


# 游戏
def football():
    global turn
    global user_score
    global robot_score
    while turn <= 5:
        user_attack()
        robot_defense()
        robot_attack()
        user_defense()
        print(f'第{turn}轮结束，比分为用户-{user_score}：电脑-{robot_score}')
        turn += 1


if __name__ == '__main__':
    print(foo1(2020, 10, 20))
    print(foo1(2019, 3, 2))
    print(foo2(2020, 10, 20))
    print(foo2(2020, 3, 2))
    print(foo2(2020, 2, 2))
    print('-------------------------------')
    football()
