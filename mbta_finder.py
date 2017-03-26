"""
Elena Meyerson
SoftDes Spring 2017

Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

from urllib.request import urlopen
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def lat_lon(data):

    results = data['results']
    dict1 = results[0]
    geo = dict1['geometry']
    loc = geo['location']
    longitude = loc['lng']
    latitude = loc['lat']
    return(latitude, longitude)


def encodeURL(place_name):
    GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
    place_name = place_name.replace(" ", "+")
    url = GMAPS_BASE_URL + "?address=" + place_name
    return url


def closestStop(lat, lon):
    MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
    MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
    url = MBTA_BASE_URL + "?api_key=" + MBTA_DEMO_API_KEY + "&lat=%s&lon=%s&format=json"%(lat,lon)
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    dist = response_data['stop'][0]['distance']
    name = response_data['stop'][0]['stop_name']
    return name, dist


def findMBTA(location):
    url = encodeURL(location)
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    loc = lat_lon(response_data)
    lat1 = loc[0]
    lon1 = loc[1]
    stop = closestStop(lat1,lon1)
    return "The closest MBTA stop is %s and it is %s miles away."%(stop[0], stop[1])

print(findMBTA('Fenway Park'))
