from numpy import zeros, array, sqrt, pi, sin, cos, log
from numpy.random import random, randint
from matplotlib.pyplot import plot, imshow, figure, show, gray, subplots, colorbar
import matplotlib.animation as animation
from matplotlib.cm import gray
from matplotlib import animation

arr=[]
dimension = 600
center = int(dimension/2)
xf = zeros((dimension,dimension), int)
xf[int(center),int(center)] = 1
rx = 0
ry = 0
rmax = 0
stop = 0
rs = 3
rkill = 7
rd = 5
imshow(xf)
show()
N = 0


def occupy():
    global rx, ry
    phi = random()*2*pi
    rx = int(rs*cos(phi))
    ry = int(rs*sin(phi))

def jump():
    global rx, ry
    r = randint(1,5)
    if r == 1: rx += 1
    elif r == 2: rx -= 1
    elif r == 3: ry += 1
    elif r == 4: ry -= 1

def check():
    x, y = rx, ry
    r = sqrt(x**2 + y**2)
    if r > rkill: return 'k'
    elif r >= rd: return 'c'
    elif xf[rx+1+center,ry+center] + xf[rx-1+center,ry+center] + xf[rx+center,ry+1+center] + xf[rx+center, ry-1+center] > 0:
        return 'a'
    else:
        return 'j'
    
def aggregate():
    global stop, rmax, rs, rd, rkill, N
    xf[center+rx,center+ry] = 1
    N += 1
    x, y = rx, ry
    rmax = max([rmax, sqrt(x**2 + y**2)])
    rs = rmax + 5
    rd = rmax + 7
    rkill = rmax + 15

    if rmax > 200: 
        stop = 1


def circlejump():
    global rx, ry
    phi = random()*2*pi
    x, y = rx, ry
    r = sqrt(x**2 + y**2)
    rx += int((r-rs)*cos(phi))
    ry += int((r-rs)*sin(phi))



def update(i):
    print(i)
    value = check()
    if value == 'k': 
        #print('k')
        occupy()
        jump()
    elif value == 'a': 
        #print('a')
        aggregate()
        occupy()
        jump()
    elif value == 'j':
        #print('j')
        jump();
    elif value == 'c':
        #print('c')
        circlejump()
    matrice.set_array(xf)

occupy()
fig, ax = subplots()
matrice = ax.matshow(xf)


ani = animation.FuncAnimation(fig, update, frames=1000000, interval=0.01)
show()