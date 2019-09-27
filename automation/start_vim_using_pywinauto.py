#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pywinauto.application import Application
import pyautogui as pag
#gvim = Application().start('gvim')
#t32start = Application().start(r'C:\T32\bin\windows64\t32start.exe')

t32_position=[1728, 177]
pag.click(t32_position[0], t32_position[1])
