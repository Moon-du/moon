# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/28 下午 04:13
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : main_page.py
# @Software : PyCharm
import unittest
from selenium import webdriver
import time
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(unittest.TestCase):

    def __init__(self, driver, wait):
        # 定义属性
        self.driver = driver
        self.wait = wait

        # 用于调试，运行时注释掉
        # self.driver = webdriver.Chrome()
        # self.wait = WebDriverWait(self.driver, 30)

        self.title = '智慧云猎聘系统'
        self.url = 'http://192.168.3.11/cloud/#/my'

        self.user_icon_locator = (By.XPATH, '//*[@id="root"]/section/section/header/div/div[2]')
        self.logout_locator = (By.XPATH, '/html/body/div[2]/div/div/ul/li[3]')
        self.edit_pwd_locator = (By.XPATH, '/html/body/div[2]/div/div/ul/li[1]')

    def verify_url(self):
        time.sleep(1)
        self.assertEqual(self.url,self.driver.current_url)

    def logout(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.user_icon_locator))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.user_icon_locator)).perform()
        self.wait.until(expected_conditions.visibility_of_element_located(self.logout_locator))
        self.driver.find_element(*self.logout_locator).click()
