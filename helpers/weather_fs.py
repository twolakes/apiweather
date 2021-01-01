import requests
from datetime import datetime

def get_weather(city_codes, api_key=0):

    # build url w query params
    base_url = 'http://api.openweathermap.org/data/2.5/group'
    units = 'imperial'      # 'imperial' or 'metric'
    key_str = ''.join(['&appid=', api_key]) if api_key else ''

    url_full = f'{base_url}?id={city_codes}{key_str}&units={units}'
    # print(url_full)    # <<<<<<<<<<< REMOVE

    # request
    response = requests.request("GET", url_full)
    return response.content
    

def parse_hrly_rpt(weather_data):
    # set weather data observation d/t in location's local time
    obs_time = datetime.utcfromtimestamp(weather_data['dt'] + weather_data['sys']['timezone'])

    # build report elements
    time_str = obs_time.strftime("%Y-%m-%d %H:%M:%S").ljust(21)
    location_str = f"{weather_data['name'][0:13].upper()} {weather_data['sys']['country']}".ljust(18)
    temp_str = f"{weather_data['main']['temp']:3.0f}F ({weather_data['main']['feels_like']:3.0f}F)".rjust(14)
    wind_str = f"{weather_data['wind']['speed']:5.1f} mph/{weather_data['wind']['deg']}".rjust(16)
    cond_str = f"{4 * ' '}{weather_data['weather'][0]['description']}"    
    
    hrly_weather_rpt = f"\n{time_str}{location_str}{temp_str}{wind_str}{cond_str}"
    
    return hrly_weather_rpt







