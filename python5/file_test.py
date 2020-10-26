# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/16 上午 11:40
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : file_test.py
# @Software : PyCharm

# 文件的处理

# 文件的读取
def foo1():
    # 1.开文件
    # open(文件路径, mode=模式)
    # 文件路径可以用绝对、相对路径
    # mode：r-读，w-写入
    # file1 = open('./test1.txt',mode='r')#相对路径
    file1 = open(r'D:\pyworkspace\t63\python5\test1.txt', mode='r', encoding='utf8')  # 打开文件，创建文件对象

    # ASCII、GBK、UTF-8

    # 2.1.读取文件内容
    # read():将整个文件的内容读取为字符串
    str1 = file1.read()
    print(str1)

    # 3.关闭文件
    file1.close()


def foo2():
    # 开文件
    # open(文件路径, mode=模式)
    # 文件路径可以用绝对、相对路径
    # mode：r-读，w-写入
    # file1 = open('./test1.txt',mode='r')#相对路径
    file1 = open(r'D:\pyworkspace\t63\python5\test1.txt', mode='r', encoding='utf8')  # 打开文件，创建文件对象

    # ASCII、GBK、UTF-8

    # 2.一次读一行，读成字符串
    str1 = file1.readline()
    str1 = file1.readline()
    print(str1)

    # 关闭文件
    file1.close()


def foo3():
    # 开文件
    # open(文件路径, mode=模式)
    # 文件路径可以用绝对、相对路径
    # mode：r-读，w-写入
    # file1 = open('./test1.txt',mode='r')#相对路径
    file1 = open(r'D:\pyworkspace\t63\python5\test1.txt', mode='r', encoding='utf8')  # 打开文件，创建文件对象

    # ASCII、GBK、UTF-8

    # 3.讲文件中的内容读成字符串的列表(重点掌握)
    list1 = file1.readlines()
    print(list1)

    # 关闭文件
    file1.close()


# 文件的写入
def foo4():
    # 1.打开文件
    # w:当文件已存在会覆盖原有内容，如果文件不存在，会新建文件
    # a:追加写入
    file1 = open('test2.txt', mode='w', encoding='utf8')

    # 2.1写入文件
    # 将字符串写入整个文件
    str1 = 'abcde\n汇智动力\n2020'
    file1.write(str1)

    # 3.关闭文件
    file1.close()


def foo5():
    # 1.打开文件
    # w:当文件已存在会覆盖原有内容，如果文件不存在，会新建文件
    # a:追加写入
    file1 = open('test3.txt', mode='w', encoding='utf8')

    # 2.2写入文件
    # 将字符串的列表写入文件(重点掌握)
    list1 = ['abcdef\n', '123123\n', '汇智动力\n']
    file1.writelines(list1)

    # 3.关闭文件
    file1.close()


def foo6():
    """
    小练习：一份文件中保存的是各位同学的各科成绩，编写程序计算出各位同学的总成绩写入文件中每行末尾
    保存学生成绩的文件格式：
    :return:None
    """
    # 1.读取数据
    with open('score1.txt', mode='r', encoding='utf8') as file1:
        list1 = file1.readlines()
    print(list1)

    # 2.处理数据
    # 2.1分割列表中的字符串
    list2 = []
    for line in list1:  # 处理每一行
        line = line.split()  # 根据空格分割为列表
        print(line)
        sum = int(line[1]) + int(line[2]) + int(line[3])  # 计算总分
        print(sum)
        line.append(str(sum))  # 在行末加上总分
        print(line)

        line = ' '.join(line) + '\n'  # 每行用空格拼接为字符串，加上换行符
        list2.append(line)
    print(list2)

    # 3.写入数据
    with open('score2.txt', mode='w', encoding='utf8') as file1:
        file1.writelines(list2)


if __name__ == '__main__':
    # foo1()
    # foo2()
    # foo3()
    # foo4()
    # foo5()
    foo6()
