from math import *

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    def describe(self):
        print("die Koordinaten von %s sind %f Lat und %f Lon." %(self.name, self.lat, self.lon))

def diffGamma(alpha, beta):  
    # differenz von winkel alpha zu Winkel beta
    dGamma = alpha - beta 
    dGammaRad = pi / 180 * dGamma
    # Erdradius in km
    r = 6378
    # länge auf lat berechnen               
    return r*sqrt(2*(1-cos(dGammaRad)))        
    
def distanceBase(dilat, dilon):
    # insgesammte länge berechnen
    return sqrt(dilon**2 + dilat**2)

def distance(city1, city2): 
    c1 = city1
    c2 = city2
    dilat = diffGamma(city1.lat, city2.lat)
    dilon = diffGamma(city1.lon, city2.lon)
    return distanceBase(dilat, dilon)

def main():
    stg = City("Stuttgart", 48.7758459, 9.1829321)
    ber = City("Berlin", 52.521918, 13.413215)
    ham = City("Hamburg", 53.551085, 9.993682)

    cities = [stg, ber, ham]

    for c in cities:
        c.describe()

    for i in range(0,len(cities)):
        for j in range(i +1, len(cities)):
            c1 = cities[i]
            c2 = cities[j]
            dist = distance(c1, c2)
            if dist == 0:
                continue
            print("Die Luftlinie von %s nach %s beträgt %.2f Kilometer." % (c1.name, c2.name, dist))

main()
