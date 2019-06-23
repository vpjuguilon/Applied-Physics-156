from numpy.random import randint, rand
from numpy import zeros, exp
from matplotlib.pyplot import plot, imshow, show, xlim, ylim, subplots, axes
from matplotlib import animation
from matplotlib.widgets import Slider


spin = [-1, 1]
N = 150 
lattice = zeros((N,N), int)
T = 2.269           #units: J/kb



for i in range(N):
    for k in range(N):
        lattice[i, k] = spin[randint(0, 2)]
imshow(lattice)
show()

def update(i):
    T = sTemp.val
    bf = [0.5, exp(-4/T), exp(-8/T)]
    for x in range(N-1):
        for y in range(N-1):
            value = lattice[x,y]*(lattice[x-1,y] + lattice[x+1, y] + lattice[x, y-1] + lattice[x, y+1])
            if value < 0 or rand() < bf[int(abs(value/2))]:
                lattice[x, y] *= -1

    for j in range(N):
        lattice[0, j] = lattice[N-1, j]
        lattice[N-1, j] = lattice[1, j]
        lattice[j, 0] = lattice[j, N-1]
        lattice[j, N-1] = lattice[j, 1]
    
    matrice.set_array(lattice)


fig, ax = subplots()
matrice = ax.matshow(lattice)
axTemp = axes([0.19, 0.05, 0.65, 0.02], facecolor='lightgoldenrodyellow')
sTemp = Slider(axTemp, 'Temp', 0.000001, 15.0, valinit=T)

ani = animation.FuncAnimation(fig, update, frames=1000000, interval=0.2)
show()