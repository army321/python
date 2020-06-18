import keyboard
import time
import pyautogui
from PIL import ImageGrab
from aip import AipOcr  # 百度aip
from PIL import Image  # 图片处理
from PIL import ImageDraw
from PIL import ImageFont


# 知识点挺多
# 功能描述：获取截图热键，这边是F1开始截图，回车完成截图。
# 然后保存剪贴板的图像到当前文件夹中
# 连接百度的智能识别功能
# 识别结果返回后显示
# 字典
# 鼠标点击
# 修改为只识别一张图片
# 增加文本中绘制分隔符

class ReGt(object):  # 百度请求
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '20232233'
        self.API_KEY = 'VEGYA43cTtvIoMEQKdNhl1CH'
        self.SECRET_KEY = '7rAVpUShsAqmtfOyFufmB4bsyEY4lTc1'
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.filePath ='D:\\python\\注意力挑战截图识别\\'
        # self.filePath ='D:\\python\爬虫学习\\截图识别\\'
        # self.filePath ='D:\\python\\截图识别\\test.png'   # 这个路径要根据情况调整
        # D:\python\爬虫学习\神经网络学习

    def screeshot(self):  # 热键监控，屏幕截图保存，读取剪贴板中的图片数据
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
        all_text = []
        #for i in req['codes_result']:  # 这个是二维码提取的
        #    all_text += str(i['text']) + '\n'
        if req['words_result'] == []:
            all_text = str(1)
        else:
            for i in req['words_result']:  # 这个是文本提取的

                all_text.append(i['words']) 

        print(all_text)
        return(all_text)

def save_image(CUT_NUM,IMG_SIZE,GRID_SIZE,SPLIT_CHAR): # 截图保存，整个区域保存一张图片，并添加分隔字符
    start_time = time.time()  #记录执行的时间
    for i in range(CUT_NUM):
        for j in range(CUT_NUM):  # 
            region = (680+(i*IMG_SIZE), 320+(j*IMG_SIZE), IMG_SIZE, IMG_SIZE)
            img = pyautogui.screenshot(region=region)  # 截屏

            img = img.convert('RGBA') 
            W, H = img.size 
            white_pixel = (255, 255, 255, 255)  
            for h in range(W):  # 循环图片的每个像素点
                for l in range(H):  
                    if h%GRID_SIZE >10 and h%GRID_SIZE <GRID_SIZE-10 and l%GRID_SIZE >9 and l%GRID_SIZE <GRID_SIZE-9:
                        if img.getpixel((h,l)) != white_pixel:  
                            img.putpixel((h,l),(0,0,0,120))  # 把颜色改成黑色
                            # img.putpixel((h,l),(0,0,0,0))  # 透明
                    else:
                        img.putpixel((h,l),(0,0,0,120))  # 把颜色改成黑色
            # img.save(out+".png")
            # 添加分隔字符
            draw = ImageDraw.Draw(img)
            font1 = ImageFont.truetype('arial', int(GRID_SIZE/2))
            for ai in range(GRID_NUM-1):
                for aj in range(GRID_NUM):
                    lacation = (GRID_SIZE-5+ai*GRID_SIZE,9+aj*GRID_SIZE)
                    draw.text(lacation,SPLIT_CHAR,'white',font=font1)

            savename = 'test' + str(i) + str(j) + '.png'  #保存图片
            img.save(savename)
    end_time = time.time()
    print("图片保存时间：" + str(end_time-start_time))

def save_dictList(result_data,SPLIT_CHAR):  # 把识别的内容保存到字典中
    start_time = time.time()  #记录执行的时间
    index_x = 0
    dictList = dict()
    for num_hang in result_data:
    # asplit =num.split("A")
        #print(num_hang)
        asplit =num_hang.split(SPLIT_CHAR)
        #print(asplit)
        #print('hanghang  '+str(index_x))
        index_x += 1
        index_y = 0
        for num_lie in asplit:
            #print(num_lie)
            #print('lielie  '+str(index_y))
            index_y += 1
            dictList[str(num_lie)] = str(index_x) + str(index_y)
    print("dictList大小是：："+ str(len(dictList)))
    print(dictList)
    end_time = time.time()
    print("创建字典时间：" + str(end_time-start_time))
    return dictList


def action_click(dictList,GRID_NUM,GRID_SIZE):  # 根据字典依次点击
    start_time = time.time()  #记录执行的时间
    for i in range(GRID_NUM*GRID_NUM):  # 按顺序读取字典的数据，把位置定位出来
        #dictList = dictList
        weizhi = dictList[str(i+1)]
        weizhi_x = int(weizhi[0:1])-1
        weizhi_y = int(weizhi[1:2])-1
        # print('x = ' + str(weizhi_x) + ',y  = ' + str(weizhi_y) + ' xw = ' + str (680 + int(weizhi_x) * GRID_SIZE ) + ' yw = ' +str (320 + int(weizhi_y) * GRID_SIZE))
        xw = (320 + int(weizhi_x) * GRID_SIZE + GRID_SIZE/2)
        yw = (680 + int(weizhi_y) * GRID_SIZE + GRID_SIZE/2)
        # print('x = ' + str(weizhi_x) + ',y  = ' + str(weizhi_y) + ' xw = ' + str(xw) + ' yw = ' +str(yw))
        pyautogui.click(yw,xw)  # 根据位置点击
    
    end_time = time.time()
    print("点击时间：" + str(end_time-start_time))

if __name__ == "__main__":
    CUT_NUM = 1  # 图片要报错几张
    IMG_SIZE = 560  #图片大小
    GRID_NUM = 7  # 对应的模式 
    GRID_SIZE = int(IMG_SIZE/GRID_NUM)  #格子大小 3=185;4= 140; 5 =110 ;6 =90 ;7=80;8=70;9=60  
    SPLIT_CHAR ='F'  # 分隔字符，可以多试试，尽量不要与数字类似，避免判断错误

    pyautogui.FAILSAFE = True
    if not keyboard.wait(hotkey='f2'):  # 按f2后开始触发
        save_image(CUT_NUM,IMG_SIZE,GRID_SIZE,SPLIT_CHAR)
        res = ReGt()
        num = res.reg('test00.png')
        # print(num)
        dictList = save_dictList(num,SPLIT_CHAR)
        action_click(dictList,GRID_NUM,GRID_SIZE)

