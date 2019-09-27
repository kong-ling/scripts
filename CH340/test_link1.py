
from tkinter import *
import webbrowser

url =['www.hao123.com','www.baidu.com','www.taobao.com']
name =['hao123','百度','淘宝']

root = Tk()
text =Text(root,width=30,height=5,font=('微软雅黑',15))
text.pack()
text.tag_config('link',foreground='blue',underline=True)

def show_hand_cursor(event):
    text.config(cursor='arrow')
def show_arrow_cursor(event):
    text.config(cursor='xterm')
def click(event,x):
    webbrowser.open(x)
def handlerAdaptor(fun,**kwds):
    return lambda event,fun=fun,kwds=kwds:fun(event,**kwds)
m=0
for each in name:
    text.tag_config(m,foreground='blue',underline=True)
    text.tag_bind(m,'<Enter>',show_hand_cursor)
    text.tag_bind(m,'<Leave>',show_arrow_cursor)
    
    text.insert(INSERT,each+'\n',m)

    text.tag_bind(m,'<Button-1>',handlerAdaptor(click,x=url[m]))
    m+=1
mainloop()
