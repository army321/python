import keyboard
import time
import pyautogui
from PIL import ImageGrab
from aip import AipOcr


# 知识点挺多
# 功能描述：获取截图热键，这边是F1开始截图，回车完成截图。
# 然后保存剪贴板的图像到当前文件夹中
# 连接百度的智能识别功能
# 识别结果返回后显示
# 字典
# 鼠标点击
class ReGt(object):
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '20232233'
        self.API_KEY = 'VEGYA43cTtvIoMEQKdNhl1CH'
        self.SECRET_KEY = '7rAVpUShsAqmtfOyFufmB4bsyEY4lTc1'
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.filePath ='D:\\python\爬虫学习\\截图识别\\'
        # self.filePath ='D:\\python\\截图识别\\test.png'   # 这个路径要根据情况调整
        # D:\python\爬虫学习\神经网络学习

    def screeshot(self):  # 热键监控
        if not keyboard.wait(hotkey='f1'):
            if not keyboard.wait(hotkey='enter'):
                print('jt')
                time.sleep(1)
                image = ImageGrab.grabclipboard()
                image.save('test.png')
    
    def reg(self, img_index):
        f = open(self.filePath+str(img_index),'rb')
        image1 = f.read()
        f.close()
        req = self.client.basicGeneral(image1)
        # req = self.client.qrcode(image1)
        # print(req)
        all_text = ''
        #for i in req['codes_result']:  # 这个是二维码提取的
        #    all_text += str(i['text']) + '\n'
        if req['words_result'] == []:
            all_text = str(1)
        else:
            for i in req['words_result']:  # 这个是文本提取的

                all_text = i['words']

        print(all_text)
        return(all_text)


if __name__ == "__main__":
    GEZI = 9
    img_hight = 60   # 4= 140; 5 =110 ;6 =95 ;7=;8=;9=60
    pyautogui.FAILSAFE = True
    if not keyboard.wait(hotkey='f2'):  # 按f2后开始触发
        start_time = time.time()  # 截图保存，每个格子保存一直图片
        for i in range(GEZI):

            for j in range(GEZI):  # 
                region = (680+(i*img_hight), 320+(j*img_hight), img_hight, img_hight)
                im = pyautogui.screenshot(region=region)  # 截屏
                savename = 'test' + str(i) + str(j) + '.png'  #保存图片
                im.save(savename)

        res = ReGt()  # 初始化百度识别软件
        dictList = dict()  # 初始化一个字典，把图片识别的结果和位置信息保存到一个字典中
        try:
        # res.screeshot()
            for i in range(GEZI):
                for j in range(GEZI):
                    savename = 'test' + str(i) + str(j) + '.png'
                    num = res.reg(savename)  # 调用图片识别，把结果返回
                    dictList[str(num)] = str(i) + str(j)
                    time.sleep(0.1)
        except:
            pass
        end_time = time.time()
        print(end_time-start_time)
        print(dictList)

        for i in range(GEZI*GEZI):  # 按顺序读取字典的数据，把位置定位出来
            weizhi = dictList[str(i+1)]
            weizhi_x = weizhi[0:1]
            weizhi_y = weizhi[1:2]
            print('x = ' + weizhi_x + ',y  = ' + weizhi_y + ' xw = ' + str (680 + int(weizhi_x) * img_hight ) + ' yw = ' +str (320 + int(weizhi_y) * img_hight))
            xw = (680 + int(weizhi_x) * img_hight + img_hight/2)
            yw = (320 + int(weizhi_y) * img_hight + img_hight/2)
            pyautogui.click(xw, yw)  # 根据位置点击

