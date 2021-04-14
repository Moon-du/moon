# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/28 下午 03:58
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : file_read_write.py
# @Software : PyCharm

import csv


# 文件的通用操作

# 读取csv文件
def read_csv_file(filepath):
    data = []
    with open(filepath, mode='r', encoding='utf8') as file:
        data = csv.reader(file)
        data = list(data)  # 将csv文件对象转换为列表
    return data


# 写入csv文件


if __name__ == '__main__':
    data = read_csv_file(r'C:\Users\Aurora\Desktop\moon\po\data\users.csv')
    print(data)
