# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/23 上午 10:08
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : select_test.py
# @Software : PyCharm


# 下拉菜单

# 下拉菜单主要有js做的，还有用<select>标签定义的
# 前者模拟用户操作逻辑：先点击下拉菜单展开选项，再对选项进行定位和点击
# <select>定义的下拉菜单也可以这么操作，也有更好的操作方式
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class SelectTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'D:\pyworkspace\t63\selenium3\example.html')

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="Selector"]/option[2]').click()
        time.sleep(1)

        # 1.找到下拉菜单元素
        element = self.driver.find_element_by_id('Selector')
        # 2.用元素构建一个Select类的对象
        select = Select(element)

        # 3.调用Select类的方法操作下拉菜单
        # 3.1根据选项index选择:从0开始
        select.select_by_index(2)
        time.sleep(1)

        # 3.2 根据选项的text选择
        select.select_by_visible_text('桔子')
        time.sleep(1)

        # 3.3 根据option的value属性值选择
        select.select_by_value('grape')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = SelectTest()
    test.setUp()
    test.test()
    test.tearDown()
