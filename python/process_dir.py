# -*- coding: utf-8 -*- 
import os
import re
import sys
import string
import datetime

currentDir = os.getcwd()
currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

#find the reports_lingkong_run and reports_lingkong_gen forlder to the html generation
pattern_gen = re.compile(r'.*_gen\/case.*')
pattern_run = re.compile(r'.*_run\/case.*')
pattern_res = re.compile(r'.*reports_[a-z]+\/case.*')
pattern_xml = re.compile(r'.*\.xml')

#dict for test
test_dict = {}
gen_log_array = []
run_log_array = []
res_log_array = []
gen_log_dict = {}
run_log_dict = {}
res_log_dict = {}

def Test1_1(rootDir):
    print "rootDir = %s" % rootDir
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        #for d in dirs: 
        #    print os.path.join(root, d)      
        #for f in sorted(files): 
        for f in (files): 
            full_f = os.path.join(root, f)

            if pattern_xml.match(full_f): #ignore xml file
                continue

            #[00, 11111, 222222, 333333, 44444444, 55555555555555, 6666666666, 777777777777777777777, 888888888888888888888888888888888888888, 9999999999999999999999, 10
            #['', 'nfs', 'site', 'proj', 'libdev', 'lte_ip.work2', 'lingkong', 'xg756_es3_latest_hw', 'bwcSwIrxProcCopyCamCvm_para_03_level1', 'reports_lingkong_run', 'cases_001_step001_012__2017-07-10_17_26_09']
            if pattern_gen.match(full_f):
                gen_log_array = full_f.split('/')
                print 'gen = %s' % gen_log_array
                gen_log_dict[gen_log_array[8]] = gen_log_array

            if pattern_run.match(full_f):
                run_log_array = full_f.split('/')
                print 'run = %s' % run_log_array
                run_log_dict[run_log_array[8]] = run_log_array

            if pattern_res.match(full_f):
                res_log_array = full_f.split('/')
                print 'res = %s' % res_log_array
                res_log_dict[res_log_array[8]] = res_log_array

    return gen_log_dict, run_log_dict, res_log_dict

def Test1(rootDir):
    print "rootDir = %s" % rootDir
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        #for d in dirs: 
        #    print os.path.join(root, d)      
        #for f in sorted(files): 
        for f in (files): 
            full_f = os.path.join(root, f)

            if pattern_xml.match(full_f): #ignore xml file
                continue

            #[00, 11111, 222222, 333333, 44444444, 55555555555555, 6666666666, 777777777777777777777, 888888888888888888888888888888888888888, 9999999999999999999999, 10
            #['', 'nfs', 'site', 'proj', 'libdev', 'lte_ip.work2', 'lingkong', 'xg756_es3_latest_hw', 'bwcSwIrxProcCopyCamCvm_para_03_level1', 'reports_lingkong_run', 'cases_001_step001_012__2017-07-10_17_26_09']
            if pattern_gen.match(full_f):
                gen_log_array = full_f.split('/')
                print 'gen = %s' % gen_log_array
                gen_log_dict[gen_log_array[8]] = gen_log_array

            if pattern_run.match(full_f):
                run_log_array = full_f.split('/')
                print 'run = %s' % run_log_array
                run_log_dict[run_log_array[8]] = run_log_array

            if pattern_res.match(full_f):
                res_log_array = full_f.split('/')
                print 'res = %s' % res_log_array
                res_log_dict[res_log_array[8]] = res_log_array

    return gen_log_dict, run_log_dict, res_log_dict

def Test2(rootDir): 
    loop = 0
    for lists in os.listdir(rootDir):
        loop += 1
        print('==============Test2 -> %d : loop ===============' % loop)
        print('lists = %s' % lists)
        path = os.path.join(rootDir, lists) 
        
        if pattern_xml.match(path): #ignore xml file
            continue
        # if it contains the result, output it.
        if pattern_gen.match(path):
            print path 
        
        if pattern_run.match(path):
            print path 
        
        #recursive
        if os.path.isdir(path): 
            Test2(path)

def Test3(rootDir, level=1): 
    if level==1: print rootDir 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        print '|  '*(level-1)+'|--'+lists 
        if os.path.isdir(path): 
            Test3(path, level+1)

if __name__ == '__main__':
    print "Run  \033[07;34m%s\033[0m" % (__file__)
    print "From \033[07;34m%s\033[0m" % (currentDir)
    print "at:  \033[05;34m%s\033[0m\n" % (currentTime)


    gen_log_dict, run_log_dict, res_log_dict = Test1(os.getcwd())
    #Test2(os.getcwd())
    #Test1('.')
    #Test2('.')
    print gen_log_dict.keys()
    print gen_log_dict.values()
    ####print run_log_dict.keys()
    print run_log_dict.values()
    ####print res_log_dict.keys()
    print res_log_dict.values()

    items = gen_log_dict.items()
    items.sort()
    print '%s' % items.sort()
    #for (k, v) in items:
    for k in gen_log_dict.keys():
        print '[%s] --> %s' % (k, gen_log_dict[k])
        ##create the dict for the whole result
        try:
            #test_dict[k] = [v, run_log_dict[k][9], run_log_dict[k][10], res_log_dict[k][9], res_log_dict[k][10]]
            ##test_dict[k] = [v, run_log_dict[k], run_log_dict[k], res_log_dict[k], res_log_dict[k]]
            ##print test_dict[k]
            #test_dict[k] = [v, run_log_dict[k], run_log_dict[k], res_log_dict[k], res_log_dict[k]]
            #print test_dict[k]
            pass
        except:
            pass

    currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    print "Run  \033[07;34m%s\033[0m" % (__file__)
    print "From \033[07;34m%s\033[0m" % (currentDir)
    print "at:  \033[07;34m%s\033[0m\n" % (currentTime)

    #Test2(os.getcwd())
    #Test3(os.getcwd())
