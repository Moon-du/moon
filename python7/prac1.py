# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/20 下午 03:48
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : prac.py
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
import time


class Animal():
    def __init__(self):
        self.weight = 50

    def eat(self):
        pass

    def crow(self):
        pass


class Sheep(Animal):
    def __init__(self):
        self.weight = 100

    def eat(self, food):
        if food == 'grass':
            self.weight += 10
        else:
            self.weight -= 10

    def crow(self):
        print('Mie...')
        self.weight -= 5


class Tiger(Animal):
    def __init__(self):
        self.weight = 200

    def eat(self, food):
        if food == 'meat':
            self.weight += 10
        else:
            self.weight -= 10

    def crow(self):
        print('Wow...')
        self.weight -= 5


class Zoo():
    def __init__(self):
        # 生成10个房间
        self.rooms = []
        for i in range(10):
            # 每个房间随机放入羊或老虎
            if random.randint(0, 1) == 0:
                # sheep1 = Sheep()
                # self.rooms.append(sheep1)
                self.rooms.append(Sheep())  # 匿名对象
            else:
                self.rooms.append(Tiger())
        print(self.rooms)

    def feed_animal(self):
        start_time = time.time()  # 记录游戏开始时间
        while True:  # 死循环
            zoom_number = random.randint(0, 9)  # 产生随机房间号
            print(f'你要喂食的是第{zoom_number + 1}号房间的动物')
            isKonck = input('是否要敲门（0-否，1-是）:')  # 询问是否敲门
            if isKonck == '1':  # 敲门
                self.rooms[zoom_number].crow()  # 房间里的动物叫
            food = input('要喂什么食物(meat/grass)：')  # 获取食物输入
            self.rooms[zoom_number].eat(food)  # 动物吃食物
            end_time = time.time()  # 获取每一次喂食结束的系统时间
            if end_time - start_time >= 20:  # 如果游戏时间超过2分钟就结束
                break

        # 计算总体重
        total_weight = 0
        for i in range(10):
            total_weight += self.rooms[i].weight
            print(self.rooms[i].weight, end=':')
        print()
        print(f'所有动物的总体重是:{total_weight}')


# 2.用面向对象的方法实现一个ATM
class ATM():
    def __init__(self):
        self.users = [
            ['袁钦洪', '123456', 5],
            ['叶飞', '666666', 60000],
            ['袁晓琴', '888888', 88888]
        ]
        self.user = None
        self.index = -1
        self.user_name = None
        self.user_pwd = None
        self.user_balance = -1

    # 登录
    def login(self):
        print('''---------欢迎使用汇智动力ATM----------''')
        isUserExist = False
        name = input('请输入账号：')
        for index in range(len(self.users)):
            if self.users[index][0] == name:
                self.user = self.users[index]
                self.index = index
                isUserExist = True
                self.verify_pwd()
        if isUserExist == False:
            print('账号不存在，请重新登录')
            self.login()

    # 验证密码
    def verify_pwd(self):
        pwd_input = input('请输入密码：')
        if self.user[1] == pwd_input:
            self.main_menu()
        else:
            print('密码错误，请重新输入')
            self.verify_pwd()

    # 主菜单
    def main_menu(self):
        print('''
---------主菜单---------
-1. 查询余额
-2. 取款
-3. 存款
-4. 转账
-5. 退出
------------------------''')
        print(self.users)
        option = input('请输入您要办的业务:')
        if option == '1':
            self.query_balance()
        elif option == '2':
            self.check_out()
        elif option == '3':
            self.save_money()
        elif option == '4':
            self.transfer()
        elif option == '5':
            self.exit()
        else:
            print('您输入了错误的业务，请重新输入')
            self.main_menu()

    # 取钱
    def check_out(self):
        money = int(input('请输入要取得金额:'))
        self.user[2] -= money
        self.users[self.index][2] = self.user[2]
        balanbce = self.user[2]
        print(f'您的账户余额为：{balanbce}元')
        # print(self.users)
        self.main_menu()

    # 查询余额
    def query_balance(self):
        balanbce = self.user[2]
        print(f'您的账户余额为：{balanbce}元')
        self.main_menu()

    # 转账
    def transfer(self):
        name = input('请输入要转账的账号:')
        isUserExist = False
        for index in range(len(self.users)):
            if self.users[index][0] == name:
                isUserExist = True
                money = int(input('请输入要转账的金额:'))
                self.user[2] -= money
                self.users[self.index][2] = self.user[2]
                self.users[index][2] += money
                balanbce = self.user[2]
                print(f'您的账户余额为：{balanbce}元')
                self.main_menu()
        if isUserExist == False:
            print('您要转账的账号不存在，请重新输入')
            self.transfer()

    # 存钱
    def save_money(self):
        money = int(input('请输入要存入的金额:'))
        self.user[2] += money
        self.users[self.index][2] = self.user[2]
        balanbce = self.user[2]
        print(f'您的账户余额为：{balanbce}元')
        # print(self.users)
        self.main_menu()

    # 退出
    def exit(self):
        print('---------欢迎再次使用，再见----------')

    def run(self):
        self.login()


from python5.db_test import db


class ATM1():
    def __init__(self):
        self.users = None
        self.user = None
        self.index = -1
        self.user_name = None
        self.user_pwd = None
        self.user_balance = -1
        self.read_db()

    def read_db(self):
        self.users = db('select * from users;')
        self.users = list(self.users)
        for index in range(len(self.users)):
            self.users[index] = list(self.users[index])

    def write_db(self):
        for user in self.users:
            sql = f"UPDATE users SET balance={user[2]} WHERE name='{user[0]}'"
            db(sql)

    # 登录
    def login(self):
        print('''---------欢迎使用汇智动力ATM----------''')
        isUserExist = False
        name = input('请输入账号：')
        for index in range(len(self.users)):
            if self.users[index][0] == name:
                self.user = self.users[index]
                self.index = index
                isUserExist = True
                self.verify_pwd()
        if isUserExist == False:
            print('账号不存在，请重新登录')
            self.login()

    # 验证密码
    def verify_pwd(self):
        pwd_input = input('请输入密码：')
        if self.user[1] == pwd_input:
            self.main_menu()
        else:
            print('密码错误，请重新输入')
            self.verify_pwd()

    # 主菜单
    def main_menu(self):
        print('''
---------主菜单---------
-1. 查询余额
-2. 取款
-3. 存款
-4. 转账
-5. 退出
------------------------''')
        print(self.users)
        option = input('请输入您要办的业务:')
        if option == '1':
            self.query_balance()
        elif option == '2':
            self.check_out()
        elif option == '3':
            self.save_money()
        elif option == '4':
            self.transfer()
        elif option == '5':
            self.exit()
        else:
            print('您输入了错误的业务，请重新输入')
            self.main_menu()

    # 取钱
    def check_out(self):
        money = int(input('请输入要取得金额:'))
        self.user[2] -= money
        self.users[self.index][2] = self.user[2]
        balanbce = self.user[2]
        print(f'您的账户余额为：{balanbce}元')
        # print(self.users)
        self.write_db()
        self.main_menu()

    # 查询余额
    def query_balance(self):
        balanbce = self.user[2]
        print(f'您的账户余额为：{balanbce}元')
        self.main_menu()

    # 转账
    def transfer(self):
        name = input('请输入要转账的账号:')
        isUserExist = False
        for index in range(len(self.users)):
            if self.users[index][0] == name:
                isUserExist = True
                money = int(input('请输入要转账的金额:'))
                self.user[2] -= money
                self.users[self.index][2] = self.user[2]
                self.users[index][2] += money
                balanbce = self.user[2]
                print(f'您的账户余额为：{balanbce}元')
                self.write_db()
                self.main_menu()
        if isUserExist == False:
            print('您要转账的账号不存在，请重新输入')
            self.transfer()

    # 存钱
    def save_money(self):
        money = int(input('请输入要存入的金额:'))
        self.user[2] += money
        self.users[self.index][2] = self.user[2]
        balanbce = self.user[2]
        print(f'您的账户余额为：{balanbce}元')
        # print(self.users)
        self.write_db()
        self.main_menu()

    # 退出
    def exit(self):
        print('---------欢迎再次使用，再见----------')

    def run(self):
        self.login()


if __name__ == '__main__':
    # chengduZoo = Zoo()
    # chengduZoo.feed_animal()
    # cbcATM = ATM()
    # cbcATM.run()
    atm = ATM1()
    atm.run()
