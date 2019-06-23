
from scipy.special import ellipk, ellipkinc, jacobi
from scipy.constants import g
from numpy import sin, sqrt, linspace, deg2rad, array, arcsin
from matplotlib.pyplot import plot, show, xlabel, ylabel, xlim, ylim


def period(phi, l):
    return 4*sqrt(l/1)*ellipk(sin(phi/2)**2)


def time(phi, amp, l):
    psi = arcsin(sin(phi/2)/sin(amp/2))
    return sqrt(l/g)*ellipkinc(psi, sin(amp/2)**2)




Amp = linspace(0, 180, 1000)
length = 1
Period = period(deg2rad(Amp), length)
plot(Amp, Period)

xlabel('Phi')
ylabel('T')
xlim(0, 180)
ylim(0)
show()
print(sin(deg2rad(30)))
