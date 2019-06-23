from numpy import exp, linspace
from matplotlib.pyplot import plot, show
from math import gamma


def pdf(y):
    return 0.5**(7/2)*exp(-y/2)*y**(7/2-1)


chi = linspace(0, 20, 1000)
density = pdf(chi)
plot(chi, density)
show()
