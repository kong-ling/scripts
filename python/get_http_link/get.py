#-*-coding:utf-8-*-
import urllib2

proxy_handler = urllib2.ProxyHandler({"http":"http://server:port"})
proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
proxy_auth_handler.add_password('realm', '', 'name', 'password')

opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
f = opener.open('link')
content = f.read()
print content

FileNameNum=1
herf='index.html'
while True:
    f=file(herf,'w')
    #urlh='http://sebug.net/paper/python/'
    urlh='http://old.sebug.net/paper/python/'
    #url=urlh+herf
    url=urlh
    print url
    response=urllib2.urlopen(url)
    html=response.read()
    NameEnd=html.find('ÏÂÒ»Ò³')-2
    if NameEnd < 0:
        break
    NameStrat=html.find('href',NameEnd-20)+6
    herf=html[NameStrat:NameEnd]
    print herf
    f.write(html)
    f.close()
    FileNameNum+=1
