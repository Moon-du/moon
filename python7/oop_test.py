# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/20 上午 11:33
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : oop_test.py
# @Software : PyCharm

# 1.面向对象概念
# 1.1什么是面向对象编程
# 一切皆对象
# 在面向过程编程思想基础之上发展而来，将数据和数据的操作封装为一个不可分割的主体，这个主体就是类或对象

# 1.2什么是对象，什么是类，类和对象的关系
# 对象和类都是由：属性（静态特征）、方法(动态特征)两部分组成
# 对象就是个体，实例
# 类是对象的集合，抽象

# 1.3什么是封装、继承、多态
# 封装：将数据和数据操作封装为一个整体，对外隐藏类的实施细节
# 继承：重用现有的类生成新的类。
# 多态：同一个父类的不同子类，以不同方式去实现父类的同一方法，在继承基础之上的

# 2.面向对象程序设计
# 2.1定义类
class Dog():
    # 属性:类变量、对象变量、局部变量
    # 变量的权限：__：私有变量；_：protected权限；没有下划线:公有变量
    classname = '狗'  # 类变量

    # 方法
    # 构造方法：
    # 1.一种特殊的方法，作用是为了完成对象的初始化/实例化
    # 2.类中必有构造方法，如果不写，系统会加一个空方法体，空参数表的方法
    def __init__(self, name, color):
        # self.变量名：对象/实例变量
        # self:代指当前对象
        self.name = name
        self.color = color

        # 方法内定义的变量称为局部变量

    # 实例方法
    def eat(self):
        # 对象变量的作用域是整个类的内部
        # 对象变量的调用通过self.
        print(f'{self.name}正在啃骨头')

    def bark(self):
        print('旺-旺-旺')


# 2.2用类生成对象
xiaohuangDog = Dog('小黄', '黄色')  # 类名()实际指的类的构造方法
xiaobaiDog = Dog('小白', '白色')

# 2.2.1调用对象的方法和属性:通过.调用
print(xiaohuangDog.classname)
print(xiaohuangDog.name)
print(xiaohuangDog.color)
xiaohuangDog.eat()
xiaohuangDog.bark()
xiaobaiDog.eat()
xiaobaiDog.bark()


# 练习：创建一个名为User 的类，其中包含属性first_name 和last_name 。
# 在类User 中定义一个名 为describe_user() 的方法，它打印用户的first_name和last_name；
# 再定义一个名为greet_user() 的方法，它向用户发出个性化的问候（hello +first_name+last_name）。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self, lname, fname):
        self.first_name = fname
        self.last_name = lname

    def descibe_user(self):
        print(f'我叫{self.last_name}{self.first_name}')

    def greet_user(self):
        print(f'你好,{self.last_name}{self.first_name}')


user1 = User('袁', '钦洪')
user2 = User('叶', '飞')
user1.greet_user()
user1.descibe_user()
user2.greet_user()
user2.descibe_user()


# 2.3 封装
class Person():
    def __init__(self, lname, fname):
        self.first_name = fname
        self.last_name = lname
        self.__money = 10000

    def descibe_user(self):
        print(f'我叫{self.last_name}{self.first_name}')

    def greet_user(self):
        print(f'你好,{self.last_name}{self.first_name}')

    def lend(self, m):
        self.__money -= m
        print(f'我的钱还剩:{self.__money}')


person1 = Person('川', '建国')
# print(person1.__money)#类的外部无法访问私有变量
person1.lend(500)  # 类的私有变量可以通过方法间接访问，提高代码的安全性


# 2.4 继承
# 支持多重继承
class HuskyDog(Dog):  # class 子类名(父类名):
    def destroy(self):
        print(f'拆家')


xiaohuaDog = HuskyDog('小花', '花色')
print(xiaohuaDog.name)
xiaohuaDog.eat()
xiaohuaDog.destroy()


# 2.5多态：override覆盖，overload重载
class ChinaGardenDog(Dog):
    def eat(self):
        print('啥都吃')


class CorgiDog(Dog):
    def eat(self):
        print('精品狗粮')


dog1 = ChinaGardenDog('旺财','金色')
dog2 = CorgiDog('富贵','棕色')
dog1.eat()
dog2.eat()