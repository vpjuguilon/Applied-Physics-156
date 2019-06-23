from scipy.special import ellipk, ellipkinc, ellipj
from scipy.constants import g
from numpy import sin, sqrt, linspace, deg2rad, array, arcsin, pi, real
from matplotlib.pyplot import plot, show, xlabel, ylabel, xlim, ylim, legend
from numpy.fft import fft


def period(phi, l):
    return 4*sqrt(l/1)*ellipk(sin(phi/2)**2)


phi0 = 0.999*pi
Period = period(phi0, 1)
t = linspace(0, Period, 1000)
SN, CN, dn, psi = ellipj(t, sin(phi0/2)**2)
Phi = 2*arcsin(sin(psi)*sin(phi0/2))
plot(t/Period, Phi/phi0, label='0.999 pi')
legend()
xlabel('t/T')
ylabel('phi/phi0')
show()

fourier = fft(Phi)
plot(abs(fourier), 'k.')
xlim(0, 14)
show()



