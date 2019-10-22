from tkinter import *
root = Tk()
strvar = StringVar()
strvar.set("Please Click Me.")
def handler():
    strvar.set("You Have Clicked Me.")

btn = Button(root, textvariable=strvar, command=handler)
btn.pack()
#root.mainloop()
#
##from Tkinter import *
##root = Tk()
root.title("Hello, World!")
root.mainloop()
