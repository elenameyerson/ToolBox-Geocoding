from urllib.request import urlopen
import json
from pprint import pprint

#f = urlopen(url)
#response_text = f.read()
#response_data = json.loads(str(response_text, "utf-8"))

def lat_lon(data):

    results = data['results']
    dict1 = results[0]
    geo = dict1['geometry']
    loc = geo['location']
    longitude = loc['lng']
    latitude = loc['lat']

    return(longitude, latitude)
#print(lat_lon(response_data))


def encodeURL(location):
    url = "https://maps.googleapis.com/api/geocode/json?address=" + str(location)
    url = url.replace(' ', '%20')
    print(url)
    return url


def closestStop(lat, lon):
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=%s&lon=%s&format=json"%(lat, lon)
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))

    results = response_data['stop']
    dict1 = results[0]
    dist = dict1['distance']
    name = dict1['stop_name']
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
    return "The closest MBTA stop is %s and it is %f miles away."%(stop[0], stop[1])

print(findMBTA('Fenway%20Park'))
#print(encodeURL('Fenway%20Park'))
#print(lat_lon(encodeURL('Fenway%20Park')))
