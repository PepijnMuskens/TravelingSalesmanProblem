from random import randint

class Optimizer:
    def __init__(self, distances):
        self.distances = distances

    def distanceChecker(self, path):
        dist = 0
        for i in range(len(path) - 1):
            dist += self.distances[path[i]][path[i + 1]]
        return dist
        

    def randomSwapper(self, path, dist):
        path2 = path.copy()
        swapindex1 = randint(1, len(path) -2)
        swapindex2 = randint(1, len(path) -2)
        swap = path2[swapindex1]
        path2[swapindex1] = path2[swapindex2]
        path2[swapindex2] = swap
        if dist > self.distanceChecker(path2):
            path = path2
            dist = self.distanceChecker(path2)
        return path
    

    def k_optImprover(self, path, dist, k):
        connections = []
        swapindexes = []
        if(k > len(path) - 2): return
        for i in range(len(path) - 1):
            connections.append([path[i],path[i+1]])
        
        # get unique indexes
        i = 0
        while i < k:
            swapindex = randint(1, len(connections) -1)
            if swapindex not in swapindexes:
                swapindexes.append(swapindex)
                i += 1
                
        return