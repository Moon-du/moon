import time

import selenium.common.exceptions
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from logger import Logger
from notification import Notification


class Listening:
    def __init__(self, city):
        """初始化连接属性"""
        self.city = city
        self.logging = Logger(self.city)
        self.n_appointment_notification_status = {}
        self.f_appointment_notification_status = {}
        self.appnium_server = 'http://localhost:4723/wd/hub'
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "a0af2699",
            "appPackage": "com.matthew.yuemiao",
            "appActivity": "com.matthew.yuemiao.ui.activity.HomeActivity",
        }
        self.driver = webdriver.Remote(self.appnium_server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 5)
        self.excepts = (
            selenium.common.exceptions.TimeoutException,
            selenium.common.exceptions.WebDriverException,
            selenium.common.exceptions.StaleElementReferenceException,
            selenium.common.exceptions.NoSuchElementException,
            selenium.common.exceptions.InvalidElementStateException,
        )

    def except_handling(self, vaccines, error_massage):
        """异常处理"""
        message = f"服务运行异常，尝试自动重启服务~\n异常信息：{error_massage}"
        self.logging.error(message)
        Notification(self.city).send_error_notification(vaccines, message)
        Listening(self.city).main()

    def set_address(self):
        """设置地址"""
        try:
            # 开启定位
            self.wait.until(ec.presence_of_element_located((By.ID, "com.matthew.yuemiao:id/go"))).click()
            self.wait.until(ec.presence_of_element_located(
                (By.ID, "com.lbe.security.miui:id/permission_allow_foreground_only_button"))).click()
            # 选择地址
            self.wait.until(ec.presence_of_element_located((By.ID, "com.matthew.yuemiao:id/search"))).set_text(
                self.city)
            self.wait.until(
                ec.presence_of_element_located((By.XPATH, f"//android.widget.TextView[@text='{self.city}']"))).click()
            self.wait.until(ec.presence_of_element_located((By.ID, "com.matthew.yuemiao:id/tv_confirm"))).click()
            # 进入医院列表
            self.wait.until(ec.presence_of_element_located((By.ID, "com.matthew.yuemiao:id/imageView17"))).click()
            self.wait.until(ec.presence_of_element_located(
                (By.XPATH,
                 f"//androidx.cardview.widget.CardView[4]/android.view.ViewGroup/android.widget.ImageView"))).click()
        except self.excepts as error_massage:
            self.except_handling("init", error_massage)

    def set_vaccines(self, vaccines):
        """设置疫苗"""
        vaccines_info = {
            "九价": 4,
            "四价": 3,
        }
        try:
            self.wait.until(ec.presence_of_element_located((By.ID, "com.matthew.yuemiao:id/textView56"))).click()
            self.wait.until(ec.presence_of_element_located(
                (By.XPATH,
                 f"//androidx.recyclerview.widget.RecyclerView/android.widget.TextView[{vaccines_info[vaccines]}]"))).click()
        except self.excepts as error_massage:
            self.except_handling(vaccines, error_massage)
        time.sleep(1)

    def get_department_info(self, vaccines):
        """获取医院信息，疫苗到货后发送通知"""
        notification_status_info = {
            "九价": self.n_appointment_notification_status,
            "四价": self.f_appointment_notification_status,
        }
        for i in range(1, 6):
            department_name, department_subscribe, department_lack = False, False, False
            name_xpath = f"//android.view.ViewGroup[{i}]/*[@resource-id='com.matthew.yuemiao:id/textView74']"
            subscribe_xpath = f"//android.view.ViewGroup[{i}]/*[@resource-id='com.matthew.yuemiao:id/textView70']"
            lack_xpath = f"//android.view.ViewGroup[{i}]/*[@resource-id='com.matthew.yuemiao:id/textView71']"
            try:
                department_name = self.wait.until(ec.presence_of_element_located((By.XPATH, name_xpath))).text
            except self.excepts as error_massage:
                self.except_handling(vaccines, error_massage)
            try:
                department_subscribe = self.driver.find_element(By.XPATH, subscribe_xpath).is_displayed()
            except selenium.common.exceptions.NoSuchElementException:
                pass
            except self.excepts as error_massage:
                self.except_handling(vaccines, error_massage)
            try:
                department_lack = self.driver.find_element(By.XPATH, lack_xpath).is_displayed()
            except selenium.common.exceptions.NoSuchElementException:
                pass
            except self.excepts as error_massage:
                self.except_handling(vaccines, error_massage)
            if department_subscribe or department_lack:
                self.logging.info(f"{department_name}需订阅或缺货")
                notification_status_info[vaccines][department_name] = 0
            else:
                self.logging.info(f"{department_name}可预约")
                if department_name in notification_status_info[vaccines]:
                    if notification_status_info[vaccines][department_name] == 0:
                        Notification(self.city).send_appointment_notification(vaccines, department_name)
                        notification_status_info[vaccines][department_name] = 1
                else:
                    Notification(self.city).send_appointment_notification(vaccines, department_name)
                    notification_status_info[vaccines][department_name] = 1

    def main(self):
        """开始监听"""
        self.set_address()
        rounds = 1
        while True:
            self.get_department_info("九价")
            self.set_vaccines("四价")
            self.get_department_info("四价")
            self.set_vaccines("九价")
            self.logging.info(f"--------------------------疫苗监听服务已运行{rounds}次-------------------------\n\n")
            rounds += 1


if __name__ == '__main__':
    Listening("济南市").main()
