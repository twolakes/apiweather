# API WEATHER TRACKER
# Tracks weather data (from openweather api) at a specified interval
# for a specified list of locations.  Prints a row of data for each
# call at each location.
# 
# Pending:
# Calls for data every 5 min or other frequent interval.  Reports general
# data every hour or other longer interval, but report immediately when
# a significant change in conditions is detected for a location.
#


import os
from dotenv import load_dotenv
import requests
import json
import datetime
import time

from helpers.weather_fs import get_weather, parse_hrly_rpt
from helpers.city_codes import get_city_code
from helpers.sys_help import clear_terminal

# load env variables
from dotenv import load_dotenv
load_dotenv()

# initialize
call_interval = 1800      # in seconds
owm_key = os.getenv("OWM_KEY")
city_list = ['Cuenca-EQ', 'La Libertad-EQ']

time_start = time.time()
city_codes = [str(get_city_code(city)) for city in city_list]

clear_terminal()
print(f"\n***** Tracking weather data for {', '.join(city_list)}") 

# main loop
while True:
    # call for weather data
    response = get_weather(','.join(city_codes), owm_key).decode('UTF-8')
    weather_data = json.loads(response)

    # output data
    for location in weather_data['list']:
        hrly_weather_rpt = parse_hrly_rpt(location)
        print(hrly_weather_rpt)
    
    time.sleep(call_interval - ((time.time() - time_start) % call_interval))

 



