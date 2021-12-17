# -*- coding: utf-8 -*-
import cv2
import pyautogui
import numpy as np
from PIL import ImageGrab
import time
import datetime
import configparser


def search_pic_click(pic_path):
    global threshold
    #print(threshold)
    #截屏，同时提前准备一张屏幕上会出现的小图bd.png
    im=ImageGrab.grab()
    im.save('screen.png', 'png')
    #加载原始RGB图像
    img_rgb= cv2.imread("screen.png")
    #img_rgb = cv2.imread(r'./screen.png')
    #创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray=cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #加载将要搜索的图像模板
    template= cv2.imread(pic_path, 0)
    #使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    #设定阈值,0.7应该可以
    #threshold = 0.85 #res大于99.9%#
    loc = np.where(res >= threshold)
    #得到原图像中的坐标
    for pt in zip(*loc[::-1]):
        print(pt[0], pt[1])
        pyautogui.click(pt[0],pt[1])
        break
    #cv2.destroyAllWindows()


def task_pvp():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " ---- pvp")
    search_pic_click(pvp_button)
    time.sleep(0.5)
    search_pic_click(ok_button)
    time.sleep(0.5)


def task_pve():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " ---- pve" )
    search_pic_click(ok_button)
    time.sleep(0.5)
    search_pic_click(challeng_button)
    time.sleep(0.5)


# task_tpye=1，只跑pvp； task_type=2，只跑pve； task_type=3，两种任务都跑
# last_time 是脚本运行的时间， 默认是半个小时
def run(task_type, last_time=1800):
    now=time.time()
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    while True:
        if task_type == 1:
            task_pvp()
        if task_type == 2:
            task_pve()
        if task_type == 3:
            task_pve()
            task_pvp()
        time.sleep(2)
        if time.time() - now > last_time:
            print('已过%s秒' % last_time)
            print(start_time)
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            #cv2.destroyAllWindows()
            break


if __name__=="__main__":
    cf = configparser.ConfigParser()
    cf.read("yohero.conf")
    duration = int(cf.get("Common", "duration"))
    task_type = int(cf.get("Common", "task_type"))
    try:
        threshold = float(cf.get("Common", "threshold"))
        print(threshold)
        #exit(0)
        #threshold = float(input("请输入图片匹配度（0-1之间的数），默认0.85:"))
        if not 0 < threshold < 1:
            threshold = 0.85
        #isinstance(float, float(threshold))
    except Exception as e:
        print("threshold输入错误，默认设置为0.85")
        threshold = 0.85

    # elif 0 < threshold < 1:
    #     threshold = float(threshold)
    # else:
    #     print("匹配度请设置为0到1之间的小数")
    pyautogui.FAILSAFE = False
    pvp_button = r'.\pic\pvp.png'
    ok_button = r'.\pic\ok_button.png'
    challeng_button = r'.\pic\challeng.png'
    print('1. 游戏语言调整为英文，\n2. 如果打PVE：调整好你的游戏需要运行的关卡\n3. 如果打PVP：无需选择关卡')
    #input('按回车脚本开始运行，默认运行30分钟')
    run(task_type, duration)
