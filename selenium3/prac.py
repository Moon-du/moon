# _*_ coding: UTF-8 _*_
# @Time : 2020/10/26 14:08
# @Author : moon
# @Site : www.ysbzc.com
# @File : page_test.py
# @Software : PyCharm

# 自动化的方式实现京东的购物流程
# 输入关键字，搜索，以销量排行
# 点击销量前5的产品，切换销量第二的产品，选择产品参数，包括数量，点击购物车，
# 完成登录流程


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


# 内嵌网页的切换

class JDTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get(r'https://www.jd.com/')

        # 搜索框输入
        self.driver.find_element(By.ID, 'key').send_keys('mate40')
        # self.driver.find_element_by_id('key')

        # 点击搜索
        self.driver.find_element(By.CLASS_NAME, 'button').click()

        # 点击销量排行
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="J_filter"]/div[1]/div[1]/a[2]').click()

        # 打开销量前5的产品
        time.sleep(1)
        for i in range(1, 6):
            self.driver.find_element(By.XPATH, f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[1]').click()
        time.sleep(2)

        # 窗口切换到销量第二
        handles = self.driver.window_handles
        # for handle in handles:
        #     self.driver.switch_to.window(handle)
        #     if self.driver.current_url=='https://item.jd.com/100012014948.html':
        #         break
        # time.sleep(2)
        self.driver.switch_to.window(handles[-2])
        time.sleep(2)

        # 选择颜色
        self.driver.find_element(By.XPATH, '//*[@id="choose-attr-1"]/div[2]/div[4]').click()
        time.sleep(2)

        # 点击数量4下
        for i in range(4):
            self.driver.find_element(By.CLASS_NAME, 'btn-add').click()
        time.sleep(2)

        # 点击支付定金
        self.driver.find_element(By.ID, 'btn-reservation').click()
        time.sleep(2)

        # 点击账号登录
        self.driver.find_element(By.LINK_TEXT, '账户登录').click()

        # 输入账号和密码，点击登录
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'loginname').send_keys('test')
        self.driver.find_element(By.ID, 'nloginpwd').send_keys('test')
        self.driver.find_element(By.ID, 'loginsubmit').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = JDTest()
    test.setUp()
    test.test()
    test.tearDown()
