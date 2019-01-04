from City import City
from copy import deepcopy
from Path import Path
from time import time

stg = City("Stg", 48.7758459, 9.1829321, 22)    #Stuttgart
ber = City("Ber", 52.521918,  13.413215, 21)    #Berlin
ham = City("Ham", 53.551085,  9.993682,  24)    #Hamburg
nür = City("Nür", 49.452030,  11.076750, 22)    #Nürnberg
fra = City("Fra", 50.110922,  8.682127,  23)    #Frankfurt
düs = City("Düs", 51.2277411, 6.7734556,  9)    #Düsseldorf
hbn = City("Hdn", 49.1426929, 9.210879,  10)    #Heilbronn
hdh = City("Hdh", 48.6893963, 10.1610948, 2)    #Heidenheim
drs = City("Drs", 51.0504088, 13.7372621, 4)    #Dresden
prs = City("Prs", 48.856614,  2.3522219,  3)    #Paris

alleCities = [stg, ber, ham, nür, fra, düs, hbn, hdh, drs, prs]
alleTodo = [ham, nür, fra, düs, hbn, hdh, drs, prs]

start = time()

#numPfad = 3*len(alleTodo) 
allePfade = []

#generiere Pfad der in Stg anfangen
p = Path(alleTodo, stg, ber)
allePfade.append(p)

#gibt alle Pfade aus
#print(allePfade) 

neuePfade = []

#hohlt bei einem Pfad eine City aus todo raus
for q in range(0,len(alleTodo)):
    for p in allePfade:
        for i in range(0,len(p.todo)):
            newP = deepcopy(p)
            cityNeu = newP.todo.pop(i)
            newP.visited.append(cityNeu)
            #newP ist neuer Pfad am anfang identisch mit p
            #print("New path: %s" %(newP))
            #newP zu neuePfade
            neuePfade.append(newP)
    #print(neuePfade)
    #länge alle Pfade (ohne neuePfade)
    #print(len(allePfade))
    allePfade = neuePfade
    neuePfade = []
    #länge alle Pfade (mit neuePfade)
    #print(len(allePfade))

#länge der Pfade

smalestDist = allePfade[0].currDist()
shortestIndex = 0
for i in range(1,len(allePfade)):
    lengh = allePfade[i].currDist()
    #print(lengh)
    if lengh < smalestDist:
        smalestDist = lengh
        shortestIndex = i

done = time()

print(len(allePfade))
print("%.2fkm" %(smalestDist))
print(allePfade[shortestIndex])
print("%.2fs Laufzeit" %(done - start))


