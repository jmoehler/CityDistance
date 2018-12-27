from math import cos, pi, sqrt

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
    stg = City("Stg", 48.7758459, 9.1829321, 22)    #Stuttgart
    ber = City("Ber", 52.521918,  13.413215, 21)    #Berlin
    ham = City("Ham", 53.551085,  9.993682,  24)    #Hamburg
    nür = City("Nür", 49.452030,  11.076750, 22)    #Nürnberg
    fra = City("Fra", 50.110922,  8.682127,  23)    #Frankfurt  

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
            print("De Luftlinie %s, %s ist %.2fKm TempDiff:%.1fC" % (c1.name, c2.name, dist, tDiff))



