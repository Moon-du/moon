# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

# 1、日期计算：输入1970年-2049年范围内的日期，判断这一天是这一年的第几天？

def fool1():
    md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    r = input('请输入要查询的日期，例如2020-10-19：')
    r = r.split('-')
    year = int(r[0])
    month = int(r[1]) - 1
    day = int(r[2])

    if month == 0:
        days = day
    elif month == 1:
        days = day + 31
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            days = day + 1
        else:
            days = day
        for i in range(month):
            days += md[i]

    print(f'{r}是这一年的第{days}天')


# 2.用函数编程实现点球大战，
# 实现了最简单的5轮比赛循环
import random


def football():
    us = 0
    rs = 0
    i = 0
    for i in range(5):
        i += 1
        uj = int(input(f'请选择第{i}轮进攻方向1，2，3：'))
        rf = random.randint(1, 3)
        if uj != rf:
            us += 1
            print(f'玩家进攻方向{uj},电脑防守方向{rf},进攻成功玩家加一分,当前分数玩家{us}分：电脑{rs}分')
        else:
            rs += 1
            print(f'玩家进攻方向{uj},电脑防守方向{rf},进攻失败电脑加一分,当前分数玩家{us}分：电脑{rs}分')

        uf = int(input(f'请选择第{i}轮防守方向1，2，3：'))
        rj = random.randint(1, 3)
        if uf != rj:
            rs += 1
            print(f'电脑进攻方向{rj},玩家防守方向{uf},防守失败电脑加一分,当前分数玩家{us}分：电脑{rs}分')
        else:
            us += 1
            print(f'电脑进攻方向{rj},玩家防守方向{uf},防守成功玩家加一分,当前分数玩家{us}分：电脑{rs}分')

    if us > rs:
        print(f'玩家得分{us},电脑得分{rs},玩家获胜')
    elif us < rs:
        print(f'玩家得分{us},电脑得分{rs},电脑获胜')
    else:
        print('比分相等开始加时赛')
        football()


if __name__ == '__main__':
    fool1()
    football()
