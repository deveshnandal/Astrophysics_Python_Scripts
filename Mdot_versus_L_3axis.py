####### Mdot versus L. Teff as second y axis

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.ticker import MultipleLocator

Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[4]))
M_Accr = np.log10((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[2])
t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[1])
Teff2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4]))
M_Accr2 = np.log10((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116]))
Lum2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3]))
Mr2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])


def create_colored_line(ax, x, y, color_data, cmap, linestyle='-'):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    lc = LineCollection(segments, cmap=cmap, linestyle=linestyle)  # Add linestyle parameter
    lc.set_array(color_data)
    lc.set_linewidth(2)  # Increase line width for better visibility
    line = ax.add_collection(lc)

    return line

# Limit the values of M_Accr and M_Accr2 arrays
M_Accr = np.maximum(M_Accr, -6)
M_Accr2 = np.maximum(M_Accr2, -6)

fig, ax = plt.subplots()

# Create colored lines
line1 = create_colored_line(ax, Lum, (M_Accr), Teff, 'coolwarm_r', '-')  # solid line
line2 = create_colored_line(ax, Lum2, (M_Accr2), Teff2, 'coolwarm_r', '--')  # dashed line

ax.set_xlabel('log ($\mathrm{L/L_{\odot}}$)', fontsize=20)
ax.set_ylabel('log ($\mathrm{\dot{M}}$) $[\mathrm{M_{\odot}/yr}]$', fontsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

# Set the x-axis and y-axis range
ax.set_xlim(5.5, 9.47)
ax.set_ylim(-4, 0)

# Add colorbar
cbar = fig.colorbar(line1, ax=ax)
cbar.set_label('log ($\mathrm{T_{eff}}$)', fontsize=20)  # Update label to "log(Teff)"
cbar.ax.tick_params(labelsize=20)
fig.set_size_inches(8, 8)
ax.tick_params(axis='x', labelsize=20, which='both', pad=10)
ax.tick_params(axis='y', labelsize=20, which='both', pad=10)

# Set the ticks on both axes to be multiples of 5
x_tick_multiple = 0.5
y_tick_multiple = 1
ax.xaxis.set_major_locator(MultipleLocator(x_tick_multiple))
ax.yaxis.set_major_locator(MultipleLocator(y_tick_multiple))

plt.show()

########################
######### Mdot vs log g and Teff as second y axis

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Constants
G = 6.67430e-8  # cm^3 g^-1 s^-2
Msol = 1.989e33  # g
Lsol = 3.828e33  # erg s^-1
sigma = 5.670374419e-5  # erg cm^-2 s^-1 K^-4

# Conversion functions
def mass_cgs(mass_frac):
    return mass_frac * Msol

def radius_cgs(lum_frac, teff):
    lum = 10 ** lum_frac * Lsol
    teff_val = 10 ** teff
    return np.sqrt(lum / (4 * np.pi * sigma * teff_val ** 4))

def surface_gravity(mass_cgs, radius_cgs):
    return G * mass_cgs / radius_cgs ** 2

def logg_array(mass_frac_array, lum_frac_array, teff_array):
    mass_cgs_array = mass_cgs(mass_frac_array)
    radius_cgs_array = radius_cgs(lum_frac_array, teff_array)
    return np.log10(surface_gravity(mass_cgs_array, radius_cgs_array))

# Load data
Teff = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[4])
M_Accr = np.log10((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[116]))
Lum = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[3])
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[2])

Teff2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4])
M_Accr2 = np.log10((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116]))
Lum2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3])
Mr2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])

# Calculate logg and logg2
logg = logg_array(Mr, Lum, Teff)
logg2 = logg_array(Mr2, Lum2, Teff2)

def create_colored_line(ax, x, y, color_data, cmap):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(color_data)
    lc.set_linewidth(2)  # Increase line width for better visibility
    line = ax.add_collection(lc)

    return line

# Limit the values of M_Accr and M_Accr2 arrays
M_Accr = np.maximum(M_Accr, -6)
M_Accr2 = np.maximum(M_Accr2, -6)

fig, ax = plt.subplots()

# Create colored lines
line1 = create_colored_line(ax, logg, (M_Accr), Teff, 'coolwarm_r')
line2 = create_colored_line(ax, logg2, (M_Accr2), Teff2, 'coolwarm_r')

ax.set_xlabel('log ($\mathrm{g}$)$[cm.s^{-2}]$', fontsize=20)
ax.set_ylabel('log ($\mathrm{\dot{M}}$) $[\mathrm{M_{\odot}/yr}]$', fontsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

# Set the x-axis and y-axis range
ax.set_xlim(-1, 5)
ax.set_ylim(-6.1, 0)

# Add colorbar
cbar = fig.colorbar(line1, ax=ax)
cbar.set_label('log($\mathrm{T_{eff}}$)', fontsize=20)  # Update label to "log(Teff)"
cbar.ax.tick_params(labelsize=20)
fig.set_size_inches(8, 8)
plt.show()


####### Mdot versus L. Teff as second y axis

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[4]))
M_Accr = np.log10((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[2])
t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[1])
Teff2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4]))
M_Accr2 = np.log10((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116]))
Lum2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3]))
Mr2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])


def create_colored_line(ax, x, y, color_data, cmap):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(color_data)
    lc.set_linewidth(2)  # Increase line width for better visibility
    line = ax.add_collection(lc)

    return line

# Limit the values of M_Accr and M_Accr2 arrays
M_Accr = np.maximum(M_Accr, -6)
M_Accr2 = np.maximum(M_Accr2, -6)

fig, ax = plt.subplots()

# Create colored lines
line1 = create_colored_line(ax, Lum, 10**(M_Accr), Teff, 'coolwarm_r')
#line2 = create_colored_line(ax, Lum2, (M_Accr2), Teff2, 'coolwarm_r')

ax.set_xlabel('log ($\mathrm{L/L_{\odot}}$)', fontsize=20)
ax.set_ylabel('log ($\mathrm{\dot{M}}$) $[\mathrm{M_{\odot}/yr}]$', fontsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

# Set the x-axis and y-axis range
ax.set_xlim(5, 8.4)
#ax.set_ylim(-6, 0)

# Add colorbar
cbar = fig.colorbar(line1, ax=ax)
cbar.set_label('log($\mathrm{T_{eff}}$)', fontsize=20)  # Update label to "log(Teff)"
cbar.ax.tick_params(labelsize=20)
fig.set_size_inches(8, 8)
plt.show()
