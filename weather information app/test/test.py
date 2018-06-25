import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re
import json
import os



State = "NY"
Zipcode = 10001
sample_longtitude_latitude = "40.748/-73.997"
#setup:
page = requests.get("http://www.geonames.org/postalcode-search.html?q=&country=US&adminCode1={0}".format(State))
soup = BeautifulSoup(page.content, 'html.parser')

city = soup.find(class_="restable")

lon_and_lat = [ll.get_text() for ll in city.select("a small")]
zipcode = [zp.get_text() for zp in city.select("tr td")][2::9]
city_name = [city.get_text() for city in city.select("tr td")][1::9]

STATE = pd.DataFrame({
            "city": city_name,
            "zip code": zipcode,
            "longitude and latitude": lon_and_lat})

identifier = "10001"

lon_lat = STATE.loc[STATE['zip code'] == identifier]

lon_lat1 = list(lon_lat["longitude and latitude"])[0]
#test:
assert lon_lat1 == sample_longtitude_latitude

weather_information_sample = {'time': 1529874290, 'summary': 'Mostly Cloudy', 'icon': 'partly-cloudy-day',
                              'nearestStormDistance': 14, 'nearestStormBearing': 78, 'precipIntensity': 0,
                              'precipProbability': 0, 'temperature': 80.23, 'apparentTemperature': 82.68,
                              'dewPoint': 67.35, 'humidity': 0.65, 'pressure': 1007.73, 'windSpeed': 5.79,
                              'windGust': 6.8, 'windBearing': 208, 'cloudCover': 0.66, 'uvIndex': 2,
                              'visibility': 9.84, 'ozone': 313.75}


# setup:
path = os.path.join(os.path.dirname(__file__), "example_responses.json")
example = open(path, "r")
weather_information = example
print(weather_information)
    #test:
    #assert weather_information == weather_information_sample
