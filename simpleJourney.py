from distance import distance
from City     import City


stg = City("Stg", 48.7758459, 9.1829321, 22)    #Stuttgart
ber = City("Ber", 52.521918,  13.413215, 21)    #Berlin
ham = City("Ham", 53.551085,  9.993682,  24)    #Hamburg
nür = City("Nür", 49.452030,  11.076750, 22)    #Nürnberg
fra = City("Fra", 50.110922,  8.682127,  23)    #Frankfurt
düs = City("Düs", 51.2277411, 6.7734556, 20)    #Düsseldorf
köl = City("Köl", 50.941278,  6.958281,  10)    #Köln

alleCities = [stg, ber, ham, nür, fra, düs,köl]  

for i in range(0,len(alleCities)):
     for j in range(0, len(alleCities)):
        c1 = alleCities[i]
        c2 = alleCities[j]
        dist = distance(c1, c2)
        if dist != 0:
            print("Der A. von %s zu %s beträgt %.1fkm" %(c1.name,c2.name,dist) )

class Meneken:
    def __init__(self, toDo, start, ziel, name):
        self.done = []
        self.toDo = toDo
        self.distanceDone = 0
        self.start = start 
        self.ziel = ziel 
        self.standort = start
        self.name = name
        self.sleeps = 0
    def info(self):
        print("Hi wir bims %s, bims grad in %s, reisen von %s nach %s.W. bims schon %.1f viel km gerannt,hams %d mal übernachtet" 
            %(self.name, self.standort.name, self.start.name, self.ziel.name, self.distanceDone, self.sleeps))

    def move(self):
        if len(self.toDo) > 0:
            nextIndex = closestCity(self.standort, self.toDo)
            nextZiel = self.toDo.pop(nextIndex)
        else: 
            nextZiel = self.ziel
        distanze = distance(nextZiel,self.standort)
        self.distanceDone += distanze
        self.done.append(nextZiel)
        self.standort = nextZiel
        self.sleeps = len(self.done)

    def istAmZiel(self):
        return self.ziel in self.done
    


def closestCity(standort, ziele):
    shortest = ziele[0]
    shortestIdx = 0
    for t in range(1, len(ziele)):
        ziel1 = shortest
        ziel2 = ziele[t]
        if distance(standort, ziel1) > distance(standort, ziel2):
            shortest = ziel2
            shortestIdx = t

    return shortestIdx


jakiPapa = Meneken([fra, ham, nür, düs, köl], stg, ber, "jaki und Papaa")
while not(jakiPapa.istAmZiel()):
    jakiPapa.move()
    jakiPapa.info()



