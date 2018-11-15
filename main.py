from distanceCalc import City, distance


stg = City("Stuttgart", 48.7758459, 9.1829321, 22)
ber = City("Berlin", 52.521918, 13.413215, 21)
ham = City("Hamburg", 53.551085, 9.993682, 24)
nür = City("Nürnberg", 49.452030, 11.076750, 22)
fra = City("Frankfurt", 50.110922, 8.682127, 23)



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
        print("Hallo wir bims %s und bims grad in %s und reisen von %s nach %s. Wir bims schon %.1f viel km gerannt und habms %d mal übernachtet" 
            %(self.name, self.standort.name, self.start.name, self.ziel.name, self.distanceDone, self.sleeps))

    def move(self):
        if len(self.toDo) > 0:
            nextZiel = self.toDo.pop(0)
        else: 
            nextZiel = self.ziel
        distanze = distance(nextZiel,self.standort)
        self.distanceDone += distanze
        self.done.append(nextZiel)
        self.standort = nextZiel
        self.sleeps = len(self.done)

    def istAmZiel(self):
        return self.ziel in self.done





jakiPapa = Meneken([fra, ham, nür], stg, ber, "jaki und Papaa")
while not(jakiPapa.istAmZiel()):
    jakiPapa.move()
    jakiPapa.info()
