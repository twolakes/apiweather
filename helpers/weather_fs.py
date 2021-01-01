import requests
from datetime import datetime

def get_weather(city_code, api_key=0):

    # build url w query params
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    units = 'imperial'      # 'imperial' or 'metric'
    key_str = ''.join(['&appid=', api_key]) if api_key else ''

    url_full = f'{base_url}?id={city_code}{key_str}&units={units}'
    # print(url_full)    # <<<<<<<<<<< REMOVE

    # request
    response = requests.request("GET", url_full)
    return response.content
    

def parse_hrly_rpt(weather_data):
    print(weather_data)
    time_str = datetime.utcfromtimestamp(weather_data['dt']).strftime("%Y-%m-%d %H:%M:%S").ljust(23)
