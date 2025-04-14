import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from optimizer import Optimizer 
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

sindex = randint(0,len(points)-1)
index = sindex
visited = []
TSPtour = []
TSPtour.append(index)
visited.append(index)
for i in range(0, len(points)-1):
    dist = 1000000000
    closesed = -1
    for point in points:
        if distances[index][point[2]] < dist and point[2] not in visited:
            dist = distances[index][point[2]]
            closesed = point[2]
    index = closesed
    visited.append(index)
    TSPtour.append(index)
TSPtour.append(sindex)

opt = Optimizer(distances)


#newtour = opt.twoOpt(TSPtour, opt.distanceChecker(TSPtour))
#while TSPtour != newtour:
#    TSPtour = newtour
#    newtour = opt.twoOpt(TSPtour, opt.distanceChecker(TSPtour))

#for i in range(1000):
#    if TSPtour != newtour:
#        TSPtour = newtour
#        newtour = opt.twoOpt(TSPtour, opt.distanceChecker(TSPtour))
    #TSPtour = opt.two_optRandom(TSPtour, opt.distanceChecker(TSPtour))
#    pass

x = []
y = []
for node in TSPtour:
    x.append(points[node][0])
    y.append(points[node][1])
xnp = np.array(x)
ynp = np.array(y)
plt.plot(xnp,ynp)
plt.title('Distance: ' + str(opt.distanceChecker(TSPtour)))
plt.show()