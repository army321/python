import tkinter as tk
import re
import requests
import webbrowser

url = 'http://www.qmaile.com/'

resp = requests.get(url)
resp.encoding = resp.apparent_encoding
response = resp.text

res = re.compile('<option value="(.*?)" selected')
reg = re.findall(res, response)
print(reg)

one1 = reg[0]
one2 = reg[1]
one3 = reg[2]
one4 = reg[3]
one5 = reg[4]

root = tk.Tk()
root.title("vip看视频")
# 窗口大小和初始位置
root.geometry('500x400+300+300')
l1 = tk.Label(root, text='播放链接', font=('arial', 12))
l1.grid()
l2 = tk.Label(root, text='播放链接', font=('arial', 12))
l2.grid(row=6, column=0)
t1 = tk.Entry(root, text='', width=50)
t1.grid(row=6, column=1)


def del_text():
    t1.delete(0, 'end')


def bf():
    webbrowser.open(var.get()+t1.get())


# 单选
var = tk.StringVar()
r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one1)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=one2)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=one3)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='播放接口4', variable=var, value=one4)
r4.grid(row=3, column=1)
# r5 = tk.Radiobutton(root,text = '播放接口5',variable = var ,value = one5)
# r5.grid(row =4,column = 1)

b1 = tk.Button(root, text='播放', font=('arial', 12), width=10, command=bf)
b1.grid(row=7, column=1)
b2 = tk.Button(root, text='清除', font=('arial', 12), width=10, command=del_text)
b2.grid(row=8, column=1)

# 循环显示窗口
root.mainloop()
