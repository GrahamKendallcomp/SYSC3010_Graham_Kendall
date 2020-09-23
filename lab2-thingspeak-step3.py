import httplib
import urllib
import requests 


URL = 'https://api.thingspeak.com/channels/1152829/feeds.json?api_key=JDS62ZBPQIVOEDGA&results=5'

data = requests.get(URL).json()

for i in data['feeds']:
    print(i['field1'])