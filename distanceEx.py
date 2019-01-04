from distance import distance, tempDiff
# how to use the distance calculations:
def distExample():
    from City import City
    stg = City("Stg", 48.7758459, 9.1829321, 22)    #Stuttgart
    ber = City("Ber", 52.521918,  13.413215, 21)    #Berlin
    ham = City("Ham", 53.551085,  9.993682,  24)    #Hamburg
    nür = City("Nür", 49.452030,  11.076750, 22)    #Nürnberg
    fra = City("Fra", 50.110922,  8.682127,  23)    #Frankfurt  
    düs = City("Düs", 51.2277411, 6.7734556, 20)    #Düsseldorf

    cities = [stg, ber, ham, nür, fra, düs]

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

distExample()


