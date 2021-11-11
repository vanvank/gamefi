# coding=utf-8
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(r'C:\Users\wan\Desktop\chromedriver.exe',chrome_options=option)
#driver.maximize_window()  # 全屏
driver.get(r'https://web.yohero.fi')

# 分辨率 640*480
driver.set_window_size(640, 480)

