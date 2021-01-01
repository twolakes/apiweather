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

# load env variables
from dotenv import load_dotenv
load_dotenv()

owm_key = os.getenv("OWM_KEY")
city_code = get_city_code('Key Largo')

response = get_weather(city_code, owm_key).decode('UTF-8')
weather_data = json.loads(response)
hrly_weather_rpt = parse_hrly_rpt(weather_data)

print(hrly_weather_rpt)

# mm/dd/yy hh:mm:ss    Cuenca EC    72F (76F)    4 mph / 90    broken clouds    



