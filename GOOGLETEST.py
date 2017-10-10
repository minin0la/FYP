import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key = 'AIzaSyANTUayx1TPQk3pSQX4OMvHdjGuRFI3NWo')

## Geocoding an address
geocode_result = gmaps.geocode('648324', {'country': 'Singapore'})

## Look up an address with reverse geocoding# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(geocode_result)
# print(geocode_result)