# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/23 下午 03:23
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : frame_test.py
# @Software : PyCharm


from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


# 内嵌网页的切换

class FrameTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'https://music.163.com/#/discover/toplist?id=3778678')

        # iframe和frame都是嵌套网页的标签
        # 打开网页操作焦点在根html，操作内嵌页面的元素需要手动切换焦点
        # driver.switch_to.frame(参数):1.index:iframe或frame的index；2.name或id属性值；3.iframe或frame元素
        self.driver.switch_to.frame('contentFrame')
        # self.driver.switch_to_frame()#过时代码，将来某个版本会不支持

        # self.driver.find_element_by_xpath('//*[@id="toplist"]/div[2]/div/div[1]/div/div[2]/div/div[3]/a[1]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="song-list-pre-cache"]/div/div[1]/table/tbody/tr[3]/td[2]/div/div/span').click()
        # 某些纯数字或者字母数字混合id有可能会自动变化，这种id不能用
        time.sleep(60)

        # 多层嵌套切换的逻辑
        # switch_to.frame()：只能向下一层切换
        # self.driver.switch_to.default_content()  # 切换到页面的根html
        # self.driver.switch_to.parent_frame()  # 切换到上一层iframe或frame

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = FrameTest()
    test.setUp()
    test.test()
    test.tearDown()
