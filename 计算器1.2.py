#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import hashlib
import time
LOG_LINE_NUM = 0
class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("计算器")
        self.init_window_name.minsize(320, 528)
        #self.init_window_name.minsize(320, 528+10+10)
        self.init_window_name["bg"] = "white"
        self.init_window_name.attributes("-alpha",0.98)
        '''
        #标签
        self.init_data_label = Label(self.init_window_name, text="标准")
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
'''
        '''
        self.set1 = Label(self.init_window_name, bd=0, text="标准", font=('msyhbd',20), bg='white', width=10)
        self.set1.grid(row=1, column=11)
        self.set1.place(x=10,y=10,20,40)
        '''
        seter1=Label(text="标准",bg='white',font=('Inkfree',16))
        seter1.place(x=35, y=5, width=70, height=30)
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
    import math
    import tkinter
    '''hypeparameter'''
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
                            result = '错误'
                    result = modifyResult(result)
                    CurrentShow.set(result)
                    STORAGE.clear()
                    IS_CALC = True
    label = tkinter.Label(self, textvariable=CurrentShow, bg='white',anchor='e', bd=-1, fg='black', font=('楷体', 38))
    label.place(x=20, y=50, width=285, height=50)
    label.attributes("-alpha",0.5)
    # --第一行
    # ----Memory clear
    button1_1 = tkinter.Button(text='MC', bg='#808080', bd=0, command=lambda:pressOperator('MC'))
    button1_1.place(x=10, y=120, width=60, height=25)
    # ----Memory read
    button1_2 = tkinter.Button(text='MR', bg='#808080', bd=0, command=lambda:pressOperator('MR'))
    button1_2.place(x=70, y=120, width=60, height=25)
    # ----Memory save
    button1_3 = tkinter.Button(text='MS', bg='#808080', bd=0, command=lambda:pressOperator('MS'))
    button1_3.place(x=130, y=120, width=60, height=25)
    # ----Memory +
    button1_4 = tkinter.Button(text='M+', bg='#808080', bd=0, command=lambda:pressOperator('M+'))
    button1_4.place(x=190, y=120, width=60, height=25)
    # ----Memory -
    button1_5 = tkinter.Button(text='M-', bg='#808080', bd=0, command=lambda:pressOperator('M-'))
    button1_5.place(x=250, y=120, width=60, height=25)
    # --第二行
    # ----删除单个数字
    button2_1 = tkinter.Button(text='del', bg='#cfd1d3', bd=0, command=lambda:delOne())
    button2_1.place(x=10, y=155, width=60, height=45)
    # ----清除当前显示框内所有数字
    button2_2 = tkinter.Button(text='CE', bg='#cfd1d3', bd=0, command=lambda:clearCurrent())
    button2_2.place(x=70, y=155, width=60, height=45)
    # ----清零(相当于重启)
    button2_3 = tkinter.Button(text='C', bg='#cfd1d3', bd=0, command=lambda:clearAll())
    button2_3.place(x=130, y=155, width=60, height=45)
    # ----取反
    button2_4 = tkinter.Button(text='+/-', bg='#cfd1d3', bd=0, command=lambda:pressOperator('+/-'))
    button2_4.place(x=190, y=155, width=60, height=45)
    # ----开根号
    button2_5 = tkinter.Button(text='√', bg='#cfd1d3', bd=0, command=lambda:pressOperator('√'))
    button2_5.place(x=250, y=155, width=60, height=45)
    # --第三行
    # ----7
    button3_1 = tkinter.Button(text='7', bg='#dddddd', bd=0, command=lambda:pressNumber('7'))
    button3_1.place(x=10, y=200, width=60, height=45)
    # ----8
    button3_2 = tkinter.Button(text='8', bg='#dddddd', bd=0, command=lambda:pressNumber('8'))
    button3_2.place(x=70, y=200, width=60, height=45)
    # ----9
    button3_3 = tkinter.Button(text='9', bg='#dddddd', bd=0, command=lambda:pressNumber('9'))
    button3_3.place(x=130, y=200, width=60, height=45)
    # ----除
    button3_4 = tkinter.Button(text='÷', bg='#cfd1d3', bd=0, command=lambda:pressOperator('/'))
    button3_4.place(x=190, y=200, width=60, height=45)
    # ----取余
    button3_5 = tkinter.Button(text='%', bg='#cfd1d3', bd=0, command=lambda:pressOperator('%'))
    button3_5.place(x=250, y=200, width=60, height=45)
    # --第四行
    # ----4
    button4_1 = tkinter.Button(text='4', bg='#dddddd', bd=0, command=lambda:pressNumber('4'))
    button4_1.place(x=10, y=245, width=60, height=45)
    # ----5
    button4_2 = tkinter.Button(text='5', bg='#dddddd', bd=0, command=lambda:pressNumber('5'))
    button4_2.place(x=70, y=245, width=60, height=45)
    # ----6
    button4_3 = tkinter.Button(text='6', bg='#dddddd', bd=0, command=lambda:pressNumber('6'))
    button4_3.place(x=130, y=245, width=60, height=45)
    # ----乘
    button4_4 = tkinter.Button(text='×', bg='#cfd1d3', bd=0, command=lambda:pressOperator('*'))
    button4_4.place(x=190, y=245, width=60, height=55)
    # ----取倒数
    button4_5 = tkinter.Button(text='1/x', bg='#cfd1d3', bd=0, command=lambda:pressOperator('1/x'))
    button4_5.place(x=250, y=245, width=60, height=55)
    # --第五行
    # ----3
    button5_1 = tkinter.Button(text='3', bg='#dddddd', bd=0, command=lambda:pressNumber('3'))
    button5_1.place(x=10, y=290, width=60, height=45)
    # ----2
    button5_2 = tkinter.Button(text='2', bg='#dddddd', bd=0, command=lambda:pressNumber('2'))
    button5_2.place(x=70, y=290, width=60, height=45)
    # ----1
    button5_3 = tkinter.Button(text='1', bg='#dddddd', bd=0, command=lambda:pressNumber('1'))
    button5_3.place(x=130, y=290, width=60, height=45)
    # ----减
    button5_4 = tkinter.Button(text='-', bg='#cfd1d3', bd=0, command=lambda:pressOperator('-'))
    button5_4.place(x=190, y=290, width=60, height=45)
    # ----等于
    button5_5 = tkinter.Button(text='=', bg='#89ccf6', bd=0, command=lambda:pressOperator('='))
    button5_5.place(x=250, y=290, width=60, height=90)
    # --第六行
    # ----0
    button6_1 = tkinter.Button(text='0', bg='#dddddd', bd=0, command=lambda:pressNumber('0'))
    button6_1.place(x=10, y=335, width=120, height=45)
    # ----小数点
    button6_2 = tkinter.Button(text='.', bg='#dddddd', bd=0, command=lambda:pressDP())
    button6_2.place(x=130, y=335, width=60, height=45)
    # ----加
    button6_3 = tkinter.Button(text='+', bg='#cfd1d3', bd=0, command=lambda:pressOperator('+'))
    button6_3.place(x=190, y=335, width=60, height=45)
    # ----版本专利说明
    buttonverson = tkinter.Button(text='''verson 1.0
    保留所有权利''', bd=-1)
    buttonverson.place(x=232, y=380)
    root.mainloop()
    if __name__ == '__main__':
        Demo()
gui_start()
