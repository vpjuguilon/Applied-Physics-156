from numpy.random import randint, random
from matplotlib.pyplot import plot, show, xlim, ylim, scatter, subplots, title, axes
from numpy import sqrt
from matplotlib import animation
from matplotlib.widgets import Slider

L = 100 
N = 100
village = []
T = 1
l = 0.7120

for counter in range(N):
    x = randint(0, 100)
    y = randint(0, 100)
    village.append([x,y])

def distance(list):
    total = 0
    previous = list[N-1]
    for address in list:
        total += sqrt( (address[0]-previous[0])**2 + (address[1]-previous[1])**2 )
        previous = address
    return total


def flip(list, p, l, N):
    if p+l < N:
        list[p:p+l+1] = reversed(list[p:p+l+1])
        return list
    else:
        list = list+list
        list[p:p+l+1] = reversed(list[p:p+l+1])
        return list[int(N/2)-1: int(N/2)+N-1]
    

xpoints = []
ypoints = []

def animate(i):
    #T = sTemp.val
    global village, T
    T *= 0.999
    China = village[:]
    xpoints = []
    ypoints = []
    p = randint(0, N)
    l = randint(1, N/2)
    subdivision = flip(China, p, l, N)
    if (distance(subdivision) < distance(village)) or random()<T:
        village = subdivision
    for house in village:
        xpoints.append(house[0])
        ypoints.append(house[1])
    xpoints.append(xpoints[0])
    ypoints.append(ypoints[0])
    line.set_xdata(xpoints)
    line.set_ydata(ypoints)
    line2.set_xdata(xpoints)
    line2.set_ydata(ypoints)
    title(('L='+ str(distance(village))+ ' T='+ str(T)))
    xlim(0, 100)
    ylim(0, 100)



fig, ax = subplots()
line, = ax.plot(xpoints, ypoints, 'k-')
line2, = ax.plot(xpoints, ypoints, 'ro', markersize=2)
#axTemp = axes([0.19, 0.05, 0.65, 0.02], facecolor='lightgoldenrodyellow')
#sTemp = Slider(axTemp, 'Temp', 0.000001, 1.0, valinit=T)
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=0.01)
#ani.save('polymer_chains.html')
show()
