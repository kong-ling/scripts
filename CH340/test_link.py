from tkinter import *
import webbrowser

url =['https://www.hao123.com/','https://www.baidu.com/','https://www.taobao.com/']
name =['hao123','百度','淘宝']

root = Tk()
text =Text(root,width=30,height=5,font=('微软雅黑',15))
text.pack()
text.tag_config('link',foreground='blue',underline=True)
for each in name:
    text.insert(INSERT,each+'\n','link')
def show_hand_cursor(event):
    text.config(cursor='arrow')
def show_arrow_cursor(event):
    text.config(cursor='xterm')
##def click(event):
##    webbrowser.open()
mainloop()

