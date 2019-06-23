from matplotlib.pyplot import plot, show, xlabel, ylabel, legend
from numpy import linspace, arctan, pi, sqrt


def gain(omega, R):
    L = 1e-3
    C = 1e-6
    return abs(C*L*omega**2/(-C**2*L**2*omega**4 + 1j*C**2*L*omega**3*R + 3.0*C*L*omega**2 - 1j*C*omega*R - 1.0))


def pshift(omega, R):
    holder = []
    L = 1e-3
    C = 1e-6
    for w in omega:
        if 1/(w*L) < w*C:
            holder.append(-arctan(sqrt(-R/(w*L) + R*w*C)))
        else:
            holder.append(arctan(sqrt(R / (w * L) - R * w * C)))
    return holder


def power(omega, r):
    l = 1e-3
    c = 1e-6
    I = 1j
    return abs(-I*c*omega*(c*l*omega**2 - 1.0)/(c*omega*(c*l**2*omega**3 - I*c*l*omega**2*r - 3.0*l*omega + I*r) + 1.0))**2*0.5*r



omega = linspace(10000, 70000, 1000)
plot(omega, gain(omega, 30), 'k-', label='R=5')
plot(omega, gain(omega, 32), 'r-', label='R=10')
plot(omega, gain(omega, 34), 'g-', label='R=300')
plot(omega, gain(omega, 36), 'b-', label='R=500')
plot(omega, gain(omega, 38), 'y-', label='R=?')
xlabel('omega')
ylabel('Vo/Vi')
legend()
show()

plot(omega, power(omega, 500)*2*500, 'r-', label='R=10')
xlabel('omega')
ylabel('power(omega)')
legend()
show()
