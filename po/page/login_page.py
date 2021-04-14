# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/28 下午 02:31
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : login_page.py
# @Software : PyCharm

import unittest
from selenium import webdriver
import time
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


# 定义登录页面
class LoginPage(unittest.TestCase):
    def __init__(self, driver, wait):
        # 要求用例层传入
        self.driver = driver
        self.wait = wait

        # 用于调试，运行时注释掉
        # self.driver = webdriver.Chrome()
        # self.wait = WebDriverWait(self.driver, 30)

        # 页面属性
        self.title = '智慧云猎聘系统'
        self.url = 'http://192.168.3.11/cloud/'

        # 页面元素的定位符
        self.user_name_locator = (By.XPATH, '//*[@id="account"]/input')  # 用户名输入框
        self.user_pwd_locator = (By.XPATH, '//*[@id="password"]/input')  # 密码输入框
        self.user_authcode_locator = (By.XPATH, '//*[@id="authCode"]/div/input')  # 验证码输入框
        self.remember_pwd_locator = (
            By.XPATH, '//*[@id="root"]/div/div[1]/form/div[4]/div/div/span/label/span[1]/input')  # 记住密码
        self.login_button_locator = (By.XPATH, '//*[@id="root"]/div/div[1]/form/div[5]/div/div/span/button')  # 登录按键

    # 页面方法
    def open(self):
        """
        打开登录页面
        :return: None
        """
        self.driver.get(self.url)

    def input_user(self, user):
        """
        输入账号
        :param user: 账号
        :return: None
        """
        self.wait.until(expected_conditions.visibility_of_element_located(self.user_name_locator))
        self.driver.find_element(*self.user_name_locator).clear()
        self.driver.find_element(*self.user_name_locator).send_keys(user)

    def input_pwd(self, pwd):
        """
        输入密码
        :param pwd: 密码
        :return: None
        """
        self.wait.until(expected_conditions.visibility_of_element_located(self.user_pwd_locator))
        self.driver.find_element(*self.user_pwd_locator).clear()
        self.driver.find_element(*self.user_pwd_locator).send_keys(pwd)

    def input_authcode(self, authcode='8888'):
        """
        输入验证码
        :param authcode: 验证码，系统万能验证码是8888
        :return:None
        """
        self.wait.until(expected_conditions.visibility_of_element_located(self.user_authcode_locator))
        self.driver.find_element(*self.user_authcode_locator).clear()
        self.driver.find_element(*self.user_authcode_locator).send_keys(authcode)

    def select_remember_pwd(self):
        """
        勾选记住密码
        :return:None
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.remember_pwd_locator))
        if self.driver.find_element(self.remember_pwd_locator).is_selected():
            pass
        else:
            self.driver.find_element(self.remember_pwd_locator).click()

    def deselect_remember_pwd(self):
        """
        取消勾选记住密码
        :return:None
        """
        self.wait.until(expected_conditions.visibility_of_element_located(self.remember_pwd_locator))
        if self.driver.find_element(self.remember_pwd_locator).is_selected():
            self.driver.find_element(self.remember_pwd_locator).click()
        else:
            pass

    def click_login(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.login_button_locator))
        self.driver.find_element(*self.login_button_locator).click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,30)
    login_page = LoginPage(driver,wait)

    login_page.open()
    login_page.input_user('admin')
    login_page.input_pwd('123456')
    login_page.input_authcode('8888')
    # login_page.select_remember_pwd()
    login_page.click_login()

