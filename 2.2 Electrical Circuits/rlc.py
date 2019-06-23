from matplotlib.pyplot import plot, show, xlabel, ylabel, legend
from numpy import linspace, arctan, pi, sqrt


def gain(w, R):
    L = 1e-3
    C = 1e-6
    return abs((w*L*1j)/(R - w**2*R*L*C + w*L*1j))


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


omega = linspace(20000, 45000, 1000)
plot(omega, gain(omega, 100), 'r-', label='R=100')
plot(omega, gain(omega, 300), 'g-', label='R=300')
plot(omega, gain(omega, 900), 'b-', label='R=900')
plot(omega, gain(omega, 2700), 'k-', label='R=2700')
xlabel('omega')
ylabel('Vo/Vi')
legend()
show()

plot(omega, pshift(omega, 100), 'r-', label='R=100')
plot(omega, pshift(omega, 300), 'g-', label='R=300')
plot(omega, pshift(omega, 900), 'b-', label='R=900')
plot(omega, pshift(omega, 2700), 'k-', label='R=2700')
xlabel('omega')
ylabel('phase(Vo)')
legend()
show()
