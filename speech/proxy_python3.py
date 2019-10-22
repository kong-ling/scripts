#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Pthon3
import urllib.request
url = "http://www.baidu.com/"

user = 'lingkong'
password = 'ssssxxxx***'
pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None,url ,user ,password)
auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)

proxies = {'http':'http://%s:%s@proxy' % (user, password),
           'https':'https://%s:%s@proxy' % (user, password)}

#????
proxy_support =urllib.request.ProxyHandler(proxies)
##???????{‘??’:‘??ip:???’}
opener = urllib.request.build_opener(proxy_support)
#opener = urllib.request.build_opener(auth_handler)
#??opener
#opener.add_hadler = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]
#add_handler ?????,????????
#urllib.request.build_opener(opener)
response=opener.open(url)
print(response.read().decode('utf-8'))
