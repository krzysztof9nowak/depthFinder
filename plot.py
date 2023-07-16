import serial
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('tkagg')

ser = serial.Serial('/dev/ttyUSB0', 115200)
ticks = []
amplitudes = []
transmission = False

plt.ion()

while True:
    l = ser.readline().decode('ASCII').strip()
    if l.endswith('cm'):
        pass
    elif l == 'S':
        ticks = []
        amplitudes = []
        transmission = True
    elif l == 'F' and transmission:
        transmission = False
        ticks = np.array(ticks).astype('float32')
        amplitudes = np.array(amplitudes)

        prescaler = 321
        speedOfSound = 1500
        coreFreq = 48e6
        dist = (speedOfSound * ticks * prescaler) / coreFreq / 2

        plt.clf()
        plt.plot(dist, amplitudes)
        plt.ylim((0, 2500))
        plt.draw()
        plt.pause(0.0001)
        plt.gcf()

    elif ' ' in l:
        t, a = l.split(' ')
        ticks.append(int(t))
        amplitudes.append(int(a))
