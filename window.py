# coding=utf-8
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(r'C:\Users\wan\Desktop\chromedriver.exe',chrome_options=option)
#driver.maximize_window()  # 全屏
driver.get(r'https://web.yohero.fi')
time.sleep(1)
#print(driver.get_window_size())
#driver.set_window_size(1280, 800)  # 分辨率 1280*800
#time.sleep(1)
#print(driver.get_window_size())

#driver.set_window_size(1024, 768)  # 分辨率 1024*768
driver.set_window_size(640, 480)
time.sleep(1)
print(driver.get_window_size())
print(driver.title)
