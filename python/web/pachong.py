#coding=utf-8
import urllib.request

#local_file, headers = urllib.request.urlretrieve("http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search&red_tag=v3538778127")
local_file, headers = urllib.request.urlretrieve("https://www.duba.com/?f=qd_chedh&ft=gjlock&--type=0&pid=1000")

print(local_file)
print(headers)
html = open(local_file)

print(html)
