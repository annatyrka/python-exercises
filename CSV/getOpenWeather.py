import requests
import sys
import json

api_id = 'aa823e736be4be8ccde8e43f6c7af2cd'

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s ' % (
    location, api_id)

response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
print(response.text)
