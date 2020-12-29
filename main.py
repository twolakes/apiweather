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

from city_codes import get_city_code

# load env variables
from dotenv import load_dotenv
load_dotenv()

owm_key = os.getenv("OWM_KEY")
# print(owm_key)        # <<<<<< REMOVE



