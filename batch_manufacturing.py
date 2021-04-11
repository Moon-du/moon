import pymysql
from faker import Faker
from openpyxl import Workbook
import random
import time


# # 循环写入数据库
# conn = pymysql.connect(host="localhost", port=3306, user="root", password="1qaz@WSX", db="test",
#                        charset="utf8")
#
# cursor = conn.cursor()
# f = Faker("zh-CN")
#
# for i in range(100):
#     sql = """insert into test( name,company,job,phone_number,address) values ('%s','%s','%s','%s','%s')""" % (
#         f.name(), f.company(), f.job(), f.phone_number(), f.address())
#
#     cursor.execute(sql)
#
# conn.commit()
# cursor.close()
# conn.close()


# 批量制造写入excel

def write_excel(file_Name, data):
    wb = Workbook()
    # 写入表头
    excel_head = ['序号', '姓名', '公司', '工作', '手机号', '地址']
    sheet0Name = '个人信息'

    sheet0 = wb.create_sheet(sheet0Name, index=0)
    for i, item in enumerate(excel_head):
        sheet0.cell(row=1, column=i + 1, value=item)

    # 写入数据
    for i, item in enumerate(data):
        i = i + 2
        for j, val in enumerate(item):
            sheet0.cell(row=i, column=j + 1, value=val)

    wb.save(file_Name + '.xlsx')


# 生成测试数据
def faker_maker(num, i):
    f = Faker("zh-CN")
    faker_list = []
    name = f.name()
    company = f.company()
    job = f.job()
    phone_number = f.phone_number()
    address = f.address()
    print(f'已生成{i+1}条数据')

    faker_list.append(str(i + 1))
    faker_list.append(name)
    faker_list.append(company)
    faker_list.append(job)
    faker_list.append(phone_number)
    faker_list.append(address)
    return faker_list


# 将数据写入excel
def faker_list_add(num):
    base_list = []
    for i in range(num):
        fake_new_list = faker_maker(num, i)
        base_list.append(fake_new_list)
    return base_list


if __name__ == "__main__":
    start_time = time.time()
    write_excel(r'F:\ym', faker_list_add(10))
    end_time = time.time()
    total_time = end_time - start_time
    print(f'用时{total_time}秒')
