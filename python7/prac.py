# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

# 1.
# 10个房间，每个里面可能是200斤老虎或者100斤羊
# 游戏开始后，系统随机给出房间号，游戏者喂里面的动物
# 喂老虎应该输入单词meat，喂羊输入单词grass
# 喂对了，体重增加10斤。喂错了，体重减少10斤
# 敲房间的门，里面的动物会叫，老虎的声音是“Wow”，羊的声音是“Mie”，动物每叫一次体重减5斤
# 游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物
# 游戏2分钟结束后，看看你喂的动物总体重是多少
import random


class Sheep():
    def __init__(self, name):
        self.name = name
        self.weight = 100

    def cry(self):
        print('Mie')

    def eatn(self, m):
        self.weight -= m
        print(f'当前体重:{self.weight}')

    def eaty(self, m):
        self.weight += m
        print(f'当前体重:{self.weight}')


class Tiger():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def cry(self):
        print('Wow')

    def eat(self):
        pass





def play():
    room = []
    for i in range(10):
        j = random.randint(0, 1)
        if j == 0:
            room.append(0)  # 0代表老虎
        else:
            room.append(1)  # 1代表羊
    print(room)
    i = random.randint(0, 9)
    print(f'房间号是{i}')
    s = int(input('请选择食物：0.meat,1.grass'))
    if s == room[i]:
        print(f'喂食成功，老虎体重加10斤，当前体重{Sheep.eaty(10)}')
    else:
        print(f'喂食失败，老虎体重减10斤，当前体重{Sheep.eaty(10)}')


# 2.用面向对象的方法实现一个ATM
if __name__ == '__main__':
    play()
