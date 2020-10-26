# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/22 上午 11:11
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : webelement_test.py
# @Software : PyCharm

from selenium import webdriver
import time


# 元素的识别和定位
# 在基于UI的自动化测试当中，元素的识别和定位起到了关键的作用
class WebElementTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get('https://www.baidu.com/')

        # 定位元素
        element = self.driver.find_element_by_id('kw')

        # 元素操作
        element.send_keys('成都地震')  # sendkeys：对输入框输入文本，只能对input元素输入
        time.sleep(1)

        # 元素定位的8种方式：
        # 1.id定位：最推荐的定位方式，一般是唯一的，而且是最快的

        # 2.name定位：
        self.driver.find_element_by_name('wd').clear()  # 清空输入框，只能对input元素输入
        self.driver.find_element_by_name('wd').send_keys('成都出太阳')
        time.sleep(1)

        self.driver.get('https://www.baidu.com/')

        # 3.class name定位:
        self.driver.find_element_by_class_name('mnav').click()  # 点击元素
        time.sleep(1)

        # 4.link text：通过<a>的text定位,只针对链接<a>元素
        self.driver.find_element_by_link_text('hao123').click()
        time.sleep(1)

        # 5.partial link text: 部分链接文本定位,只针对链接<a>元素
        self.driver.find_element_by_partial_link_text('地').click()

        # 6.tag name定位:一般用于定位多个元素
        elements = self.driver.find_elements_by_tag_name('a')
        for element in elements:
            print(element.text)  # 获取元素的text

        # 7.css selector：css路径定位
        self.driver.find_element_by_css_selector('#s-top-left > a:nth-child(4)').click()

        # 8.xpath:
        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[5]').click()

        # 获取元素的属性值
        element = self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[6]')
        print(element.get_attribute('href'))  # 获取元素的href属性值
        print(element.get_attribute('class'))  # 获取元素的class属性值
        print(element.text)  # 获取元素文本

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = WebElementTest()
    test.setUp()
    test.test()
    test.tearDown()
