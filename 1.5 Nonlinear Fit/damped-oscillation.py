from numpy import sin, e, arange, pi, linspace, array
from matplotlib.pyplot import plot, show
from numpy.random import uniform, random
from scipy.optimize import curve_fit
from scipy.stats import chi2
from scipy.special import gammainc


def sinusoid(t, a , b, c, d):
    return a*sin(b*t + c) * e**(-d*t)


density = []
for loops in range(1):
    t = arange(0, 3*pi, 0.3*pi)
    T = linspace(0, 3*pi, 1000)
    param = [1, 1, 0, 0.1]
    yhold = []
    for i in t:
        yhold.append(sinusoid(i, param[0], param[1], param[2], param[3]) + 0.4*random() - 0.2)
    y = array(yhold, float)
    plot(t, y, 'k.')
    popt, pcov = curve_fit(sinusoid, t, y, bounds=(0, 2))

    zhold = []
    for j in T:
        zhold.append(sinusoid(j, popt[0], popt[1], popt[2], popt[3]))
    z = array(zhold, float)
    plot(T, z, 'b-')
    print(popt)
    show()
chisq0 = chi2(y)
print(chisq0)


