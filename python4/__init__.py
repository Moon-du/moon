# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/15 上午 10:56
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : __init__.py.py
# @Software : PyCharm

# def fool1(n):
#     if n == 1:
#         return 1
#     else:
#         return n + fool1(n - 1)
#
#
# if __name__ == '__main__':
#     print(fool1(4))

# 字符串的分割和拼接
str1 = 'My name is Trump'
# 分割：根据特定字符串将字符串分割为字符串的列表
# 默认根据空格分割
list1 = str1.split()
print(list1)
str2 = 'My,nammme,is,Trump'
list2 = str2.split(',')
print(list2)
list3 = str2.split('m')
print(list3)

# 拼接:将字符串的列表拼接为字符串
# 格式:'拼接字符串'.join(列表)
str4 = ' '.join(list1)
print(str4)

print(".".join(list("Hello world!")))