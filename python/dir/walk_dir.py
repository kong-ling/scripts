#coding=utf8
import os
import time
import datetime
g = os.walk(r'C:\posv_cv_script-scripts\python')
print(g)
g_for_datetime = g
g_for_time = g
g_for_time_clock = os.walk(r'C:\posv_cv_script-scripts\python')

g_for_get = 'C:\posv_cv_script-scripts\python'

def walk_dir(dir):
    for path, dir_list, file_list in g:
        for file_name in file_list:
            print(os.path.join(path, file_name))

def run_time_using_datetime(dir):
    starttime = datetime.datetime.now()
    walk_dir(dir)
    endtime = datetime.datetime.now()
    print('%d seconds' % (endtime - starttime).seconds)

def run_time_using_time(dir):
    starttime = time.time()
    walk_dir(dir)
    endtime = time.time()
    print('%d seconds' % (endtime - starttime))

def run_time_using_time_clock(dir):
    starttime = time.perf_counter()
    walk_dir(dir)
    endtime = time.perf_counter()
    print('%d seconds' % (endtime - starttime))

def get_all_files(dir):
    files = os.listdir(dir)
    s = []
    for file in files:
        if not os.path.isdir(file): #is file
            f = open(dir + '\\' + file)
            iter_f = iter(f)
            str = ''
            for line in iter_f:
                str = str + line
            s.append(str)
    print(s)

run_time_using_time(g)
#run_time_using_datetime(g_for_datetime)
#run_time_using_time_clock(g_for_time_clock)
#get_all_files(g_for_get)
type(g_for_time_clock)
for g in g_for_time_clock:
    print(g)
