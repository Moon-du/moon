# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/16 上午 11:25
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : prac.py
# @Software : PyCharm

# 1.递归实现阶乘：
# n！=nxn-1xn-2x....1
def fool1(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * fool1(n - 1)


# 2.实现1！+2！+3！+。。。+10！
def fool2(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * fool1(n - 1)


def fool3(a):
    sum = 0
    for i in range(1, a + 1):
        sum += fool2(i)
        i += 1
    print(sum)


# 3.现有文件1（见附件）， 记录了公司员工的薪资，其内容格式如下
#
# name: Jack   ;    salary:  12000
#  name :Mike ; salary:  12300
# name: Luk ;   salary:  10030
#   name :Tim ;  salary:   9000
# name: John ;    salary:  12000
# name: Lisa ;    salary:   11000
#
# 每个员工一行，记录了员工的姓名和薪资，
# 每行记录 原始文件中并不对齐，中间有或多或少的空格
#
# 现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
# 以如下格式存入新的文件2中，如下所示
#
# name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
# name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
# name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
# name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
# name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
# name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900
#
# 要求对齐，上面看着如果不齐，应该是字体原因
# tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数
def fool4():
    list2 = []
    with open('test1.txt', mode='r', encoding='utf8') as file1:
        list1 = file1.readlines()
    for line in list1:
        line = line.split(';')
        line = ' '.join(line)
        line = line.split(':')
        line = ' '.join(line)
        line = line.split()
        line = ' '.join(line)
        line = line.split()
        tax = int(line[3]) * 0.1
        line.append('tax')
        line.append(str(round(tax)))
        income = int(line[3]) - tax
        line.append('income')
        line.append(str(round(income)))
        line = ' \t'.join(line) + '\n'
        list2.append(line)
    with open('test2.txt', mode='w', encoding='utf8') as file2:
        file2.writelines(list2)


# 4、008.zip中存在三张表，teacher.txt存的是老师的id和老师的名字，course.txt存的是课程Id和课程名称，teacher_course.txt存的是课程id和老师Id的对应关系
# 题目要求，根据teacher_course.txt表将老师的名字和课程的名称对应在一起，存到新的文件里，格式如下：
#
# 小猪老师:软件测试框架课程
# mandy老师:web测试技术课程
# 小阳老师:app测试技术课程
# ....
def fool5():
    with open('course.txt', encoding='utf8') as file1:
        list1 = file1.read().splitlines()[1:]
    with open('teacher.txt', encoding='utf8') as file2:
        list2 = file2.read().splitlines()[1:]

    cDict = {}

    for line1 in list1:
        if not line1.strip():
            continue

        parts = line1.split(';')
        cId = parts[0]
        cName = parts[1]
        cDict[cId] = cName

    tDict = {}
    for line2 in list2:
        if not line2.strip():
            continue

        parts = line2.split(';')
        tId = parts[0]
        tName = parts[4]
        tDict[tId] = tName

    with open('teacher_course.txt') as file3:
        list3 = file3.read().splitlines()[1:]

    with open('test3.txt', 'w', encoding='utf8') as file4:
        for line3 in list3:
            if not line3.strip():
                continue

            parts = line3.split(';')
            tId = parts[0]
            cId = parts[1]

            if (tId not in tDict) or (cId not in cDict):
                print(f'skip record {line3}')
                continue

            test = f"{tDict[tId]:10} : {cDict[cId]}"

            print(test)

            file4.write(test + '\n')


if __name__ == '__main__':
    # print(fool1(4))
    # fool3(3)
    # fool4()
    fool5()
