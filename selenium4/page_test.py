# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PageTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'http://news.baidu.com/')

        # 下翻页
        self.driver.find_element_by_xpath('/html').send_keys(Keys.PAGE_DOWN)

        # 向下滚动
        for i in range(20):
            self.driver.find_element_by_xpath('/html').send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)

        # 回到页面最顶部
        self.driver.find_element_by_xpath('/html').send_keys(Keys.HOME)
        time.sleep(2)

        # 模拟ctrl+a：多个按键同时按下
        # sendkeys(key1,key2,...)
        self.driver.find_element(By.XPATH, '/html').send_keys(Keys.CONTROL, 'a')
        time.sleep(2)

        # 截图
        # 1.对整个页面截图(推荐)
        self.driver.get_screenshot_as_file(r'D:\pyworkspace\t63\selenium4\1.png')

        # 2.对元素截图
        element = self.driver.find_element(By.ID, 'imgView')
        element.screenshot(r'D:\pyworkspace\t63\selenium4\2.png')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = PageTest()
    test.setUp()
    test.test()
    test.tearDown()
