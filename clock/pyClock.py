from tkinter import *
from datetime import *

class WorldClock(Frame):
    pass

#create window
root = Tk()

#title and size,location
root.title = 'World Clock'
root.geometry('550x400+550+230')

tz_cared = ['Asia/Shanghai', 'America/Los_Angeles', 'Europe/Berlin', 'Asia/Kolkata', 'America/North_Dakota/Center']
city_timezone = {"Xi'An    ":tz_cared[0],
                 "San Diego":tz_cared[1],
                 "Munich   ":tz_cared[2],
                 "Bangalore":tz_cared[3],
                 "Austin   ":tz_cared[4],
                }

list_for_timezone = Listbox(root)

for k in city_timezone:
    list_for_timezone.insert(0, k)

city_lables = []
city_entrys = []
city_times = []
xian_time = ''

#world_clock = LabelFrame(height=200, width=300, text='World Clock', bg='green')
world_clock = LabelFrame(height=300, width=500, text='World Clock')
world_clock.grid(row = 0, column = 0)

def Init():
    idx = 0
    for k in city_timezone:
        city_lables.append(Label(world_clock, text='%10s' % k, font=('Calibri', 15)))
        city_lables[idx].grid(row = idx, column = 0)
        city_entrys.append(Entry(world_clock, textvariable='Just for fun', font=('Calibri', 15)))
        city_entrys[idx].grid(row = idx, column = 1)
        idx += 1

def StartClock():
    xian_time = datetime.now()
    #city_entrys[0].textvariable = xian_time
    target_string = StringVar()
    target_string.set(xian_time)
    print(target_string.get())
    city_entrys[0].insert(0, target_string.get())
    return target_string

Init()

for lbl in city_lables:
    print(lbl)
for city_entry in city_entrys:
    print(city_entry.get())


text_to_display = StringVar()

label_test =  Label(root, textvariable = StringVar().set(datetime.now()))
start_button = Button(root, text='Start', command=StartClock)
label_test.grid(row = 1, column = 0)
start_button.grid(row = 2, column = 0)

root.after(1000, StartClock)
#list_for_timezone.pack()
root.update()

def trickit():
    now = datetime.now()
    entry_xian.config(text=now)
    entry_xian.after(1000, trickit)


root.mainloop()
