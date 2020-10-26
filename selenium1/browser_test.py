# _*_ coding: UTF-8 _*_
# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

from selenium import webdriver
import time

class BrowserTest():
    # 前置条件
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()

    # 测试步骤（包含预期结果）
    def test(self):
        time.sleep(3)

    # 后置处理：关闭浏览器，清理资源
    def tearDown(self):
        #关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    test = BrowserTest()
    test.setUp()
    test.test()
    test.tearDown()
