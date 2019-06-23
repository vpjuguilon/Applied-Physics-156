from matplotlib.pyplot import plot, show, scatter, hist, legend, xlabel, ylabel, xlim, ylim
from numpy import linspace
def f(x, r):
    return 4*r*x*(1-x)




x1 = []
x2 = []
x4 = []
x6 = []
x8 = []
rval = linspace(0, 1, 750)

for j in rval:
    R = 0.87
    x1.append(f(j, R))
    x2.append(f(f(j, R), R))
    x4.append(f(f(f(f(j, R),R), R), R))
    x6.append(f(f(f(f(f(f(j, R),R), R), R), R), R))
    x8.append(f(f(f(f(f(f(f(f(j, R),R), R), R), R), R), R), R))

plot(rval, rval, 'k-')
plot(rval, x1, 'r-', label='f(x)')
plot(rval, x2, 'g-', label ='f2(x)')
plot(rval, x4, 'b-', label = 'f3(x)')
xlim(0, 1)
ylim(0, 1)
xlabel('x')
legend()
show()


for i in rval:
    X = [0.65]
    R = [i]
    for j in range(848):
        X.append(f(X[j], i))
    R = R*750
    X = X[99:949]
    plot(R, X, 'k,')
xlabel('r')
show()




rval2 = linspace(0.88, 1, 500)
for i in rval2:
    X = [0.65]
    R = [i]
    for j in range(598):
        X.append(f(X[j], i))
    R = R*500
    X = X[99:699]
    plot(R, X, 'k,')
xlabel('r')
show()



