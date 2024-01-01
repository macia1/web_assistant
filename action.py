import logging
from selenium.webdriver.common.by import By


class WebAction(object):

    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.tmp = {}

    # 点击事件
    def click(self, xpath, val):
        self.webdriver.find_element(By.XPATH, xpath).click()

    def input(self, xpath, val):
        if val.startswith('#'):
            val = self.tmp[val]
            logging.log("获取临时变量:", val)
        self.webdriver.find_element(By.XPATH, xpath).send_keys(val)

    def tmp_store(self, xpath, val):
        self.tmp[val] = self.webdriver.find_element(By.XPATH, xpath).get_attribute(val)

    def screenshot(self, xpath, val):
        if val.startswith('#'):
            val = self.tmp[val]
            logging.log("获取临时变量:", val)
        self.webdriver.save_screenshot(val + ".png")

    def time_sleep(self,xpath,val):
        import time
        print(f"开始休眠'{val}'")
        time.sleep(int(val))
        print("休眠结束")
