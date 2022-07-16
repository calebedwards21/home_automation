import requests
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':

    config_path = './web_scraper/configs/tooele_weather.json'
    file = open(config_path)
    config = json.load(file)

    url=config['url']
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.title)

    # TODO : Parse html correctly
    print(soup.b)