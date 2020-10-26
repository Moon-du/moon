# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/23 下午 05:10
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : prac.py
# @Software : PyCharm

# 自动化的方式实现京东的购物流程
# 输入关键字，搜索，以销量排行
# 点击销量前5的产品，切换销量第二的产品，选择产品参数，包括数量，点击购物车，
# 完成登录流程

from selenium import webdriver
import time


class webJd():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.maximize_window()

    def test(self):
        self.driver.get('https://www.jd.com/')
        self.driver.find_element_by_id('key').send_keys('键盘')
        self.driver.find_element_by_xpath('//*[@clstag="h|keycount|head|search_a"]').click()
        time.sleep(2)

        # self.driver.find_element_by_css_selector(
        #     '#J_selector > div:nth-child(2) > div > div.sl-value > div.sl-v-list > ul > li:nth-child(1) > a').click()
        # self.driver.find_element_by_link_text('销量').click()
        # self.driver.find_element_by_css_selector(
        #     '#J_goodsList > ul > li:nth-child(2) > div > div.p-img > a').click()  # 选择商品
        #
        # handles = self.driver.window_handles
        # for handle in handles:
        #     self.driver.switch_to.window(handle)
        #     if self.driver.title == "【英特尔i7-10700K】英特尔（Intel）i7-10700K 8核16线程 盒装CPU处理器【行情 报价 价格 评测】-京东":
        #         break
        #
        # self.driver.find_element_by_xpath(
        #     '/html/body/div[6]/div/div[2]/div[5]/div[8]/div[1]/div[2]/div[1]/a/i').click()  # 选择规格
        self.driver.find_element_by_css_selector(
            '#J_filter > div.f-line.top > div.f-sort > a:nth-child(2) > span').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#J_goodsList > ul > li:nth-child(2) > div > div.p-img > a').click()
        time.sleep(2)
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == "【小米小米无线键鼠套装】小米 无线键鼠套装 简洁轻薄 全尺寸104键键盘 舒适鼠标 2.4G无线传输 电脑办公套装【行情 报价 价格 评测】-京东":
                break
        time.sleep(2)
        self.driver.find_element_by_css_selector('#choose-attr-1 > div.dd > div:nth-child(1) > a').click()
        time.sleep(3)

        for i in range(4):
            self.driver.find_element_by_xpath(
                '/html/body/div[6]/div/div[2]/div[5]/div[17]/div/div/a[2]').click()  # 选择数量

        self.driver.find_element_by_link_text('加入购物车').click()

        self.driver.find_element_by_link_text('账户登录').click()
        time.sleep(1)
        self.driver.find_element_by_id('loginname').send_keys('test')
        self.driver.find_element_by_id('nloginpwd').send_keys('123456')
        self.driver.find_element_by_id('nloginpwd').click()

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    jd = webJd()
    jd.setUp()
    jd.test()
    jd.tearDown()
