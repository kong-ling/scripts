import os
import sys
import time
import datetime
#from pytz import timezone
import pytz

now = datetime.datetime.now()
print(now)

tz_cared = ['Asia/Shanghai', 'America/Los_Angeles', 'Europe/Berlin', 'Asia/Kolkata']
city_timezone = {"Xi'An    ":tz_cared[0],
                 "San Diego":tz_cared[1],
                 "Munich   ":tz_cared[2],
                 "Bangalore":tz_cared[3],
                }

def insert_space(num):
    return ' ' * num

def tz_gtm(timezone):
    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz)
    timezone_str = str(now)[-6:]
    print(tz)
    print(now)
    print(timezone_str)
    return timezone_str

def list_all_timezones():
    #for tz in pytz.all_timezones:
    #    #print(tz)
    #    pass
    pass

list_all_timezones()

tz_file = open('tz_file.txt', 'w')

#tz_gtm('Asia/Shanghai')

if __name__ == '__main__':
    while True:
        print('/\\' * 20)
        for city in city_timezone:
            now = datetime.datetime.now()
            tm = now.astimezone(pytz.timezone(city_timezone[city]))
            print('%s%s -> %s-%02d-%s %02d:%02d:%02d' % (city, insert_space(20-len(city)), tm.year, tm.month, tm.day, tm.hour, tm.minute, tm.second)),
            #tz_file.writelines('%s%s -> %s-%02d-%s %02d:%02d\n' % (city, insert_space(20-len(city)), tm.year, tm.month, tm.day, tm.hour, tm.minute)),
        time.sleep(10)
        #os.system('cls')
