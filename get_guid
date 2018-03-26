
#获得guid对应的文件名 for vr人生
import requests
import sys
import os
import os.path
import urllib.request

#下载图片
def down_pic(url,_name):
	path1 = 'C:/python/pic/'
	houzhui = '.png'
	path = path1+_name+houzhui

	web_url =  	'http://cs.101.com/v0.1/static/'
	pic_url = web_url+url[12:]
	print(pic_url)
  #  print('下载图片： '+_name)
	response = urllib.request.urlopen(pic_url)
	pic = response.read()
	with open(path, 'wb') as f:
		f.write(pic)

#存放要查找的ID文件 aff97325-b552-4b52-8d91-934a7eafb5ef.assetbundle
#rootdir = "C:/python/VRguid" 


#用于拼装网址 url = uri0+i+uri1
uri0= "http://esp-lifecycle.web.sdp.101.com/v0.6/assets/"
uri1= '?words&include=LC,TI,CG,CR&limit=(0,999)&coverage=Org/nd/'

#存入查找的ID文件的文件名

names = os.listdir(rootdir)
i=0  #用于统计文件数量是否正确，不会写到文件里  
train_val = open('C:/python/guid.txt','w')  #查找文件夹的结果存到txt文件中
for name in names:  
    index = name.rfind('.')  
    name = name[:index]  
    train_val.write(name+'\n')  
    i=i+1  
print ('查找文件数量：'+str(i)+'\n 开始搜索网页') 

train_val.close();

#查找的内容文本
f1 = open('C:/python/guid.txt','r')

#查找结果写入的文本
f = open('C:/python/test.txt','a')
f2 = open('C:/python/t1.txt','a')

guid_list = f1.readlines()

f1.close()

#拼装网址并请求网页内容，然后写入到指定文本
for i in guid_list :
	try:
		url = uri0+i+uri1
		#print(url)
	
		net =  requests.get(url)
		f.write(net.text+'\n'*3)
		
		#找出返回的json文件里面的id和名字
		id = net.json()['identifier']
		name= net.json()['title']
	
		pic_id = net.json()['preview']['cover']
		down_pic(pic_id,name)
	
		f2.write(name+' ' + id+'\n')
	except :
		pass

f.close()
f2.close()

print("查找完成，请打开 C:/python/t1.txt  查看内容...")

