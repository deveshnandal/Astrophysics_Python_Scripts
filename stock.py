# Stock investment script
import numpy as np
import matplotlib.pyplot as plot
time        = np.arange(0, 30, 0.1);
amplitude   = np.sin(time/3)

plt.plot(time, amplitude)
plt.title('Stock summary')
plt.xlabel('Time$(Days)$')
plt.ylabel('N_${Stock performace}$')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()
plt.show()

import matplotlib.pyplot as plt
import math

# ------------------------------------------------------------------------
def get_amplitude(x):
    for amplitude_change in amplitude_changes:
        if x >= amplitude_change['x']:
            amplitude = amplitude_change['amplitude']

    return amplitude


# --------------------------------------------------------------------------
def y_func(x, amplitude):
    return amplitude * math.sin(x)

# --------------------------------------------------------------------------

amplitude_changes = [
                        {'x': -1, 'amplitude': 1},
                        {'x': 2.5, 'amplitude': 0.1},
                        {'x': 3.7, 'amplitude': 0.1},
                        {'x': 5.1, 'amplitude': 0.5},
                        {'x': 7.8, 'amplitude': 0.5},
                        {'x': 8.3, 'amplitude': 0.2},
                        {'x': 9.2, 'amplitude': 0.2},
                        {'x': 11.3, 'amplitude': 0.2},
                        {'x': 12.8, 'amplitude': 0.2},
                        {'x': 15.8, 'amplitude': 0.4},
                        {'x': 15.9, 'amplitude': 0.4},
                        {'x': 16.8, 'amplitude': 0.4},
                        {'x': 18.6, 'amplitude': 0.3},
                        {'x': 19.2, 'amplitude': 0.3},
                        {'x': 20.5, 'amplitude': 0.3},
                        {'x': 22.3, 'amplitude': 0.3},
                        {'x': 28.9, 'amplitude': 0.5},
                        {'x': 29.1, 'amplitude': 0.5},
                        {'x': 30, 'amplitude': 0.7},
                    ]

x_values = []
y_values = []

x = 0
max_x = 30
step = 0.1

while x <= max_x:
    x_values.append(x)
    amplitude = get_amplitude(x)
    y_values.append(y_func(x, amplitude))
    x += step

# ------------------------------------------------------------------------
def get_amplitude2(x2):
    for amplitude_change2 in amplitude_changes2:
        if x2 >= amplitude_change2['x2']:
            amplitude2 = amplitude_change2['amplitude2']

    return amplitude2


# --------------------------------------------------------------------------
def y_func(x2, amplitude2):
    return amplitude2 * math.sin(x2)

# --------------------------------------------------------------------------

amplitude_changes2 = [
                        {'x2': -1, 'amplitude2': 0.5},
                        {'x2': 6.5, 'amplitude2': 0.5},
                        {'x2': 6.7, 'amplitude2': 0.5},
                        {'x2': 9.1, 'amplitude2': 0.5},
                        {'x2': 9.2, 'amplitude2': 0.7},
                        {'x2': 9.4, 'amplitude2': 0.7},
                        {'x2': 10.2, 'amplitude2': 0.8},
                        {'x2': 10.8, 'amplitude2': 0.4},
                        {'x2': 11.6, 'amplitude2': 0.4},
                        {'x2': 12.3, 'amplitude2': 0.4},
                        {'x2': 13, 'amplitude2': 0.3},
                        {'x2': 15.9, 'amplitude2': 0.5},
                        {'x2': 20.6, 'amplitude2': 0.3},
                        {'x2': 21.2, 'amplitude2': 0.2},
                        {'x2': 22.5, 'amplitude2': 0.6},
                        {'x2': 23.3, 'amplitude2': 0.7},
                        {'x2': 25.9, 'amplitude2': 0.8},
                        {'x2': 27.1, 'amplitude2': 0.5},
                        {'x2': 30, 'amplitude2': 0.5},
                    ]

x_values2 = []
y_values2 = []

x2 = 0
max_x2 = 30
step2 = 0.1

while x2 <= max_x2:
    x_values2.append(x2)
    amplitude2 = get_amplitude2(x2)
    y_values2.append(y_func(x2, amplitude2))
    x2 += step2


# ------------------------------------------------------------------------
def get_amplitude3(x3):
    for amplitude_change3 in amplitude_changes3:
        if x3 >= amplitude_change3['x3']:
            amplitude3 = amplitude_change3['amplitude3']

    return amplitude3


# --------------------------------------------------------------------------
def y_func(x3, amplitude3):
    return amplitude3 * math.sin(x3)

# --------------------------------------------------------------------------

amplitude_changes3 = [
                        {'x3': -1, 'amplitude3': 0.1},
                        {'x3': 2.5, 'amplitude3': 0.1},
                        {'x3': 5.7, 'amplitude3': 0.1},
                        {'x3': 7.1, 'amplitude3': 0.2},
                        {'x3': 8.2, 'amplitude3': 0.1},
                        {'x3': 11.4, 'amplitude3': 0.1},
                        {'x3': 13.2, 'amplitude3': 0.3},
                        {'x3': 14.8, 'amplitude3': 0.3},
                        {'x3': 15.6, 'amplitude3': 0.1},
                        {'x3': 16.3, 'amplitude3': 0.1},
                        {'x3': 17, 'amplitude3': 0.4},
                        {'x3': 17.9, 'amplitude3': 0.4},
                        {'x3': 20.6, 'amplitude3': 0.4},
                        {'x3': 21.2, 'amplitude3': 0.9},
                        {'x3': 23.5, 'amplitude3': 0.9},
                        {'x3': 24.3, 'amplitude3': 0.5},
                        {'x3': 26.9, 'amplitude3': 0.5},
                        {'x3': 28.1, 'amplitude3': 0.8},
                        {'x3': 30, 'amplitude3': 0.8},
                    ]

x_values3 = []
y_values3 = []

x3 = 0
max_x3 = 30
step3 = 0.1

while x3 <= max_x3:
    x_values3.append(x3)
    amplitude3 = get_amplitude3(x3)
    y_values3.append(y_func(x3, amplitude3))
    x3 += step3


time        = np.arange(0, 30, 0.1);
amplitude   = np.sin(time/3)

plt.plot(time, amplitude,linestyle='dotted')
plt.plot(x_values, y_values,color='blue',linewidth=2., label="CF N Fertilizer")
plt.plot(x_values2, y_values2,color='black',linewidth=2., label="CI Health service")
plt.plot(x_values3, y_values3,color='red',linewidth=2., label="FTI Oil")
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.title('Stock Summary')
plt.xlabel('Time$(Weeks)$')
plt.ylabel('$N_{Stock performace}$')
leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})
plt.show()
