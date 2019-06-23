from numpy import zeros, array, sqrt, pi, sin, cos, log
from numpy.random import random, randint
from matplotlib.pyplot import plot, imshow, figure, show, gray, close
import matplotlib.animation as anim
from matplotlib.cm import gray

p = 0.4
dimension = 1500
lattice = zeros((dimension,dimension), int)
center = int(dimension/2)
lattice[center, center] = 2
pointCheckList = [array([center,center],int)]
brake = 0
lattice2 = zeros((dimension,dimension), int)

def check(coordinate):
    global brake
    #
    if lattice[coordinate[0] + 1,coordinate[1]] == 0:
        if random() < p:
            lattice[coordinate[0] + 1,coordinate[1]] = 2
            pointCheckList.append(coordinate + [1,0])
        else:
            lattice[coordinate[0] + 1,coordinate[1]] = 1
    #
    if lattice[coordinate[0] - 1,coordinate[1]] == 0:
        if random() < p:
            lattice[coordinate[0] - 1,coordinate[1]] = 2
            pointCheckList.append(coordinate + [-1,0])
        else:
            lattice[coordinate[0] - 1,coordinate[1]] = 1
    #
    if lattice[coordinate[0],coordinate[1] + 1] == 0:
        if random() < p:
            lattice[coordinate[0],coordinate[1] + 1] = 2
            pointCheckList.append(coordinate + [0,1])
        else:
            lattice[coordinate[0],coordinate[1] + 1] = 1
    #
    if lattice[coordinate[0],coordinate[1] - 1] == 0:
        if random() < p:
            lattice[coordinate[0],coordinate[1] - 1] = 2
            pointCheckList.append(coordinate + [0,-1])
        else:
            lattice[coordinate[0],coordinate[1] - 1] = 1
    
    
    if coordinate[0] > 1490 or coordinate[1] > 1490:
        brake = 1

for i in pointCheckList:
    check(i)
    if brake == 1:
        break


Figure = imshow(lattice)
show()    




for j in range(dimension-1):
    for k in range(dimension-1):
        if random() < p:
            lattice2[j,k] = 1

imshow(lattice2)
show()




