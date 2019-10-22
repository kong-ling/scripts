import requests
from lxml import html

#url = 'https://movie.douban.com/'
#url = 'https://intelpedia.intel.com/Proxy_at_Intel#Proxy_Environment_Variables_to_set'
url = 'https://employeecontent.intel.com/content/news/home/circuithome.html'

page = requests.Session().get(url)
tree = html.fromstring(page.text)
result = tree.xpath('//td[@class="title"]//a/text()')
print(result)
