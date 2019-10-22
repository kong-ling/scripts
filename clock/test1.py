'''3.Tk8.4以后Frame又添加了一类LabelFrame，添加了Title的支持'''
from tkinter import *
root = Tk()
for lf in ['red','blue','yellow']:
    #可以使用text属性指定Frame的title
    LabelFrame(height = 200,width = 300,text = lf, bg = lf).pack()
root.mainloop()
