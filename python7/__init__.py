# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/20 上午 11:33
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : __init__.py.py
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
