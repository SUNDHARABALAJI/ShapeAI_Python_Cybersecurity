import requests
from datetime import datetime
api_key='c762da0f60395af8f03eb46aaed3e295'
location=input("Enter the city name : ")

complete_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
humidity=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']

date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


with open("F:/Weather.txt",'w') as file:
  file.write("---------------------------------------------------------------------------------\n")
  file.write("Weather status for - {} || {} \n".format(location.upper(),date_time))
  file.write("---------------------------------------------------------------------------------\n")
  file.write("Current Temperature is: {:.2f} deg C\n".format(temp_city))
  file.write("Current Weather desc  : {}\n".format(weather_desc))
  file.write("Current Humidity      : {} %\n".format(humidity))
  file.write("Current Wind Speed    : {} kmph\n".format(wind_spd))

with open('F:/Weather.txt','r') as file:
    print(file.read())
