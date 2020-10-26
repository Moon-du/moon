# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/23 下午 04:32
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : window_test.py
# @Software : PyCharm


from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


# 内嵌网页的切换

class WindowTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'http://news.baidu.com/')

        for i in range(1, 7):
            self.driver.find_element_by_xpath(f'//*[@class="hotnews"]/ul/li[{i}]').click()

        # 窗口的切换
        # switch_to.window(参数):1.windows的标题 2.window的句柄handle（推荐）
        # 1.获取窗口的句柄
        handles = self.driver.window_handles  # 获取所有窗口的句柄
        for handle in handles:
            # 2.根据handle切换窗口
            self.driver.switch_to.window(handle)
            time.sleep(1)
            if self.driver.title == '习近平：中华民族是吓不倒、压不垮的！':  # 根据网页title判断是否停止切换
                break

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = WindowTest()
    test.setUp()
    test.test()
    test.tearDown()
