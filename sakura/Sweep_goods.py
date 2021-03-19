# _*_ coding: UTF-8 _*_
# @Time : 2021/3/19 11:02
# @Author : moon
# @Site : www.ysbzc.com
# @File : Sweep_goods.py
# @Software : PyCharm

from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()


def login():
    driver.get("https://www.jd.com/")
    if driver.find_element_by_class_name("link-login"):
        driver.find_element_by_class_name("link-login").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        driver.get("https://cart.jd.com/cart.action")
    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(buytime)
        print(now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                if driver.find_element_by_class_name("submit-btn"):
                    driver.find_element_by_class_name("submit-btn").click()
                    driver.find_element_by_id("order-submit").click()
            except:
                time.sleep(0.01)
        print(now)
        time.sleep(0.01)


if __name__ == "__main__":
    # 将下列时间改为你需要的抢购时间(例如格式：2021-03-26 00:00:00)
    times = "2021-03-26 00:00:00"
    login()
    buy(times)