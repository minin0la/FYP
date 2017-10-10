# actual tempreture(High/Low)
# 1 week forecast
# wind/huminity
# cloud status
import pyowm
import json

def get_observation():
    try:
        owm = pyowm.OWM('a78e2cc0bcbe919d628ac38decd35a55')
        USER_LOCATION = "648324"

        # Search for current weather in London (UK)
        observation = owm.weather_at_place(USER_LOCATION)
        # w = observation.get_weather()
        # the_list = json.loads(observation.to_JSON())
        # print(the_list["reception_time"])

        # # Weather details
        # wind_speed = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
        # humidity = w.get_humidity()              # 87
        # temperature = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        # message = "The weather info in {}.\nThe temperature is {}\nThe wind speed is {} m/s\nThe humidity is {}\n".format(the_list["Location"]["name"], temperature['temp'], wind_speed["speed"], humidity)
        # return the_list
        return observation
    except:
        message = "Please enable internet"
        return message

def get_weather_icon():
    owm = pyowm.OWM('a78e2cc0bcbe919d628ac38decd35a55')
    USER_LOCATION = "648324"
    observation = owm.weather_at_place(USER_LOCATION)
    result = json.loads(observation.to_JSON())["Weather"]["weather_icon_name"]
    return result

def get_weather():
    owm = pyowm.OWM('a78e2cc0bcbe919d628ac38decd35a55')
    USER_LOCATION = "648324"

    observation = owm.weather_at_place(USER_LOCATION)
    w = observation.get_weather()
    return w
