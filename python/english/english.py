import wx
import os
import datetime
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


def handler(signum):
    is_exit = True
    print("Receive a signal %d, is_exit = %d" % (signum, is_exit))

global frame
global current

s = sched.scheduler(time.time,time.sleep)

timer_interval = 1

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        wx.Frame.__init__(self, parent, title=title, size=(1000,618))
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        global panel
        panel = wx.Panel(self, -1, size=(1000,618))
        panel.SetBackgroundColour('Green')
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        pos_statictext = wx.StaticText(panel, -1, "Cursor Position:", pos=(10, 10))
        self.mousePosition = wx.TextCtrl(panel, -1, "", pos=(350,10), size=(200,40))

        global current_textctrl
        current_statictext = wx.StaticText(panel, -1, "Pattern", pos=(10, 70)) 
        current_textctrl = wx.TextCtrl(panel, -1, "", pos=(350,70), size=(200,40))

        font = wx.Font(24, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        self.mousePosition.SetFont(font)
        pos_statictext.SetFont(font)
        current_textctrl.SetFont(font)
        current_statictext.SetFont(font)

        #self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)


        #text for output words
        wordLabel = wx.StaticText(panel, -1, 'matched:', size=(100, 200), pos=(10, 100))
        text = wx.TextCtrl(panel, -1, '', size=(100, 200), pos=(10, 200))
        wordLabel.SetFont(font)
        text.SetFont(font)

        self.sizer2.Add(panel, 1, wx.EXPAND)
        self.sizer2.Add(wordLabel, 1, wx.EXPAND)
        self.sizer2.Add(text, 1, wx.EXPAND)

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



def create_thread():
    mymain()

def event_func():
    #print('Current Time %s' % datetime.datetime.now())
    pass

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
    title = 'Hello, English'
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

