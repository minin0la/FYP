import googlemaps
from datetime import datetime
from dataIO import fileIO

gmaps = googlemaps.Client(key='AIzaSyANTUayx1TPQk3pSQX4OMvHdjGuRFI3NWo')

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

def get_travel_time():
# Request directions via public transit
    settings = fileIO("data/settings.json", "load")
    start = settings[0]["Home"]
    end = settings[0]["Location 1"]
    now = datetime.now()
    driving = gmaps.distance_matrix(start, end,
                                    mode="driving",
                                    departure_time=now)
    driving = driving['rows'][0]['elements'][0]['duration']['text']
    walking = gmaps.distance_matrix(start, end,
                                    mode="walking",
                                    departure_time=now)
    walking = walking['rows'][0]['elements'][0]['duration']['text']
    # bicycling = gmaps.distance_matrix("10540 Thailand",
    #                                 "10540 Thailand",
    #                                 mode="bicycling",
    #                                 departure_time=now)
    # bicycling = bicycling['rows'][0]['elements'][0]['duration']['text']
    transit = gmaps.distance_matrix(start, end,
                                    mode="transit",
                                    departure_time=now)
    try:
        transit = transit['rows'][0]['elements'][0]['duration']['text']
    except KeyError:
        transit = "Not Available"
    origin = gmaps.distance_matrix(start, end,
                                    mode="transit",
                                    departure_time=now)
    origin = origin['origin_addresses'][0]
    destination = gmaps.distance_matrix(start, end,
                                    mode="transit",
                                    departure_time=now)
    destination = destination['destination_addresses'][0]
    return ("Traffic Status: Driving: {}, Walking: {}, Transit: {}".format(driving, walking, transit), destination)

def get_travel_time2():
# Request directions via public transit
    settings = fileIO("data/settings.json", "load")
    start = settings[0]["Home"]
    end = settings[0]["Location 2"]
    now = datetime.now()
    driving = gmaps.distance_matrix(start, end,
                                    mode="driving",
                                    departure_time=now)
    driving = driving['rows'][0]['elements'][0]['duration']['text']
    walking = gmaps.distance_matrix(start, end,
                                    mode="walking",
                                    departure_time=now)
    walking = walking['rows'][0]['elements'][0]['duration']['text']
    # bicycling = gmaps.distance_matrix("10540 Thailand",
    #                                 "10540 Thailand",
    #                                 mode="bicycling",
    #                                 departure_time=now)
    # bicycling = bicycling['rows'][0]['elements'][0]['duration']['text']
    transit = gmaps.distance_matrix(start, end,
                                    mode="transit",
                                    departure_time=now)
    try:
        transit = transit['rows'][0]['elements'][0]['duration']['text']
    except KeyError:
        transit = "Not Available"
    origin = gmaps.distance_matrix(start, end,
                                    mode="transit",
                                    departure_time=now)
    origin = origin['origin_addresses'][0]
    destination = gmaps.distance_matrix(start, end,
                                    mode="transit",
                                    departure_time=now)
    destination = destination['destination_addresses'][0]
    return ("Traffic Status: Driving: {}, Walking: {}, Transit: {}".format(driving, walking, transit), destination)