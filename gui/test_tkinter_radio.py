#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

from tkinter import *

# 第1步，实例化object，建立窗口window
window = Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
#window.geometry('500x300')  # 这里的乘是小x

var= StringVar()
l = Label(window, bg='yellow')
l.pack()
def print_selection():
    l.config(text=var.get())

ra=Radiobutton(window, text='A', variable=var, value='A', command=print_selection)
rb=Radiobutton(window, text='B', variable=var, value='B', command=print_selection)
rc=Radiobutton(window, text='C', variable=var, value='C', command=print_selection)
ra.pack()
rb.pack()
rc.pack()

lbf = LabelFrame(window, text='Good at:')

var1= IntVar()
var2= IntVar()
l1 = Label(lbf, bg='red')
l1.pack()
def print_sel():
    if ((var1.get() == 1) & (var2.get() == 0)):
        l1.config(text='Python')
    elif ((var1.get() == 0) & (var2.get() == 1)):
        l1.config(text='C++')
    elif ((var1.get() == 0) & (var2.get() == 0)):
        l1.config(text='Not a programmer')
    else:
        l1.config(text='Both are fine')

cb1 = Checkbutton(lbf, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_sel)
cb2 = Checkbutton(lbf, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_sel)

cb1.pack()
cb2.pack()

lbf.pack()

lable_scale = Label(window, bg='green', text='empty')
lable_scale.pack()

def print_scale(v):
    lable_scale.config(text=v)

s = Scale(window, label='set font', from_=0, to=5, orient=HORIZONTAL, length=200, showvalue=0, tickinterval=1, resolution=0.5, command=print_scale)
s1 = Scale(window, label='set font', from_=5, to=10, orient=HORIZONTAL, length=200, showvalue=1, tickinterval=1, resolution=0.5, command=print_scale)
s.pack()
s1.pack()

canvas = Canvas(window, bg='green', height=200, width=300)
#image_file = PhotoImage(file='TkInterColorCharts.png')
#image = canvas.create_image(400, 0, anchor='n', image=image_file)


x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)

def moveit():
    canvas.move(oval, 2, 2)

Button(window, text='Move', command=moveit).pack()

canvas.pack()


# 第8步，主窗口循环显示
window.mainloop()
