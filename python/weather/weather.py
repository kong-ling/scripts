import requests as req
r= req.get('http://www.weather.com.cn/data/sk/101020100.html')
print(r.status_code)
print(r.contents)
print(r.json())

