from scipy.special import ellipk, ellipkinc, ellipj
from scipy.constants import g
from numpy import sin, sqrt, linspace, deg2rad, array, arcsin, pi
from matplotlib.pyplot import plot, show, xlabel, ylabel, xlim, ylim, legend


def period(phi, l):
    return 4*sqrt(l/1)*ellipk(sin(phi/2)**2)


def time(phi, amp, l):
    psi = arcsin(sin(phi/2)/sin(amp/2))
    return sqrt(l/g)*ellipkinc(psi, sin(amp/2)**2)


AMP = array([pi/10, 4*pi/5, 19*pi/20, 99*pi/100, 999*pi/1000], float)
for phi0 in AMP:
    Period = period(phi0, 1)
    t = linspace(0, Period, 1000)
    SN, CN, dn, psi = ellipj(t, sin(phi0/2)**2)
    Phi = 2*arcsin(SN*sin(phi0/2))
    plot(t/Period, Phi/phi0, label=str(phi0/pi) + ' pi')
    legend()
xlabel('t/T')
ylabel('phi/phi0')
show()
