#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 第一行
        self.Label_f = Label(self)
        self.Label_f["text"] = "apk地址："
        self.Label_f.grid(row=0, column=0, sticky=E)

        self.input_f = Entry(self)
        self.input_f.grid(row=0, column=1)

        # 第二行
        self.Label_s = Label(self)
        self.Label_s["text"] = "apkID："
        self.Label_s.grid(row=1, column=0 ,sticky=E)

        self.input_s = Entry(self)
        self.input_s.grid(row=1, column=1)

        # 第三行
        self.Label_d = Label(self)
        self.Label_d["text"] = "设备ID："
        self.Label_d.grid(row=2, column=0 ,sticky=E)

        self.input_d = Entry(self)
        self.input_d.grid(row=2, column=1)

        self.button_d = Button(self)
        self.button_d["text"] = "获取"
        self.button_d.grid(row=2, column=3)
        # 第四行
        self.Label_4 = Label(self)
        self.Label_4["text"] = " "
        self.Label_4.grid(row=3, column=0)
        self.button_f = Button(self)
        self.button_f["text"] = "保存"
        self.button_f.grid(row=4, column=0)

        self.button_5 = Button(self, command=self.hello)
        self.button_5["text"] = "安装"
        self.button_5.grid(row=4, column=1)
        # photo = PhotoImage(file='img/1.gif')
        # self.label_img = Label(image=photo)
        # self.label_img.grid(row=0, column=4, columnspan=2, rowspan=3, sticky=E, padx=5, pady=5)
        # self.nameInput = Entry(self)
        # self.nameInput.pack()
        # self.alertButton = Button(self, text='Hello', command=self.hello)
        # self.alertButton.pack()

    def hello(self):
        name = self.input_f.get() or 'world'
        # messagebox.showinfo('Message', 'Hello, %s' % name)
        print name

app = Application()
# 设置窗口标题:
app.master.title('adb工具')
app.master.geometry('500x300+500+200')
app.master.iconbitmap('ico/title.ico')
# 主消息循环:
app.mainloop()