#das is ne schöne Stadt

class City:

    def __init__(self, name, lat, lon, temp):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.temp = temp

    def describe(self):
        print("%s:  %.1f Lat,  %.1f Lon Temp %.1fC" %(self.name, self.lat, self.lon, self.temp))
    
    def info(self):
        print("%s:  %.1f Lat,  %.1f Lon" %(self.name, self.lat, self.lon))
   
    def __str__(self):
        #return "%s (%.1f, %.1f)" %(self.name, self.lat, self.lon)
        return "%s" %(self.name)
   
    def __repr__(self):
        return self.__str__()





    