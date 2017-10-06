import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyANTUayx1TPQk3pSQX4OMvHdjGuRFI3NWo')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
mode = "transit"
directions_result = gmaps.distance_matrix("10540 Thailand",
                                     "10540 Thailand",
                                     mode=mode,
                                     departure_time=now)
print("It would take {} from {} to {} by {}".format(directions_result['rows'][0]['elements'][0]['duration']['text'], directions_result['origin_addresses'][0], directions_result['destination_addresses'][0], mode))
new = gmaps.places_autocomplete("Singapore Polytechnic")
for thenew in new:
    print(thenew["description"])