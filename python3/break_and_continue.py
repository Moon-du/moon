# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 上午 10:53
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : break_and_continue.py
# @Software : PyCharm


# 循环的控制语句
# break：终止整个循环
for i in range(1, 6):
    print(f'{i}次break之前')
    if i == 3:
        break
    print(f'{i}次break之后')

# continue：提前结束本次循环，直接开启下一次循环,只影响continue之后的代码
print('----------------------------------')
for i in range(1, 6):
    print(f'{i}次break之前')
    if i == 3:
        continue
    print(f'{i}次break之后')
