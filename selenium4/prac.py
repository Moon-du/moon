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


# 在百度地图，搜索一个地名，选择，设置终点和起点，选择出行方式-驾车，增加途经点，拖拽途经点，最后截图保存
class mapTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'https://map.baidu.com/@11585280.82,3555907.48,12z')
        time.sleep(2)
        self.driver.find_element(By.ID, 'sole-input').send_keys('熊猫基地')
        self.driver.find_element(By.ID, 'search-button').click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, '成都大熊猫繁育研究基地').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="route-go"]/span[2]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[1]/input').send_keys(
            '丰德国际广场')
        self.driver.find_element(By.ID, 'search-button').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="route-searchbox-content"]/div[1]/div[1]/div[2]/span').click()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(800, 750).perform()
        time.sleep(2)
        ActionChains(self.driver).context_click().perform()
        time.sleep(1)
        self.driver.find_element(By.ID, 'cmitem_pass').click()
        time.sleep(2)
        t = self.driver.find_element(By.XPATH, '//*[@id="platform"]/div[2]/div[2]/div[2]')
        ActionChains(self.driver).move_to_element(t).perform()
        ActionChains(self.driver).click_and_hold().perform()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(80, 70).release().perform()
        time.sleep(2)
        self.driver.get_screenshot_as_file(r'C:\Users\Aurora\Desktop\moon\selenium4\1.png')

    def tearDown(self):
        self.driver.quit()


# 完成一个苏宁易购的购物流程，验证商品单价和总价
class SuTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'https://www.suning.com/')

        # 电脑办公
        time.sleep(1)
        t = self.driver.find_element(By.LINK_TEXT, '电脑办公')
        ActionChains(self.driver).move_to_element(t).perform()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, '机械键盘').click()
        time.sleep(3)

        # 切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        time.sleep(3)

        # 点击销量排行
        self.driver.find_element(By.NAME, 'ssdsn_search_sort_sales').click()
        time.sleep(2)

        # 打开销量前5的产品
        for i in range(1, 6):
            self.driver.find_element(By.XPATH, f'/html/body/div[10]/div/ul/li[{i}]/div/div/div[1]/div/a/i/img').click()
        time.sleep(2)

        # 窗口切换到销量第二
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-2])
        time.sleep(3)

        # 选择颜色
        self.driver.find_element(By.XPATH, '//*[@id="colorItemList"]/dd/ul/li[1]/a/span').click()
        time.sleep(3)

        # 点击数量4下
        for i in range(4):
            self.driver.find_element(By.NAME, 'item_10396996684_gmq_fuhaojia').click()
        time.sleep(2)

        # 点击购买
        self.driver.find_element(By.ID, 'buyNowAddCart').click()
        time.sleep(2)

        # 切换嵌套
        self.driver.switch_to.frame('iframeLogin')

        # 输入账号和密码，点击登录
        time.sleep(1)
        self.driver.find_element(By.ID, 'userName').send_keys('test')
        self.driver.find_element(By.ID, 'password').send_keys('test')
        time.sleep(2)
        h = self.driver.find_element(By.XPATH, '//*[@id="siller1_dt_child_content_containor"]/div[3]')
        ActionChains(self.driver).move_to_element(h).perform()
        ActionChains(self.driver).click_and_hold().perform()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(330, 0).release().perform()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, '登 录').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # test = mapTest()
    # test.setUp()
    # test.test()
    # test.tearDown()
    test = SuTest()
    test.setUp()
    test.test()
    test.tearDown()
