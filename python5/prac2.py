# _*_ coding: UTF-8 _*_
# @Time     : 2020/8/14 下午 04:23
# @Author   : Li jie
# @Site     : http://www.cdtest.cn/
# @File     : prac.py
# @Software : PyCharm

import random


# 1、文件操作：
#
# 现有文件1（见附件）， 记录了公司员工的薪资，其内容格式如下
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
def foo1():
    # 1.读取文件
    with open('salary.txt', 'r', encoding='utf8') as file1:
        data = file1.readlines()
    print(data)
    # 2.处理数据
    # 2.1 将数据去除\n和空格
    data_new = []
    for line in data:
        line = line.rstrip('\n')
        line_new = []
        print(line)
        line = line.split(';')
        print(line)
        for line1 in line:
            line1 = line1.split(':')
            print(line1)
            for line2 in line1:
                line2 = line2.strip()
                print(line2)
                line_new.append(line2)
        data_new.append(line_new)

        # 2.2 将数据处理为固定格式
        data_new_1 = []
        for line in data_new:
            line = f'''{line[0]}: {line[1]:<7};    {line[2]}:{line[3]:>7} ; tax:{int(int(line[3]) * 0.1):5} ; income:{int(
                int(line[3]) * 0.9):7}+\n'''
            data_new_1.append(line)

            print(data_new)
            print(data_new_1)

            # 3.写入文件
            with open('salary_new.txt', 'w', encoding='utf8') as file1:
                file1.writelines(data_new_1)

                # 2.008.zip中存在三张表，teacher.txt存的是老师的id和老师的名字，course.txt存的是课程Id和课程名称，teacher_course.txt存的是课程id和老师Id的对应关系
                # 题目要求，根据teacher_course.txt表将老师的名字和课程的名称对应在一起，存到新的文件里，格式如下：
                #
                # 小猪老师:软件测试框架课程
                # mandy老师:web测试技术课程
                # 小阳老师:app测试技术课程
                # ....


def read_file(file_path):
    '''
    :param file_path:文件路径
    :return:字符串list
    '''
    with open(file_path, 'r', encoding='utf8') as file1:
        data = file1.readlines()
    return data


def write_file(file_path, data):
    '''
    :param file_path: 文件路径
    :param data: 写入数据，必须是字符串list
    :return: None
    '''
    with open(file_path, 'w', encoding='utf8') as file1:
        file1.writelines(data)


def foo2():
    # 1.读取三个文件
    courses = read_file('course.txt')
    teachers = read_file('teacher.txt')
    teacher_courses = read_file('teacher_course.txt')
    print(courses)
    print(teachers)
    print(teacher_courses)

    # 2.处理数据
    # 2.1处理\n,分割三个数据的；,去掉表头
    for index in range(1, len(courses)):
        courses[index] = courses[index].rstrip('\n').split(';')
    courses.pop(0)
    print(courses)
    for index in range(1, len(teachers)):
        teachers[index] = teachers[index].rstrip('\n').split(';')
    teachers.pop(0)
    print(teachers)
    for index in range(1, len(teacher_courses)):
        teacher_courses[index] = teacher_courses[index].rstrip('\n').split(';')
    teacher_courses.pop(0)
    print(teacher_courses)

    # 2.2 对teacher_courses的数据进行替换
    for index in range(len(teacher_courses)):
        # 查找并替换老师id
        teacher_id = teacher_courses[index][0]
        for teacher in teachers:
            if teacher[0] == teacher_id:
                teacher_name = teacher[4]
                break
        teacher_courses[index][0] = teacher_name

        # 查找并替换课程id
        course_id = teacher_courses[index][1]
        for course in courses:
            if course[0] == course_id:
                course_name = course[1]
                break
        teacher_courses[index][1] = course_name
    print(teacher_courses)

    # 2.3对每行数据拼接，加上换行符
    for index in range(len(teacher_courses)):
        teacher_courses[index] = ':'.join(teacher_courses[index]) + '\n'
    print(teacher_courses)

    # 3.写入数据
    write_file('teacher_course_new.txt', teacher_courses)


# 3.使用函数编程实现一个ATM的操作
# # 登录，打印主菜单，取钱，存钱，转账，查询余额
# # 所有用户数据用文件

# users = [
#     ['李源', '123456', 10000000],
#     ['李鹏飞', '666666', 1],
#     ['严枫', '888888', 100]
# ]
users = []

id = -1


def read_data():
    global users
    with open('users.txt', 'r', encoding='utf8') as file1:
        data = file1.readlines()
    for index in range(len(data)):
        data[index] = data[index].split()
    users = data
    # print(users)


def write_data():
    global users
    data = users
    for index in range(len(data)):
        data[index] = ' '.join(data[index]) + '\n'
    with open('users.txt', 'w', encoding='utf8') as file1:
        file1.writelines(data)


# 插卡
def insert_card():
    global users
    global id
    read_data()
    is_user_exist = False
    name = input('请输入您的账号：')
    for index in range(len(users)):
        if users[index][0] == name:
            is_user_exist = True
            pwd = input('请输入密码：')
            if pwd == users[index][1]:
                id = index
                main_menu()
            else:
                print('密码输入错误，请重新输入')
                insert_card()
    if not is_user_exist:
        print('账号不存在，请重新输入')
        insert_card()


# 主菜单
def main_menu():
    choice = input('''
--------欢迎使用汇智动力ATM--------
-1. 查询余额
-2. 取钱
-3. 存钱
-4. 转账
-0. 退出
-----------------------------------
请输入你要办理的业务：''')
    if choice == '1':
        query_balance()
    elif choice == '2':
        check_out()
    elif choice == '3':
        save_money()
    elif choice == '4':
        transfer_money()
    elif choice == '0':
        exit()
    else:
        print('输入选项不合法，请重新输入！')
        main_menu()


# 查询余额
def query_balance():
    global id
    read_data()
    balance = users[id][2]
    print(f'您的账户余额为：{balance}元')
    main_menu()


# 取钱
def check_out():
    global id
    read_data()
    balance = int(users[id][2])
    money = int(input('请输入您要取出的金额:'))
    if money <= balance:
        users[id][2] = str(int(users[id][2]) - money)
        print(f'成功取出:{money}元，您的账户余额为:{users[id][2]}元.')
        write_data()
        main_menu()
    else:
        print('您的余额不足，请重新输入')
        check_out()


# 存钱
def save_money():
    global id
    read_data()
    money = int(input('请输入要存入的金额：'))
    users[id][2] = str(int(users[id][2]) + money)
    print(f'成功存入:{money}元，您的账户余额为:{users[id][2]}元.')
    write_data()
    main_menu()


# 转账
def transfer_money():
    global users
    global id
    read_data()
    name = input('请输入要转账的用户名：')
    for index in range(len(users)):
        is_user_exist = False
        if users[index][0] == name:
            is_user_exist = True
            money = int(input('请输入要转账的金额：'))
            users[id][2] = str(int(users[id][2]) - money)
            users[index][2] = str(int(users[index][2]) + money)
            print(f'成功转账:{money}元，您的账户为:{users[id][2]}元')
            write_data()
            main_menu()
    if not is_user_exist:
        print('您要转账的用户不存在，请重新输入：')
        transfer_money()


# 退出
def exit():
    print('----------欢迎再次使用----------')
    print('----------    再见    ----------')


if __name__ == '__main__':
    # foo1()
    # print(random.randint(1,19))
    # foo2()
    insert_card()
    # read_data()
