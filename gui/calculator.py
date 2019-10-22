from tkinter import *

root = Tk()

lbl = Label(root).grid(row=10, column=0)

def tell_key():
    print('Hello')
cursors = ["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "heart", "man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "trek", "watch"]
for i in range(20):
    Button(root, text= '%X' % i, font=('Consolas', 14), bg='green', width=4, height=2, command=tell_key, cursor=cursors[i]).grid(row = i//4, column = i % 4, padx=5, pady=5)

root.mainloop()
