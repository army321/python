# coding=utf-8
#处理图片
#首次运行需要导入pip install Pillow和pip3 install numpy
from PIL import Image
#import cv2
import  numpy as np



infile = 'C:/python/pic/build_1.png'
outfile = 'C:/python/pic/pic1.jpg'

outfile1 = 'C:/python/pic/build_12.png'

"""按照固定尺寸处理图片"""
im = Image.open(infile)
x,y = im.size

try:
	p = Image.new('RGBA',im.size,(111,111,255))
	p.paste(im,(0,0,x,y),im)
	p.save(outfile1)
except:
		pass
#out = im.resize((240, 240),Image.ANTIALIAS)
#out.save(outfile)


		
