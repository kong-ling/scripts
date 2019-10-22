#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8

import os
import sys
import re
import io
from Tkinter import *

frmMain = Tk()

user_input = Label(frmMain, text="search what")

user_input.pack()

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
#os.system('chcp 936')

words = open('vocabulary.txt', 'r', encoding='UTF-8')
wordlists = words.readlines()

while True:
    #get user input
    print('\n============baibaoxiang===============')
    pattern = input('Input you option, Please: ')
    print('your input is "%s"\n' % pattern)

    matched_words = []
    for word in wordlists:
        if re.search(pattern, word, re.IGNORECASE):
            #print(word, end=''),
            matched_words.append(word)

    if len(matched_words):
        #for res in matched_words:
        #    #print("'\e[0;30m' %s '\e[0m'" % res)
        #    print(" %s" % res)
        for idx in range(len(matched_words)):
            #print("'\e[0;30m' %s '\e[0m'" % res)
            #print("%3d:  %s" % (idx+1, matched_words[idx]), end='')
            #print("%3d:  %s" % (idx+1, matched_words[idx]))
            word = matched_words[idx].encode('utf-8')
            #word = matched_words[idx]
            print("%3d:  %s" % (idx+1, word.decode('utf-8')))
    else:
        print('No word matches your input')


frmMain.mainloop()
