from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.hzdlstudy.com/web/index
    page.goto("https://www.hzdlstudy.com/web/index")

    # Click :nth-match(:text("登录"), 2)
    page.click(":nth-match(:text(\"登录\"), 2)")
    # assert page.url == "https://www.hzdlstudy.com/web/user/login"

    # Click #weiXinLogin i
    page.click("#weiXinLogin i")
    # assert page.url == "https://open.weixin.qq.com/connect/qrconnect?appid=wx1e76a0d854e22ba3&redirect_uri=https%3A%2F%2Fwww.hzdlstudy.com%2Fweb%2FthirdLogin%2FweiXinLoginCallback&response_type=code&scope=snsapi_login&state=STATE#wechat_redirect"

    # Go to https://www.hzdlstudy.com/web/index
    page.goto("https://www.hzdlstudy.com/web/index")

    # Click text=19节 Python接口自动化 视频 学习: 86 299.0 >> img
    page.click("text=19节 Python接口自动化 视频 学习: 86 299.0 >> img")
    # assert page.url == "https://www.hzdlstudy.com/web/course/courseInfo?courseId=67534"

    # Click text=点击领取
    page.click("text=点击领取")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)