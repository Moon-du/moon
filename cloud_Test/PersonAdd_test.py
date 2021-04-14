# _*_ coding: UTF-8 _*_
# @Time : 2020/10/27 18:49
# @Author : HU HUI
# @Site : http://www.cdtest.cn/
# @File : PersonAdd_test.py
# @Software : Pycharm
#人员管理中,人员添加功能测试
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class PersonAdd(unittest.TestCase):  # 必须继承unittest.TestCase
    # 前置条件
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,20)
        self.driver.get(r'http://192.168.3.20/cloud/#/open/login')
        time.sleep(4)
        self.driver.find_element(By.XPATH,'//*[@id="account"]/input').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="password"]/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="authCode"]/div/input').send_keys('8888')
        p = self.driver.find_element(By.CLASS_NAME,'ant-checkbox-input').is_selected()
        if p == False:
            self.driver.find_element(By.CLASS_NAME,'ant-checkbox-input').click()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/form/div[5]/div/div/span/button').click()
        time.sleep(4)

    def test(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,r'//*[@id="root"]/section/aside/div/ul/li[3]/div/span')))
        # time.sleep(5)
        self.driver.find_element(By.XPATH,r'//*[@id="root"]/section/aside/div/ul/li[3]/div/span').click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, r'/html/body/div/section/aside/div/ul/li[3]/ul/li/a')))
        self.driver.find_element(By.XPATH,r'/html/body/div/section/aside/div/ul/li[3]/ul/li/a').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, r'// *[ @ id = "root"] / section / section / main / div / div[1] / button[2]')))
        self.driver.find_element(By.XPATH, r'// *[ @ id = "root"] / section / section / main / div / div[1] / button[2]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="name"]')))
        self.driver.find_element(By.XPATH,'//*[@id="name"]').send_keys('刘德华')
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="account"]')))
        self.driver.find_element(By.XPATH, '//*[@id="account"]').send_keys('ldh')
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="pwd"]')))
        self.driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys('h123456')
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="sex"]/div/div/div')))
        self.driver.find_element(By.XPATH, '//*[@id="sex"]/div/div/div').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/ul/li[1]')))
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/ul/li[1]').click()

        self.driver.find_element(By.ID, 'cityComId').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="深圳"]')))
        self.driver.find_element(By.XPATH, '//*[text()="深圳"]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="中能深圳"]')))
        self.driver.find_element(By.XPATH, '//*[text()="中能深圳"]').click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="请选择用户职位"]')))
        self.driver.find_element(By.XPATH, '//*[text()="请选择用户职位"]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="人事经理"]')))
        self.driver.find_element(By.XPATH, '//li[text()="人事经理"]').click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="请输入工作地点"]')))
        self.driver.find_element(By.XPATH, '//*[text()="请输入工作地点"]').click()
        time.sleep(3)
        blank = self.driver.find_element(By.XPATH,'//*[text()="请输入工作地点"]')
        ActionChains(self.driver).move_to_element_with_offset(blank,0,80).click().perform()
        # ActionChains(self.driver).click().perform()

        # self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/ul/li[2]')))
        # self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[2]').click()
        # self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/ul/li[2]')))
        # self.driver.find_element(By.XPATH,'//*[@id="eef1665d-9b75-475b-f283-90359fc88178"]/ul/li[1]').click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="phone"]')))
        self.driver.find_element(By.XPATH,'//*[@id="phone"]').send_keys('13111856771')

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="请选择用户工作状态"]')))
        self.driver.find_element(By.XPATH, '//*[text()="请选择用户工作状态"]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="允许"]')))
        self.driver.find_element(By.XPATH, '//li[text()="允许"]').click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('123883277@qq.com')

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="请选择产品"]')))
        self.driver.find_element(By.XPATH, '//*[text()="请选择产品"]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="智慧社区管理系统"]')))
        self.driver.find_element(By.XPATH, '//*[text()="智慧社区管理系统"]').click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="请选择部门"]')))
        self.driver.find_element(By.XPATH, '//*[text()="请选择部门"]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="市场部"]')))
        self.driver.find_element(By.XPATH, '//*[text()="市场部"]').click()

        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]/span').click()
        time.sleep(10)


        # self.wait.until(expected_conditions.visibility_of_element_located(()))
        # self.driver.find_element(By.XPATH, '')
        # self.wait.until(expected_conditions.visibility_of_element_located(()))
        # self.driver.find_element(By.XPATH, '')













    # 后置处理：清理环境
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()
