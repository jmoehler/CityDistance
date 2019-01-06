import pyproj


def distance(city1,city2):
    geod = pyproj.Geod(ellps='WGS84')
    angle1,angle2,distance = geod.inv(city1.lon, city1.lat, city2.lon, city2.lat)
    return distance/1000.0

def tempDiff(city1, city2):
    return abs(city1.temp - city2.temp)
    