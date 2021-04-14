# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/27 上午 09:52
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : wait_test.py
# @Software : PyCharm

# 自动化测试当中的等待
# 1.为什么需要等待
# 同步页面显示/加载和操作，保证在操作元素之前元素必须显示或者加载成功

# 2.哪些时候需要等待
# 页面加载，页面刷新，页面跳转，JS菜单弹出，AJAX菜单

# 3.等待有几种方式
# 强制等待，隐式等待，显式等待（推荐）

# 3.1 强制等待time.sleep
# 等待时间不灵活，一般用于调试和演示自动化用例


# 3.2隐式等待
# 用例中只用设置一次，等待时间不是定死是最大的等待时长
# 不能等待某个元素，等待的页面的所有元素加载完成，当页面局部刷新不能重新等待，菜单弹出不会等待


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class ImplicitlyWaitTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 隐式等待
        self.driver.implicitly_wait(30)  # 30:等待的最大时长

    def test(self):
        self.driver.get(r'https://www.jd.com/')

        # 搜索框输入
        self.driver.find_element(By.ID, 'key').send_keys('mate40')
        # self.driver.find_element_by_id('key')

        # 点击搜索
        self.driver.find_element(By.CLASS_NAME, 'button').click()

        # 点击销量排行
        self.driver.find_element(By.XPATH, '//*[@id="J_filter"]/div[1]/div[1]/a[2]').click()

    def tearDown(self):
        self.driver.quit()


# 3.3显式等待
# 时间灵活，有弹性，等待具体某一个元素，会以默认0.5秒的速度扫描等待条件是否成立
# 写起来稍微复杂，有时候不好设置等待条件需要和强制等待混合使用

# 导入三个包：
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class WebDriverWaitTest():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 生成WebDriverWait对象
        # WebDriverWait(driver, timeout):timeout-最大等待时间，默认以0.5秒的速度扫描元素
        self.wait = WebDriverWait(self.driver, 30)

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

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = WebDriverWaitTest()
    test.setUp()
    test.test()
    test.tearDown()
