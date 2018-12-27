from distance import distance
from City     import City


class Path:
    def __init__(self, todo, start ):
        self.visited = [start]  
        self.todo = todo 
    def currDistance():
        #berechnen aus den visited 
        #ausprobieren mit mehr als 1 stadt in visited
        pass
    def info(self):
        print ("visited: %s todo: %s" %(self.visited, self.todo))


        

stg = City("Stg", 48.7758459, 9.1829321, 22)    #Stuttgart
ber = City("Ber", 52.521918,  13.413215, 21)    #Berlin
ham = City("Ham", 53.551085,  9.993682,  24)    #Hamburg
nür = City("Nür", 49.452030,  11.076750, 22)    #Nürnberg
fra = City("Fra", 50.110922,  8.682127,  23)    #Frankfurt

alleCities = [ber, ham, nür, fra]


def closestCity1():
    numPfad = 3*len(alleCities) 
    allePfade = []
    for i in range(0,numPfad):
        p = Path(alleCities, stg)
        allePfade.append(p)

    for j in range(0,numPfad):
        allePfade [j].info()
        

# einen Pfad nehmen.
#zeile 8,9
#5 neue produzieren 
#sortieren mit di Papa
#dist von reproduzierten ausgeben





  #  if theBest == 0:
   #     theBest = dist(pop(theBest), ToDoA)
        
    #else:
     #   distA = dist(pop(theBest), ToDoA)
      #  if distA < dist(theBest):
       #     theBest = distA
        #else schau weiter bis es passt oder der String rausfliegt
 #return #keine Ahnung

closestCity1()