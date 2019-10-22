#<<<<<<< HEAD
#!/usr/bin/python
# -*- coding: UTF-8 
import json
import urllib.request
from urllib.parse import quote
import string
from xml.dom import minidom
import time

#12.获取当前天气情况
def get_support_city(province):
    pass
    url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity?byProvinceName='+province
    url = quote (url, safe=string.printable)
    ret=urllib.request.urlopen(url)
    txt=ret.read().decode('utf-8')
    string_str=''
    key_value=''
    key_value_list=[]
    word_flag=0
    # print (txt)
    for i in txt:
        string_str += i
        # print(string_str)
        if string_str.replace(' ','').replace('\t','').replace('\n','').replace('\r','')== '<string>':
            # print ('---------------------------string_str')
            word_flag = 1
        if i=='>':
            string_str=''
        if word_flag==1:
            key_value+=i
            # print(key_value,'*************************************')
        else:
            key_value=''
        if i=='<' and word_flag==1:
            key_value_list.append(key_value.replace('<','').replace('>','').replace('(','').replace(')',''))
            key_value=''
            word_flag=0
    # print(key_value_list)
    support_city={}
    for i in key_value_list:
        # print(i)
        word=i.split(' ')
        support_city[word[0]]=word[1]
    # print(support_city)
    return support_city
#（2）获取天气
def get_weather(name):
    page = urllib.request.urlopen("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName="+name)
    lines = page.readlines()
    page.close()
    document = ""
    for line in lines :
        document = document + line.decode('utf-8')
    #print(document)

    from xml.dom.minidom import parseString
    dom =parseString(document)
    strings = dom.getElementsByTagName("string")
    print ('今日天气实况：',strings[10].childNodes[0].data)


if __name__ == '__main__':
    pass
    #province=input('请输入要查询的省份：')
    #province = quote (province, safe=string.printable)
    #support_city=get_support_city(province)
    #print(support_city)
    #name=input('请在上述城市中选择城市：')
    ## name = quote (name, safe=string.printable)
    #name=support_city[name]
    #city_weather = get_weather (name)
    states = ['陕西', '河南', '上海', '北京', '重庆', '天津']
    #states = ['陕西', '河南', '上海', '广东', '北京']
    #states = ['陕西']
    #province=input('请输入要查询的省份：')
    #province = quote (province, safe=string.printable)
    for province in states:
        support_city=get_support_city(province)
        print(support_city)
        for name in sorted(support_city.keys()):
            name=support_city[name]
            #print(name)
            try:
                time.sleep(0.1)
                city_weather = get_weather (name)
            except:
                #print(name)
                pass
#=======
#import requests as req
#r= req.get('http://www.weather.com.cn/data/sk/101020100.html')
#print(r.status_code)
#print(r.contents)
#print(r.json())
#
#>>>>>>> 12bb23d86a12f1c17a463d0b319dad9655366fd0
