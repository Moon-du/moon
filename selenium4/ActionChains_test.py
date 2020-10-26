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
from selenium.webdriver.common.action_chains import ActionChains


class ActionsChainsTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'https://map.baidu.com/@11585280.82,3555907.48,12z')
        time.sleep(2)

        # 单击鼠标右键
        # context_click(element=None):element被右键单击的元素，默认值为None，不给元素会在鼠标当前位置单击右键
        # 整个页面显示区域的坐标原点是左上角(0,0)，向右是x轴的正方向，向下是y轴的正方向
        # selenium的鼠标位置不由电脑鼠标控制，由语句控制，初始位置在原点
        ActionChains(self.driver).context_click().perform()
        time.sleep(1)

        # 双击鼠标左键
        # double_click(element=None):element被双击的元素，默认值为None，不给元素会在鼠标当前位置双击左键
        ActionChains(self.driver).double_click().perform()
        time.sleep(1)

        # 点击鼠标不放
        # click_and_hold(element=None):element被点击不放的元素，默认值为None，不给元素会在鼠标当前位置点击左键不放
        ActionChains(self.driver).click_and_hold().perform()
        time.sleep(1)

        # 移动鼠标
        # move_by_offset(xoffset,yoffset):offset,yoffset偏移量，移动距离
        # 移动鼠标，坐标不可以超出边界
        # release():释放鼠标
        ActionChains(self.driver).move_by_offset(200, 200).release().perform()
        # 移动鼠标到某个元素上方
        # ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(1)

        # 动作链条
        ActionChains(self.driver).click_and_hold().move_by_offset(-200, -200).release().perform()
        time.sleep(1)

        # 拖拽鼠标
        ActionChains(self.driver).drag_and_drop_by_offset(None, 400, 400).perform()
        time.sleep(3)

        #按住键盘的某个键不放
        # ActionChains(self.driver).key_down(key).perform()
        #松开键盘的按键
        # ActionChains(self.driver).key_up(key).perform()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = ActionsChainsTest()
    test.setUp()
    test.test()
    test.tearDown()
