from distance import distanceCalc
from City     import City



distDict = {}

def calcOnce(alleCities):
    leng = len(alleCities)
    for i in range(0,leng):
        for j in range(0, leng):
            c1 = alleCities[i]
            c2 = alleCities[j]
            dist = distanceCalc(c1, c2)
            nameCon = c1.name + c2.name
            distDict[nameCon] = dist


def distance(nameA, nameB):
    nameCon = nameA.name + nameB.name
    distDicta = distDict[nameCon]
    return distDicta

