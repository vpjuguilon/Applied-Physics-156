
from matplotlib.pyplot import plot, show, scatter, hist, xlabel, ylabel
from numpy import linspace
def f(x, r):
    return 4*r*x*(1-x)

Xhistogram = [0.65]
R3 = 0.934
for j in range(100000):
    Xhistogram.append(f(Xhistogram[j], R3))
hist(Xhistogram, bins=350)
xlabel('f(x)')
ylabel('frequency')
show()
