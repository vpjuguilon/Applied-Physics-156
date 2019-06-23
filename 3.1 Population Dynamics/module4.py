from matplotlib.pyplot import plot, show, scatter, hist, xlabel, ylabel
from numpy import linspace
def f(x, r):
    return 4*r*x*(1-x)

X = [1/3]
for i in range(100):
    X.append(f(X[i], 0.97))
print(X)