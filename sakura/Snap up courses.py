# _*_ coding: UTF-8 _*_
# @Time : 2021/3/25 19:53
# @Author : moon
# @Site : www.ysbzc.com
# @File : Snap up courses.py
# @Software : PyCharm

import datetime
import time

from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # 打开网址
    page = context.new_page()
    page.goto("https://www.hzdlstudy.com/web/index")
    # 点击登陆
    page.click(":nth-match(:text(\"登录\"), 2)")
    # 选择微信登陆
    page.click("#weiXinLogin i")
    # 在15秒内扫码登陆
    time.sleep(15)
    # 进入首页
    page.goto("https://www.hzdlstudy.com/web/index")
    # 选择课程
    page.click("text=19节 Python接口自动化 视频 学习: 86 299.0 >> img")
    # 领取优惠券
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        buytime = "2021-03-26 11:00:00"
        print(buytime)
        print(now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                page.click("text=点击领取")
            except:
                time.sleep(0.005)
        print(now)
        time.sleep(0.005)


# page.click("text=点击领取")
# # ---------------------
# context.close()
# browser.close()

with sync_playwright() as playwright:
    run(playwright)
