import requests
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':

    config_path = '../web_scraper/configs/tooele_weather.json'
    file = open(config_path)
    config = json.load(file)

    url=config['url']
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.title)

    temp = ''
    for div in soup.find_all('div', {'data-testid':'ConditionsSummary', 'class':'DailyContent--ConditionSummary--1X5kT'}):
        temp = div.find_all('span', {'data-testid':'TemperatureValue', 'class':'DailyContent--temp--3d4dn'})
    print(temp)
    print(type(temp[0].text))