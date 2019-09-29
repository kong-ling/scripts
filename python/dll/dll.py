#!/bin/env python
#-*- coding:utf-8 -*-

import ctypes
lib = ctypes.CDLL('msvcrt.dll')
lib.printf(b'hello world\n')

lib = ctypes.cdll.LoadLibrary('msvcrt.dll')
lib.printf(b'hello world\n')
