import requests
#import os
from datetime import datetime



api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#write data to a weather file usin append

file = open("app.txt","w")

hr                 = "\n-------------------------------------------------------------\n"
city_name          = "\nWeather Stats for - {}  || {}".format(location.upper(), date_time)
temperature        = "\nCurrent temperature is: {:.2f} deg C".format(temp_city)
weather            = "\nCurrent weather desc  :"+str(weather_desc)
humidity           = "\nCurrent Humidity      :"+str(hmdt)+ '%' 
wind               = "\nCurrent wind speed    :"+str(wind_spd) +'kmph'
file.write(hr)
file.write(city_name)
file.write(hr)
file.write(temperature)
file.write(weather)
file.write(humidity)
file.write(wind)

file.close()