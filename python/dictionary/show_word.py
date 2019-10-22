#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

import os
import sys
import re

words = open('vocabulary.txt', 'r', encoding='UTF-8')
wordlists = words.readlines()

while True:
    #get user input
    print('\n============百宝箱===============')
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
            print("%3d:  %s" % (idx+1, matched_words[idx]), end='')
    else:
        print('No word matches your input')
