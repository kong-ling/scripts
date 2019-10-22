# -*- coding: utf-8 -*-
from win32gui import *
import win32gui
import win32con
from time import sleep

def foo(hwnd,mouse):
    global config_contents
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        for content in config_contents:
            ads_info = []
            if not '|' in content :
                continue
            else:
                ads_info = content.split('|')
                print(ads_info)
            if GetClassName(hwnd)==ads_info[1] and GetWindowText(hwnd)==ads_info[0]:
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)


config_file = open("C:\\Users\\lingkong\\Desktop\\1.txt","r")
config_contents = config_file.readlines()
while 1:
    EnumWindows(foo, 0)
    sleep(0.5)
