from matplotlib.pyplot import plot, show, xlabel, ylabel, legend
from numpy import linspace, arctan, pi, sqrt, sin, arange, multiply, array
from numpy.fft import rfft, irfft, rfftfreq
from matplotlib.pyplot import plot, show, xlim
from scipy.signal import sawtooth

f = 3
L = 1e-3
C = 1e-6
wRes = 1/sqrt(L*C)
sawtoothFreq = (f*wRes)/(2*pi)
period = 1/sawtoothFreq

def gain(w):
    R = 5
    return abs((-w*L*1j)/(-R + w**2*R*L*C - w*L*1j))



samples = 2500
T = linspace(0, 3*period, samples)
signal = sawtooth(2*pi*2*pi*sawtoothFreq*T)
plot(T/period, signal, 'k.')
xlabel('t/T')
ylabel('Vi(t)')
xlim(0,0.49)
show()

signalfft = rfft(signal)
signalGain = []
GainArr = []

d = 3*period/samples
n = len(signal)
frequencies = rfftfreq(n,d)
print(len(frequencies))

for k in range(len(signalfft)):
    GainArr.append(gain(frequencies[k]))
    signalGain.append(gain(frequencies[k])*signalfft[k])

newSignal = irfft(array(signalGain, complex))

plot(frequencies, abs(signalfft))
xlabel('omega')
ylabel('fourier amplitude')
show()

plot(abs(array(GainArr, complex)))
xlabel('omega')
ylabel('gain(omega)')
show()
plot(frequencies)
show()
plot(abs(array(signalGain, complex)))
xlabel('omega')
ylabel('signal gain')
show()
plot(T/period, newSignal,'k.')
xlabel('t/T')
ylabel('Vo(t)')
xlim(0, 0.5)
show()





