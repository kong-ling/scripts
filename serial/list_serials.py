#!/usr/bin/env python
#-*- coding: utf-8 -*
import serial
import serial.tools.list_ports
import re

from tkinter import *
root = Tk()
frm = Frame(root)
frm.grid(row=0, column=0)
var = StringVar()
lbfrm=LabelFrame(root, width=200, height=62, text='Ports(COM & LPT)', bg='gray', bd=5, padx=20, pady=30)
lbfrm.grid(row=0, column=1)
ports = Listbox(lbfrm, listvariable=var, bg='yellow', width=50)
ports.grid(row=1, column=0)

def selected():
    desc = ports.get(ACTIVE)
    print(ports.get(ACTIVE))
    pat = '\((\w+\d)\)'
    if re.search(pat, desc):
        print(re.search(pat, desc).group(1))

getActive = Button(frm, text='Get', command=selected)
getActive.grid(row=2, column=0)
plist = list(serial.tools.list_ports.comports())


if len(plist) <= 0:
    print ("The Serial port can't find!")
else:
    for p in plist:
        port = list(p)
        #plist_0 =list(plist[0])
        #serialName = plist_0[0]
        #serialFd = serial.Serial(serialName,9600,timeout = 60)
        #print ("check which port was really used >",serialFd.name)
        #ports.insert('end', serialFd.name)
        serialFd = serial.Serial(list(p)[0],9600,timeout = 60)
        #if 'USB-SERIAL' in port[1]:
        #    ports.insert('end', port[1])
        ports.insert('end', port[1])


root.mainloop()
