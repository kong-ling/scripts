import wx
import os
import datetime
import threading
import queue
import time
import sys
import getopt
import sched

try:
    from serial.tools.list_ports import comports
except ImportError:
    comports = None

import serial_control

info = '''
A program to control the Agilent Power Supply over RS-232 port\r\n\
        Author: Ling Kong
Email:  kong.ling@intel.com
WWID:   11390837
'''

module_name = 'Agilent E3631A'

#save user command to a file for later reference
user_cmd_record = open('user_cmd_record.txt', 'a') #append mode

class Agilent_E3431A(wx.Frame):
    output_off_status = 'OUTPUT OFF'
    output_on_status  = 'OUTPUT ON'

    # parameters:
    # init_output_state:   power on/off status
    # q:                   message queue
    def __init__(self, parent, title, init_output_state, q):
        self.user_cmd_count = 0
        self.q = q
        self.dirname=''
        self.read_sched = sched.scheduler(time.time,time.sleep) # define the scheduler for the background current/voltage reading
        self.measure_disabled = 0

        wx.Frame.__init__(self, parent, title=title, size=(500,300))
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        self.panel = wx.Panel(self, -1, size=(700,420))

        #specify the icon for the application
        self.icon = wx.Icon('power.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.selected_output = 1 #selected_output
        self.output_state = init_output_state
        print(self.output_state)

        self.model_statictext   = wx.StaticText(self.panel, -1, model_name, pos=(20, 10), size=wx.DefaultSize, style=wx.ALIGN_CENTRE_HORIZONTAL)

        #Voltage statictext
        self.voltage_statictext      = wx.StaticText(self.panel, -1, "Voltage:", pos=(20,   70))
        #Voltage
        self.voltage_textctrl        = wx.TextCtrl(self.panel, -1, "",           pos=(120,  70), size=(150,40))
        #Voltage Limit
        self.voltage_textctrl_limit  = wx.TextCtrl(self.panel, -1, "",           pos=(320,  70), size=(150,40))

        #Current statictext
        self.current_statictext      = wx.StaticText(self.panel, -1, "Current:", pos=(20,  130))
        #Current
        self.current_textctrl        = wx.TextCtrl(self.panel, -1, "",           pos=(120, 130), size=(150,40))
        #Current Limit
        self.current_textctrl_limit  = wx.TextCtrl(self.panel, -1, "",           pos=(320, 130), size=(150,40))

        self.set_limit_button      = wx.Button(self.panel, -1, "Set\nLimit", pos=(500, 70), size=(120, 100))
        self.set_limit_button.SetToolTip("Set the limits")

        #if '1' in self.output_state: # 1: on
        #    print('output=1')
        #    on_off_button_label = 'OUTPUT ON'
        #    on_off_button_value = 1
        #    panel_bg_color = 'Green'
        #else:                  # 0: off
        #    print('output=0')
        #    on_off_button_label = 'OUTPUT OFF'
        #    on_off_button_value = 0
        #    panel_bg_color = 'Red'

        #self.on_off_button         = wx.ToggleButton(self.panel, -1, on_off_button_label, pos=(320, 200), size=(300,90))
        #self.on_off_button.SetValue(on_off_button_value)
        #self.on_off_button.SetToolTipString('Output on/off')
        ##self.panel.SetBackgroundColour(panel_bg_color)
        #self.panel.SetBackgroundColour('Spring Green')
        #self.panel.Refresh() #refresh the colour setting

        #serial_statictext = wx.StaticText(self.panel, -1, "Selected Serial Port:", pos=(20,  190))
        self.serial_port = wx.TextCtrl(self.panel, -1, serial_port_selected, (20, 210), (100,40))

        #self.channel = wx.RadioBox(self.panel, -1, 'Select Output', (150, 190), (100, 100), channel_names, channel_number, wx.RA_SPECIFY_ROWS)
        #self.channel.SetItemToolTip(0, "Select Output 1")
        #self.channel.SetItemToolTip(1, "Select Output 2")

        self.panel.Bind(wx.EVT_MOTION, self.OnMove)
        self.user_cmd_textctrl        = wx.TextCtrl(self.panel, -1, "", pos=(20,310), size=(360,40), style=wx.TE_PROCESS_ENTER)
        self.send_user_cmd_button     = wx.Button(self.panel, -1, "Send", pos=(400, 310), size=(40,40))
        self.user_cmd_result_textctrl = wx.TextCtrl(self.panel, -1, "", pos=(20,360), size=(360,40), style=wx.TE_PROCESS_ENTER | wx.TE_MULTILINE)
        self.mousePosition            = wx.TextCtrl(self.panel, -1, "", pos=(470,310), size=(150,40))

        #Select the font
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        #self.mousePosition.SetFont(font)
        #self.model_statictext.SetFont(font)
        #self.voltage_statictext.SetFont(font)
        #self.current_statictext.SetFont(font)
        #self.voltage_textctrl.SetFont(font)
        #self.current_textctrl.SetFont(font)
        #self.voltage_textctrl_limit.SetFont(font)
        #self.current_textctrl_limit.SetFont(font)
        ##self.channel.SetFont(font)
        #self.on_off_button.SetFont(font)
        ##self.user_cmd_textctrl.SetFont(font)
        ##self.send_user_cmd_button.SetFont(font)
        #self.set_limit_button.SetFont(font)

        # Setting up the menu.
        filemenu= wx.Menu()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        helpmenu = wx.Menu()
        menuAbout= helpmenu.Append(wx.ID_ABOUT, "&About"," Information about this program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&Options") # Adding the "filemenu" to the MenuBar
        menuBar.Append(helpmenu,"&Help") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        ## Events.
        #self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        #self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        #self.Bind(wx.EVT_TOGGLEBUTTON, self.SwitchOutput, self.on_off_button)
        #self.Bind(wx.EVT_BUTTON, self.SetLimit, self.set_limit_button)
        #self.Bind(wx.EVT_BUTTON, self.SendUserCmd, self.send_user_cmd_button)
        #self.Bind(wx.EVT_RADIOBOX, self.SelectOutput, self.channel)
        self.Bind(wx.EVT_COMBOBOX,   self.SelectComPort, self.serial_port)
        #self.Bind(wx.EVT_TEXT,       self.SelectComPort, self.serial_port)
        self.Bind(wx.EVT_TEXT_ENTER, self.SelectComPort, self.serial_port)
        self.Bind(wx.EVT_TEXT_ENTER, self.SendUserCmd, self.user_cmd_textctrl)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

        self.sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.sizer2.Add(self.panel, 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        self.panel.Refresh()

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self, e):
        #The version info for this program
        dlg = wx.MessageDialog(self, info)
        dlg.ShowModal() # Show it
        dlg.Destroy() # Finally destroy it when finished

    def OnExit(self, e):
        serialPort.SendCMD('system:local')
        self.Close(True) # Close the frame

    def OnMove(self,e):
        # Create a message dialog box
        pos = e.GetPosition()
        self.mousePosition.SetValue("%s, %s" % (pos.x, pos.y))

    def OnIdle(self, e):
        #print('Current Time %s' % datetime.datetime.now())
        #self.process_queue()
        #self.MeasureVoltCurr()
        pass

    def SwitchOutput(self,e):
        ''' Switch the output
            If current status is ON, then change to OFF
            If current status is OFF, then change to ON
        '''
        self.measure_disabled = 1
        #print('self.measure_disabled = ', self.measure_disabled)
        queueLock.acquire();
        print('queue Size ', self.q.qsize())
        if (self.on_off_button.GetValue() == True): #On
            print('SwitchOutput if')
            self.q.put('output on', 1) #if queue is full, block the thread
            self.on_off_button.SetValue(1)
            self.on_off_button.SetLabel(self.output_on_status)
            self.on_off_button.SetBackgroundColour('Green')
        else:
            print('SwitchOutput else')
            self.q.put('output off', 1) #if queue is full, block the thread
            self.on_off_button.SetValue(0)
            self.on_off_button.SetLabel(self.output_off_status)
            self.on_off_button.SetBackgroundColour('Red')
        queueLock.release();

        self.measure_disabled = 0
        #print('self.measure_disabled = ', self.measure_disabled)

        #refresh panel
        #self.panel.Refresh()

    def SendUserCmd(self,value):
        self.user_cmd_count += 1
        user_cmd = self.user_cmd_textctrl.GetValue()
        self.user_cmd_textctrl.SelectAll()
        self.user_cmd_result_textctrl.AppendText('\n%d: %s->' % (self.user_cmd_count, user_cmd))

        #write to record file for later reference
        user_cmd_record.write('%s\n' % user_cmd)

        queueLock.acquire()
        if '?' in user_cmd: # if Query Command issued?
            response = serialPort.SendCMD_and_ReceiveResult(user_cmd)
            self.q.put(user_cmd, 1)
            self.user_cmd_result_textctrl.AppendText(response)
        else:
            #serialPort.SendCMD(user_cmd)
            self.q.put(user_cmd, 1)
        queueLock.release()

    def SetLimit(self, e):
        voltage_limit = frame.voltage_textctrl_limit.GetValue()
        current_limit = frame.current_textctrl_limit.GetValue()
        print(voltage_limit)
        print(current_limit)
        try:
            queueLock.acquire()
            #serialPort.SendCMD('VOLT %.2f' % float(voltage_limit))
            #serialPort.SendCMD('CURR %.3f' % float(current_limit))
            #serialPort.SendCMD('*SAV {1}')
            self.q.put('VOLT %.2f' % float(voltage_limit), 1)
            self.q.put('CURR %.3f' % float(current_limit), 1)
            self.q.put('*SAV 1', 1)
            self.UpdateVoltageCurrent(True)
            queueLock.release()
        except Exception as e:
            print(e)
            pass

    def UpdateVoltageCurrent(self, limit):
        current_voltage = serialPort.ReadVoltage(limit)
        current_current = serialPort.ReadCurrent(limit)

        if limit == True:   #display voltage/current limit
            try:
                frame.SetVoltage_textctrl_limit("%.2f" % current_voltage)
                frame.SetCurrent_textctrl_limit("%.3f" % current_current)
            except Exception as e:
                pass

        else:               #display voltage/current
            try:
                frame.SetVoltage_textctrl("%.2f V" % current_voltage)
                frame.SetCurrent_textctrl("%.3f A" % current_current)
                new_title = "%.3f A / %.2f V" % (current_current, current_voltage)
            except Exception as e:
                frame.SetVoltage_textctrl("N/A")
                frame.SetCurrent_textctrl("N/A")
                new_title = "N/A"
                print("UpdateVoltageCurrent:", e)
            finally:
                frame.SetFrameTitle(new_title)


    def DisplayLimit(self):
        self.UpdateVoltageCurrent(True)

    def SelectComPort(self,e):
        print(self.serial_port.GetValue())
        return

    def SelectOutput(self,e):
        print(self.channel.GetItemLabel(self.channel.GetSelection()))
        serialPort.SelectOutput(self.channel.GetSelection() + 1)
        frame.DisplayLimit()
        return

    def SetCurrent_textctrl(self, value):
        self.current_textctrl.SetValue(value)

    def SetVoltage_textctrl(self, value):
        self.voltage_textctrl.SetValue(value)

    def SetCurrent_textctrl_limit(self, value):
        self.current_textctrl_limit.SetValue(value)

    def SetVoltage_textctrl_limit(self, value):
        self.voltage_textctrl_limit.SetValue(value)

    def SetFrameTitle(self, value):
        self.SetTitle(value)

    def MeasureVoltCurr(self):
        """ Measure the voltage and current of the power supply """
        while self.measure_disabled == 1:
            print('self.measure_disabled = ', self.measure_disabled)
            continue

        output_status = serialPort.ReadOutputStatus()
        #print(output_status)

        #check whether the 'Output On/Off'button is pressed by someone on the supply
        if '1' in output_status:
            #print('measurement if')
            self.on_off_button.SetLabel(self.output_on_status)
            self.on_off_button.SetValue(1)   #change the button to On
            #self.panel.SetBackgroundColour('Green')
            self.on_off_button.SetBackgroundColour('Green')
        else:
            #print('measurement else')
            self.on_off_button.SetLabel(self.output_off_status)
            self.on_off_button.SetValue(0)
            #self.panel.SetBackgroundColour('Red')
            self.on_off_button.SetBackgroundColour('Red')

        self.UpdateVoltageCurrent(False)

        errorState = serialPort.ReadError()
        while 'No error' not in errorState:
            print(errorState)
            errorState = serialPort.ReadError()

        #self.panel.Refresh()

    # thread for the voltage/current measurement
    def event_func(self):
        #print('Current Time %s' % datetime.datetime.now())
        #self.MeasureVoltCurr()
        pass

    def perform(self, inc):
        self.read_sched.enter(inc, 0, self.perform, (inc,))
        self.event_func()

    def mymain(self, inc=0.9):
        self.read_sched.enter(0, 0, self.perform, (inc,))
        self.read_sched.run()

    def create_thread(self):
        self.mymain()

    def process_queue(self):
        queueLock.acquire()
        while True:
            if self.q.empty(): # queue is Empty
                break
            else:
                data = self.q.get(True, 1)
                print('process_queue queue Size ', self.q.qsize())
                print('queue data = %s' % data)
                print('process_queue: ', serialPort.SendCMD_and_ReceiveResult(data))

        queueLock.release()

#def List_serial_ports():
#    comport_dict = {} #dictionary
#    if comports:
#        for port, desc, hwid in sorted(comports()):
#            print('---%-20s %s' % (port, desc))
#            comport_dict[desc] = port
#
#        for com in comport_dict.keys():
#            print(com, comport_dict[com])
#
#        return comport_dict
def List_serial_ports():
    comport_dict = [] #list
    if comports:
        for port, desc, hwid in sorted(comports()):
            print('---%-20s %s' % (port, desc))
            comport_dict.append(port)

        #for com in comport_dict.keys():
        #    print(com, comport_dict[com])

        return comport_dict

def Usage():
    #The usage of the tool
    print('''
    Usage:
    python e3631a.py [-gui]
    -h, --help Show the usage information,     -h, or --help
    -p, --port Specify the serial port to use, -p COM1, or --port COM1
    -g, --gui  Use the GUI for the the control,-g or --gui
    ''')

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hgp:", ["help", "gui", "port="])
    except getopt.GetoptError:
        sys.exit()

    serial_port_selected = ''
    gui_mode = False

    for name, value in opts:
        if name in ("-h", "--help"):
            Usage()
            sys.exit()
        elif name in ("-p", "--port"):
            serial_port_selected = value
        elif name in ("-g", "--gui"):
            gui_mode = True

    if gui_mode == True or len(sys.argv) == 1:
        app = wx.App(False)

        if serial_port_selected == '':
            #Get serial port list
            com_dict = List_serial_ports()
            com_port_description = []
            #for com in com_dict.keys():
            #    com_port_description.append(com_dict[com])

            # Show dialog to select serial port
            #dialog = wx.SingleChoiceDialog(None, 'Available Ports', 'Select Serial Port', com_dict.keys())
            dialog = wx.SingleChoiceDialog(None, 'Available Ports', 'Select Serial Port', com_dict)
            print(dialog.GetSelection())
            #dialog.GetSelection()
            result = dialog.ShowModal()
            print(dialog.GetSelection())
            if result == wx.ID_OK:
                #serial_port_selected = com_dict[dialog.GetStringSelection()]
                serial_port_selected = com_dict[dialog.GetSelection()]
                print(serial_port_selected)
            else:
                serial_port_selected = 'COM1'
                print('Cancel')
            dialog.Destroy()

        serialPort = serial_control.Serial_Control_Port(serial_port_selected)
        model_name = serialPort.ReadIDN()
        print('model_name = ', model_name)

        #if 'E3646' in model_name: #operation needed to done in remote mode
        #    channel_names = ['1', '2']
        #    channel_number = 2
        #elif 'E3631A' in model_name: #operation needed to done in remote mode
        #    serialPort.SendCMD('system:remote')
        #    channel_names = ['P6V', 'P25V', 'N25V']
        #    channel_number = 3
        #else:
        #    print('No Equipment Connected. Please check it.')
        #    sys.exit() #exit the program completely

        global output_status
        output_status = serialPort.ReadOutputStatus()
        print(output_status)

        threads = []  #thread pool
        queueLock = threading.Lock()
        #workqueue = queue.queue(0) #unlimited queue

        frame = Agilent_E3431A(None, model_name, output_status, None)
        #frame.DisplayLimit()

        #Thread for measurement
        #thread_for_measurement = threading.Thread(target= frame.create_thread, args=())
        #thread_for_measurement.setName('thread_for_measurement')
        #thread_for_measurement.setDaemon(True)
        #thread_for_measurement.start()
        #threads.append(thread_for_measurement)

        app.MainLoop()

    else:
        print('Command Line Mode is selected')
        serialPort = serial_control.Serial_Control_Port(serial_port_selected)
