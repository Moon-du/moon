# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/16 上午 11:25
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : prac.py
# @Software : PyCharm

# 1.递归实现阶乘：
# n！=nxn-1xn-2x....1
# 5!=5x4！
def foo1(n):
    if n == 1:
        return 1
    else:
        return n * foo1(n - 1)


def foo2(n):
    sum = 1
    # for i in range(1,n+1):
    #     sum *=i
    # return sum
    for i in range(n, 0, -1):
        sum *= i
    return sum


# 2.实现1！+2！+3！+。。。+10！
def foo3(n):
    sum = 0
    for i in range(1, n + 1):
        n = 1
        for j in range(1, i + 1):
            n = n * j
        sum += n
    return sum


def foo4(n):
    sum = 0
    for i in range(1, n + 1):
        sum += foo1(i)
    return sum


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

def foo5():
    # 1.读取数据
    with open(r'D:\pyworkspace\t63\python5\salary.txt', mode='r', encoding='utf8') as file1:
        list1 = file1.readlines()

    # 2.处理数据
    print(list1)
    list2 = []
    for line in list1:
        line = line.replace(';', ":")
        line = line.split(':')
        name = line[1].strip()
        salary = int(line[3].strip())
        tax = int(salary * 0.1)
        income = int(salary * 0.9)
        line = f"name: {name:7};    salary:{salary:7d} ;  tax:{tax:5d} ; income:{income:7d}\n"
        print(line)
        list2.append(line)
    print(list2)

    # 3.写入数据
    with open('salary2.txt', mode='w', encoding='utf8') as file2:
        file2.writelines(list2)


# 4、008.zip中存在三张表，teacher.txt存的是老师的id和老师的名字，course.txt存的是课程Id和课程名称，teacher_course.txt存的是课程id和老师Id的对应关系
# 题目要求，根据teacher_course.txt表将老师的名字和课程的名称对应在一起，存到新的文件里，格式如下：
#
# 小猪老师:软件测试框架课程
# mandy老师:web测试技术课程
# 小阳老师:app测试技术课程
# ....

def foo6():
    # 1.读取数据
    with open('teacher.txt', 'r', encoding='utf8') as file1, open('course.txt', 'r', encoding='utf8') as file2, open(
            'teacher_course.txt', 'r', encoding='utf8') as file3:
        teacher = file1.readlines()
        course = file2.readlines()
        teacher_course = file3.readlines()
    # print(teacher)
    # print(course)
    # print(teacher_course)

    # 2.查找并替换数据
    # 2.1 分割三个列表
    for index in range(len(teacher)):
        teacher[index] = teacher[index].rstrip('\n').split(';')
    # print(teacher)
    for index in range(len(course)):
        course[index] = course[index].rstrip('\n').split(';')
        # print(course[index])
    # print(course)
    for index in range(len(teacher_course)):
        teacher_course[index] = teacher_course[index].rstrip('\n').split(';')
        # print(teacher_course[index])
    # print(teacher_course)

    # 2.2根据teacher_course列表，查teacher id和course id
    for index in range(len(teacher_course)):
        teacher_id = teacher_course[index][0]
        course_id = teacher_course[index][1]

        # 查找teacher中的teacher id对应的teacher name
        for line in teacher:
            if line[0] == teacher_id:
                teacher_name = line[4]
                teacher_course[index][0] = teacher_name

        # 查找course中的course id对应的course name
        for line in course:
            if line[0] == course_id:
                course_name = line[1]
                teacher_course[index][1] = course_name

    print(teacher_course)

    # 2.3 拼接每行数据加上换行符
    for index in range(len(teacher_course)):
        if index ==0:
            teacher_course[index] = "teacher_name;course_name\n"
        else:
            teacher_course[index] = ';'.join(teacher_course[index])+'\n'
    print(teacher_course)

    # 3.写入文件
    with open('teacher_course_new.txt',mode='w',encoding='utf8') as file1:
        file1.writelines(teacher_course)


if __name__ == "__main__":
    print(foo1(5))
    print(foo2(5))
    print(foo3(3))
    print(foo4(3))
    print('------------------------------------------')
    foo5()
    print('------------------------------------------')
    foo6()
