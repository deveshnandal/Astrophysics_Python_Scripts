import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt
#Sub-sample of your opacity table
#First 9 Values of log(T)
Mdot = [1.e-1, 1, 10]
#First 9 Values of log(rho)
M = [112053, -15., -14., -13., -12., -11., -10., -9., -8., -7., -6., -5., -4., -3., -2.]
# Opacity values for the corrsponginf log(T) and log(rho) reported above
Xc = [[-13.05, -12.62, -12.11, -11.51, -10.73, -9.79, -8.79, -7.79, -6.79, -5.79, -4.79, -3.79, -2.79, -1.79, -0.79],
     [-12.77, -12.35, -11.86, -11.29, -10.53, -9.58, -8.58, -7.59, -6.59, -5.59, -4.59, -3.59, -2.59, -1.59, -0.58],
     [-12.48, -12.08, -11.60, -11.06, -10.29, -9.34, -8.35, -7.36, -6.36, -5.36, -4.36, -3.36, -2.36, -1.36, -0.36],
     [-12.22, -11.82, -11.36, -10.83, -10.08, -9.15, -8.18, -7.19, -6.20, -5.20, -4.20, -3.20, -2.20, -1.20, -0.20],
     [-11.95, -11.57, -11.11, -10.60, -9.89, -8.99, -8.05, -7.10, -6.14, -5.17, -4.18, -3.18, -2.18, -1.18, -0.18],
    [-11.68, -11.32, -10.87, -10.37, -9.69, -8.84, -7.97, -7.10, -6.23, -5.32, -4.38, -3.41, -2.42, -1.42, -0.43],
    [-11.41, -11.06, -10.61, -10.13, -9.49, -8.70, -7.91, -7.14, -6.37, -5.57, -4.72, -3.79, -2.80, -1.80, -0.80],
    [-11.14, -10.80, -10.36, -9.88, -9.28, -8.55, -7.84, -7.16, -6.50, -5.80, -5.01, -4.08, -3.09, -2.09, -1.09],
    [-10.86, -10.54, -10.10, -9.62, -9.06, -8.39, -7.74, -7.15, -6.55, -5.89, -5.04, -4.07, -3.07, -2.07, -1.07],
    [-10.58, -10.27, -9.84, -9.36, -8.82, -8.20, -7.61, -7.09, -6.56, -5.88, -4.98, -4.00, -3.00, -2.00, -1.00],
    [-10.29, -10.00, -9.57, -9.10, -8.58, -8.00, -7.45, -6.98, -6.47, -5.47, -4.80, -3.82, -2.82, -1.83, -0.82],
    [-9.93, -9.72, -9.30, -8.83, -8.32, -7.78, -7.27, -6.83, -6.30, -5.49, -4.54, -3.59, -2.62, -1.63, -0.63],
    [-8.81, -8.93, -8.92, -8.56, -8.07, -7.54, -7.06, -6.62, -6.01, -5.10, -4.30, -3.47, -2.55, -1.60, -0.63],
    [-7.46, -7.87, -8.00, -8.06, -7.77, -7.29, -6.82, -6.36, -5.68, -4.91, -4.26, -3.54, -2.76, -1.94, -1.06],
    [-7.40, -7.40, -7.40, -7.38, -7.25, -6.95, -6.55, -6.08, -5.41, -4.82, -4.33, -3.71, -3.08, -2.34, -1.63]]
#Compute a function that performs a 2D interpolation by taking x, y and z as inputs
#The function below does perform extrapolation. Read more about the documentation about this function at https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.interp2d.html
f = interpolate.interp2d(Mdot, M, Xc, kind='cubic')
# Compute the opacity value that you need, depending on the (log(rho),log(T)) given
# Example z_opacity = f(-15, 1.8)
z_int = f(-15.5, 1.85)
z_int1 = f(-17.00, 3.7877)
print("My opacity value = "+str(z_int1))




import math
import pandas as pd
import matplotlib.pyplot as plt
M_GR = [112053,223591,449661,925661,1903890]
Accr_rate = [1.00e-1,1.00,10.00,100.00,1000.00]


x2 = [0.1]
y2 = [112053]
x3 = [1]
y3 = [223591]
x4 = [10]
y4 = [449661]
x5 = [100]
y5 = [925661]
x6 = [1000]
y6 = [1903890]

a = 100000
b = 2060000
plt.axhspan(a, b, color='c', alpha=0.5, lw=0)
plt.plot(Accr_rate,M_GR, color='black', linewidth=2.5)

plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x4, y4, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x5, y5, marker="x", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x6, y6, marker="x", markersize=8, markeredgecolor="red", markerfacecolor="green")



plt.text(0.087, 122346, 'X$_c$=0.244', fontsize = 12)
plt.text(0.217, 220501, 'X$_c$=0.525', fontsize = 12)
plt.text(1.892, 437423, 'X$_c$=0.630', fontsize = 12)
plt.text(20.440, 898392, 'X$_c$=0.735', fontsize = 12)


plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Maximum attainable mass and Xc at GR")
plt.xlabel("Accretion rate (M$_{\odot}$/year)")
plt.ylabel("Mass(M$_{\odot}$) ")
#plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()



import math
import pandas as pd
import matplotlib.pyplot as plt
Xc_GR = [0.244,0.525,0.630,0.735,0.840]
Accr_rate = [1.00e-1,1.00,10.00,100.00,1000.00]




a = 0.01
b = 1.00
plt.axhspan(a, b, color='c', alpha=0.5, lw=0)
plt.plot(Accr_rate,Xc_GR, color='black', linewidth=2.5)
plt.text(0.087, 122346, 'X$_c$=0.244', fontsize = 12)
plt.text(0.217, 220501, 'X$_c$=0.525', fontsize = 12)
plt.text(1.892, 437423, 'X$_c$=0.630', fontsize = 12)


plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Xc at GR")
plt.xlabel("Accretion rate (M$_{\odot}$/year)")
plt.ylabel("Xc")
#plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()
