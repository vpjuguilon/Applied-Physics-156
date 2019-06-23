import time
from matplotlib import animation
import Adafruit_ADS1x15
from matplotlib.pyplot import plot, show, subplots


adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
adc.start_adc(0, gain=GAIN)

print('Reading ADS1x15 channel 0 for 5 seconds...')
start = time.time()
TimeArray = []
AnalogArray = []
fig, ax = subplots()
line, = ax.plot(TimeArray, AnalogArray)

def animate(i):
    value = adc.get_last_result()
    TimeArray.append(time.time() - start)
    AnalogArray.append(value)
    line.set_xdata(TimeArray)
    line.set_ydata(AnalogArray)
    print(i)
    return line,
    

adc.stop_adc()
ani = animation.FuncAnimation(fig, animate, frames=100000, interval=10)
show()