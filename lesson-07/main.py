"""Selenium"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

def test():
    path = 'C:\Program Files (x86)\Google\chromedriver.exe'
    url = 'https://www.transfermarkt.ru/'

    #driver = webdriver.Chrome(path)
    driver = webdriver.Safari()

    driver.get(url)

    query = driver.find_element_by_name('query')
    query.send_keys('Messi')
    query.submit()

    players_url = driver.find_elements_by_css_selector('td.hauptlink a')
    all_players = []
    players_url = [i.get_attribute('href') for i in players_url][:10]

    for i in players_url:
        try:
            driver.get(i)
            time.sleep(2)
            player = driver.find_element_by_css_selector('div.dataName h1').text
            goals = driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]\
            /div[2]/div[2]/div[3]/a/span')
            assists = driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]\
            /div[2]/div[2]/div[5]/a/span')
            goals_to_integer = int(goals.text)
            assists_to_integer = int(assists.text)
            goals_and_assists = goals_to_integer + assists_to_integer
            player_details = {
                'Name': player,
                'Goals + Assists': goals_and_assists
            }
        except:
            player_details = {
                'Name': None,
                'Goals + Assists': None
            }
        all_players.append(player_details)

    driver.close()

    pd.DataFrame(all_players).to_csv('players.csv')

def auth(driver, url):

    driver.get(url + "/desktop")

    # time.sleep(1)

    password = driver.find_element_by_name("password")
    password.send_keys("531651&Gelios")

    login = driver.find_element_by_name("login")
    login.send_keys("3213876")

    login.submit()


url = "https://mail.ukr.net"

driver = webdriver.Safari()

auth(driver, url)

time.sleep(5)

letters_url = driver.find_elements_by_css_selector('td.msglist__row-subject a')

#print(letters_url)

letters_url = [i.get_attribute('href') for i in letters_url][:10]

all_letters = []

for i in letters_url:

    try:
        driver.get(i)
        time.sleep(5)

        sender = driver.find_element_by_xpath('//*[@id="readmsg"]/div[2]/section/div[1]/div/div[4]/div[1]/a/em').text
        text = driver.find_element_by_xpath('//*[@id="readmsg"]/div[2]/section/div[2]/div[1]/span/span[2]/div/p[4]/b/i/span')
        date = driver.find_element_by_xpath('//*[@id="readmsg"]/div[2]/section/div[1]/div/div[3]').get_attribute('title')
        subject = driver.find_element_by_xpath('//*[@id="readmsg"]/div[2]/section/div[1]/h3').text


        letter_details = {
            'sender': sender,
            'date': date,
            'subject': subject,
            'text': text
        }
    except:
        letter_details = {
            'sender': None,
            'date': None,
            'subject': None,
            'text': None
        }

    all_letters.append(letter_details)

#time.sleep(5)

driver.close()

pd.DataFrame(all_letters).to_csv('letters.csv')


