# _*_ coding: UTF-8 _*_
# @Time : 2021/1/11 18:27
# @Author : moon
# @Site : www.ysbzc.com
# @File : sakura3.py
# @Software : PyCharm

from turtle import *
import random


def drawTree(length):
    if length > 1:
        if length < 30 and length > 14:  # 缩小一下树干
            pensize(4)
        elif length < 15 and length > 5:  # 长度这个范围内那么就是绿叶
            color('#04B486')  #
            pensize(3)
        elif length < 5 and length > 1:  # 红花
            color('#FE2E9A')
            pensize(2)
        else:
            color('#5E5E5E')  # 其他范围就是正常的树干
            pensize(5)
        # 随机角度与长度
        randangle = 2 * random.random()
        randlen = 2 * random.random()

        # 每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20 * randangle)
        drawTree(length - 10 * randlen)

        # 这里是向左的角度转动
        left(40 * randangle)
        drawTree(length - 10 * randlen)

        # 为什么需要再向右转20度？那是因为我一共向左转了40度，使用backward后退，必须是相同的角度，不然退回去角度就不同了位置就不会对
        right(20 * randangle)

        up()
        backward(length)
        down()


def fallingFlowers(m):
    x, y = -1000, -750
    for i in range(30):
        up()
        goto(x, y)
        x += 100
        down()
        yval = 50
        for i in range(m):
            a = 100 * random.random()
            b = 2 * random.random()
            print(a)
            if a > 59:
                color('#FE2E9A')
            else:
                color('#04B486')
            circle(5)
            up()
            goto(x, y + (yval * b))
            fd(a)
            yval += 50
            down()


setworldcoordinates(-1000, -750, 1000, 750)
tracer(False)

fallingFlowers(10)  # 绘制落叶
bgcolor("#F5F6CE")
color('#5E5E5E')
pensize(5)

up()
goto(0, -700)  # 跳到绘制起始点
down()

left(80)
fd(140)
drawTree(120)

input()

