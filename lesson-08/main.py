import pandas as pd
import requests

class mycsv():

    def __init__(self, url):
        self.url = url



    def getData(self):
        data = requests.get(self.url)
        file = open('data.csv', 'wb')
        file.write(data.content)
        file.close()

        return

    def processData(self):
        df = pd.read_csv('data.csv')
        self.df = df.loc[df['country'] == 'Украина']
        return self.df


if __name__ == "__main__":
    csvfile = mycsv("https://minzdrav.gov.ru/opendata/7707778246-grls/data-20170301T0000-structure-20151217T0000.csv")

    csvfile.getData()

    df = csvfile.processData()
    print(df)


