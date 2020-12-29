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

from helpers.weather_fs import get_weather
from helpers.city_codes import get_city_code

# load env variables
from dotenv import load_dotenv
load_dotenv()

owm_key = os.getenv("OWM_KEY")
city_code = get_city_code('Cuenca-EQ')

weather_data = get_weather(city_code, owm_key)
print(weather_data)



