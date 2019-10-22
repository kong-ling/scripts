from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import serial
import sys
import os
import argparse
import serial.tools.list_ports
import re

parser = argparse.ArgumentParser(description='Power control using CH340')
#parser.add_argument('-p', '--port', dest='port', required=True, help='the serial port\'s full name for the switch')
parser.add_argument('-p', '--port', dest='port', required=False, help='the serial port\'s full name for the switch')
parser.add_argument('-d', '--duration', dest='duration', default=1, required=False, help='duration for off')
parser.add_argument('-r', '--repeats', dest='repeats', default=1, required=False, help='repeat times for on/off')
args = parser.parse_args()

class relay:
    def __init__(self, com='COM5'):
        self.info = '''
        this program is to assist you for power control using ch340.
        You can use it to power on/off or power cycle
        Author: Ling Kong(kong.ling@intel.com)
        wwid: 11390837
        '''
        self.root = Tk()
        self.root.title('Power Control using CH340 Relay')
        self.root.iconbitmap(default='power_32x32.ico')
        self.root.resizable(0, 0)
        #self.relay = serial.Serial(com, 9600)
        self.var_on    = StringVar()
        self.var_off   = StringVar()
        self.var_cycle = StringVar()
        self.var_on.set('On')
        self.var_off.set('Off')
        self.var_cycle.set('Power\nCycle')

        lbfmr_top = LabelFrame(self.root, text='Port Selection', bd=3, labelanchor=N, padx=5, pady=5)
        lbfmr_top.grid(row=0, column=0, sticky=W)
        Label(lbfmr_top, text='Port number:').grid(row=0, column=0, sticky=W)
        self.com_ports = ttk.Combobox(lbfmr_top, width=60, state='readonly')
        self.com_ports.grid(row=0, column=1, sticky=W)
        self.refresh = Button(lbfmr_top, text='Refresh', command=self.list_serial_ports)
        self.refresh.grid(row=0, column=2, sticky=W)
        Label(lbfmr_top, text='Active port:').grid(row=0, column=3, sticky=W)
        self.active_port = StringVar()
        active_port_lbl = Label(lbfmr_top, textvariable=self.active_port, fg='red', bg='yellow').grid(row=0, column=4, sticky=W)

        lbfmr_below = LabelFrame(self.root, text='Port Selection', bd=3, labelanchor=N, padx=5, pady=5)
        lbfmr_below.grid(row=1, column=0, sticky=W)
        lbfmr_left = LabelFrame(lbfmr_below, text='Power Control', bd=3, labelanchor=N, padx=5, pady=5, height=30)
        lbfmr_left.grid(row=1, column=0, sticky=SW)
        self.button_on    = Button(lbfmr_left, textvariable=self.var_on,   relief=RAISED, bd=6, font=('Consolas', 14), command=self.On,    width=20, height=11, padx=5, pady=5, cursor='heart', activebackground='yellow')
        self.button_off   = Button(lbfmr_left, textvariable=self.var_off,  relief=RAISED, bd=6, font=('Consolas', 14), command=self.Off,   width=20, height=11, padx=5, pady=5, cursor='man', activebackground='yellow')

        lbfmr_right = LabelFrame(lbfmr_below, text='Power Cycle', bd=3, labelanchor=N, padx=5, pady=5, height=40)
        lbfmr_right.grid(row=1, column=1, rowspan=2, sticky=SW)
        #lbfmr_right.grid(row=1, column=1, sticky=SW)
        self.offtime = Entry(lbfmr_right, justify=CENTER, width=10, bg='spring green')
        self.offtime.insert(0, 3)
        self.offtime.focus()
        self.offtime.selection_range(0, END)
        Label(lbfmr_right, text='Off Time:').grid(row=0, column=0)
        self.offtime.grid(row=0, column=1)
        Label(lbfmr_right, text='Seconds').grid(row=0, column=2)
        self.button_cycle = Button(lbfmr_right, textvariable=self.var_cycle, relief=RAISED, bd=6, font=('Consolas', 14), command=self.Cycle, width=20, height=10, padx=5, pady=5, cursor='spider', activebackground='yellow')
        self.button_on.grid(row=0, column=0)
        self.button_off.grid(row=0, column=1)
        self.button_cycle.grid(row=1, column=0, columnspan=3)

        self.list_serial_ports()
        self.com = self.selected()
        self.com_ports.bind("<<ComboboxSelected>>", self.change_port)

        #get the current status
        self.show_current_status()
        menubar = self.add_menu()
        self.root.config(menu=menubar)
        self.root.mainloop()

    def show_current_status(self):
        if self.status():
            self.On()
        else:
            self.Off()

    def change_port(self, event):
        self.selected()
        #print(self.selected())
        #pass
        self.show_current_status()

    def selected(self):
        self.offtime.selection_range(0, END)
        p = self.com_ports.get()
        pat = '\((\w+\d)\)'
        if re.search(pat, p):
            print(re.search(pat, p).group(1))
            ser = re.search(pat, p).group(1)
            self.relay = serial.Serial(ser, 9600)
            self.active_port.set(ser)
            return ser

    def On(self):
        self.relay.write([0x11])
        time.sleep(0.1)
        n=self.relay.inWaiting()
        self.button_on.configure(bg='green2')
        self.button_off.configure(bg='gray99')
        #self.button_cycle.configure(bg='gray99')
        return ord(self.relay.read(n))

    def Off(self):
        self.relay.write([0x21])
        time.sleep(0.1)
        n=self.relay.inWaiting()
        self.button_off.configure(bg='red')
        self.button_on.configure(bg='gray99')
        #self.button_cycle.configure(bg='gray99')
        return ord(self.relay.read(n))

    def Cycle(self):
        t = self.offtime.get()
        print(t)
        self.Off()
        self.button_cycle.after(int(float(t)*1000), self.On)

    def status(self):
        self.relay.write([0x31])
        time.sleep(0.1)
        n=self.relay.inWaiting()
        return ord(self.relay.read(n))

    def close(self):
        self.relay.close()
        print('Closing %s' % self.com)

    def list_serial_ports(self):
        all_ports = []
        plist = list(serial.tools.list_ports.comports())
        for p in plist:
            port = list(p)
            #ports.insert('end', port[1])
            #print(port[1])
            if 'USB-SERIAL' in port[1]:
                all_ports.append(port[1])

        self.com_ports['values'] = all_ports
        for idx, p in enumerate(all_ports):
            if 'USB-SERIAL' in p:
                self.com_ports.current(idx)
                break


    def exit(self):
        sys.exit()

    def about(self):
        messagebox.showinfo(title='About WorldClock', message=self.info)

    def common(self):
        print(self.info)

    def add_menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File',  menu=filemenu)
        filemenu.add_command(label='Open', command=self.common)
        filemenu.add_command(label='New',  command=self.common)
        filemenu.add_command(label='Save', command=self.common)
        filemenu.add_command(label='Exit', command=self.exit)
        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help',   menu=helpmenu)
        helpmenu.add_command(label='Usage', command=self.common)
        helpmenu.add_command(label='About', command=self.about)
        return menubar

#ch340 = relay(args.port)
ch340 = relay()
