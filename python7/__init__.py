# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

import random

def room():
    room = []
    for j in range(10):
        j = random.randint(0, 1)
        if j == 0:
            room.append(0)  # 0代表老虎
        else:
            room.append(1)  # 1代表羊
    print(room)


room()
