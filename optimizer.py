import copy
from random import randint
from random import choice

class Optimizer:
    def __init__(self, distances):
        self.distances = distances

    def distanceChecker(self, path):
        dist = 0
        for i in range(len(path) - 1):
            dist += self.distances[path[i]][path[i + 1]]
        return dist
    
    def createPath(self, connections):
        path = []
        cons = copy.deepcopy(connections)
        startindex = cons[0][0]
        index = startindex
        path.append(index)
        for i in range(0,len(cons)):
            for con in cons:
                if index in con:
                    con.remove(index)
                    index = con[0]
                    con.remove(index)
                    path.append(index)
                    break
        return path
    
    def testfullconnectionpath(self, connections):
        i = 0
        cons = copy.deepcopy(connections)
        index = cons[0][0]
        while i < len(cons):
            found = False
            for con in cons:
                if index in con:
                    con.remove(index)
                    index = con[0]
                    con.remove(index)
                    found = True
                    i += 1
                    break
            if not found:
                return False
        return True

    def randomSwapper(self, path, dist):
        if(2 > len(path)): return
        path2 = copy.deepcopy(path)
        swapindex1 = randint(1, len(path) -2)
        swapindex2 = randint(1, len(path) -2)
        swap = path2[swapindex1]
        path2[swapindex1] = path2[swapindex2]
        path2[swapindex2] = swap
        if dist > self.distanceChecker(path2):
            path = path2
            dist = self.distanceChecker(path2)
        return path
    
    def twoOpt(self, path, dist):
        connections = []
        if(len(path) < 4): return
        for i in range(len(path) - 1):
            connections.append([path[i],path[i+1]])
        cons = copy.deepcopy(connections)
        for i in range(len(path)-1):
            shorterpathfound = False
            for j in range(i+2, len(path)-1):
                connections = copy.deepcopy(cons)
                path2 = self.two_optImprover(connections, path, i, j, dist)
                if path != path2:
                    shorterpathfound = True
                    break
            if shorterpathfound: break
            for j in range (0, i-1):
                connections = copy.deepcopy(cons)
                path2 = self.two_optImprover(connections, path, i, j, dist)
                if path != path2:
                    shorterpathfound = True
                    break
            if shorterpathfound: break
        return path2
    
    def two_optRandom(self, path, dist):
        connections = []
        if(len(path) < 4): return
        for i in range(len(path) - 1):
            connections.append([path[i],path[i+1]])
        
        # get unique connections not attatched
        index1 =  randint(0,len(path)-2)
        exclindexes = []
        exclindexes.append(index1)
        if(index1 + 1 > len(path) -2):
            exclindexes.append(0)
            exclindexes.append(index1 -1)
        else:
            exclindexes.append(index1 + 1)
            if(index1 - 1  < 0):
                exclindexes.append(len(path) -2)
            else:
                exclindexes.append(index1 - 1)
        index2 =  choice([i for i in range(0,len(path)-2) if i not in exclindexes])
        return self.two_optImprover(connections, path, index1, index2, dist)

    def two_optImprover(self, connections, path, index1, index2, dist):
        # try first swap option
        swap = connections[index1][0]
        connections[index1][0] = connections[index2][0]
        connections[index2][0] = swap
        if not (self.testfullconnectionpath(connections)):
            # second swap
            swap =  connections[index1][0]
            connections[index1][0] = connections[index2][1]
            connections[index2][1] = swap

        path2 = self.createPath(connections)
        newdist =  self.distanceChecker(path2)
        if newdist < dist:
            dist = newdist
            return path2
        return path