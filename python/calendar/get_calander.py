#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import win32com.client

namespace = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')

if __name__ == '__main__':
    calendar = namespace.GetDefaultFolder(9)
    for item in calendar.Items:
        print(item.Subject)