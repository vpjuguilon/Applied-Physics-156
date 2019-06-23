import matplotlib.pyplot as plt
import matplotlib.animation as anim
from numpy.random import random, randint

def plot_cont(fun, 1000):
    y = []
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    def update(i):
        yi = random()
        y.append(yi)
        x = range(len(y))
        ax.clear()
        ax.plot(x, y)


    a = anim.FuncAnimation(fig, update, frames=1000, repeat=False)
    plt.show()
