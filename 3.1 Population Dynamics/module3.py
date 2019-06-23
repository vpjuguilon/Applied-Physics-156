from matplotlib.pyplot import plot, show, scatter, hist, xlabel, ylabel
from numpy import linspace
def f(x, r):
    return 4*r*x*(1-x)

X = [0.65]
for i in range(40):
    X.append(f(X[i], 0.87))
plot(X, 'k.--')
xlabel('n')
ylabel('x(n)')
show()