from distanceDict     import distance1

class Path:
    def __init__(self, todo, startCity,endCity ):
        self.visited = [startCity]  
        self.todo = todo 
        self.endCity = endCity
    def currDist(self):
        dist = 0
        for i in range(1,len(self.visited)):
            CityPrev = self.visited[i-1]
            CityI = self.visited[i]
            dist1 = distance1(CityPrev,CityI)
            dist += dist1 
        dist += distance1(self.visited[-1],self.endCity)
        return dist

    def __lt__(self,other):
        return self.currDist() < other.currDist()
        
        #konvertierung um stings mit print auszugeben
    def __str__(self):
        return "<visited: %s todo: %s End:%s, dist %.0f >" %(self.visited, self.todo, self.endCity, self.currDist())
    def __repr__(self):
        return self.__str__()
    


        