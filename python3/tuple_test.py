# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 下午 02:19
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : tuple_test.py
# @Software : PyCharm

# 2.元祖tuple
# 元祖可以看做是不可变的列表，不能新增元素，不能删除元素，不能修改元素的值，只能查询

# 2.1元祖的定义
tuple1 = (1, 1.1, 1, 'abc', False)

# 访问方式
print(tuple1[0])
print(tuple1[4])

# 操作元祖的函数
tuple2 = (-11, 0, 99, 5)
print(len(tuple2))
print(max(tuple2))
print(min(tuple2))

# 2.2元祖的操作
# 不能增、删、改
# tuple2[0] = -20
# print(tuple2)

# 遍历查询
for i in tuple2:
    print(i)

for i in range(len(tuple2)):
    print(tuple2[i])