import urllib.request as req
import json

weather_url = "http://api.openweathermap.org/data/2.5/forecast?q=wuhan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996"

result = req.urlopen(weather_url).read().decode("utf-8")
print(result)
# 将字符串转换成json对象
result_json = json.loads(result)
print("="*30)

city = result_json['city']['name']
time = result_json['list'][0]['dt_txt']
weather = result_json['list'][0]['weather'][0]['description']
wind = result_json['list'][0]['wind']['speed']
temp = result_json['list'][0]['main']['temp']
pressure = result_json['list'][0]['main']['pressure']

len1 = len(result_json['list'])

for i in range(0,len1):
    print("城市名称:%s,天气:%s,气温:%s,气压:%s,时间:%s" %(result_json['city']['name'],result_json['list'][i]['weather'][0]['description'],str(result_json['list'][i]['main']['temp']),str(result_json['list'][i]['main']['pressure']),str(result_json['list'][i]['dt_txt'])))
