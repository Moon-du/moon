# _*_ coding: UTF-8 _*_
# @Time : 2020/10/27 18:17
# @Author : moon
# @Site : www.ysbzc.com
# @File : system_test.py
# @Software : PyCharm

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class city_Test(unittest.TestCase):  # 必须继承unittest.TestCase
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

        # 选择城市列表
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="sys$Menu"]/li[1]')))
        self.driver.find_element(By.XPATH, '//*[@id="sys$Menu"]/li[1]').click()

        # 添加城市
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '/html/body/div/section/section/main/div/div[1]/button[1]')))
        self.driver.find_element(By.XPATH, '/html/body/div/section/section/main/div/div[1]/button[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="city"]').send_keys('苏州')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # 编辑城市
        self.driver.refresh()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH,
             '//*[@id="root"]/section/section/main/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td['
             '1]/span/label/span')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/section/section/main/div/div['
                                 '2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td[1]/span/label/span').click()

        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/section/section/main/div/div[1]/button[2]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="city"]').clear()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="city"]').send_keys('扬州')
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # 删除城市
        self.driver.refresh()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/section/section/main/div/div[1]/button[3]/span')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/section/section/main/div/div['
                                 '2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td[1]/span/label/span').click()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/section/section/main/div/div[1]/button[3]').click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')))
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()

    # 后置处理：清理环境
    def tearDown(self) -> None:
        self.driver.quit()
