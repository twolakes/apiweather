# apiweather working project
# uses openweather api to monitor weather
# for specified location(s).
# provides hourly updates and alerts when
# conditions change
#

import os
from dotenv import load_dotenv
import requests
import json
import datetime

from helpers.weather_fs import get_weather, parse_hrly_rpt
from helpers.city_codes import get_city_code
from helpers.sys_help import clear_terminal

# load env variables
from dotenv import load_dotenv
load_dotenv()

owm_key = os.getenv("OWM_KEY")
city_list = ['La Libertad-EQ', 'Cuenca-EQ']
city_codes = ''
for city in city_list:
    city_codes += ','
    city_codes += str(get_city_code(city))

clear_terminal()

response = get_weather(city_codes[1:], owm_key).decode('UTF-8')
weather_data = json.loads(response)
for location in weather_data['list']:
    hrly_weather_rpt = parse_hrly_rpt(location)
    print(hrly_weather_rpt)



# mm/dd/yy hh:mm:ss    Cuenca EC    72F (76F)    4 mph / 90    broken clouds    



