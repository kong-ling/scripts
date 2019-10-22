import wx
import os
import datetime
import serial
import time
import sched
import threading
import signal

clear_error  = '*CLS\r\n'
meas_volt    = 'MEAS:VOLT?\r\n'
meas_curr    = 'MEAS:CURR?\r\n'
output_off   = 'output off\r\n'
output_on    = 'output on\r\n'
output_off_status   = 'OUTPUT OFF\r\n'
output_on_status    = 'OUTPUT ON\r\n'
output_stat  = 'output:state?\r\n'
idn          = '*IDN?\r\n'

is_exit = False

serial_lock = threading.RLock() #Create a lock object

def handler(signum):
    is_exit = True
    print("Receive a signal %d, is_exit = %d" % (signum, is_exit))

global frame
global ser
global current
global voltage
global s
global on_off_status
global outputStatus

ser = serial.Serial(port='com5', baudrate=9600, stopbits=serial.STOPBITS_TWO)
ser.timeout = 2

s = sched.scheduler(time.time,time.sleep)

timer_interval = 1
def ReadIDN():
    #read current
    serial_lock.acquire()
    ser.write(idn)
    output = ser.readline()
    serial_lock.release()
    return output

def ReadOutputStatus():
    #read current
    serial_lock.acquire()
    ser.write(output_stat)
    output = ser.readline()
    serial_lock.release()
    return output

def ReadVoltage():
    #read Voltage
    serial_lock.acquire()
    ser.write(meas_volt)
    volt = ser.readline()
    serial_lock.release()
    print("volt=%s" % volt)
    print("volt.rstrip=%s" % volt.rstrip())
    if 'E' in volt:
        f_volt = float(volt.rstrip())
        #print("f_volt=%s" % f_volt
        return f_volt
        #voltage.SetValue('%.4f V' % f_volt)
        #voltage.SetValue(volt)
    else:
        volt = ser.readline()
        f_volt = float(volt.rstrip())
        return f_volt
        return -1

def ReadCurrent():
    #read Current
    serial_lock.acquire()
    ser.write(meas_curr)
    curr = ser.readline()
    serial_lock.release()
    print("curr=%s" % curr)
    print("curr.rstrip=%s" % curr.rstrip())
    if 'E' in curr:
        f_curr = float(curr.rstrip())
        #print("f_curr=%s" % f_curr
        return f_curr
        #current.SetValue("%.4f A" % f_curr)
        #f_curr = float(curr.rstrip())
        #current.SetValue(curr)
    else:
        return -1

def MeasureVoltCurr():
    """ Measure the voltage and current of the power supply """
    #print("Thread running"
    global voltage_textctrl
    global current_textctrl
    voltage_textctrl.SetValue("%.2f V" % ReadVoltage())
    current_textctrl.SetValue("%.3f A" % ReadCurrent())
    new_title = "%.2f V / %.3f A" % (ReadVoltage(), ReadCurrent())
    frame.SetTitle(new_title)

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        #wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        wx.Frame.__init__(self, parent, title=title, size=(500,300))
        #self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        global power_model
        power_model = ReadIDN()
        print(power_model)

        global panel
        panel = wx.Panel(self, -1, size=(700,250))
        panel.SetBackgroundColour('Yellow')
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        pos_statictext = wx.StaticText(panel, -1, "Position:", pos=(10, 10))
        self.mousePosition = wx.TextCtrl(panel, -1, "", pos=(140,10), size=(150,40))

        global current_textctrl
        global voltage_textctrl
        current_statictext = wx.StaticText(panel, -1, "Current:", pos=(10, 70)) 
        current_textctrl = wx.TextCtrl(panel, -1, "", pos=(140,70), size=(150,40))
        voltage_statictext = wx.StaticText(panel, -1, "Voltage:", pos=(10, 130))
        voltage_textctrl = wx.TextCtrl(panel, -1, "", pos=(140,130), size=(150,40))
        idn_statictext = wx.StaticText(panel, -1, power_model, pos=(10, 190))

        font = wx.Font(24, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        self.mousePosition.SetFont(font)
        pos_statictext.SetFont(font)
        current_textctrl.SetFont(font)
        voltage_textctrl.SetFont(font)
        current_statictext.SetFont(font)
        voltage_statictext.SetFont(font)
        idn_statictext.SetFont(font)

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to edit")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&OpenCom"," Open a COM port")
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        #self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        #self.buttons = []
        #for i in range(0, 2):
        #    self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
        #    self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        serial_lock.acquire();
        ser.write(output_stat)
        outputStatus = ser.readline()
        serial_lock.release();
        outputStatus = ReadOutputStatus()
        if ('1' in outputStatus):
            on_off_status = output_on_status
            panel.SetBackgroundColour('Green')
        else:
            on_off_status = output_off_status
            panel.SetBackgroundColour('Red')

        global on_off_button
        on_off_button = wx.Button(self, -1, on_off_status, pos=(140,200),size=(50,30))
        on_off_button.SetForegroundColour = 'Yellow'
        on_off_button.SetBackgroundColour = 'Green'
        self.Bind(wx.EVT_BUTTON, self.ToggleOutput, on_off_button)
        on_off_button.SetDefault()
        on_off_button.SetFont(font)

        self.sizer2.Add(panel, 1, wx.EXPAND)
        self.sizer2.Add(on_off_button, 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        panel.Refresh()

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnMove(self,e):
        # Create a message dialog box
        pos = e.GetPosition()
        self.mousePosition.SetValue("%s, %s" % (pos.x, pos.y))

    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " A sample editor \n in wxPython", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def ToggleOutput(self, e):
        """ Toggle output on/off"""

        global on_off_button
        global current_textctrl
        global voltage_textctrl
        serial_lock.acquire()
        if (on_off_button.GetLabel() == output_on_status):
            ser.write(output_off)
            #self.on_off_button.SetForegroundColour = 'blue'
            on_off_button.SetBackgroundColour = 'Green'
            panel.SetBackgroundColour('Red')
            on_off_button.SetLabel(output_off_status)
            current_textctrl.SetBackgroundColour = 'Red'
        else:
            ser.write(output_on)
            #self.on_off_button.SetForegroundColour = 'yellow'
            on_off_button.SetBackgroundColour = 'Red'
            panel.SetBackgroundColour('Green')
            on_off_button.SetLabel(output_on_status)
            current_textctrl.SetBackgroundColour = 'Red'

        serial_lock.release()

        on_off_button.Refresh()
        panel.Refresh()
        serial_lock.acquire()
        ser.write(clear_error)
        serial_lock.release()

        MeasureVoltCurr()
        #voltage_textctrl.SetValue("%.2f V" % ReadVoltage())
        #current_textctrl.SetValue("%.3f A" % ReadCurrent())

def create_thread():
    mymain()

def event_func():
    #print('Current Time %s' % datetime.datetime.now()
    MeasureVoltCurr()

def perform(inc):
    s.enter(inc, 0, perform, (inc,))
    event_func()
def mymain(inc=0.3):
    s.enter(0, 0, perform, (inc,))
    s.run()


def create_wx_application():
    app = wx.App(False)
    frame = MainWindow(None, "Power Control via COM port")
    app.MainLoop()


if __name__ == '__main__':

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    threads = []  #thread pool
    print('Program start %s' % datetime.datetime.now())

    #Thread for wxpython
    ##thread_for_wxpython = threading.Thread(target= create_wx_application, args=())
    ##thread_for_wxpython.setName('thread_for_wxpython')
    ##thread_for_wxpython.setDaemon(True)
    ##thread_for_wxpython.start()
    ##threads.append(thread_for_wxpython)
    app = wx.App(False)
    #frame = MainWindow(None, "Power Control via COM port")
    title = "%sV %sA" % (ReadVoltage(), ReadCurrent())
    frame = MainWindow(None, title)

    #Thread for measurement
    thread_for_measurement = threading.Thread(target= create_thread, args=())
    thread_for_measurement.setName('thread_for_measurement')
    thread_for_measurement.setDaemon(True)
    thread_for_measurement.start()
    threads.append(thread_for_measurement)
    app.MainLoop()

    #wait for the complete of threads
    for th in threads:
        th.join()
    #while threading.active_count() > 0:
    #    time.sleep(1)

