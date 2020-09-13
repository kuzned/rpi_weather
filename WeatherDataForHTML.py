from yahoo_weather.weather import YahooWeather
import time

class WeatherData:
    temperature = ''
    weather_conditions = ''
    wind_speed = ''
    city = ''
    
    def __init__(self, city):
        self.city = city
        
        weather = YahooWeather(APP_ID="Your App ID",
            api_key="Your API KEY",
            api_secret="Your API secret")
        weather.get_yahoo_weather_by_city(self.city)
        
        self.temperature = weather.condition.temperature
        self.weather_conditions = weather.condition.text
        self.wind_speed = weather.wind.speed
        
    def getTemperature(self):
        return str(self.temperature) + " C"
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return str(self.wind_speed) + " kph"
    
    def getCity(self):
        return self.city
        
    def getTime(self):
        return time.ctime()

if __name__=="__main__":

    current_weather = WeatherData("Yekaterinburg")
    print(current_weather.getTemperature())
    print(current_weather.getWeatherConditions())
    print(current_weather.getWindSpeed())
    print(current_weather.getTime())