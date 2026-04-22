import requests
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
    
    bot=WeatherManager("4e6fd757bc0e738b9c33c7822edb5411")
    data=bot.get_current_weather("Dhanbad")
    bot.display_current_report(data)


    forcast_data=bot.get_forecast("Dhanbad")
    #print(forcast_data)

    bot.today_forcast(forcast_data)

