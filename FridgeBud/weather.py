# actual tempreture(High/Low)
# 1 week forecast
# wind/huminity
# cloud status
import pyowm

owm = pyowm.OWM('a78e2cc0bcbe919d628ac38decd35a55')
USER_LOCATION = "Singapore,SG"

# Search for current weather in London (UK)
observation = owm.weather_at_place(USER_LOCATION)
w = observation.get_weather()

# Weather details
wind_speed = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
humidity = w.get_humidity()              # 87
temperature = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print ("The weather info in {}.\nThe temperature is {}\nThe wind speed is {} m/s\nThe humidity is {}\n".format(USER_LOCATION, temperature['temp'], wind_speed["speed"], humidity))
