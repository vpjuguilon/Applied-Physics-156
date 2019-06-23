from numpy.random import random, randint
from random import randrange
from matplotlib.pyplot import plot, show, xlim, ylim, scatter, subplots
from numpy import arange, sqrt
from matplotlib import animation

loops = 1
totalLength = 0
length = 10
xpoints = [0]*length
ypoints = list(range(0, length, 1))
reverseCheck = 0
arraypoints = []
L = sqrt(length)
for i in range(length):
    arraypoints.append([xpoints[i],ypoints[i]])

fig, ax = subplots()
line, = ax.plot(xpoints, ypoints, 'k--.')
line2, = ax.plot(xpoints[len(xpoints)-1], ypoints[len(xpoints)-1], 'ro', markersize=2)



def forward():
    global xpoints, ypoints, arraypoints, reverseCheck, totalLength
    headx = xpoints[len(xpoints)-1]
    heady = ypoints[len(ypoints)-1]
    options = [[1,0],[-1,0],[0,-1],[0,1]]
    previous = [xpoints[len(xpoints)-2] - xpoints[len(xpoints)-1], ypoints[len(ypoints)-2] - ypoints[len(ypoints)-1]]
    options.remove(previous)
    random_index = randint(0,3)
    delta = options[random_index]
    newx = headx+delta[0]
    newy = heady+delta[1]

    if [newx,newy] in arraypoints:
        print('REVERSE!')
        reverseCheck = 1

    else:
        xpoints.append(newx)
        ypoints.append(newy)
        arraypoints.append([newx,newy])
        xpoints.pop(0)
        ypoints.pop(0)
        arraypoints.pop(0)



def reverse():
    global xpoints, ypoints, arraypoints, reverseCheck
    xpoints.reverse()
    ypoints.reverse()
    arraypoints.reverse()
    reverseCheck = 0


def animate(i):
    global totalLength, loops, L
    totalLength += sqrt( (xpoints[len(xpoints)-1]-xpoints[0])**2 + (ypoints[len(ypoints)-1]-ypoints[0])**2   )
    print("Relative average length: ", (totalLength/loops)/L)
    loops += 1
    forward()
    if reverseCheck == 1:
        reverse()
    line.set_xdata(xpoints)
    line.set_ydata(ypoints)
    line2.set_xdata(xpoints[len(xpoints)-1])
    line2.set_ydata(ypoints[len(xpoints)-1])

    if i%100 == 0: 

        xlim(min([min(xpoints),min(ypoints)])-10, max([max(xpoints),max(ypoints)])+5)
        ylim(min([min(xpoints),min(ypoints)])-10, max([max(xpoints),max(ypoints)])+5)



ani = animation.FuncAnimation(fig, animate, frames=1000, interval=1)
#ani.save('polymer_chains.html')
xlim(-50,50)
ylim(-50,50)
show()