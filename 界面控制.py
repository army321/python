import pyautogui
import time

# http://www.4399.com/flash/154247_3.htm 游戏地址
# 用截图控制鼠标点击
pyautogui.FAILSAFE = True
time.sleep(3)

while True:
    region = (644, 478, 320, 20)
    im = pyautogui.screenshot(region=region)
    im.save('test.png')
    for i in range(40, 300, 80):
        px = im.getpixel((i, 10))
        print(px)

        if px[0] == 1:
            pyautogui.click(region[0] + i, region[1] + 10)
