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
button1.grid_configure(column=1,row=3,columnspan=1,rowspan=2)
button2.grid_configure(column=2,row=3,columnspan=1,rowspan=1)
def loginbutton(textbox1,textbox2):###对按钮的命令进行函数定义，并回调函数
    x=textbox1.get()
    y=textbox2.get()
    flag=False
    for i in list(teacher_dic.items()):
        if {x:y} in i:
            flag=True
    if not flag:
        tkinter.messagebox.showerror('登录失败','用户名或密码错误')
    else:
        
        tkinter.messagebox.showinfo('登陆成功','欢迎，教师'+str(x))
        global nexttop
        top.destroy()
        nexttop=Tk()
        nexttop.title('学生管理系统登录系统')
        c_button1=Button(nexttop,text='添加成绩',command=lambda:gradeassign()).pack()
        c_button2=Button(nexttop,text='查看成绩',command=lambda:searchgrade()).pack()
        c_button3=Button(nexttop,text='退出系统',command=lambda:logoutgrade()).pack()
        def gradeassign():
            name=tkinter.simpledialog.askstring('提示','请输入学生姓名')
            if name in list(student_dic.keys()):
                tkinter.messagebox.showwarning('错误','该学生已存在')
            if name not in list(student_dic.keys()) :
                while name=='':
                    tkinter.messagebox.showwarning('提示','您未输入姓名')
                    name=tkinter.simpledialog.askstring('提示','请输入学生姓名')
                    while name in list(student_dic.keys()):
                        tkinter.messagebox.showwarning('错误','该学生已存在')
                        name=tkinter.simpledialog.askstring('提示','请输入学生姓名')
                grade=tkinter.simpledialog.askinteger('提示','请输入学生成绩')
                while grade==None:
                    tkinter.messagebox.showwarning('提示','您未输入成绩')
                    grade=tkinter.simpledialog.askinteger('提示','请输入学生成绩')
                student_dic[name]=grade
                tkinter.messagebox.showinfo('提示','学生成绩输入成功')
        
        def searchgrade():                
            for i in student_dic:
                print('姓名: '+i+'        '+'成绩: '+str(student_dic[i]))
        def logoutgrade():
            nexttop.destroy()
def logoutbutton(textbox1,textbox2):
    top.destroy()
top.mainloop()
     
    

