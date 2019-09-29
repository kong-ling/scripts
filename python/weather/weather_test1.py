__author__ = 'dyb'

import os
import urllib.request
import urllib.parse
import json


class weather(object):

    # 获取城市代码的uri
    citycode_uri = "http://apistore.baidu.com/microservice/cityinfo?cityname="

    # 获取天气信息的uri
    weather_uri = "http://apistore.baidu.com/microservice/weather?cityid="

    #主要业务逻辑处理
    def mainHandle(self):
        print("输入你要查询天气的城市：")
        city_name = input()
        uri = self.citycode_uri + urllib.parse.quote(city_name)
        ret = json.loads(urllib.request.urlopen(uri).read().decode("utf8"))
        if(ret['errNum']) != 0:
            print('网络或者服务器出错')
            return False
        else:
            weather_uri = self.weather_uri + ret['retData']['cityCode']
            data = json.loads(urllib.request.urlopen(weather_uri).read().decode("utf8"))
            if data['errNum'] == 0:
                ret_data = data['retData']
                output = "城市名:" + ret_data['city'] + "\r\n"
                output += "更新时间:" + ret_data["date"] + " " + ret_data["time"] + "\r\n"
                output += "城市编码:" + ret_data['citycode'] + "\r\n"
                output += "经度:" + str(ret_data['longitude']) + "\r\n"
                output += "维度:" + str(ret_data['latitude']) + "\r\n"
                output += "邮编:" + ret_data['postCode'] + "\r\n"
                output += "海拔:" + ret_data['altitude'] + "\r\n"
                output += "天气情况:" + ret_data["weather"] + "\r\n"
                output += "温度:" + ret_data["temp"] + "\r\n"
                output += "最低气温:" + ret_data['l_tmp'] + "\r\n"
                output += "最高气温:" + ret_data['h_tmp'] + "\r\n"
                output += "风向:" + ret_data['WD'] + "\r\n"
                output += "风力:" + ret_data['WS'] + "\r\n"
                output += "日出时间:" + ret_data['sunrise'] + "\r\n"
                output += "日落时间:" + ret_data['sunset'] + "\r\n"
                print(output)
                return True
            else:
                print('网络或者服务器出错')
                return False


if __name__ == "__main__":
    weather = weather()
    weather.mainHandle()
