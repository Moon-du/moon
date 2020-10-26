# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

# 单选和复选框的选择

# 直接点击要点击的项

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class CheckBoxRadioBox():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'http://127.0.0.1/zentao/user-login.html')

        a = self.driver.find_element_by_name('keepLogin[]').is_selected()  # 获取元素是否被勾选，是-True
        print(a)

        self.driver.find_element_by_name('keepLogin[]').click()

        a = self.driver.find_element_by_name('keepLogin[]').is_selected()
        print(a)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = CheckBoxRadioBox()
    test.setUp()
    test.test()
    test.tearDown()
