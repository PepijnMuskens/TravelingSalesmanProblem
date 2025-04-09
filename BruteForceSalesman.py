import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from random import randint
points = []
distances = [[]]
with open('PointsGen.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    index = 0
    for row in data:
        if(row[0] != 'x;y'):
            point = row[0].split(';')
            points.append([int(point[0]),int(point[1]), index])
            index += 1
#get distances between all nodes
for i in range(len(points)):
    distances.append([])
    for j in range(len(points)):
        distances[i].append(0)
        distances[i][j] = math.sqrt((points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1]))
    



# Find mst T of graph
unvisited = points.copy()

visited = []
rndindex = randint(0,len(unvisited) - 1)
visited.append(unvisited[rndindex])
unvisited.remove(unvisited[rndindex])

connections = []
for i in range(len(points) -1):
    shortestdist = 1000000
    connections.append([0,0])
    for vis in visited:
        for unvis in unvisited:
            if(distances[vis[2]][unvis[2]] < shortestdist):
                shortestdist = distances[vis[2]][unvis[2]]
                connections[i] = [vis[2], unvis[2]]

    visited.append(points[connections[i][1]])
    unvisited.remove(points[connections[i][1]])
print(connections)
    
# Isolate Set of odd-degree Vertices S
oddindexes = []
for i in range(len(points)):
    count = 0
    for con in connections:
        if con[0] == i or con[1] == i:
            count +=1
    if count % 2 != 0:
        oddindexes.append(i)
print(oddindexes)

# find min weight perfect matching M of S

class shortestdistancesolver:
    def __init__(self):
        self.shortestpath = []
        self.currentpath = []
        for i in range(int(len(oddindexes)/2)):
            self.currentpath.append([])
        self.shortestdistodds = -1
        self.depth = -1

    def linkoddsreqursive(self, remainingindexes, distance):
        self.depth += 1
        if(len(remainingindexes) < 2):
            if self.shortestdistodds == -1 or distance < self.shortestdistodds:
                self.shortestdistodds = distance    
                self.shortestpath = self.currentpath
            return distance
        for index in remainingindexes:
            if len(remainingindexes) % 2 != 0:
                break
            remainingindexes.remove(index)
            for index2 in remainingindexes:
                distance += distances[index][index2]
                passalonglist = remainingindexes.copy()
                passalonglist.remove(index2)
                self.currentpath[self.depth] = [index, index2]
                self.linkoddsreqursive(passalonglist, distance)
                self.depth -= 1
        return self.shortestdistodds
    
sds = shortestdistancesolver()
sds.linkoddsreqursive(oddindexes, 0)
print(sds.shortestpath)

# Combine T and M into multigraph G
connections += sds.shortestpath
print(connections)

# generate Eulerian tour of G

EulerianTour = [connections[0][0]]
lastcrossing = -1
RemovedEdges = []
while(len(connections) > 0):
    for connection in connections:
        foundstep = False
        if EulerianTour[-1] in connection:
            foundstep = True
            RemovedEdges.append(connection)
            connection.remove(EulerianTour[-1])
            EulerianTour.append(connection[0])
            connections.remove(connection)
            break
    if not foundstep:
        i = len(EulerianTour) -1
        putbacklist = []
        while i > 0:
            free = False
            for step in connections:
                if EulerianTour[i] in step:
                    free = True
                    break
            if(free):break
            putbacklist.append([EulerianTour[i],EulerianTour[i-1]])
            EulerianTour.pop(i)
            i -= 1
        connections += putbacklist
            

print(EulerianTour)

# Generate TSP from Eulerian tour