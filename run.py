# -*- coding: utf-8 -*-

import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


username = ""
password = ""


class Moments(object):
    def __init__(self):
        # 驱动配置
        server = "http://localhost:4723/wd/hub"
        desired_caps = {
          "platformName": "Android",
          "deviceName": "MI_5s_Plus",
          "appPackage": "com.tencent.mm",
          "appActivity": ".ui.LauncherUI"
            }
        self.driver = webdriver.Remote(server, desired_capabilities=desired_caps)
        self.wait = WebDriverWait(self.driver, 30)

    def login(self):
        """
        登陆微信
        :return:
        """
        dl = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/d1w")))
        dl.click()
        # 点击用qq号登陆
        qq = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/bwm")))
        qq.click()
        # passwd = self.driver.find_elements_by_id("com.tencent.mm:id/hx")
        # 输入账号
        user_passwd = self.driver.find_elements_by_id("com.tencent.mm:id/hx")
        user = user_passwd[0]
        passwd = user_passwd[1]
        user.set_text(username)
        # 输入密码
        passwd.set_text(password)
        # 点击登陆按钮
        submit = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/bwn")))
        submit.click()
        # 不匹配通讯录
        alk = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/alk")))
        alk.click()

    def wait_data(self):
        """
        等待加载数据
        :return:
        """
        is_exist = True
        # times = 0
        try:
            while is_exist:
                # times += 1
                # print("正在加载数据%s"% times)
                is_exist = self.driver.find_element_by_id("com.tencent.mm:id/xe")
                time.sleep(0.5)
        except Exception as e:
            print("数据加载完成...")

    def enter(self):
        # 加载微信数据
        self.wait_data()
        # 点击发现选项卡
        finds = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@resource-id='com.tencent.mm:id/ayn']")))
        finds[2].click()
        # 进入朋友圈
        friend = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/a9d")))
        friend.click()

    def crawl(self):
        flick_start_x = 300
        flick_start_y = 300
        flick_distance = 700
        while True:
            self.driver.swipe(flick_start_x, flick_start_y+flick_distance, flick_start_x, flick_start_y)
            self.get_page_info()

    def get_page_info(self):
        items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@resource-id='com.tencent.mm:id/ddn']//android.widget.LinearLayout")))
        for item in items:
            try:
                # 昵称
                nickname = item.find_element_by_id("com.tencent.mm:id/apv").get_attribute("text")
                # 正文
                content = item.find_element_by_id("com.tencent.mm:id/deq").get_attribute("text")
                print("{}---{}".format(nickname, content.replace("\n", "")))
            except NoSuchElementException:
                pass

    def run(self):
        # 登陆微信
        self.login()
        # 进入朋友圈
        self.enter()
        # 抓取信息模拟上滑
        self.crawl()


if __name__ == "__main__":
    m = Moments()
    m.run()
