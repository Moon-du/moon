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
        # 打开浏览器
        self.driver = webdriver.Chrome()

        # 最大化浏览器
        self.driver.maximize_window()

    # 测试步骤（包含预期结果）
    def test(self):
        # 打开网页
        self.driver.get('http://www.baidu.com')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        time.sleep(1)
        # # 后退
        # self.driver.back()
        # time.sleep(1)
        #
        # # 前进
        # self.driver.forward()
        # time.sleep(1)
        #
        # # 刷新页面
        # self.driver.refresh()

        # 获取网页标题:主要判断是否打开正确的网页
        title = self.driver.title
        print(title)

        # 获取网页url：主要判断是否打开正确的网页
        # url：统一资源定位符，协议://ip或域名:端口号/资源路径
        url = self.driver.current_url
        print(url)

        time.sleep(3)

    # 后置处理：关闭浏览器，清理资源
    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

        # 关闭当前窗口:当浏览器只有一个窗口，关闭浏览器
        # self.driver.close()


if __name__ == '__main__':
    test = BrowserTest()
    test.setUp()
    test.test()
    test.tearDown()
