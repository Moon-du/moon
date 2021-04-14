# _*_ coding: UTF-8 _*_
# @Time : 2020/10/27 18:09
# @Author : moon
# @Site : www.ysbzc.com
# @File : __init__.py.py
# @Software : PyCharm
import unittest
import time
from selenium import webdriver


class TestLogin():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(r'https://www.jd.com/')
        self.driver.maximize_window()
    time.sleep(3)
    def test_login_1(self):
        self.driver.find_element_by_name("loginId").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("sys123456")
        self.driver.find_element_by_id("button_submit").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    tset = TestLogin()
    tset.setUp()
