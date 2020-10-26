# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm


# 文件上传
# 1.上传按键是<input>,直接对<input>sendkeys，文件的路径
# 2.上传按键不是<input>，借助第三方工具AutoIt来操作操作系统文件浏览器

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class UploadTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'D:\pyworkspace\t63\selenium3\example.html')

        #文件上传
        self.driver.find_element_by_name('attach[]').send_keys(r'C:\Users\LiJie\Pictures\软件测试进入渠道.png')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = UploadTest()
    test.setUp()
    test.test()
    test.tearDown()
