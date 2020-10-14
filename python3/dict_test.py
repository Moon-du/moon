# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/14 下午 03:32
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : dict_test.py
# @Software : PyCharm

# 字典：dict
# 字典不是序列，没有index，元素是无序的

# 字典的定义:{key1:value1,key2:value2,...}
# key必须是可以hash的类型，一般用数值或者字符串，不可以重复，必须唯一
# value可以是任意任意类型，可以重复
dict1 = {'名字': '袁钦洪',
         '身高': 2.08,
         '体重': 180
         }

# 两层字典的定义：
students = {
    '袁钦洪': {
        '身高': 208,
        '体重': 180
    },
    '昝晓琴': {
        '身高': 180,
        '体重': 208
    }
}

# 字典的元素访问：通过key来访问对应value
print(dict1['名字'])
print(dict1['身高'])

print(students['袁钦洪']['体重'])
print(students['昝晓琴']['身高'])

# 两层list：
list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(list1[0][1])
print(list1[1][2])
print(list1[2][2])

# 字典的主要操作：增，删，改，查

# 新增：新增一对键值对
# 对不存在的键赋值就是新增
dict1['年龄'] = 18
print(dict1)

# 修改：
# 对存在的键赋值就是修改value
dict1['身高'] = 1.78
print(dict1)

# 删除:
# 1.dict.pop('键')
dict1.pop('体重')
print(dict1)

# del dict[键]
del dict1['身高']
print(dict1)

# 遍历查询
# 直接遍历字典,得到的是key
for key in dict1:
    print(key)
    print(dict1[key])

#获取所有的键
k = dict1.keys()
print(k)

#获取所有的值
v = dict1.values()
print(v)