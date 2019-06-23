from matplotlib.pyplot import plot, show, xlabel, ylabel, legend
from numpy import linspace, arctan, pi, sqrt, sin, arange, multiply, array
from numpy.fft import rfft, irfft
from matplotlib.pyplot import plot, show


def gain(w):
    fRatio = 1
    fRes = 1/sqrt(L*C)
    L = 10e-3
    C = 1e-6
    fRes = 1/sqrt(L*C)
    R = 2700
    return abs((w*L*1j)/(-C**2*L**2*w**4 + 1j*C**2*L*w**3*R + 3.0*C*L*w**2 - 1j*C*w*R - 1.0))


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


def sawtooth(t, PRD):
    holder = []
    for i in t:
        holder.append(i % PRD)
    return holder


samples = 10000
period = 1/30000                       #Period here
T = linspace(0, 3*period, samples)
Fhold = linspace(0, 3*(1/period), samples)
signal = sawtooth(T, period)
plot(T/period, signal, 'k.')
xlabel('t/T')
ylabel('Vi(t)')
show()

signalfft = rfft(signal)
signalGain = []
GainArr = []
for k in range(signalfft.size):
    GainArr.append(gain((k / 3) * (1/period)))
    signalGain.append(gain((k/3)*(1/period))*signalfft[k])

newSignal = irfft(array(signalGain, complex))

plot(abs(signalfft))
xlabel('omega')
ylabel('fourier amplitude')
show()
plot(abs(array(GainArr, complex)))
xlabel('omega')
ylabel('gain(omega)')
show()
plot(abs(array(signalGain, complex)))
xlabel('omega')
ylabel('signal gain')
show()
plot(T/period, array(newSignal, complex))
xlabel('t/T')
ylabel('Vo(t)')
show()





