from matplotlib.pyplot import plot, show, scatter, hist, xlabel, ylabel
from numpy import linspace
def f(x, r):
    return 4*r*x*(1-x)

R = 0.9642
xvals = linspace(0, 1, 1000)
ypara = f(xvals, R)
plot(xvals, xvals, 'k-')
plot(xvals, ypara, 'k-')


Xhistogram = [0.65]
for j in range(1000):
    Xhistogram.append(f(Xhistogram[j], R))

Xhistogram = Xhistogram[99:949]
Ypop = []
Xpop = []

for k in Xhistogram:
    Xpop.append(k)
    Ypop.append(f(k, R))
    Xpop.append(f(k, R))
    Ypop.append(f(k, R))
plot(Xpop, Ypop, 'k.-', linewidth = 0.1)
xlabel('x')
ylabel('f(x)')
show()

