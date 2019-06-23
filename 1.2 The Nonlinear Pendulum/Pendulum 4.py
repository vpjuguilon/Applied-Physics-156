from scipy.special import ellipk, ellipkinc, ellipj
from scipy.constants import g
from numpy import sin, sqrt, linspace, deg2rad, array, arcsin, pi, real, arccos, meshgrid, cos, arange
from matplotlib.pyplot import plot, show, xlabel, ylabel, xlim, ylim, legend, contour, xticks
from numpy.fft import fft


def period(phi, l):
    return 4*sqrt(l/1)*ellipk(sin(phi/2)**2)


x = linspace(-pi, pi, 100)
y = linspace(-3, 3, 100)
X, Y = meshgrid(x, y)
Z = 0.5*Y**2 - cos(X)
contour(X, Y, Z, levels=[-1/2, 0, 1/2, 1, 3/2, 2])
xticks(arange(-pi, pi, pi/2))
show()

