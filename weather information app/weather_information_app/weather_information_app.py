import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re
import json
from dotenv import load_dotenv
import os
acronym_of_state_name = input("Please enter the acronym of state in uppercase you live in: ")

page = requests.get("http://www.geonames.org/postalcode-search.html?q=&country=US&adminCode1={0}".format(acronym_of_state_name))
soup = BeautifulSoup(page.content, 'html.parser')

city = soup.find(class_="restable")

lon_and_lat = [ll.get_text() for ll in city.select("a small")]
zipcode = [zp.get_text() for zp in city.select("tr td")][2::9]
city_name = [city.get_text() for city in city.select("tr td")][1::9]

STATE = pd.DataFrame({
            "city": city_name,
            "zip code": zipcode,
            "longitude and latitude": lon_and_lat})

print(STATE)
identifier = input("Please enter the ZIP code: " )

lon_lat = STATE.loc[STATE['zip code'] == identifier]

lon_lat1 = list(lon_lat["longitude and latitude"])[0]

lon_lat2 = list(lon_lat1.split("/"))

longitude_latitude = lon_lat2[0:7]

latitude = longitude_latitude[0]
longitude = longitude_latitude[1]




url = f"https://api.darksky.net/forecast/{api_key}/{latitude},{longitude}"

response = requests.get(url)
weather_information = json.loads(response.text)
weather = weather_information["currently"]
print("-------------------------------------")
print("Today's Weather: ")
print("....." + "summary: " + weather["summary"])
print("....." + "icon: " + weather["icon"])
print("....." + "temperature: " + "{0:,.2f}".format(weather["temperature"]))
print("-------------------------------------")
print("Suggestion: ")
if weather["icon"] == "rain":
    print("..." + "Take an Umbrella")
else:
    pass
if float(weather["temperature"]) > 70:
    print("..." + " Wear Your T-Shirt And Shorts")
else:
    print("..." + "Wear Your Long Sleeves And Pants")
print("Have a Good Day!")

print("-------------------------------------")
