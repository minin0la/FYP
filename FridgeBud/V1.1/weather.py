import pyowm
import json

def get_observation(USER_LOCATION):
    try:
        owm = pyowm.OWM('a78e2cc0bcbe919d628ac38decd35a55')
        observation = owm.weather_at_place(USER_LOCATION)
        return observation
    except:
        message = "Please enable internet"
        return message

def get_weather_icon(USER_LOCATION):
    try:
        owm = pyowm.OWM('a78e2cc0bcbe919d628ac38decd35a55')
        # USER_LOCATION = "London,GB"
        observation = owm.weather_at_place(USER_LOCATION)
        result = json.loads(observation.to_JSON())["Weather"]["weather_icon_name"]
    except:
        result = "Error"
    return result

def get_weather(USER_LOCATION):
    owm = pyowm.OWM('a78e2cc0bcbe919d628ac38decd35a55')
    # USER_LOCATION = "London,GB"

    observation = owm.weather_at_place(USER_LOCATION)
    w = observation.get_weather()
    return w