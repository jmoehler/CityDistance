from distance import distance
from City     import City



distDict = {}

def calcOnce(leng,alleCities):
    for i in range(0,leng):
        for j in range(0, leng):
            c1 = alleCities[i]
            c2 = alleCities[j]
            dist = distance(c1, c2)
            if dist != 0:
                nameCon = c1.name + c2.name
                distDict[nameCon] = dist


def distance1(nameA, nameB):
    nameCon = nameA.name + nameB.name
    distDicta = distDict[nameCon]
    return distDicta

