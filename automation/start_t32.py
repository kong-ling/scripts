#import  os
#import  sys
#import  time
#import pyautogui as pag
#
#t32_position=[1739, 178]
#pag.click(t32_position[0], t32_position[1])

from pywinauto.application import Application
t32start = Application().start(r'C:\T32\bin\windows64\t32start.exe')

t32start.window(title_re='T32Start', class_name='TMainWindow').click()
t32start['Start'].click()
