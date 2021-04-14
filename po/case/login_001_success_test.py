# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/28 下午 03:35
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : login_001_success_test.py
# @Software : PyCharm

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from po.page.login_page import LoginPage
from po.page.main_page import MainPage
from po.common.file_read_write import read_csv_file


class Login_001_Success(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)

        # 生成页面对象
        self.login_page = LoginPage(self.driver, self.wait)
        self.main_page = MainPage(self.driver, self.wait)

        # 读取用户账号数据
        self.data = read_csv_file(r'C:\Users\Aurora\Desktop\moon\po\data\users.csv')

    def test(self):
        for user in self.data:
            self.login_page.open()
            self.login_page.input_user(user[0])
            self.login_page.input_pwd(user[1])
            self.login_page.input_authcode()
            self.login_page.click_login()
            # self.main_page.verify_url()
            self.main_page.logout()

    def tearDown(self) -> None:
        self.driver.quit()
