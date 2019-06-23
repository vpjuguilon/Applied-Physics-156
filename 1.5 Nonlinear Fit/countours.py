from numpy import sin, e, arange, pi, linspace, array
from matplotlib.pyplot import plot, show
from numpy.random import uniform, random
from scipy.optimize import curve_fit
from scipy.stats import chisquare
from scipy.special import gammainc


def chisq(randata, data):
    holder1 = []
    for counterx in range(len(data)):
        holder1.append(data-randata)
    return sum(holder1)**2


def sinusoid(t, a , b, c, d):
    return a*sin(b*t + c) * e**(-d*t)


from scipy.special import ellipk, ellipkinc, ellipj
from scipy.constants import g
from numpy import sin, sqrt, linspace, deg2rad, array, arcsin, pi, real, arccos, meshgrid, cos, arange
from matplotlib.pyplot import plot, show, xlabel, ylabel, xlim, ylim, legend, contour, xticks
from numpy.fft import fft


def period(phi, l):
    return 4*sqrt(l/1)*ellipk(sin(phi/2)**2)


param = [1, 1, 0, 0.1]
DATA = []
t = arange(0, 3*pi, 0.3*pi)
for countera123 in t:
    DATA.append(sinusoid(countera123, param[0], param[1], param[2], param[3]))


a = linspace(-0.05, 0.2, 100)
b = linspace(-0.4, 1.4, 100)
A, B = meshgrid(a, b)
Z = []
for countera in a:
    for counterb in b:
        yhold = []
        for i in t:
            yhold.append(sinusoid(i, countera, counterb, param[2], param[3]) + 0.4*random() - 0.2)
        y = array(yhold, float)
        Z.append(chisq(y, DATA))


contour(A, B, Z)
show()
