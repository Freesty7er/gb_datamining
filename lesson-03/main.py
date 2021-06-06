from bs4 import BeautifulSoup
import requests
import lxml
from fake_headers import Headers
import json
from pymongo import MongoClient


def RabotaUA(vacancy_name, vacancy_list):
    header = Headers(headers=True).generate()
    site_head = 'https://rabota.ua/'
    url = 'https://rabota.ua/zapros/'+vacancy_name+'/украина'

    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.content, 'lxml')
    #print(soup.prettify())

    unprocessed_vacancy = soup.select('h2.card-title a.ga_listing')
    unprocessed_salary = soup.select('span.salary')


    for i,value in enumerate(unprocessed_vacancy):

        salary = unprocessed_salary[i].string
        if salary is None:
            salary = '0.00  грн'
        vacancy = {
            'Name': value['title'],
            'SiteLink': site_head + value['href'],
            'Salary': salary.replace(u'\xa0', u''),
            'Site': 'rabota.ua'
        }

        vacancy_list.append(vacancy)


def GRC(vacancy_name, vacancy_list):
    header = Headers(headers=True).generate()
    site_head = 'https://grc.ua/'
    url = 'https://grc.ua/vacancies/'+vacancy_name

    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.content, 'lxml')
    #print(soup.prettify())

    unprocessed_vacancy = soup.select('span.g-user-content a.bloko-link')
    unprocessed_salary = soup.select('div.vacancy-serp-item__sidebar span')
    #print(unprocessed_salary)

    for i, value in enumerate(unprocessed_vacancy):

        salary = unprocessed_salary[i].string
        if salary is None:
            salary = '0.00  грн'

        vacancy = {
            'Name': value.string,
            'SiteLink': site_head + value['href'],
            'Salary': salary.replace(u'\u202f', u''),
            'Site': 'grc.ua'
        }

        vacancy_list.append(vacancy)

def mdb_insert(document, db):
    #print(document['SiteLink'])

    result = db.vacancy.find( { "SiteLink": document['SiteLink']} )

    if result.count() == 0:
        print(document)
        db.vacancy.insert_one(document)

vacancy_list = []

RabotaUA('грузчик', vacancy_list)

GRC('gruzchik', vacancy_list)

#print(vacancy_list)

mongo_client = MongoClient('localhost', 27017)
db = mongo_client['lesson_03']

for i, value in enumerate(vacancy_list):
    #print(value)
    mdb_insert(value, db)

#with open('vacancy.json', mode='w', encoding='utf-8') as l:
#    json.dump(vacancy_list, l, indent=4)
