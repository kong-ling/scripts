#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *           # 导入 Tkinter 库
root = Tk('word-killer')                     # 创建窗口对象的背景色
                                # 创建两个列表
textsearch = Text(root)
textresult = scrolledtext(root)

textsearch.pack()
textresult.pack()
root.mainloop()                 # 进入消息循环
