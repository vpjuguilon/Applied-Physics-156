from math import sin, cos
from numpy import arange, pi, sin, array
from matplotlib.pyplot import plot, xlabel, ylabel, show, figure, rcParams, ylim, xlim, grid
import matplotlib.animation as animation



def f(x,t):
    phi = x[0]
    omega = x[1]
    theta = x[2]
    r = 0.25
    a = 0
    wd = 2/3
    return array([omega, -r*omega -sin(phi) + a*cos(theta), wd], float)


a = 0.0
b = 500
N = 2000
h = (b-a)/N
wd = 2/3

tpoints = arange(a, b, h)
Phi = []
Omega = []
PhiPoin = []
OmegaPoin = []
TPoin = []
x = array([pi/2, 0, 0], float)

for t in tpoints:
    phiVal = x[0]
    if phiVal < -pi:
        while phiVal < -pi:
            phiVal += 2*pi
    elif phiVal > pi:
        while phiVal > pi:
            phiVal -= 2*pi
    Phi.append(phiVal)

    omegaVal = x[1]
    if omegaVal < -pi:
        while omegaVal < -pi:
            omegaVal += 2*pi
    elif omegaVal > pi:
        while omegaVal > pi:
            omegaVal -= 2*pi
    Omega.append(omegaVal)

    tj = 2*pi/wd
    if t%tj < 0.2 and t > 100:
        PhiPoin.append(phiVal)
        OmegaPoin.append(omegaVal)
        TPoin.append(t)

    k1 = h*f(x, t)
    k2 = h*f(x+0.5*k1, t+0.5*h)
    k3 = h*f(x+0.5*k2, t+0.5*h)
    k4 = h*f(x+k3, t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints, Phi, 'k-')
xlabel('t (s)')
ylabel('phi (rad)')
grid()
show()
plot(Phi, Omega, 'k-', linewidth=0.5)
xlabel('phi')
ylabel('omega')
grid()
show()
plot(PhiPoin, OmegaPoin, 'k.')
xlabel('phi')
ylabel('omega')
grid()
show()
print(TPoin)


fig = figure(figsize=(5, 5), facecolor='w')
ax = fig.add_subplot(1, 1, 1)
rcParams['font.size'] = 15
lns = []

for i in range(len(Phi)):
    ln, = ax.plot([0, 0.25*sin(Phi[i])], [0, -0.25*cos(Phi[i])], 'k--.', lw=1)
    tm = ax.text(-0.3, 0.3, 'time = %.1fs' % tpoints[i])
    lns.append([ln, tm])
    print(i)
ax.set_aspect('equal', 'datalim')
ax.grid()
ani = animation.ArtistAnimation(fig, lns, interval=65, blit=True)
ylim(-0.4, 0.4)
xlim(-0.4, 0.4)
show()
