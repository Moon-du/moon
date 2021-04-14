# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/27 上午 11:03
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : unittest_test.py
# @Software : PyCharm

# unittest测试框架
# 1.什么是测试框架
# 对用例进行组织和管理，提供方法对用例预期和实际进行检查验证，提供测试过程数据和执行结果，提供测试报告

# 2.unittest的使用
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class JDTest(unittest.TestCase):  # 必须继承unittest.TestCase
    # 前置条件
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 生成WebDriverWait对象
        # WebDriverWait(driver, timeout):timeout-最大等待时间，默认以0.5秒的速度扫描元素
        self.wait = WebDriverWait(self.driver, 30)

    # 测试步骤以及预期结果验证
    # 测试方法必须以test开头
    def test(self):
        self.driver.get(r'https://www.jd.com/')

        # 等待搜索输入框
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, 'key')))  # 注意多打一层圆括号
        # 搜索框输入
        self.driver.find_element(By.ID, 'key').send_keys('mate40')
        # self.driver.find_element_by_id('key')

        self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'button')))
        # 点击搜索
        self.driver.find_element(By.CLASS_NAME, 'button').click()

        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="J_filter"]/div[1]/div[1]/a[2]')))
        # 点击销量排行
        self.driver.find_element(By.XPATH, '//*[@id="J_filter"]/div[1]/div[1]/a[2]').click()

        # 验证销量第一的价格是否是4488.00
        # self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/strong/i')))
        time.sleep(1)
        price = self.driver.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/strong/i').text
        # assertEqual(预期值,实际值)：当预期值和实际值不符合会抛出异常，将用例标记为执行失败
        self.assertEqual('0000.00', price)

    # 后置处理：清理环境
    def tearDown(self) -> None:
        self.driver.quit()
