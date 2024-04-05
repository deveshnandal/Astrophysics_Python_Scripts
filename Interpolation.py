#Script for Uganda

import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt


#Sub-sample of your opacity table

#First 9 Values of log(T)
y = [1.80, 1.90, 2.00, 2.10, 2.20, 2.30, 2.40, 2.50, 2.60]

#First 9 Values of log(rho)
x = [-16., -15., -14., -13., -12., -11., -10., -9., -8.]

# Opacity values for the corrsponginf log(T) and log(rho) reported above

z = [[-4.36, -4.36, -4.36, -4.36, -4.36, -4.36, -4.36, -4.36, -4.36],
     [-4.54, -4.54, -4.54, -4.54, -4.54, -4.54, -4.54, -4.53, -4.53],
     [-4.71, -4.71, -4.71, -4.71, -4.71, -4.71, -4.71, -4.71, -4.69],
     [-4.89, -4.89, -4.89, -4.89, -4.89, -4.89, -4.89, -4.88, -4.85],
     [-5.06, -5.06, -5.06, -5.06, -5.06, -5.06, -5.05, -5.05, -4.99],
    [-5.39, -5.29, -5.24, -5.22, -5.22, -5.22, -5.22, -5.21, -5.11],
    [-6.01, -5.98, -5.90, -5.75, -5.57, -5.45, -5.40, -5.36, -5.23],
    [-6.08, -6.08, -6.08, -6.07, -6.05, -5.98, -5.86, -5.68, -5.39],
    [-6.13, -6.13, -6.13, -6.13, -6.13, -6.12, -6.10, -6.00, -5.60]]

#Compute a function that performs a 2D interpolation by taking x, y and z as inputs
#The function below does perform extrapolation. Read more about the documentation about this function at https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.interp2d.html

f = interpolate.interp2d(x, y, z, kind='cubic')




# Compute the opacity value that you need, depending on the (log(rho),log(T)) given
# Example z_opacity = f(-15, 1.8)

z_int = f(-15.5, 1.85)
z_int1 = f(-10.26, 4.188)
print("My opacity value = "+str(z_int1))
