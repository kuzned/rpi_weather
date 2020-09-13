from yahoo_weather.weather import YahooWeather

class CurrentWeather:
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
        return self.temperature
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return self.wind_speed
    
    def getCity(self):
        return self.city

if __name__=="__main__":
    current_weather = CurrentWeather("Yekaterinburg")
    print("%s %sC %s wind speed %s km/h"
           %(current_weather.getCity(),
           current_weather.getTemperature(),
           current_weather.getWeatherConditions(),
           current_weather.getWindSpeed()))