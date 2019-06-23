from matplotlib.pyplot import plot, show, xlabel, ylabel, legend
from numpy import linspace, arctan, pi, sqrt, sin, arange, multiply, array
from numpy.fft import rfft, irfft, rfftfreq
from matplotlib.pyplot import plot, show, xlim
from scipy.signal import square

f = 1
l = 1e-3
c = 1e-6
wRes = 1/sqrt(l*c)
sawtoothFreq = (f*wRes)/(2*pi)
period = 1/sawtoothFreq
print(2*pi*sawtoothFreq)

def gain(omega):
    r = 500
    I = 1j
    return abs(c*l*omega**2*r/(c*l*omega**2*r + (I*c*l*omega**2 + c*omega*r - I)*(I*c*l*omega**2*r + l*omega - I*r)))



samples = 2500
T = linspace(0, 3*period, samples)
signal = square(2*pi*(2*pi*sawtoothFreq)*T)
plot(T/(period*0.158), signal, 'k--.')
plot([-5, 5], [0, 0], 'k-', linewidth=1)
xlabel('t/T')
ylabel('V$_i$(t)')
xlim(0, 3)
show()

signalfft = rfft(signal)
signalGain = []
GainArr = []

d = 3*period/samples
n = len(signal)
frequencies = rfftfreq(n,d)


for k in range(len(signalfft)):
    GainArr.append(gain(frequencies[k]))
    signalGain.append(gain(frequencies[k])*signalfft[k])

newSignal = irfft(array(signalGain, complex))

plot(frequencies, abs(signalfft))
xlabel('omega')
ylabel('fourier amplitude')
show()

plot(frequencies, abs(array(GainArr, complex)))
xlabel('omega')
ylabel('gain(omega)')
show()
plot(frequencies)
show()
plot(abs(array(signalGain, complex)))
xlabel('omega')
ylabel('signal gain')
show()
plot(T/(period*0.158), newSignal,'k.')
plot([-5, 5], [0, 0], 'k-', linewidth=1)
xlabel('t/T')
ylabel('V$_o$(t)')
xlim(0, 3)
show()






