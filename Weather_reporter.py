import requests
import os
from dotenv import load_dotenv
from datetime import datetime

class WeatherManager:
    def __init__(self,api_key):
        self.api_key=api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.forecast_url= "http://api.openweathermap.org/data/2.5/forecast"
    
    def get_current_weather(self,city):
        if not isinstance(city,str) or not city.strip():
            return "City must be an non-empty string. Try to call the function again."
        
        params={'q':city, 'appid':self.api_key, 'units':'metric'}
        response=requests.get(self.base_url,params=params)
        return response.json()
    
    def get_forecast(self,city):
        if not isinstance(city,str) or not city.strip():
            return "City must be an non-empty string. Try to call the function again."
        
        params={'q':city, 'appid':self.api_key, 'units':'metric'}
        response=requests.get(self.forecast_url,params=params)
        return response.json()

    def today_forcast(self,data):
        if int(data.get("cod")) != 200:
            print("An error occured while getting the data from the server.")
            return
        
        today=datetime.now().strftime('%Y-%m-%d')
        print(f"Forecast for {today}:-")

        for i in data['list']:
            if i['dt_txt'].startswith(today):
                time = i['dt_txt'].split(" ")[1]
                temp = i['main']['temp']
                description = i['weather'][0]['description']
                print(f"Time: {time} | Temp: {temp}°C | {description.capitalize()}")
    
    def forecast_report(self,data):
        pass

    def display_current_report(self,data):
        if int(data.get("cod")) != 200:
            print("An error occured while getting the data from the server.")
            return
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']

    # Formatting the output
        print(f"--- Weather Report for {city} ---")
        print(f"Condition: {desc.capitalize()}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print("-" * 30)


#main
if __name__ == "__main__":
    
    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")
    bot=WeatherManager(api_key)
    data=bot.get_current_weather("Dhanbad") 
    #you can change the name as per your requirement or the script as module. I need a teacher and don't have money. Help!!!!
    bot.display_current_report(data)


    forcast_data=bot.get_forecast("Dhanbad")
    #print(forcast_data)

    bot.today_forcast(forcast_data)

