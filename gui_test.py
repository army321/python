import tkinter as tk

# https://www.cnblogs.com/shwee/p/9427975.html 学习资料
# pack 是自动适应，默认中间对齐
# grid(row=7, column=1)  是网格形式，方便布局

window = tk.Tk()
# 窗口名字
window.title("gui功能学习")
# 窗口大小和初始位置
window.geometry('500x300+300+300')
# 文本内容
showtext = tk.StringVar()
showtext.set("这里显示动态文本")
l1 = tk.Label(window, font=('arial', 12), bg='red', width=20, height=3, textvariable=showtext)
l1.pack()


# 输入框
t1 = tk.Entry(window, text='', width=50)
t1.pack()


def Listbox_window():
    window2 = tk.Tk()
    window2.title("列表选择")
    window2.geometry('300x200')

    var1 = tk.StringVar(window2)  # 这里设置一个值用来改变label里面的值
    var1.set('这里显示选择的值')
    l2 = tk.Label(window2, font=('arial', 12), bg='green', width=20, textvariable=var1)
    l2.grid(row=0, column=1)

    var2 = tk.StringVar(window2)
    # 为变量var2设置值
    var2.set((1, 2, 3, 4))
    # 创建Listbox
    # 将var2的值赋给Listbox
    lb = tk.Listbox(window2, listvariable=var2, height=3)
    lb.grid(row=2, column=1)

    def print_select():
        value = lb.get(lb.curselection())
        var1.set(value)

    # 按钮
    b1 = tk.Button(window2, text='显示选择值', font=('arial', 12), width=10, command=print_select)  # 指定大小和宽度
    b1.grid(row=1, column=1)


def Radiobutton_window():
    window2 = tk.Tk()
    window2.title("Radiobutton_window")
    window2.geometry('300x200')

    var1 = tk.StringVar(window2)  # 这里设置一个值用来改变label里面的值
    var1.set('这里显示选择的值')
    l2 = tk.Label(window2, font=('arial', 12), bg='green', width=20, textvariable=var1)
    l2.grid(row=0, column=1)

    #创建一个触发函数
    def print_select():
        var1.set("选中"+select.get())

    select = tk.StringVar(window2)
    rb1 = tk.Radiobutton(window2, text='op 1', variable=select, height=1, value='A', command=print_select)
    rb1.grid(row=2, column=1)
    rb2 = tk.Radiobutton(window2, text='op 2', variable=select, height=1, value='b', command=print_select)
    rb2.grid(row=3, column=1)
    rb3 = tk.Radiobutton(window2, text='op 3', variable=select, height=1, value='c', command=print_select)
    rb3.grid(row=4, column=1)


def Checkbutton_window():
    window2 = tk.Tk()
    window2.title("Checkbutton_window")
    window2.geometry('300x200')

    var1 = tk.StringVar(window2)  # 这里设置一个值用来改变label里面的值
    var1.set('这里显示选择的值')
    l2 = tk.Label(window2, font=('arial', 12), bg='green', width=20, textvariable=var1)
    l2.grid(row=0, column=1)

    # 创建一个触发函数
    def print_select():
        var1.set("选择的是："+var2.get()+var3.get())

    var2 = tk.StringVar(window2)
    var3 = tk.StringVar(window2)
    cb1 = tk.Checkbutton(window2, text='op 1', variable=var2, height=1, onvalue='1选中', offvalue='1没选中', command=print_select)
    cb1.grid(row=2, column=1)
    cb2 = tk.Checkbutton(window2, text='op 2', variable=var3, height=1, onvalue='2选中', offvalue='2没选中', command=print_select)
    cb2.grid(row=3, column=1)


def Scale_window():
    window2 = tk.Tk()
    window2.title("Scale_window")
    window2.geometry('300x200')

    var1 = tk.StringVar(window2)  # 这里设置一个值用来改变label里面的值
    var1.set('这里显示选择的值')
    l2 = tk.Label(window2, font=('arial', 12), bg='green', width=20, textvariable=var1)
    l2.pack()

    # 创建一个触发函数
    def print_select(var3):
        var1.set('当前刻度：'+var3)

    var3 = tk.StringVar(window2)
    scale1 = tk.Scale(window2, label='滚动条，试着滑动吧。', from_=0, to=10, 
    orient=tk.HORIZONTAL,  # 水平摆放
    length=200,  # 显示的宽度
    resolution=0.01,  # 最小的精度
    variable=var3,  # 传的值，不是get方法，值直接传
    showvalue=0,  # 是否在上面显示数值
    tickinterval=2,  # 刻度显示间距
    command=print_select)
    scale1.pack()


def Canvas_window():
    window2 = tk.Tk()
    window2.title("Canvas_window")
    window2.geometry('400x300')

    newCanvas = tk.Canvas(window2, bg = 'green', height=200, width=300)
    line = newCanvas.create_line(50,50,80,90)
    newCanvas.pack()


b2 = tk.Button(window, text='列表Listbox', font=('arial', 12), width=10, command=Listbox_window)  # 指定大小和宽度
b2.pack()

b3 = tk.Button(window, text='单选框Radiobutton', font=('arial', 12), width=20, command=Radiobutton_window)  # 指定大小和宽度
b3.pack()

b4 = tk.Button(window, text='复选框Checkbutton', font=('arial', 12), width=20, command=Checkbutton_window)  # 指定大小和宽度
b4.pack()

b5 = tk.Button(window, text='拉动条Scale', font=('arial', 12), width=20, command=Scale_window)  # 指定大小和宽度
b5.pack()

b6 = tk.Button(window, text='画布', font=('arial', 12), width=20, command=Canvas_window)  # 指定大小和宽度
b6.pack()


# 循环显示窗口
window.mainloop()
