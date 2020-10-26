# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


# 元素的识别和定位
# 在基于UI的自动化测试当中，元素的识别和定位起到了关键的作用
class upLoad_test():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'http://news.baidu.com/')
        time.sleep(1)
        for i in range(1, 7):
            self.driver.find_element_by_xpath(f'//*[@class="hotnews"]/ul/li[{i}]').click()

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == '中国人的故事 | 致英雄孙占元：忘不了那句“跟我上”！您从未远离_新闻频道_中国青年网':
                break
            time.sleep(1)

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = upLoad_test()
    test.setUp()
    test.test()
    test.tearDown()
