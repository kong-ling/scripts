from tkinter import *
from tkinter import messagebox
import datetime
import pytz

guifont = ('Courier New', 18)

class WorldClock(Frame):
    period_for_update = 1000 #1 second
    color = 'Gray'
    world_cities = ['xa', 'blr', 'sn', 'imu', 'an']
    city_lables = []
    show_timetable = True
    start_or_stop = ''
    hide_or_show_tb = ''

    TIME_ZONE      = 0
    TIME_DIFF      = 1
    TIME_CURTIME   = 2
    TIME_TIMETABLE = 3

    ###############################################################
    ####  combo: timezone, difference, currenttime, timetable
    ###############################################################
    combo = {
        # city        timezone                          difference , curtime, timetable
        "City     ": ['Asia/Shanghai'              ,    0                              ],
        "Xi'An    ": ['Asia/Shanghai'              ,    0                              ],
        "San Diego": ['America/Los_Angeles'        ,    15                             ],
        "Munich   ": ['Europe/Berlin'              ,    7                              ],
        "Bangalore": ['Asia/Kolkata'               ,    2.5                            ],
        "Austin   ": ['America/North_Dakota/Center',    13                             ],
        "Toronto  ": ['America/Toronto',                12                             ],
        "Sydney   ": ['Australia/Sydney'           ,    -2                             ],
    }

    """
    city        curtime     diff    timetable
    city        curtime     diff    timetable
    city        curtime     diff    timetable
    city        curtime     diff    timetable
    city        curtime     diff    timetable
        start      show
    """
    def __init__(self, parent=None, **kw):
        #print('__init__ started')
        Frame.__init__(self, parent, kw)
        self.makeWidgets()
        #self.create_timetables()
        self.start()

    def create_tbl(self, difference = 0):
        '''
        difference is the time difference between remote site and local site
        '''
        tmp = ''
        for i in range(24):
            j = i - difference
            if (j < 0):
                j += 24
            if (j>=24):
                j -= 24
            tmp += '%02d ' % j
        return tmp

    def create_timetables(self):
        for city in self.combo:
            if 'City' in city:
                self.combo[city][3].set('Time Table')
            else:
                self.combo[city][3].set(self.create_tbl(self.combo[city][1]))

    def set_timetables(self):
        show='S\nh\no\nw\n'
        hide='H\ni\nd\ne\n'
        if self.hide_or_show_tb.get() == 'Show Timetable':
            self.create_timetables()
            self.hide_or_show_tb.set('Hide Timetable')
        else:
            for city in self.combo:
                self.combo[city][3].set('')
            self.hide_or_show_tb.set('Show Timetable')
        #if self.hide_or_show_tb.get() == show:
        #    self.create_timetables()
        #    self.hide_or_show_tb.set(hide)
        #else:
        #    for city in self.combo:
        #        self.combo[city][3].set('')
        #    self.hide_or_show_tb.set(show)

        self.show_timetable = not self.show_timetable

    def makeWidgets(self):
        #world_clock = LabelFrame(self, height=300, width=600, text='World Clock', bg='Purple', bd=2, padx=5, pady=5)
        world_clock = LabelFrame(self, height=300, width=2000, text='World Clock', bg=self.color, bd=2, padx=20, pady=20)
        #timetbl = LabelFrame(self, height=300, width=2000, text='Time Table', bg=self.color, bd=2, padx=20, pady=20)

        ## create label and entry
        idx = 0
        for city in self.combo:
            if 'City' in city:
                #city name, like: Xi'An, Austin, San Diego
                Label(world_clock, text='%10s:' % city, bg='yellow', font=guifont).grid(row = idx, column = 0)

                #city current time
                self.combo[city].insert(2, StringVar())
                #Label(world_clock, textvariable=self.combo[city][2], bd=1, font=guifont, bg='yellow').grid(row = idx, column = 1)
                Label(world_clock, textvariable=self.combo[city][2], bd=1, font=guifont, bg='yellow').grid(row = idx, column = 1)

                #time diff
                Label(world_clock, text='TD', bd=1, font=guifont, bg='yellow').grid(row = idx, column = 2)

                # and time list
                self.combo[city].insert(3, StringVar())
                Label(world_clock, textvariable=self.combo[city][3], bd=1, font=guifont, bg='yellow').grid(row = idx, column = 4)
                #Label(timetbl, textvariable=self.combo[city][3], bd=1, font=guifont, bg='sky blue').grid(row = idx, column = 4)
                pass
            else:
                #city name, like: Xi'An, Austin, San Diego
                Label(world_clock, text='%10s:' % city, font=guifont).grid(row = idx, column = 0)

                #city current time
                self.combo[city].insert(2, StringVar())
                Label(world_clock, textvariable=self.combo[city][2], bd=1, font=guifont, bg='spring green').grid(row = idx, column = 1)

                #time diff
                Label(world_clock, text='%02d' % self.combo[city][1], bd=1, font=guifont, bg='red').grid(row = idx, column = 2)

                # and time list
                self.combo[city].insert(3, StringVar())
                Label(world_clock, textvariable=self.combo[city][3], bd=1, font=guifont, bg='sky blue').grid(row = idx, column = 4)
                #Label(timetbl, textvariable=self.combo[city][3], bd=1, font=guifont, bg='sky blue').grid(row = idx, column = 4)

            idx += 1

        self.start_or_stop = StringVar()
        self.hide_or_show_tb = StringVar()
        self.start_or_stop.set('Start')
        self.hide_or_show_tb.set('Hide Timetable')
        #self.hide_or_show_tb.set('H\ni\nd\ne')
        stopWatch = Button(world_clock, textvariable=self.start_or_stop, command=self.start, font=guifont, bg='green')
        stopWatch.grid(row=10, column=0)
        showHide = Button(world_clock, textvariable=self.hide_or_show_tb, command=self.set_timetables, font=guifont, bg='maroon1')
        self.set_timetables()
        showHide.grid(row=10, column=1)
        #showHide.grid(row=0, column=3, rowspan=6)
        ## layout for elements
        world_clock.grid(row = 0, column = 0)
        #timetbl.grid(row = 0, column = 1)
        self.grid(row=2, column=0)

    def insert_space(self, num):
        return ' ' * num

    def _update(self):
        self._settime()
        self.timer = self.after(self.period_for_update, self._update)

    def _settime(self):

        for city in self.combo:
            now = datetime.datetime.now()
            tm = now.astimezone(pytz.timezone(self.combo[city][0]))
            #print('%s%s -> %s-%02d-%s %02d:%02d:%02d' % (city, insert_space(20-len(city)), tm.year, tm.month, tm.day, tm.hour, tm.minute, tm.second)),
            #msg = '%s%s -> %s-%02d-%s %02d:%02d:%02d' % (city, self.insert_space(20-len(city)), tm.year, tm.month, tm.day, tm.hour, tm.minute, tm.second)
            msg = '%04d-%02d-%02d %02d:%02d:%02d' % (tm.year, tm.month, tm.day, tm.hour, tm.minute, tm.second)
            #msg = '%s-%02d-%s %02d:%02d' % (tm.year, tm.month, tm.day, tm.hour, tm.minute)
            #print(tm.tzinfo)

            if 'City' in city:
                self.combo[city][2].set('    Current Time    ')
            else:
                self.combo[city][2].set(msg)

    def start(self):
        self._update()
        pass


if __name__ == '__main__':
    root = Tk()
    hide_or_show = StringVar()
    hide_or_show.set('Hide')

    def about():
        info = '''
        this program is to assist you for world clock.
        initial author is:
        Ling Kong kong.ling@intel.com
        wwid: 11390837
        '''
        messagebox.showinfo(title='About WorldClock', message=info)

    def common():
        usage = '''
        this program is to assist you for world clock.
        initial author is:
            Ling Kong kong.ling@intel.com
            wwid: 11390837
        '''
        print(usage)


    def exit():
        sys.exit()

    def add_menu():
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Open', command=common)
        filemenu.add_command(label='New', command=common)
        filemenu.add_command(label='Save', command=common)
        filemenu.add_command(label='Exit', command=exit)
        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='Usage', command=common)
        helpmenu.add_command(label='About', command=about)
        return menubar

    def show_position(event):
        #print('left click: position'),
        #print(event.x, event.y)
        pass

    def show_help(event):
        #print('right click: Usage:')
        pass

    def show_author(event):
        #print('middle click: version'),
        #print('Author: kong.ling@intel.com')
        pass

    def show_or_hide_timetable():
        global hide_or_show
        if hide_or_show.get() == 'Hide':
            hide_or_show.set('Show')
        else:
            hide_or_show.set('Hide')
            pass

    def main():
        #root = Tk()
        menubar = add_menu()
        root.config(menu=menubar)
        #root.iconbitmap(default='256x256.ico')
        #root.iconbitmap(default='64x64.ico')
        root.iconbitmap(default='32x32.ico')

        root.bind('<Button-1>', show_position)
        root.bind('<Button-2>', show_author)
        root.bind('<Button-3>', show_help)

        #title and size,location
        #root.geometry('550x400+550+230')
        #root.geometry('1200x400')
        root.resizable(0, 0)

        frame1 = Frame(root)
        frame1.grid(row=6, column=0)

        clk = WorldClock(root)
        ######worldWatch = Button(frame1, text='World Clock', command=clk.start, font=guifont)
        ######worldWatch.grid(row=7, column=6)
        ######dispWorldWatch = Button(frame1, textvariable=hide_or_show, command=show_or_hide_timetable, font=guifont)
        ######dispWorldWatch.grid(row=7, column=8)

        root.title('World Clock')
        root.mainloop()

    main()
