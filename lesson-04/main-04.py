from fake_headers import Headers
from pprint import pprint
from lxml import html
import requests
import json

header = Headers(headers=True).generate()

url = "https://1kr.ua/m/"

response = requests.get(url,headers=header)

root = html.fromstring(response.text)
#print(response.text)

news_list = []

find_news = root.xpath("//a[contains(@class,'post-link')]")
for news in find_news:

    href = news.xpath("./@href")
    name = news.xpath("./article/h2/text()")
    date_time = news.xpath("./article/p[@class='meta']/time/text()")

    news_descr = {
        'site': '1kr',
        'title': name,
        'link': href,
        'date': date_time
    }

    news_list.append(news_descr)
    print(news_descr)
    # /html/body/main/section[1]/a[2]/article/h2

with open('news_list.json', 'w') as fp:
    json.dump(news_list, fp)