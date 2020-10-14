# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/12 上午 11:26
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : data_format.py
# @Software : PyCharm

# 数据类型有三种：数值（整数、浮点数）、布尔值、字符串
# 1.数值
# 1.1 整数int
a = 1
# 1.2 浮点数float
b = 1.1

# 2.布尔值bool：表达真或假，True/False
c = True
d = False

# 3.字符串string：一串字符,用'或者''或者'''或者"""括起来的字符
e = 'a'
f = '123'
g = "abc"
# 多行字符串用'''或者"""括起来
h = '''123
abc
'''

print(type(a))
print(type(b))
print(type(c))
print(type(e))

# 数据类型转换
# 错误的示例
age = 18
# print('My age is:' + age)

# 数据类型的转换函数
# 1.str()：把其它数据类型转换为字符串
print('My age is:' + str(age))

# 2.int()：将其它类型数据转换为int类型,不是所有字符串都可以转换为int
print(int(c))
print(int(f))
# print(int(g)) #含有非数字字符的字符串不可以转换为int

# 3.float()：将其它类型数据转换为float类型,不是所有字符串都可以转换为float
print(float(c))
print(float(f))
# print(float(g)) #含有非数字字符的字符串不可以转换为float

# 4. bool:将其它类型数据转换为bool类型,把所有非零、非空的数据都转为True
print(bool(0))  # False
print(bool(0.1))  # True
print(bool('abc'))  # True
print(bool(None))  # False
