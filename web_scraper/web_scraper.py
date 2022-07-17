import requests
from bs4 import BeautifulSoup
import json
import influx

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
    temperature = int(temp[0].text[:-1])
    print(temperature)

    influx_client = influx.Influx_Client_V2()
    print(influx_client.client.ready())
    measurement = 'temp'
    tags = {'location':'Tooele'}
    fields = {'temperature':temperature}
    influx_client.write(measurement, tags, fields) 
    try:
        influx_client.write(measurement, tags, fields)    
    except:
        print('Write Error : Logging to local file for so no data is lost')
        # Log to local file
    
    influx_client.query('from(bucket:"my-bucket") |> range(start: -10m)')