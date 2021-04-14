# _*_ coding: UTF-8 _*_
# @Time : 2020/10/28 10:53
# @Author : moon
# @Site : www.ysbzc.com
# @File : dept_test.py
# @Software : PyCharm

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class dept_Test(unittest.TestCase):  # 必须继承unittest.TestCase
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
        self.driver.get(r'http://192.168.3.11/cloud/#/open/login')

        # 登陆
        self.driver.find_element(By.XPATH, '//*[@id="account"]/input').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="password"]/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="authCode"]/div/input').send_keys('8888')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div[1]/form/div[4]/div/div/span/label/span[1]/input').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/form/div[5]/div/div/span/button').click()

        # 选择系统管理
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/section/aside/div/ul/li[4]/div')))
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/aside/div/ul/li[4]/div').click()

        # 选择部门列表
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '/html/body/div/section/aside/div/ul/li[4]/ul/li[3]/a')))
        self.driver.find_element(By.XPATH, '/html/body/div/section/aside/div/ul/li[4]/ul/li[3]/a').click()

        # 添加部门
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '/html/body/div/section/section/main/div/div[1]/button[1]')))
        self.driver.find_element(By.XPATH, '/html/body/div/section/section/main/div/div[1]/button[1]').click()

        # 部门名称
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div['
                                 '2]/div/span/input').send_keys('非正常人类研究院')
        # 绑定产品
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div['
                                           '2]/div/div[2]/div/span/div/div/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/ul/li[1]').click()
        # 所属地区
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div['
                                 '2]/div/span/div/div/div/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[8]').click()

        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # 编辑部门
        self.driver.refresh()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/section/section/main/div/div['
                                 '2]/div/div/div/div/div/div/div/table/tbody/tr[3]/td['
                                 '1]/span/label/span/input').click()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/section/section/main/div/div[1]/button[2]').click()
        # 编辑部门名称
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div['
                                           '1]/div/div[2]/div/span/input').clear()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div['
                                           '1]/div/div[2]/div/span/input').send_keys('UFO研究中心')
        # 编辑绑定产品
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div['
                                           '2]/div/div[2]/div/span/div/div/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/ul/li[4]').click()

        # 编辑部门地区
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div['
                                 '2]/div/span/div/div/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[7]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # 删除部门
        self.driver.refresh()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/section/section/main/div/div['
                                 '2]/div/div/div/div/div/div/div/table/tbody/tr[3]/td['
                                 '1]/span/label/span/input').click()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/section/section/main/div/div[1]/button[3]').click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')))
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()

    # 后置处理：清理环境
    def tearDown(self) -> None:
        self.driver.quit()
