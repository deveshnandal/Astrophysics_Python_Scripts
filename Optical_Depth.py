##### Optical depth calculation using interpolation ############

################# 1Msun/yr test ##################
#### 10 ###

import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np
import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M_10 = 10*M_sun
L_10 = 3.846e+33*(10**4.0806)
Teff_10 = (10**3.6790)**4
M_dot_10 = (1*M_sun)/3.154e+7

R_ini_10= (L_10/(4*pi*sigma*(Teff_10)))**0.5 # which equates to 11178765750673.912 or 1.11e13
R_10 = np.linspace(1.11e13,2.040e18,200000)
v_10 = (2*G*M_10/(R_10))**0.5
rho_10 = M_dot_10/(4*pi*(np.power(R_10,2))*v_10)
rho_10_log = np.log(rho_10)
k_10 = np.empty(200000)  # This created an empty list with 2040 spaces
k_10.fill(1.547e-3)
k_array_10 = np.linspace(3.98107e-8,1.17489e-38,200000)
l_10 = 1/(k_array_10*rho_10)
int_10 = np.empty(200000)
int_10[0] = 0
for i in range(1,len(k_array_10)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_10[i] = int_10[i-1] + k_array_10[i]*rho_10[i]*(R_10[i]-R_10[i-1])

##### 100 ###

M_100 = 100*M_sun
L_100 = 3.846e+33*(10**6.0641)
Teff_100 = (10**3.7040)**4
M_dot_100 = (1*M_sun)/3.154e+7

R_ini_100= (L_100/(4*pi*sigma*(Teff_100)))**0.5 # which equates to 97756097456129.72 or 9.77e13
R_100 = np.linspace(9.77e13,2.040e18,200000)
v_100 = (2*G*M_100/(R_100))**0.5
rho_100 = M_dot_100/(4*pi*(np.power(R_100,2))*v_100)
rho_100_log = np.log(rho_100)

k_100 = np.empty(200000)  # This created an empty list with 2040 spaces
k_100.fill(1.15e-3)
k_array_100 = np.linspace(3.9810706e-8,1.31825e-40,200000)
l_100 = 1/(k_array_100*rho_100)
int_100 = np.empty(200000)
int_100[0] = 0
for i in range(1,len(k_array_100)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_100[i] = int_100[i-1] + k_array_100[i]*rho_100[i]*(R_100[i]-R_100[i-1])

#### 1000 ###

M_1000 = 1000*M_sun
L_1000 = 3.846e+33*(10**7.4214)
Teff_1000 = (10**3.7516)**4
M_dot_1000 = (1*M_sun)/3.154e+7

R_ini_1000 = (L_1000/(4*pi*sigma*(Teff_1000)))**0.5 # which equates to 374622498209563.7 or 3.74e14
R_1000 = np.linspace(3.74e14,2.040e18,200000)
v_1000 = (2*G*M_1000/(R_1000))**0.5
rho_1000 = M_dot_1000/(4*pi*(np.power(R_1000,2))*v_1000)
rho_1000_log = np.log(rho_100)

k_1000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_1000.fill(0.0340)
k_array_1000 = np.linspace(3.9810706e-8,1.31825e-40,200000)
l_1000 = 1/(k_array_1000*rho_1000)
int_1000 = np.empty(200000)
int_1000[0] = 0
for i in range(1,len(k_array_1000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_1000[i] = int_1000[i-1] + k_array_1000[i]*rho_1000[i]*(R_1000[i]-R_1000[i-1])

#### 10000 ###

M_10000 = 10000*M_sun
L_10000 = 3.846e+33*(10**8.5193)
Teff_10000 = (10**3.7877)**4
M_dot_10000 = (1*M_sun)/3.154e+7

R_ini_10000 = (L_10000/(4*pi*sigma*(Teff_10000)))**0.5 # which equates to 1122907171987070.0 or 1.12e15
R_10000 = np.linspace(1.122e15,2.040e18,200000)
v_10000 = (2*G*M_10000/(R_10000))**0.5
rho_10000 = M_dot_10000/(4*pi*(np.power(R_10000,2))*v_10000)
rho_10000_log = np.log(rho_100)

k_10000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_10000.fill(0.076)
k_array_10000 = np.linspace(3.9810706e-8,1.31825e-40,200000)
l_10000 = 1/(k_array_10000*rho_10000)
int_10000 = np.empty(200000)
int_10000[0] = 0
for i in range(1,len(k_array_10000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_10000[i] = int_10000[i-1] + k_array_10000[i]*rho_10000[i]*(R_10000[i]-R_10000[i-1])

#### 100000 ###

M_100000 = 100000*M_sun
L_100000 = 3.846e+33*(10**9.552)
Teff_100000 = (10**3.9164)**4
M_dot_100000 = (1*M_sun)/3.154e+7

R_ini_100000 = (L_100000/(4*pi*sigma*(Teff_100000)))**0.5 # which equates to 2038420863198279.2 or 2.03e15
R_100000 = np.linspace(2.03e15,2.040e18,200000)
v_100000 = (2*G*M_100000/(R_100000))**0.5
rho_100000 = M_dot_100000/(4*pi*(np.power(R_100000,2))*v_100000)
rho_100000_log = np.log(rho_100)

k_100000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_100000.fill(0.307)
k_array_100000 = np.linspace(3.9810706e-8,1.31825e-40,200000)

l_100000 = 1/(k_array_100000*rho_100000)
int_100000 = np.empty(200000)
int_100000[0] = 0
for i in range(1,len(k_array_100000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_100000[i] = int_100000[i-1] + k_array_100000[i]*rho_100000[i]*(R_100000[i]-R_100000[i-1])


fig,ax=plt.subplots()
ax.plot(R_10,int_10,linewidth=3., label="10M$_{\odot}$")
ax.plot(R_100,int_100,linewidth=3., label="100M$_{\odot}$")
ax.plot(R_1000,int_1000,linewidth=3., label="1000M$_{\odot}$")
ax.plot(R_10000,int_10000,linewidth=3., label="10000M$_{\odot}$")
ax.plot(R_100000,int_100000,linewidth=3., label="100000M$_{\odot}$")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Optical depth')

leg = plt.legend(loc='upper left', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
####### For 1Msun/yr at 100000, T and rho plot vs R
#Teff_100000 = (L_100000/(4*pi*(np.power(R_100000,2))*sigma))**0.25
Teff_100000 = np.empty(200000)  # This created an empty list with 2040 spaces
Teff_100000.fill(10**3.9164)
Teff_10 = (10**3.6790)
Teff_100 = (10**3.7040)
Teff_1000 = (10**3.7516)
Teff_10000 = (10**3.7877)
Teff_100000 = (10**3.9164)

fig,ax=plt.subplots()
ax.plot(R_100000,rho_100000,color='tab:blue',linewidth=3., label="Density")
ax.plot(R_100000,Teff_100000,color='tab:red',linewidth=3., label="Temperature")
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Physical quantities')

leg = plt.legend(loc='center right', shadow=True,prop={'size': 8})

plt.show()


############# Interpolation test ##############

import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt
#Sub-sample of your opacity table
#First 9 Values of log(T)
y = [1.80, 1.90, 2.00, 2.10, 2.20, 2.30, 2.40, 2.50, 2.60, 2.70, 2.80, 2.90, 3.00, 3.10, 3.20]
#First 9 Values of log(rho)
x = [-16., -15., -14., -13., -12., -11., -10., -9., -8., -7., -6., -5., -4., -3., -2.]
# Opacity values for the corrsponginf log(T) and log(rho) reported above
z = [[-13.05, -12.62, -12.11, -11.51, -10.73, -9.79, -8.79, -7.79, -6.79, -5.79, -4.79, -3.79, -2.79, -1.79, -0.79],
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
f = interpolate.interp2d(x, y, z, kind='cubic')
# Compute the opacity value that you need, depending on the (log(rho),log(T)) given
# Example z_opacity = f(-15, 1.8)
z_int = f(-15.5, 1.85)
z_int1 = f(-17.00, 3.7877)
print("My opacity value = "+str(z_int1))
