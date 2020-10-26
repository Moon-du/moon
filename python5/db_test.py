# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/16 下午 04:09
# @Author   :Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : db_test.py
# @Software : PyCharm

import pymysql


# 数据库的操作
# 读取数据库
def read_db():
    # 1.打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test')

    # 2.生成游标
    cursor = connect.cursor()

    # 3.执行sql语句
    sql = 'select * from students;'
    cursor.execute(sql)

    # 4.获取查询结果集
    resultSet = cursor.fetchall()
    print(resultSet)

    # 5.关闭数据库连接
    connect.close()

    return resultSet


# 写入数据
def write_db():
    # 1.打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test')

    # 2.生成游标
    cursor = connect.cursor()

    # 3.执行sql语句
    sql = 'insert into students values (4,"袁钦洪","男","四川省达州市");'
    cursor.execute(sql)

    # 4.提交事务
    connect.commit()

    # 5.关闭数据库连接
    connect.close()


def db(sql):
    # 1.打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test')

    # 2.生成游标
    cursor = connect.cursor()

    # 3.执行sql语句
    cursor.execute(sql)

    # 4.获取查询结果集
    resultSet = cursor.fetchall()

    # 5. 提交事务
    connect.commit()

    # 6.关闭数据库连接
    connect.close()

    return resultSet


if __name__ == '__main__':
    # read_db()
    # write_db()
    rs = db('select * from students;')
    print(rs)
    db('delete from students where id=1222;')