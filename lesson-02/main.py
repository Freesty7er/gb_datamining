from bs4 import BeautifulSoup
import requests
import lxml
from fake_headers import Headers
import json


def RabotaUA(vacancy_name, vacancy_list):
    header = Headers(headers=True).generate()
    site_head = 'https://rabota.ua/'
    url = 'https://rabota.ua/zapros/'+vacancy_name+'/украина'

    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.content, 'lxml')
    #print(soup.prettify())

    unprocessed_result = soup.select('h2.card-title a.ga_listing')

    for i in unprocessed_result:
        vacancy = {
            'Name' : i['title'],
            'Link' : site_head + i['href'],
            'Site' : 'rabota.ua'
        }
        #print(i['href'])
        #print(i['title'])

        vacancy_list.append(vacancy)

def GRC(vacancy_name, vacancy_list):
    header = Headers(headers=True).generate()
    site_head = 'https://grc.ua/'
    url = 'https://grc.ua/vacancies/'+vacancy_name

    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.content, 'lxml')
    #print(soup.prettify())

    unprocessed_result = soup.select('span.g-user-content a.bloko-link')
    #print(unprocessed_result)

    for i in unprocessed_result:
        vacancy = {
            'Name' : i.string,
            'Link' : site_head + i['href'],
            'Site' : 'grc.ua'
        }
        #print(i['href'])
        #print(i['title'])

        vacancy_list.append(vacancy)

vacancy_list = []

RabotaUA('грузчик', vacancy_list)

GRC('gruzchik', vacancy_list)

#print(vacancy_list)

with open('vacancy.json', mode='w', encoding='utf-8') as l:
    json.dump(vacancy_list, l, indent=4)
