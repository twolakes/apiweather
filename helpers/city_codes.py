# provides storage and handling of city
# for use with openweather api
#
# to look up location codes:  https://openweathermap.org
#

city_codes = {
    'Charleston SC': 4574324,
    'Colon-PAN': 3712076,
    'Cuenca-EQ': 3658666,
    'Key Largo': 4160795,
    'Kissimmee': 4160983,
    'La Libertad-EQ': 3655131,
    'Miami': 4164138,
    'Nassau-BAH': 3571824
}

def get_city_code(loc_name):
    return city_codes[loc_name]

