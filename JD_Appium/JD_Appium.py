from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import *

class Action():
    def __init__(self):
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': 'com.jingdong.app.mall',
            'appActivity': 'main.MainActivity',
            'noReset': True,
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.x = self.driver.get_window_size()['width'] # 获取屏幕宽度
        self.y = self.driver.get_window_size()['height'] # 获取屏幕高度
        # 向上滑的起点和终点
        self.x1 = int(self.x * 0.5)
        self.y1 = int(self.y * 0.75)
        self.y2 = int(self.y * 0.25)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
    
    def comments(self):
        # 点击进入搜索页面(实在找不到它的id，xpath也复杂，只能用坐标了)
        self.driver.tap([(209,268),(1225,366)],500)
        # 输入搜索文本
        search = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.search.feature:id/add')))
        search.send_keys(KEYWORD)
        # 点击搜索按钮
        button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/a9b')))
        button.click()
    
    def scroll(self):
        # 模拟拖动
        while True:
            self.driver.swipe(self.x1, self.y1, self.x1, self.y2)
            sleep(SCROLL_SLEEP_TIME)
    
    def main(self):
        self.comments()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()

