# _*_ coding: UTF-8 _*_
# @Time : 2021/3/16 19:26
# @Author : moon
# @Site : www.ysbzc.com
# @File : diff_time.py
# @Software : PyCharm

import datetime
import time


def diff_time(start, end):
    date1 = time.strptime(start, "%Y-%m-%d %H:%M:%S")
    date2 = time.strptime(end, "%Y-%m-%d %H:%M:%S")
    date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
    date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
    Seconds = (date2 - date1).seconds
    minute = Seconds/60
    Hour = minute/60
    Days = (date2 - date1).days

    print(f'秒数:{Seconds}')
    print(f'分钟数:{minute}')
    print(f'小时数:{Hour}')
    print(f'天数:{Days}')


if __name__ == "__main__":
    diff_time("2021-3-16 13:12:10", "2021-3-16 19:10:10")
