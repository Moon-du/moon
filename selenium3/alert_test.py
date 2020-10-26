# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm
# 弹出警告框的处理

# 弹出警告框当弹出时，无法操作页面，警告框是属于浏览器定义的，无法通过元素定位的方式操作

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class AlertTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'D:\pyworkspace\t63\selenium3\example.html')

        self.driver.find_element_by_name('alterbutton').click()
        time.sleep(1)

        # 1.alert弹出框
        # 1.1获取弹出框对象，并切换到弹出框
        alert = self.driver.switch_to.alert

        # 1.2调用alert对象的方法
        alert.accept()  # 点击“确定”
        time.sleep(2)

        self.driver.find_element_by_name('confirmbutton').click()
        time.sleep(1)
        # 2.confirm弹出框
        #2.1
        confirm = self.driver.switch_to.alert

        #2.2
        confirm.dismiss()  # 点击取消
        time.sleep(1)
        confirm.accept()  # 点击确定
        time.sleep(2)

        #3.prompt弹出框
        self.driver.find_element_by_name('promptbutton').click()
        time.sleep(1)

        #3.1
        prompt = self.driver.switch_to.alert

        #3.2
        prompt.send_keys('汇智动力')
        time.sleep(1)

        prompt.accept()
        time.sleep(1)

        prompt.accept()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = AlertTest()
    test.setUp()
    test.test()
    test.tearDown()
