import requests
from aip import AipOcr

image = requests.get('https://static.pandateacher.com/7b5d6d8d9dea5691705d04fef2306b52.png').content

APP_ID = '16149264'
API_KEY = 'yxYg9r4OuAs4fYvfcl8tqCYd'
SECRET_KEY = 'yWg3KMds2muFsWs7MBSSFcgMQl8Wng4s'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)
if 'words_result' in res.keys():
    for item in res['words_result']:
        print(item['words'])
else:
    print(res)
