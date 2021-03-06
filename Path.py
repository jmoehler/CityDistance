from distanceDict     import distance

class Path:
    def __init__(self, todo, startCity,endCity ):
        self.visited = [startCity]  
        self.todo = todo 
        self.endCity = endCity
        self.lastDist = 0
        self.lastDistVisited = []
    def currDist(self):
        if len(self.visited) == self.lastDistVisited:
            return self.lastDist
        dist = 0
        for i in range(1,len(self.visited)):
            CityPrev = self.visited[i-1]
            CityI = self.visited[i]
            dist1 = distance(CityPrev,CityI)
            dist += dist1 
        dist += distance(self.visited[-1],self.endCity)
        self.lastDist = dist
        self.lastDistVisited = len(self.visited)
        return dist

    def __lt__(self,other):
        return self.currDist() < other.currDist()
        
        #konvertierung um stings mit print auszugeben
    def __str__(self):
        return "<visited: %s todo: %s End:%s, dist %.0f >" %(self.visited, self.todo, self.endCity, self.currDist())
    def __repr__(self):
        return self.__str__()
    


        