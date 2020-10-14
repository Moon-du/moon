# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/13 上午 10:27
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : operator_test.py
# @Software : PyCharm

# 运算符

# 3.逻辑运算符：两边运算布尔值，得到布尔值
# and：逻辑与关系，并且，求两个条件的交集，当缩小范围时应该用and运算

# or：逻辑或关系，或者，求两个条件的并集，当扩大范围的时候用or运算

# not：逻辑非关系，非真为假，非假为真


# 4.赋值运算符：赋值的优先级，都是先右后左
a = 1
b = 2
b += a  # 等同于b=b+a
b += a * b
print(b)

# 5.成员运算符in和身份运算符is
# in操作符的运算值是布尔值，a in b：a是否是b的成员
print(3 in (1, 2, 3, 4, 5))
print(0 in (1, 2, 3, 4, 5))

# 6.位和位移运算符
# 位运算：运算数值得到数值，& | ~，讲数值转换为2进制，从低位对齐按位做相应的与、或、非运算
print(3&5)
print(3|5)
print(~5)
