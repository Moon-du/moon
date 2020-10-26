# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/15 上午 10:56
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : __init__.py.py
# @Software : PyCharm

def fool1(n):
    if n == 1:
        return 1
    else:
        return n + fool1(n - 1)


if __name__ == '__main__':
    print(fool1(4))