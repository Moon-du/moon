# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/12 下午 03:42
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : string_format.py
# @Software : PyCharm

# 字符串的格式化：为了在字符串中混合变量输出
name = '川普'
age = 75
print('我的名字是:' + name + ',我的年龄是：' + str(age))

# 1.占位符：%s,%d,%f,%x
print('我的名字是:%s，我的年龄是:%d' % (name, age))
# 1.2指定宽度
print('我的名字是:%s，我的年龄是:%10d' % (name, age))  # 指定宽度
print('我的名字是:%s，我的年龄是:%010d' % (name, age))  # 指定宽度，高位补零
pi = 3.14159265
print('圆周率是:%10f' % pi)  # 小数点要占一位
print('圆周率是:%10.2f' % pi)  # 指定宽度和小数位数(%x.yf):x整个位数，y小数位数
print('圆周率是:%-010.2f' % pi)  # 左对齐

print('-----------------------------------------------------------')
# 2. f''函数:python3.6开始支持的新特性
print(f'我的名字是:{name}，我的年龄是:{age}')
# 2.2指定宽度
print(f'圆周率是:{pi:10}')  # 指定宽度
print(f'圆周率是:{pi:10.2f}')  # 指定宽度和小数位数
print(f'圆周率是:{pi:010.2f}')  # 补零
print(f'圆周率是:{pi:<010.2f}')  # 左对齐，低位会补零
