# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/12 上午 11:25
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : __init__.py.py
# @Software : PyCharm

i = int(input('输入一个1000以内的数字：'))
for num in range(2, i):
    g = (num % 10)
    s = (num // 10 % 10)
    b = (num // 100 % 10)
    # print(f'{b}{s}{g}')
    if g ** 3 + s ** 3 + b ** 3 == num:
        print(num)
