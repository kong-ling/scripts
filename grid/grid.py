from tkinter import *

root = Tk()
frm_l = Frame(root)
frm_l.grid(row=0, column=1, sticky='w')
frm_r = Frame(root)
frm_r.grid(row=0, column=2, sticky='e')

TOTAL = 40

lbls = []
for i in range(TOTAL):
    lbls.append(StringVar())
    Label(frm_l, textvariable=lbls[i], font=('Consolas', 14), bg='green').grid(row = i//8, column = i % 8)
    Label(frm_r, textvariable=lbls[i], font=('Consolas', 14), bg='red').grid(row = i//8, column = i % 8)

for i in range(TOTAL):
    lbls[i].set('lbls%02d' % i)


root.mainloop()
