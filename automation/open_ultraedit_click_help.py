# coding=utf-8

from pywinauto import application

#app = application.Application(backend="win32").start(cmd_line=r"C:\Program Files (x86)\IDM Computer Solutions\UltraEdit\Uedit32.exe")
app = application.Application(backend="win32").start(cmd_line=r"gvim.exe")
print(app)
app.GVIM8.MenuSelect('Help->About')
