from math import cos, acos, pi, sqrt, sin

class City:
    def __init__(self, name, lat, lon, temp):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.temp = temp
    def describe(self):
        print("Die Koordinaten von %s sind %f Lat und %f Lon. Die Temperatur beträgt %.1f Grad Celcius." %(self.name, self.lat, self.lon, self.temp))
    def info(self):
        print("Die Koordinaten von %s sind %.1f Lat und %.1f Lon." %(self.name, self.lat, self.lon))
    
#def distanceneu(c1, c2): 
   # a1 = c1.lon
    #a2 = c2.lon
    #b1 = c1.lat
    #b2 = c2.lat 
    # Erdradius in km
    #r = 6378
    # länge auf lat berechnen               
    #return r*acos(cos(b1)*cos(b2)*cos(a1-a2)+sin(b1)*sin(b2))

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
    dilat = diffGamma(city1.lat, city2.lat)
    dilon = diffGamma(city1.lon, city2.lon)
    return distanceBase(dilat, dilon)

def tempDiff(city1, city2):
    return abs(city1.temp - city2.temp)


def distStart():
    stg = City("Stuttgart", 48.7758459, 9.1829321, 22)
    ber = City("Berlin", 52.521918, 13.413215, 21)
    ham = City("Hamburg", 53.551085, 9.993682, 24)
    nür = City("Nürnberg", 49.452030, 11.076750, 22)
    fra = City("Frankfurt", 50.110922, 8.682127, 23)

    cities = [stg, ber, ham, nür, fra]

    for c in cities:
        c.describe()

    for i in range(0,len(cities)):
        for j in range(i +1, len(cities)):
            c1 = cities[i]
            c2 = cities[j]
            dist = distance(c1, c2)
            tDiff = tempDiff(c1, c2)
            if dist == 0:
                continue
            print("Die Luftlinie von %s nach %s beträgt %.2f Kilometer. Der Temperaturunterschied beträgt %.1f Grad Celcius" % (c1.name, c2.name, dist, tDiff))
