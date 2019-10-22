#coding=utf-8
from Tkinter import *
click_count = 0

top = Tk()
top.title('Start SLE with specified version')
top.geometry('800x494')
top.resizable(width=False, height=True)

scrollbar = Scrollbar(top)
scrollbar.pack(side = RIGHT, fill = Y)

versions = ['18ww50d', '18ww43d', '18ww43d', '18ww40e', '18ww37b']
qslots = ['standard', 'priority', 'bulk', 'interactive']
label_for_versions = Label(top, text='Available versions:', font=('Arial', 11), bg='green', width=30, height=1)
label_for_qslots = Label(top, text='Available qslots:', font=('Arial', 11), bg='green', width=30, height=1)
list_versions = Listbox(top, width=30, height=5)
list_qslots = Listbox(top, width=30, height=4)
#cmd_history = Text(top, width=30, height=2, yscrollcommand = scrollbar.set)
#cmd_history = Listbox(top, fg = 'blue', bg = 'cyan', yscrollcommand = scrollbar.set)
cmd_history = Listbox(top, fg = 'blue', bg = 'cyan')


mylist = Listbox(top, fg = 'red', bg = 'yellow', yscrollcommand = scrollbar.set )

mylist.pack( side = BOTTOM, fill = BOTH )
scrollbar.config( command = mylist.yview )

var = StringVar()
cmd_entry = Entry(top, textvariable=var)
var.set('Just for test')

def submit():
    global click_count
    click_count = click_count + 1
    cmd_history.insert(END, '%d: submit' % click_count)
    mylist.insert(END, '%d: submit' % click_count)
    #cmd_history.insert(END, 'submit\n')

cmd_button = Button(top, text='Submit', command=submit)

for item in versions:
    list_versions.insert(0, item)

for item in qslots:
    list_qslots.insert(0, item)
label_for_versions.pack(side=TOP)
list_versions.pack()
label_for_qslots.pack(side=TOP)
list_qslots.pack()
cmd_button.pack(side=RIGHT)
cmd_history.pack(side = RIGHT, fill = X)
cmd_entry.pack()

top.mainloop()
