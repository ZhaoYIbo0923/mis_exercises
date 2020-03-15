# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:58:11 2019

@author: Zhao Yibo
"""

from tkinter import *###引入第三方库
import tkinter.messagebox
import tkinter.simpledialog 
teacher_dic={'admin':{'Admin':'123456'},
             'admin2':{'Admin2':'987654321'}}###为系统提供基础数据库
student_dic={'BZB':100,
             'bzb':80,
             'Bzb':95}
top=Tk()###构造交互界面父界面
top.title('学生管理系统登录系统')###命名
label1=Label(top,text='用户名:')###构造页面组件，标签，文本框，按键
label2=Label(top,text='密码:')
textbox1=Entry(top,bd=6)
textbox2=Entry(top,bd=6,show='*')
button1=Button(top,text='Login',command=lambda:loginbutton(textbox1,textbox2))
button2=Button(top,text='退出',command=lambda:logoutbutton(textbox1,textbox2))
label1.grid_configure(column=1,row=1,columnspan=1,rowspan=1)###构造页面布局
label2.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
textbox1.grid_configure(column=2,row=1,columnspan=1,rowspan=1)
textbox2.grid_configure(column=2,row=2,columnspan=1,rowspan=1)