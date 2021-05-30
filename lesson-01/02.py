import requests


url = 'https://api.weatherbit.io/v2.0/current'

qs = {"lat":"35.7796", "lon":"-78.6382", "key":"f00d554ea702438995e7e3ef47f89a8d","include":"minutely"}

response = requests.get(url,params=qs)

print(response.text)

f = open('response.txt', 'w')
f.write(response.text + '\n')