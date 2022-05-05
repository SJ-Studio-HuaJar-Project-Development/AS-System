print('AS System 1.3.5 Beta   [兼容模式]down py verson3.7   May1   L:Chinese')
system_name='AS System 1.3.5 Beta'
#检测是否需要更改路径
try:
    open('E:\AS System\AS System 1.3.5 Beta\downloader\path.txt')
    #维持程序运行
    #日志所需组件
    import datetime
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
    #系统加载项组件
    import sys
    import pygame
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time,'  Loading required components')
    '''
    #解析asp文件
    from tkinter import Tk, Label, Button, Frame, Menu
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    from os import listdir, mkdir, remove
    from os.path import split as path_split
    from os.path import exists
    from PIL.Image import open as imread
    from PIL.ImageTk import PhotoImage
    from tkinter.messagebox import showinfo, askyesno
    from base64 import b64decode
    '''
    #设置背景颜色组件
    import easygui
    import easygui as g
    #帮助加载项
    import pygame
    import sys
    import random
    import time
    import tkinter as tk
    from tkinter import filedialog, messagebox
    import easygui as gui
    import win32gui
    import win32api
    #登录账号所需组件
    import datetime
    #系统菜单结构
    #系统菜单组件
    import tkinter
    from tkinter import Label
    from tkinter import Entry
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time,'  Load the system menu structure')
    menuroot = tkinter.Tk()
    menuroot.iconbitmap('AS_system.ico')
    menuroot.resizable(width=True, height=True)
    menuroot.minsize(400,500)
    menuroot.title(system_name)
    #文字编辑器组件
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import messagebox
    import os
    #计算器组件
    import math
    #MD5加密组件
    from tkinter import *
    import hashlib
    import time
    Entry(bg='#292929',bd=0,fg='#ffffff',selectforeground='#cfc8ff',font=('楷体',25))
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time,'  Load menu options')
    标题1=Label(text="AS System",bg='#292929',fg='#ffffff',font=('Inkfree',25))
    标题1.place(x=-910, y=-973, width=2000, height=2000)
    button1_1 = tkinter.Button(text='显示菜单', bg='#292929',fg='#ffffff',bd=1,font=('楷体',18), command=lambda:pressOperator('显示menu'))
    button1_1.place(x=10, y=120, width=120, height=80)
    button1_1 = tkinter.Button(text='显示公告', bg='#292929',fg='#ffffff',bd=3,font=('楷体',10), command=lambda:pressOperator('显示board'))
    button1_1.place(x=180, y=12, width=60, height=30)
    def pressOperator(operator):
        global STORAGE
        global IS_CALC
        if operator == '显示menu':
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  According to the menu')
            button1_1 = tkinter.Button(text='计算器', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('计算器'))
            button1_1.place(x=10, y=120, width=120, height=80)
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  Load calculator icon')
            button1_2 = tkinter.Button(text='文本编辑', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('文本编辑'))
            button1_2.place(x=135, y=120, width=120, height=80)
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  Load text editor icon')
            button1_3 = tkinter.Button(text='MD5加密', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('MD5加密'))
            button1_3.place(x=260, y=120, width=120, height=80)
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  Load MD5 encryption icon')
            button1_4 = tkinter.Button(text='设置', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('设置'))
            button1_4.place(x=10, y=210, width=120, height=80)
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  Load Settings icon')
            button1_set = tkinter.Button(text='帮助',bd=2,font=('楷体',12),command=lambda:pressRun('帮助'))
            button1_set.place(x=2, y=470, width=80, height=30)
            #icon_setting = tk.PhotoImage(file='设置_#333333_128_21562523.gif')
            #print(type(icon_setting))
            #lab=tk.Label(menuroot,compound='LEFT',image=icon_setting).pack(side="left")
            #setting_icon=tkinter.Lable(compound='LEFT',image='E:\AS System\AS System 1.3.3\record\icons\设置_#333333_128_21562523.png')
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  Load helper icon')
    def pressRun(runer):
        global STORAGE
        global IS_CALC
        if runer == '计算器':
            bg=Label(text="",bg='white',font=('Inkfree',25))
            bg.place(x=480, y=0, width=1000, height=1000)
            menuroot.minsize(850,500)
            menuroot.iconbitmap('AS计算器.ico')
            menuroot.title(system_name+'   *计算器*')
            Entry(bg='#292929',bd=0,fg='#ffffff',selectforeground='#cfc8ff',font=('楷体',25))
            menuroot.resizable(width=False, height=False)
            '''hypeparameter'''
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  Load the calculator boot TAB')
            #是否按下了运算符
            IS_CALC = False
            #存储数字
            STORAGE = []
            #显示框最多显示多少个字符
            MAXSHOWLEN = 10
            #当前显示的数字
            CurrentShow = tkinter.StringVar()
            CurrentShow.set('0')
            '''按下数字键(0-9)'''
            #数字超出范围减小字体
            fontsizelow=False
            def pressNumber(number):
                global IS_CALC
                if IS_CALC:
                    CurrentShow.set('0')
                    IS_CALC = False
                if CurrentShow.get() == '0':
                    CurrentShow.set(number)
                else:
                    if len(CurrentShow.get()) < MAXSHOWLEN:
                        CurrentShow.set(CurrentShow.get() + number)


            '''按下小数点'''
            def pressDP():
                    global IS_CALC
                    if IS_CALC:
                            CurrentShow.set('0')
                            IS_CALC = False
                    if len(CurrentShow.get().split('.')) == 1:
                            if len(CurrentShow.get()) < MAXSHOWLEN:
                                    CurrentShow.set(CurrentShow.get() + '.')


            '''清零'''
            def clearAll():
                    global STORAGE
                    global IS_CALC
                    STORAGE.clear()
                    IS_CALC = False
                    CurrentShow.set('0')


            '''清除当前显示框内所有数字'''
            def clearCurrent():
                    CurrentShow.set('0')


            '''删除显示框内最后一个数字'''
            def delOne():
                    global IS_CALC
                    if IS_CALC:
                            CurrentShow.set('0')
                            IS_CALC = False
                    if CurrentShow.get() != '0':
                            if len(CurrentShow.get()) > 1:
                                    CurrentShow.set(CurrentShow.get()[:-1])
                            else:
                                    CurrentShow.set('0')


            '''计算答案修正'''
            def modifyResult(result):
                    result = str(result)
                    if len(result) > MAXSHOWLEN:
                        if len(result.split('.')[0]) > MAXSHOWLEN:
                            downfont=MAXSHOWLEN-len(result.split('.')[0])
                            result='数据过大'
                            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            print(time,'  ERROR:The data is too large  =error_deta#00124=')
                            fontsizelow=True
                        else:
                            # 直接舍去不考虑四舍五入问题
                            result = result[:MAXSHOWLEN]
                    return result


            '''按下运算符'''
            def pressOperator(operator):
                    global STORAGE
                    global IS_CALC
                    if operator == '+/-':
                            if CurrentShow.get().startswith('-'):
                                    CurrentShow.set(CurrentShow.get()[1:])
                            else:
                                    CurrentShow.set('-'+CurrentShow.get())
                    elif operator == '1/x':
                            try:
                                    result = 1 / float(CurrentShow.get())
                            except:
                                    result = 'illegal operation'
                            result = modifyResult(result)
                            CurrentShow.set(result)
                            IS_CALC = True

                    elif operator == '√':
                            try:
                                    result = math.sqrt(float(CurrentShow.get()))
                            except:
                                    result = 'illegal operation'
                            result = modifyResult(result)
                            CurrentShow.set(result)
                            IS_CALC = True

                    elif operator == 'MC':
                            STORAGE.clear()
                    elif operator == 'MR':
                            if IS_CALC:
                                    CurrentShow.set('0')
                            STORAGE.append(CurrentShow.get())
                            expression = ''.join(STORAGE)
                            try:
                                    result = eval(expression)
                            except:
                                    result = 'illegal operation'
                            result = modifyResult(result)
                            CurrentShow.set(result)
                            IS_CALC = True
                    elif operator == 'MS':
                            STORAGE.clear()
                            STORAGE.append(CurrentShow.get())
                    elif operator == 'M+':
                            STORAGE.append(CurrentShow.get())
                    elif operator == 'M-':
                            if CurrentShow.get().startswith('-'):
                                    STORAGE.append(CurrentShow.get())
                            else:
                                    STORAGE.append('-' + CurrentShow.get())
                    elif operator in ['+', '-', '*', '/', '%']:
                            STORAGE.append(CurrentShow.get())
                            STORAGE.append(operator)
                            IS_CALC = True
                    elif operator == '=':
                            if IS_CALC:
                                    CurrentShow.set('0')
                            STORAGE.append(CurrentShow.get())
                            expression = ''.join(STORAGE)
                            try:
                                    result = eval(expression)
                            # 除以0的情况
                            except:
                                    result = '除0错误'
                            result = modifyResult(result)
                            CurrentShow.set(result)
                            STORAGE.clear()
                            IS_CALC = True
            '''Demo'''
            def set_init_window(self):
                self.init_window_name["bg"] = "white"
                self.init_window_name.attributes("-alpha",0.5)
            #def Demo():
                #menuroot.minsize(800,500)
                #menuroot.title('AS System  *计算器*')
                #Entry(bg='#292929',bd=0,fg='#ffffff',selectforeground='#cfc8ff',font=('楷体',25))
            # 布局
            # --文本框

            label = tkinter.Label(menuroot, textvariable=CurrentShow, bg='white', anchor='e', bd=-1, fg='black', font=('楷体', 38))
            label.place(x=520, y=50, width=285, height=50)
            sumtip='Calculator process::  '
            # --第一行
            # ----Memory clear
            button1_1 = tkinter.Button(text='MC', bg='#808080', bd=0, command=lambda:pressOperator('MC'))
            button1_1.place(x=510, y=140, width=60, height=25)
            print(sumtip,'function Memory clear')
            # ----Memory read
            button1_2 = tkinter.Button(text='MR', bg='#808080', bd=0, command=lambda:pressOperator('MR'))
            button1_2.place(x=570, y=140, width=60, height=25)
            print(sumtip,'function Memory read')
            # ----Memory save
            button1_3 = tkinter.Button(text='MS', bg='#808080', bd=0, command=lambda:pressOperator('MS'))
            button1_3.place(x=630, y=140, width=60, height=25)
            print(sumtip,'function Memory save')
            # ----Memory +
            button1_4 = tkinter.Button(text='M+', bg='#808080', bd=0, command=lambda:pressOperator('M+'))
            button1_4.place(x=690, y=140, width=60, height=25)
            print(sumtip,'function Memory +')
            # ----Memory -
            button1_5 = tkinter.Button(text='M-', bg='#808080', bd=0, command=lambda:pressOperator('M-'))
            button1_5.place(x=750, y=140, width=60, height=25)
            print(sumtip,'function Memory -')
            # --第二行
            # ----删除单个数字
            button2_1 = tkinter.Button(text='del', bg='#cfd1d3', bd=0, command=lambda:delOne())
            button2_1.place(x=510, y=175, width=60, height=45)
            print(sumtip,'function delete a single number')
            # ----清除当前显示框内所有数字
            button2_2 = tkinter.Button(text='CE', bg='#cfd1d3', bd=0, command=lambda:clearCurrent())
            button2_2.place(x=570, y=175, width=60, height=45)
            print(sumtip,'function clears all numbers in the current display box')
            # ----清零(相当于重启)
            button2_3 = tkinter.Button(text='C', bg='#cfd1d3', bd=0, command=lambda:clearAll())
            button2_3.place(x=630, y=175, width=60, height=45)
            print(sumtip,'function reset')
            # ----取反
            button2_4 = tkinter.Button(text='+/-', bg='#cfd1d3', bd=0, command=lambda:pressOperator('+/-'))
            button2_4.place(x=690, y=175, width=60, height=45)
            print(sumtip,'function the not')
            # ----开根号
            button2_5 = tkinter.Button(text='√', bg='#cfd1d3', bd=0, command=lambda:pressOperator('√'))
            button2_5.place(x=750, y=175, width=60, height=45)
            print(sumtip,'function square root')
            # --第三行
            # ----7
            button3_1 = tkinter.Button(text='7', bg='#dddddd', bd=0, command=lambda:pressNumber('7'))
            button3_1.place(x=510, y=220, width=60, height=45)
            print(sumtip,'floating 7')
            # ----8
            button3_2 = tkinter.Button(text='8', bg='#dddddd', bd=0, command=lambda:pressNumber('8'))
            button3_2.place(x=570, y=220, width=60, height=45)
            print(sumtip,'floating 8')
            # ----9
            button3_3 = tkinter.Button(text='9', bg='#dddddd', bd=0, command=lambda:pressNumber('9'))
            button3_3.place(x=630, y=220, width=60, height=45)
            print(sumtip,'floating 9')
            # ----除
            button3_4 = tkinter.Button(text='÷', bg='#cfd1d3', bd=0, command=lambda:pressOperator('/'))
            button3_4.place(x=690, y=220, width=60, height=45)
            print(sumtip,'function addition')
            # ----取余
            button3_5 = tkinter.Button(text='%', bg='#cfd1d3', bd=0, command=lambda:pressOperator('%'))
            button3_5.place(x=750, y=220, width=60, height=45)
            print(sumtip,'function take more than')
            # --第四行
            # ----4
            button4_1 = tkinter.Button(text='4', bg='#dddddd', bd=0, command=lambda:pressNumber('4'))
            button4_1.place(x=510, y=265, width=60, height=45)
            print(sumtip,'floating 4')
            # ----5
            button4_2 = tkinter.Button(text='5', bg='#dddddd', bd=0, command=lambda:pressNumber('5'))
            button4_2.place(x=570, y=265, width=60, height=45)
            print(sumtip,'floating 5')
            # ----6
            button4_3 = tkinter.Button(text='6', bg='#dddddd', bd=0, command=lambda:pressNumber('6'))
            button4_3.place(x=630, y=265, width=60, height=45)
            print(sumtip,'floating ')
            # ----乘
            button4_4 = tkinter.Button(text='×', bg='#cfd1d3', bd=0, command=lambda:pressOperator('*'))
            button4_4.place(x=690, y=265, width=60, height=55)
            print(sumtip,'function take')
            # ----取倒数
            button4_5 = tkinter.Button(text='1/x', bg='#cfd1d3', bd=0, command=lambda:pressOperator('1/x'))
            button4_5.place(x=750, y=265, width=60, height=55)
            print(sumtip,'function take the bottom')
            # --第五行
            # ----3
            button5_1 = tkinter.Button(text='3', bg='#dddddd', bd=0, command=lambda:pressNumber('3'))
            button5_1.place(x=510, y=310, width=60, height=45)
            print(sumtip,'floating 3')
            # ----2
            button5_2 = tkinter.Button(text='2', bg='#dddddd', bd=0, command=lambda:pressNumber('2'))
            button5_2.place(x=570, y=310, width=60, height=45)
            print(sumtip,'floating 2')
            # ----1
            button5_3 = tkinter.Button(text='1', bg='#dddddd', bd=0, command=lambda:pressNumber('1'))
            button5_3.place(x=630, y=310, width=60, height=45)
            print(sumtip,'floating 1')
            # ----减
            button5_4 = tkinter.Button(text='-', bg='#cfd1d3', bd=0, command=lambda:pressOperator('-'))
            button5_4.place(x=690, y=310, width=60, height=45)
            print(sumtip,'function reduction')
            # ----等于
            button5_5 = tkinter.Button(text='=', bg='#89ccf6', bd=0, command=lambda:pressOperator('='))
            button5_5.place(x=750, y=310, width=60, height=90)
            print(sumtip,'function equal')
            # --第六行
            # ----0
            button6_1 = tkinter.Button(text='0', bg='#dddddd', bd=0, command=lambda:pressNumber('0'))
            button6_1.place(x=510, y=355, width=120, height=45)
            print(sumtip,'floating zero')
            # ----小数点
            button6_2 = tkinter.Button(text='.', bg='#dddddd', bd=0, command=lambda:pressDP())
            button6_2.place(x=630, y=355, width=60, height=45)
            print(sumtip,'function the decimal point')
            # ----加
            button6_3 = tkinter.Button(text='+', bg='#cfd1d3', bd=0, command=lambda:pressOperator('+'))
            button6_3.place(x=690, y=355, width=60, height=45)
            print(sumtip,'function add')
            # ----版本专利说明
            buttonverson = tkinter.Label(text='''verson 1.3
    保留所有权利''',bg='#ffffff',bd=-1)
            print(sumtip,'information Version patent Description')
            buttonverson.place(x=715, y=400)
            menuroot.mainloop()

        elif runer == '文本编辑':
            mywindow = tk.Tk()
            mywindow.title("AS Word1.2.0")
            mywindow.iconbitmap('ast.ico')
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  loading text editing')
            filename=""
            def mypopup(event):
                editmenu.tk_popup(event.x_root,event.y_root)
            def undo():
                global mytext
                mytext.event_generate("<<Undo>>")
            def cut():
                global mytext
                mytext.event_generate("<<Cut>>")
            def copy():
                global mytext
                mytext.event_generate("<<Copy>>")
            def paste():
                global mytext
                mytext.event_generate("<<Paste>>")
            def delete():
                global mytext
                mytext.event_generate("<<Backspace>>")
            def myopen():
                global filename
                filename=filedialog.askopenfilename(defaultextension=".ast")
                filename=filedialog.askopenfilename(defaultextension=".docx")
                if filename=="":
                    filename=None
                else:
                    mywindow.title("AS Word1.2.0"+os.path.basename(filename))
                    mytext.delete(1.0,tk.END)
                    f=open(filename,'r')
                    mytext.insert(tk.INSERT,f.read())
                    f.close()
            def mysave():
                global filename
                f=filedialog.asksaveasfilename(initialfile="AST文本文件",defaultextension=".ast")
                filename=f
                fh=open(f,'w')
                msg=mytext.get(1.0,tk.END)
                fh.write(msg)
                fh.close()
                mywindow.title("AS Word1.2.0"+os.path.basename(f))
            def mysave2():
                global filename
                f=filedialog.asksaveasfilename(initialfile="未命名.ast",defaultextension=".ast")
                filename=f
                fh=open(f,'w')
                msg=mytext.get(1.0,tk.END)
                fh.write(msg)
                fh.close()
                mywindow.title("AS Word1.2.0"+os.path.basename(f))
            mytext=tk.Text(mywindow,undo=True)
            mytext.pack(expand=1,fill=tk.BOTH)

            savemenu = tk.Menu(mywindow)
            savemenu.add_command(label="另存为",accelerator="Ctrl+Shift+S",command = mysave)
            newtxt = tk.Menu(mywindow)
            newtxt.add_command(label="新建.ast文件",accelerator="Shift+W",command = mysave2)
            filemenu = tk.Menu(mywindow)
            filemenu.add_cascade(label="新建",menu=newtxt)
            filemenu.add_checkbutton(label="打开",accelerator="Alt+D",command = myopen)
            filemenu.add_cascade(label="保存", accelerator="Ctrl+S",menu=savemenu)
            filemenu.add_separator()
            filemenu.add_radiobutton(label="页面设置",state=tk.NORMAL)
            filemenu.add_separator()
            filemenu.add_radiobutton(label="退出",accelerator="Alt+F4")
            editmenu = tk.Menu(mywindow)

            savemenu = tk.Menu(mywindow)
            savemenu.add_command(label="(.ast)")
            newtxt = tk.Menu(mywindow)
            swfmenu = tk.Menu(mywindow)
            swfmenu.add_cascade(label="格式",menu=savemenu,accelerator="")
            mymenu = tk.Menu(mywindow)

            editmenu.add_command(label="撤销",accelerator="Ctrl+Z",command=undo)
            editmenu.add_separator()
            editmenu.add_radiobutton(label="剪切",accelerator="Ctrl+X",command=cut)
            editmenu.add_radiobutton(label="复制",accelerator="Ctrl+C",command=copy)
            editmenu.add_command(label="粘贴",accelerator="Ctrl+V",command=paste)
            editmenu.add_command(label="删除",accelerator="Backspace",command=delete)
            editmenu.add_separator()
            editmenu.add_checkbutton(label="全选",accelerator="Ctrl+A")
            mymenu = tk.Menu(mywindow)

            savemenu = tk.Menu(mywindow)
            savemenu.add_command(label="(默认)",accelerator="*",command = mysave)
            savemenu.add_command(label="最小化",accelerator="Ctrl+L*",command = mysave)
            newtxt = tk.Menu(mywindow)
            finmenu = tk.Menu(mywindow)
            finmenu.add_cascade(label="窗口大小",menu=savemenu,accelerator="")
            mymenu = tk.Menu(mywindow)

            savemenu = tk.Menu(mywindow)
            savemenu.add_command(label="1.",accelerator="""点击对话框虚线可以
    单独打开此界面.""")
            newtxt = tk.Menu(mywindow)
            helpmenu = tk.Menu(mywindow)
            helpmenu.add_cascade(label="获取帮助",menu=savemenu,accelerator="")
            mymenu = tk.Menu(mywindow)

            mymenu.add_cascade(label="文件",menu=filemenu )
            mymenu.add_cascade(label="编辑",menu=editmenu )
            mymenu.add_cascade(label="格式",menu=swfmenu )
            mymenu.add_cascade(label="查看",menu=finmenu)
            mymenu.add_cascade(label="帮助",accelerator="Ctrl+M",menu=helpmenu)
            mytext.bind("<Button-3>",mypopup)
            mywindow["menu"] = mymenu

        elif runer == '图片查看':
            class one():
                def __init__(self):
                    self.root = Tk()
                    self.root.geometry('900x740+100+40')
                    self.root.title('图片查看器')
                    self.choose = Button(self.root,
                                         text='选择要浏览的图像',
                                         font=30,
                                         relief='groove',
                                         bg='#e6e6e6', bd=8,
                                         command=self.openfile_tomwindow,
                                         )
                    self.choose.pack(expand='yes', anchor='center', )

                    self.root.mainloop()

                def openfile_tomwindow(self):
                    pass
                def openfile_tomwindow(self):
                    img_path = askopenfilename(
                        title='请选择图片文件',
                        # 筛选常见图片文件
                        filetypes=[('图片', '.asp .jpg .png .gif .bmp .jpeg')],
                        )
                    if img_path and img_path.endswith(('.asp','.jpg', '.png', '.gif', '.jpeg', '.bmp')):
                        self.path = img_path
                        self.dir = path_split(self.path)[0]
                        self.get_imgs()
                        self.choose.destroy()
                        self.main_window()
                # 获取图片路径后，制作图片路径集，存于self.imgs 变量中
                def get_imgs(self):
                    # 定义一个小函数，判断是否是图片
                    def is_pic(path):
                        if path.endswith(('.asp','.gif', '.jpg', '.jpeg', '.png', '.bmp')):
                            return True
                        else:
                            return False
                    files = [self.dir + f'/{name}' for name in listdir(self.dir)]
                    self.imgs = list(filter(is_pic, files))
                    self.all_imgs = len(self.imgs)
                def main_window(self):
                        # 进入主界面之前先准备参数
                    self.do_params()
                    #----------顶部菜单栏--------
                    self.mnu = Menu(self.root)
                    filemenu = Menu(self.mnu, tearoff=0)
                    self.mnu.add_cascade(label='文件', menu=filemenu)
                    filemenu.add_command(label='打开', command=self.openfile)
                    filemenu.add_command(label='另存为', command=self.save_im)
                    filemenu.add_command(label='删除', command=self.del_im)
                    othermenu = Menu(self.mnu, tearoff=0)
                    self.mnu.add_cascade(label='其它', menu=othermenu)
                    othermenu.add_command(label='function1', command=self.function1)
                    othermenu.add_command(label='function2', command=self.function2)
                    # 放置菜单栏
                    self.root.config(menu=self.mnu)
                   
                    # 设置窗口最小尺寸限制
                    self.root.minsize(900, int(self.size[1]*self.upper)+60)
                    
                    # 调用show函数显示图像
                    self.show()

                    # 缩放控件布置
                    fram1 = Frame(self.root)
                    self.bgr = imread(self.pics_path[2])
                    self.bgr = PhotoImage(self.bgr)
                    bgger = Button(fram1,
                                   image=self.bgr,
                                   relief='flat',
                                   command=lambda: self.chg_size(1))
                    bgger.grid(row=0, column=4)
                    for i in range(1, 10, 2):
                        Button(fram1, width=12, state='disabled', relief='flat').grid(row=0, column=i)
                    self.sml = imread(self.pics_path[3])
                    self.sml = PhotoImage(self.sml)
                    smller = Button(fram1,
                                    image=self.sml,
                                    relief='flat',
                                    command=lambda: self.chg_size(0))
                    smller.grid(row=0, column=6)
                    
                    # 逆时针旋转按键布置
                    self.nsz = imread(self.pics_path[4])
                    self.nsz = PhotoImage(self.nsz)
                    n_rtate = Button(fram1,
                                     image=self.nsz,
                                     relief='flat',
                                     command=lambda: self.rotate_p(0))
                    n_rtate.grid(row=0, column=2)
                    
                    # 顺时针旋转按键布置
                    self.ssz = imread(self.pics_path[5])
                    self.ssz = PhotoImage(self.ssz)
                    s_rtate = Button(fram1,
                                     image=self.ssz,
                                     relief='flat',
                                     command=lambda: self.rotate_p(1))
                    s_rtate.grid(row=0, column=8)
                    
                    # 切换
                    # 上一张 按键布置
                    self.pre_pic = imread(self.pics_path[6])
                    self.pre_pic = PhotoImage(self.pre_pic)
                    prev = Button(fram1,
                                  image=self.pre_pic,
                                  relief='flat',
                                  command=lambda: self.turn_page(0))
                    prev.grid(row=0, column=0)
                    
                    # 下一张 按键布置
                    self.next_p = imread(self.pics_path[7])
                    self.next_p = PhotoImage(self.next_p)
                    next = Button(fram1,
                                  image=self.next_p,
                                  relief='flat',
                                  command=lambda: self.turn_page(1))
                    next.grid(row=0, column=10)
                    fram1.pack(in_=self.root, side='bottom',)




        elif runer == 'MD5加密':
            LOG_LINE_NUM = 0
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time,'  loading MD5 encryption')
            class MY_GUI():
                def __init__(self,init_window_name):
                    self.init_window_name = init_window_name


                #设置窗口
                def set_init_window(self):
                    self.init_window_name.title("AS文本加密工具_v1.2")
                    self.init_window_name.geometry('320x160+10+10')
                    self.init_window_name.geometry('1068x681+10+10')
                    self.init_window_name["bg"] = "white"
                    self.init_window_name.attributes("-alpha",0.98)
                    #标签
                    self.init_data_label = Label(self.init_window_name, text="待处理数据")
                    self.init_data_label.grid(row=0, column=0)
                    self.result_data_label = Label(self.init_window_name, text="输出结果")
                    self.result_data_label.grid(row=0, column=12)
                    self.log_label = Label(self.init_window_name, text="日志")
                    self.log_label.grid(row=12, column=0)
                    #文本框
                    self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
                    self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
                    self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
                    self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
                    self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
                    self.log_data_Text.grid(row=13, column=0, columnspan=10)
                    #按钮
                    self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
                    self.str_trans_to_md5_button.grid(row=1, column=11)


                #功能函数
                def str_trans_to_md5(self):
                    src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
                    #print("src =",src)
                    if src:
                        try:
                            myMd5 = hashlib.md5()
                            myMd5.update(src)
                            myMd5_Digest = myMd5.hexdigest()
                            #print(myMd5_Digest)
                            #输出到界面
                            self.result_data_Text.delete(1.0,END)
                            self.result_data_Text.insert(1.0,myMd5_Digest)
                            self.write_log_to_Text("INFO:str_trans_to_md5 success")
                        except:
                            self.result_data_Text.delete(1.0,END)
                            self.result_data_Text.insert(1.0,"字符串转MD5失败")
                    else:
                        self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


                #获取当前时间
                def get_current_time(self):
                    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    return current_time


                #日志动态打印
                def write_log_to_Text(self,logmsg):
                    global LOG_LINE_NUM
                    current_time = self.get_current_time()
                    logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
                    if LOG_LINE_NUM <= 7:
                        self.log_data_Text.insert(END, logmsg_in)
                        LOG_LINE_NUM = LOG_LINE_NUM + 1
                    else:
                        self.log_data_Text.delete(1.0,2.0)
                        self.log_data_Text.insert(END, logmsg_in)


            def gui_start():
                init_window = Tk()              #实例化出一个父窗口
                ZMJ_PORTAL = MY_GUI(init_window)
                # 设置根窗口默认属性
                ZMJ_PORTAL.set_init_window()

                init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
            gui_start()
        elif runer == '帮助':
        #绘制help界面
            pygame.init()
            # 设置主屏窗口
            screen = pygame.display.set_mode((300,400))
            # 设置窗口的标题，即游戏名称
            pygame.display.set_caption('帮助')
            # 引入字体类型
            f1 = pygame.font.Font('simsun.ttc',40)
            f2 = pygame.font.Font('simkai.ttf',20)
            # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
            # 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
            helptext_t = f1.render('帮助',True,(255,255,255),(0,0,0))
            helptext_wa1 = f2.render('计算器问题:',True,(255,255,255),(0,0,0))
            helptext_wa11 = f2.render(' 1.乘方运算未添加',True,(255,255,255),(0,0,0))
            helptext_wa12 = f2.render('  [官方回答]抱歉，此版本因排版',True,(255,255,255),(0,0,0))
            helptext_wa13 = f2.render(' 问题未能添加此功能，将在下',True,(255,255,255),(0,0,0))
            helptext_wa14 = f2.render(' 一个正式版更新解决此问题。',True,(255,255,255),(0,0,0))
            #获得显示对象的rect区域坐标
            textRect_t =helptext_t.get_rect()
            textRect_wa1 =helptext_wa1.get_rect()
            textRect_wa11 =helptext_wa11.get_rect()
            textRect_wa12 =helptext_wa12.get_rect()
            textRect_wa13 =helptext_wa13.get_rect()
            textRect_wa14 =helptext_wa14.get_rect()
            # 设置显示对象
            textRect_t.center = (43,30)
            textRect_wa1.center = (63,60)
            textRect_wa11.center = (80,80)
            textRect_wa12.center = (135,100)
            textRect_wa13.center = (130,120)
            textRect_wa14.center = (130,140)
            # 将准备好的文本信息，绘制到主屏幕 Screen 上。
            screen.blit(helptext_t,textRect_t)
            screen.blit(helptext_wa1,textRect_wa1)
            screen.blit(helptext_wa11,textRect_wa11)
            screen.blit(helptext_wa12,textRect_wa12)
            screen.blit(helptext_wa13,textRect_wa13)
            screen.blit(helptext_wa14,textRect_wa14)
            # 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
            while True:
                # 循环获取事件，监听事件状态
                for event in pygame.event.get():
                    # 判断用户是否点了"X"关闭按钮,并执行if代码段
                    if event.type == pygame.QUIT:
                        #卸载所有模块
                        pygame.quit()
                        #终止程序，确保退出程序
                        sys.exit()
                pygame.display.flip() #更新屏幕内容
        elif runer == '设置':
            menuroot.title(system_name+'   *设置*')
            menuroot.minsize(850,500)
            menuroot.iconbitmap('AS_system.ico')
            bg=Label(text="",bg='white',font=('Inkfree',25))
            bg.place(x=480, y=0, width=1000, height=1000)
            setword=Label(text="设置",bg='white',font=('楷体',25))
            setword.place(x=480, y=0, width=100, height=60)
            button1_set = tkinter.Button(text='登录账号',bd=2,font=('楷体',12),command=lambda:pressset('账号登录'))
            button1_set.place(x=500, y=80, width=80, height=30)
            def pressset(setting):
                global STORAGE
                global IS_CALC
                if setting=='账号登录':
                    #系统菜单结构
                    menuroot.title(system_name+'   *账号登录*')
                    bg=Label(text="",bg='white',font=('Inkfree',25))
                    bg.place(x=480, y=0, width=1000, height=1000)
                    setword=Label(text="账号登录",bg='white',font=('楷体',25))
                    setword.place(x=480, y=0, width=160, height=60)
                    button1_set = tkinter.Button(text='账户名',bd=2,font=('楷体',12),command=lambda:pressper('账户名'))
                    button1_set.place(x=500, y=80, width=80, height=30)
                    button2_set = tkinter.Button(text='账号',bd=2,font=('楷体',12),command=lambda:pressper('账号'))
                    button2_set.place(x=500, y=135, width=80, height=30)
                    def pressper(per):
                        global STORAGE
                        global IS_CALC
                        if per == '账户名':
                            personname=easygui.enterbox('输入账户名:')
                            if personname == 'yz' or 'YZ' or '叶子' or '叶紫' or '阿紫':
                                timeforuser=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                txtFile=open('E:\\AS System\\AS System 1.3.1\\record\\Account login data\\deta.txt','a')
                                txtFile.write('账户名：')
                                txtFile.write(personname)
                                txtFile.write('    账户类型：VIP')
                                txtFile.write('    登录时间：'+timeforuser)
                                txtFile.write('''
    ''')
                                txtFile.close()
                                用户名1=Label(text=personname,bg='#ffffff',fg='#4a44f3',font=('Inkfree',18))
                                用户名1.place(x=600, y=78, width=50, height=30)
                            else:
                                timeforuser=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                txtFile=open('E:\\AS System\\AS System 1.3.1\\record\\Account login data\\deta.txt','a')
                                txtFile.write('账户名：')
                                txtFile.write(personname)
                                txtFile.write('    账户类型：普通')
                                txtFile.write('    登录时间：'+timeforuser)
                                txtFile.write('''
    ''')
                                txtFile.close()
                                用户名1=Label(text=personname,bg='#ffffff',fg='#4a44f3',font=('Inkfree',18))
                                用户名1.place(x=600, y=78, width=50, height=30)
                        elif per == '账号':
                            timeforpassword=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            person_password=easygui.enterbox('输入账号:')
                            password_len = len(person_password)
                            password_len_word_a = '*'*password_len
                            账号1=Label(text=password_len_word_a,bg='#ffffff',fg='#4a44f3',font=('Inkfree',18))
                            账号1.place(x=600, y=133, width=150, height=30)
                            person_password_ask=easygui.enterbox('是否保存信息(y or n):')
                            if person_password_ask == 'y':
                                messagebox.showinfo('提示','''为了您的安全，保存信息将抹去过去的所有数据，请检查此文档

    临时登录数据文件路径：...\AS System 1.3.5 Beta\record\Account data\other\Temporary account data.txt''')
                                person_password_ask_again=easygui.enterbox('再次确认是否保存信息(y or n):')
                                if person_password_ask_again == 'y':
                                    txtFile=open('E:\\AS System\\AS System 1.3.5 Beta\\record\\Account data\\other\\Temporary account data.txt','w')
                                    txtFile.write('登录信息')
                                    txtFile.write('''
    时间：''')
                                    txtFile.write(timeforpassword)
                                    txtFile.write('''
    用户名：''')
                                    txtFile.write('*User*')
                                    txtFile.write('''
    账号：''')
                                    txtFile.write(person_password)
                                    txtFile.write('''
    账户类型：-  (*该文件不提供信息*)''')
                                    txtFile.close()
                                else:
                                    g.msgbox('已为您取消','取消','好的')
                                    menuroot.resizable(width=True, height=True)
                                    bg=Label(text="",bg='white',font=('Inkfree',25))
                                    bg.place(x=480, y=0, width=1000, height=1000)
                                    menuroot.title(system_name+'   *User*')
                                    Entry(bg='#292929',bd=0,fg='#ffffff',selectforeground='#cfc8ff',font=('楷体',25))
                                    标题1=Label(text="AS System",bg='#292929',fg='#ffffff',font=('Inkfree',25))
                                    标题1.place(x=-910, y=-973, width=2000, height=2000)
                                    button1_1 = tkinter.Button(text='AS Store', bg='#5ff7b7',fg='#ffffff',bd=1,font=('楷体',18), command=lambda:pressOperator('显示menu'))
                                    button1_1.place(x=10, y=120, width=120, height=80)
                                    button1_2 = tkinter.Button(text='小助手', bg='#292929',fg='#ffffff',bd=3,font=('楷体',10), command=lambda:pressOperator('显示board'))
                                    button1_2.place(x=180, y=12, width=60, height=30)
                                    button1_3 = tkinter.Button(text='设置', bg='#292929',fg='#ffffff', bd=3,font=('楷体',10),command=lambda:pressRun('设置'))
                                    button1_3.place(x=250, y=210, width=60, height=30)
                                    button1_set = tkinter.Button(text='帮助', bg='#292929',fg='#ffffff',bd=2,font=('楷体',10),command=lambda:pressRun('帮助'))
                                    button1_set.place(x=2, y=470, width=60, height=30)
                                def pressOperator(operator):
                                    global STORAGE
                                    global IS_CALC
                                    if operator == '显示menu':
                                        button1_1 = tkinter.Button(text='计算器', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('计算器'))
                                        button1_1.place(x=10, y=120, width=120, height=80)
                                        button1_2 = tkinter.Button(text='文本编辑', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('文本编辑'))
                                        button1_2.place(x=135, y=120, width=120, height=80)
                                        button1_3 = tkinter.Button(text='MD5加密', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('MD5加密'))
                                        button1_3.place(x=260, y=120, width=120, height=80)
                                def pressRun(runer):
                                    global STORAGE
                                    global IS_CALC

                            else:
                                g.msgbox('已为您取消','取消','好的')
                                menuroot.title(system_name+'   *User*')
                                messagebox.showinfo('开发者提示','此界面尚未开发')
                                menuroot.resizable(width=True, height=True)
                                bg=Label(text="",bg='white',font=('Inkfree',25))
                                bg.place(x=480, y=0, width=1000, height=1000)
                                Entry(bg='#292929',bd=0,fg='#ffffff',selectforeground='#cfc8ff',font=('楷体',25))
                                标题1=Label(text="AS System",bg='#292929',fg='#ffffff',font=('Inkfree',25))
                                标题1.place(x=-910, y=-973, width=2000, height=2000)
                                button1_1 = tkinter.Button(text='AS Store', bg='#5ff7b7',fg='#ffffff',bd=1,font=('楷体',18), command=lambda:pressusermore('AS Store'))
                                button1_1.place(x=10, y=120, width=120, height=80)
                                button1_2 = tkinter.Button(text='小助手', bg='#292929',fg='#ffffff',bd=3,font=('楷体',10), command=lambda:pressusermore('小助手'))
                                button1_2.place(x=180, y=12, width=60, height=30)
                                button1_3 = tkinter.Button(text='设置', bg='#292929',fg='#ffffff', bd=3,font=('楷体',10),command=lambda:pressusermore('设置'))
                                button1_3.place(x=67, y=435, width=60, height=30)
                                button1_set = tkinter.Button(text='帮助', bg='#292929',fg='#ffffff',bd=2,font=('楷体',10),command=lambda:pressusermore('帮助'))
                                button1_set.place(x=2, y=470, width=60, height=30)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:  # 如果点击关闭窗口，则退出
                                        sys.exit()
                                def presspressusermore(usermore):
                                    global STORAGE
                                    global IS_CALC
                                    if usermore == 'AS Store':
                                        messagebox.showinfo('开发者提示','此界面尚未开发')
                                        button1_1 = tkinter.Button(text='计算器', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('计算器'))
                                        button1_1.place(x=10, y=120, width=120, height=80)
                                        button1_2 = tkinter.Button(text='文本编辑', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('文本编辑'))
                                        button1_2.place(x=135, y=120, width=120, height=80)
                                        button1_3 = tkinter.Button(text='MD5加密', bg='#5fa7ef',fg='#ffffff', bd=3,font=('楷体',18),command=lambda:pressRun('MD5加密'))
                                        button1_3.place(x=260, y=120, width=120, height=80)
                                    elif usermore == '小助手':
                                        messagebox.showinfo('开发者提示','此界面尚未开发')
except:
    print('PATH NOT FOUND')
    g.msgbox('提示','''请更改路径
请在downloader文件夹中打开download_mod.bat文件，并更改目录,下载AS System1.3.5Beta所需插件''')
    print('''提示：请更改路径
请在downloader文件夹中打开download_mod.bat文件，并更改目录,下载AS System1.3.5Beta所需插件''')
