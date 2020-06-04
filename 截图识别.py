import keyboard
import time
from PIL import ImageGrab
from aip import AipOcr

# 知识点挺多
# 功能描述：获取截图热键，这边是F1开始截图，回车完成截图。
# 然后保存剪贴板的图像到当前文件夹中
# 连接百度的智能识别功能
# 识别结果返回后显示
class ReGt(object):
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '20232233'
        self.API_KEY = 'VEGYA43cTtvIoMEQKdNhl1CH'
        self.SECRET_KEY = '7rAVpUShsAqmtfOyFufmB4bsyEY4lTc1'
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.filePath ='D:\\python\\截图识别\\test.png'

    def screeshot(self):
        if not keyboard.wait(hotkey='f1'):
            if not keyboard.wait(hotkey='enter'):
                print('jt')
                time.sleep(1)
                image = ImageGrab.grabclipboard()
                image.save('test.png')
    
    def reg(self):
        f = open(self.filePath,'rb')
        image1 = f.read()
        f.close()
        #req = self.client.basicGeneral(image1)
        req = self.client.qrcode(image1)
        print(req)
        all_text = ''
        for i in req['codes_result']:  # 这个是二维码提取的
            all_text += str(i['text']) + '\n'
        # for i in req['words_result']:  # 这个是文本提取的
        #    all_text += i['words'] +'\n'

        print(all_text)

if __name__ == "__main__":
    
    res = ReGt()
    res.screeshot()
    res.reg()

