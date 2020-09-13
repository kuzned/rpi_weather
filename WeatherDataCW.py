from yahoo_weather.weather import YahooWeather

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
        
        self.temperature = float(weather.condition.temperature)
        self.weather_conditions = weather.condition.text
        self.wind_speed = float(weather.wind.speed)
        
    def getServoValue(self):
        temp_factor = (self.temperature*100)/30
        wind_factor = (self.wind_speed*100)/20
        servo_value = temp_factor-(wind_factor/20)
        
        if(servo_value >= 100):
            return 100
        elif (servo_value <= 0):
            return 0
        else:
            return servo_value
    
    def getLEDValue(self):   
        if (self.weather_conditions=='Thunderstorms'):
            return 2
        elif(self.weather_conditions=='Showers'):
            return 1    
        elif(self.weather_conditions=='Rain'):
            return 1
        else:
            return 0
    
    def getTemperature(self):
        return self.temperature
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return self.wind_speed
    
    def getCity(self):
        return self.city
    
if __name__=="__main__":

    current_weather = WeatherData("Yekaterinburg")
    print("%s %sC %s wind speed %s km/h"
           %(current_weather.getCity(),
           current_weather.getTemperature(),
           current_weather.getWeatherConditions(),
           current_weather.getWindSpeed()))

    weather = WeatherData('Yekaterinburg')
    print(weather.getServoValue())
    print(weather.getLEDValue())