##-*-coding:utf-8-*-
#import win32gui,win32con
##下面的是窗口的标题名称，这样是一定错的，但在控制台就可以正常使用
##写在文件里要用U编码
#a=u"TRACE32"
##用控件的ID取得控件的句柄，模拟写入输入框文本并按下提交按键
##t1=win32gui.GetDlgItem(dlg,1012)
##t2=win32gui.GetDlgItem(dlg,1001)
##k1=win32gui.GetDlgItem(dlg,1605)
##win32gui.SendMessage(t1,win32con.WM_SETTEXT,None,'902723')
##win32gui.SendMessage(t2,win32con.WM_SETTEXT,None,'761209')
##win32gui.SendMessage(k1,win32con.BM_CLICK,None,None)
#dlg=win32gui.FindWindow('Notepad',None)
#print(win32gui.GetWindowText(dlg))
#print(win32gui.GetClassName(dlg))
#
#trace32=win32gui.FindWindow('TRACE32 PowerView',None)
#trace32=win32gui.FindWindow('t32start.exe',None)
#print(win32gui.GetWindowText(trace32))
##print(win32gui.GetClassName(trace32))

#! /usr/bin/env python
# -*- coding: utf-8 -*-
from win32gui import *

titles = set()
i = 0
def foo(hwnd,mouse):
    #去掉下面这句就所有都输出了，但是我不需要那么多
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        windowtitle = GetWindowText(hwnd)
        classname   = GetClassName(hwnd)
        titles.add(GetWindowText(hwnd))

trace32=FindWindow('T32',None)
print('windowtext = %s' % GetWindowText(trace32))
print('classname  = %s' % GetClassName(trace32))

EnumWindows(foo, 0)
lt = [t for t in titles if t]
lt.sort()
for t in lt:
    if 'T32' in t or 'T32Start' in t or 'Vim' in t:
        print(t)
