##### Mdot vs Teff, L, M for 491

import numpy as np
from matplotlib import pyplot as plt
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[4]))
M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[2])
fig,ax=plt.subplots()

ax.plot(Lum,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
#ax.plot(Teff,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
#ax.plot(Mr,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(R,Dconv,linewidth=1.5, color='blue',label="$D_{conv}$")

#plt.text(0.308, 13.06, 'Dconv', fontsize = 13)

#ax.set_xlabel('M$[M_{\odot}]$', fontsize = 20)
#ax.set_xlabel('log T$_{eff}$[K]', fontsize = 20)
ax.set_xlabel('log $L/L_{\odot}$', fontsize = 20)

ax.set_ylabel('Accretion rate $[M_{\odot}/yr]$)', fontsize = 20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.show()

##### Mdot vs Teff, L, M for 1331

import numpy as np
from matplotlib import pyplot as plt
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1331M_SS14/P002z0S0.dat',skip_header=0))[4]))
M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1331M_SS14/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1331M_SS14/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1331M_SS14/P002z0S0.dat',skip_header=0))[2])
fig,ax=plt.subplots()

ax.plot(Lum,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
#ax.plot(Mr,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
#ax.plot(Teff,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(R,Dconv,linewidth=1.5, color='blue',label="$D_{conv}$")

#plt.text(0.308, 13.06, 'Dconv', fontsize = 13)

#ax.set_xlabel('M$[M_{\odot}]$', fontsize = 20)
#ax.set_xlabel('log T$_{eff}$[K]', fontsize = 20)
ax.set_xlabel('log $L/L_{\odot}$', fontsize = 20)

ax.set_ylabel('Accretion rate $[M_{\odot}/yr]$)', fontsize = 20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.show()
##### Mdot vs Teff, L, M for 1662

import numpy as np
from matplotlib import pyplot as plt
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[4]))
M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[2])
t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[1])

fig,ax=plt.subplots()

#ax.plot(Lum,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
#ax.plot(Mr,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
ax.plot(Lum,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(Teff,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(R,Dconv,linewidth=1.5, color='blue',label="$D_{conv}$")

#plt.text(0.308, 13.06, 'Dconv', fontsize = 13)

ax.set_xlabel('M$[M_{\odot}]$', fontsize = 20)
#ax.set_xlabel('log T$_{eff}$[K]', fontsize = 20)
#ax.set_xlabel('log $L/L_{\odot}$', fontsize = 20)

ax.set_ylabel('Accretion rate $[M_{\odot}/yr]$)', fontsize = 20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.show()

##### Mdot vs Teff, L, M for 4477

import numpy as np
from matplotlib import pyplot as plt
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4]))
M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])
fig,ax=plt.subplots()

#ax.plot(Lum,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
#ax.plot(Mr,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
ax.plot(Teff,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(R,Dconv,linewidth=1.5, color='blue',label="$D_{conv}$")

#plt.text(0.308, 13.06, 'Dconv', fontsize = 13)

#ax.set_xlabel('M$[M_{\odot}]$', fontsize = 20)
ax.set_xlabel('log T$_{eff}$[K]', fontsize = 20)
#ax.set_xlabel('log $L/L_{\odot}$', fontsize = 20)

ax.set_ylabel('Accretion rate $[M_{\odot}/yr]$)', fontsize = 20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.show()
##### Mdot vs Teff, L, M for 6127

import numpy as np
from matplotlib import pyplot as plt
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test1_6127M_SS0/P002z0S0.dat',skip_header=0))[4]))
M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test1_6127M_SS0/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test1_6127M_SS0/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test1_6127M_SS0/P002z0S0.dat',skip_header=0))[2])
t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test1_6127M_SS0/P002z0S0.dat',skip_header=0))[1])

fig,ax=plt.subplots()

#ax.plot(Lum,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
#ax.plot(Mr,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")
ax.plot(t,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(Teff,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(R,Dconv,linewidth=1.5, color='blue',label="$D_{conv}$")

#plt.text(0.308, 13.06, 'Dconv', fontsize = 13)

ax.set_xlabel('M$[M_{\odot}]$', fontsize = 20)
#ax.set_xlabel('log T$_{eff}$[K]', fontsize = 20)
#ax.set_xlabel('log $L/L_{\odot}$', fontsize = 20)

ax.set_ylabel('Accretion rate $[M_{\odot}/yr]$)', fontsize = 20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.show()
############################

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

L_C = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[3])
T_C = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[4])
#L_Cstar = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/MS_Mag/P060Z14S0.4Coef12/P060Z14S0.4.dat',skip_header=0))[3])
#T_Cstar = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/MS_Mag/P060Z14S0.4Coef12/P060Z14S0.4.dat',skip_header=0))[4])
fig,ax=plt.subplots()
ax.plot(T_C,L_C,linewidth=1.5, color='red',linestyle='dashed',label="C")
#ax.plot(T_Cstar,L_Cstar,linewidth=1.5, color='magenta',linestyle='dashdot',label="C*")
#ax.plot(T_E,L_E,linewidth=1.5, color='red',linestyle='solid')
#ax.plot(T_F,L_F,linewidth=1.5, color='blue',linestyle='solid')
#plt.text(4.401, 4.52, 'F', fontsize = 13)
#plt.text(4.373, 4.60, 'D', fontsize = 13)
#plt.text(4.402, 4.67, 'E', fontsize = 13)
#plt.text(4.409, 4.71, 'C', fontsize = 13)
#plt.text(4.410, 4.40, '15M$_{\odot}, Z=0.014$', fontsize = 14)
#plt.text(4.400, 4.37, 'V/V$_{crit}=0.4$', fontsize = 14)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
#ax.set_xlim(4.35, 4.500)
#ax.set_ylim(4.2, 4.84)
ax.set_xlabel('log$(T_{\mathrm{eff}}[K])$',fontsize=20)
ax.set_ylabel('log$(L/L_{\odot}$)',fontsize=20)
ax.invert_xaxis()
leg = plt.legend(loc='lower left', shadow=True,prop={'size': 14})

#plt.xticks(np.arange(4.35, 4.500, 0.05))
plt.show()

################## deut vs time

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

XD2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[110])
time = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[1])
fig,ax=plt.subplots()
ax.plot(time,XD2,linewidth=1.5, color='red',linestyle='dashed',label="491")
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.set_xlabel('$Time$',fontsize=20)
ax.set_ylabel('Central Deuterium mass frac.',fontsize=20)
#leg = plt.legend(loc='lower left', shadow=True,prop={'size': 14})
plt.show()

###############Not working yet.

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4]))
#M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])
Mdot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116])

M_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])
M_accr_2 = M_sun*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])
L_accr_2 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0)))[3])
Teff_accr_2 = (10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0)))[4])**4
t_accr = Mr/Mdot
R_accr_2 = (L_accr_2/(4*pi*sigma*(Teff_accr_2)))**0.5 # Correct
t_top_2 = 0.5*G*(M_accr_2**2) # Correct
t_bot_2 = R_accr_2*L_accr_2 # Correct
t_KH_2 = (t_top_2/t_bot_2)*year  # Correct
Time_2 = t_accr/t_KH_2 # Correct


fig,ax=plt.subplots()
ax.plot(Mr,Time_2,linewidth=1.5, color='red',linestyle='dashed',label="491")
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.set_xlabel('$Mass[M_{\odot}]$',fontsize=20)
ax.set_ylabel('$T_{accr}/T_{KH}$',fontsize=20)
#leg = plt.legend(loc='lower left', shadow=True,prop={'size': 14})
plt.show()


###### All 10 HRD with Mdot and isoradius lines
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified points A and B,
    and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    ax.plot(log_T_range, log_L, linestyle='--', color='grey', alpha=alpha)

# Load the data
data_files = [
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/771M_SS40/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/778M_SS39/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/932M_SS27/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1135M_S20/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1331M_SS14/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1923M_SS6/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test1_6127M_SS0/P002z0S0.dat'
]

fig, ax = plt.subplots()

for data_file in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L = np.transpose(data[:, 3])
    T = np.transpose(data[:, 4])
    M_dot = np.transpose(data[:, 116])

    # Create line segments for individual coloring
    points = np.array([T, L]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Set colormap and create LineCollection
    cmap = 'tab20'
    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

# Add colorbar
cbar = fig.colorbar(line, ax=ax, ticks=[0, 0.05, 0.1, 0.15, 0.2, 0.25])
cbar.set_label('Accretion Rate', fontsize=16)
cbar.ax.tick_params(labelsize=16)

# Plot isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max = 5.2, 3.6
alpha = 0.5
for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    label_position = ((point_A[0] + point_B[0]) / 2, (point_A[1] + point_B[1]) / 2)
    ax.text(label_position[0], label_position[1], label, fontsize=10, color='grey', alpha=alpha, ha='center', va='center')

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=18)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=18)
ax.tick_params(axis='both', labelsize=16)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 8.44)

# Show the plot
plt.show()


###### HRD with Mdot and isoradius lines
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified points A and B,
    and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    ax.plot(log_T_range, log_L, linestyle='--', color='grey', alpha=alpha)

# Load the data
data_files = [
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat', '4477M$_\odot$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat', '1662M$_\odot$')
]

fig, ax = plt.subplots()

# Define an empty list to store lines and labels for the legend
lines = []
labels = []

fig, ax = plt.subplots()

for data_file, label in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L = np.transpose(data[:, 3])
    T = np.transpose(data[:, 4])
    M_dot = np.transpose(data[:, 116])

    # Create line segments for individual coloring
    points = np.array([T, L]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Set colormap and create LineCollection
    cmap = 'tab20'
    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

    # Store the line and label for the legend
    lines.append(line)
    labels.append(label)

# Add colorbar
cbar = fig.colorbar(line, ax=ax, ticks=[0, 0.05, 0.1, 0.15, 0.2, 0.25])
cbar.set_label('Accretion Rate', fontsize=16)
cbar.ax.tick_params(labelsize=16)
# Plot isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max = 5.2, 3.6
alpha = 0.5
for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    label_position = ((point_A[0] + point_B[0]) / 2, (point_A[1] + point_B[1]) / 2)
    ax.text(label_position[0], label_position[1], label, fontsize=10, color='grey', alpha=alpha, ha='center', va='center')

# Set axis labels and limits
ax.text(4,54, 7.34, '1662M', fontsize = 13)
ax.text(4,54, 7.99, '4477M', fontsize = 13)

ax.set_xlabel('$\log(T_{eff})$', fontsize=16)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=16)
ax.tick_params(axis='both', labelsize=16)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 8.44)
ax.legend(lines, labels, loc='lower left', fontsize=12)

# Show the plot
plt.show()


########## HRD with Mdot --correct one with isoradius
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified points A and B,
    and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    ax.plot(log_T_range, log_L, linestyle='--', color='grey', alpha=alpha)

# Load the data
data_files = [
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat'
]

fig, ax = plt.subplots()

for data_file in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L = np.transpose(data[:, 3])
    T = np.transpose(data[:, 4])
    M_dot = np.transpose(data[:, 116])

    # Create line segments for individual coloring
    points = np.array([T, L]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Set colormap and create LineCollection
    cmap = 'tab20'
    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

# Add colorbar
cbar = fig.colorbar(line, ax=ax, ticks=[0, 0.05, 0.1, 0.15, 0.2, 0.25])
cbar.set_label('Accretion Rate', fontsize=22)
cbar.ax.tick_params(labelsize=20)

# Plot isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max = 5.2, 3.6
alpha = 0.7

for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    label_position = ((point_A[0] + point_B[0]) / 2, (point_A[1] + point_B[1]) / 2)
    ax.text(label_position[0], label_position[1], label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=22)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=22)
ax.tick_params(axis='both', labelsize=20)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 8.44)
fig.set_size_inches(8, 8)
# Show the plot
plt.show()

#############
############################
##### HRD all models with isoradius



import numpy as np
import matplotlib.pyplot as plt

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified points A and B,
    and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    ax.plot(log_T_range, log_L, linestyle='--', color='grey', alpha=alpha)

data_files = [
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/Test2_491M_SS71/P002z0S0.dat', '491M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/771M_SS40/P002z0S0.dat', '771M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/778M_SS39/P002z0S0.dat', '778M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/932M_SS27/P002z0S0.dat', '932M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1135M_S20/P002z0S0.dat', '1135M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1331M_SS14/P002z0S0.dat', '1331M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1662M_SS10/P002z0S0.dat', '1662M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1923M_SS6/P002z0S0.dat', '1923M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/4477M_SS1/P002z0S0.dat', '4477M$_{\odot}$'),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/Test1_6127M_SS0/P002z0S0.dat', '6127M$_{\odot}$'),
    # Add other data files and labels in the same format
]

fig, ax = plt.subplots()

labels = []
for data_file, label in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L = np.transpose(data[:, 3])
    T = np.transpose(data[:, 4])

    ax.plot(T, L, label=label)
    labels.append(label)

# Plot isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max = 5.2, 3.6
alpha = 0.7
for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    label_position = ((point_A[0] + point_B[0]) / 2, (point_A[1] + point_B[1]) / 2)
    ax.text(label_position[0], label_position[1], label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=22)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=22)
ax.tick_params(axis='both', labelsize=20)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 8.50)
ax.text(3.810, 2.120, 'I', fontsize=26)
ax.text(4.430, 5.089, 'II', fontsize=26)
ax.text(3.761, 5.200, 'III', fontsize=26)
ax.text(3.820, 5.885, 'IV', fontsize=26)
ax.text(3.725, 6.682, 'V', fontsize=26)
# Add legend
ax.legend(labels, loc='lower left', fontsize=14)
fig.set_size_inches(8, 8)


# Show the plot
plt.show()


######### 4477 M HRD to show accretion during H burning
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    ax.plot(log_T_range, log_L, linestyle='--', color='grey', alpha=alpha)

data_files = [
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat'
]

fig, ax = plt.subplots()

for data_file in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L = np.transpose(data[:, 3])
    T = np.transpose(data[:, 4])
    M_dot = np.transpose(data[:, 116])

    points = np.array([T, L]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    cmap = 'tab20'
    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

min_acc_rate = np.min(M_dot)
max_acc_rate = np.max(M_dot)

cbar = fig.colorbar(line, ax=ax)
lc.set_clim(vmin=min_acc_rate, vmax=max_acc_rate)
cbar.set_label('Accretion Rate', fontsize=22)
cbar.ax.tick_params(labelsize=20)

isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max = 5.2, 3.6
alpha = 0.7
for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    label_position = ((point_A[0] + point_B[0]) / 2, (point_A[1] + point_B[1]) / 2)
    ax.text(label_position[0], label_position[1], label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

ax.set_xlabel('$\log(T_{eff})$', fontsize=22)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=22)
ax.tick_params(axis='both', labelsize=20)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 8.44)
fig.set_size_inches(8, 8)
# Show the plot
plt.show()





########## HRD with H1c --correct one with isoradius
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified points A and B,
    and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    ax.plot(log_T_range, log_L, linestyle='--', color='grey', alpha=alpha)

# Load the data
data_files = [
    '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat'

]

fig, ax = plt.subplots()

for data_file in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L = np.transpose(data[:, 3])
    T = np.transpose(data[:, 4])
    M_dot = np.transpose(data[:, 21])

    # Create line segments for individual coloring
    points = np.array([T, L]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Set colormap and create LineCollection
    cmap = 'tab20'
    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

# Add colorbar
ticks = np.linspace(0, 0.7516,10)
cbar = fig.colorbar(line, ax=ax, ticks=ticks)
cbar.set_label('$^{1}$H[centr. mass frac.]', fontsize=22)
cbar.ax.tick_params(labelsize=20)

# Plot isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max = 5.2, 3.6
alpha = 0.7

for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    label_position = ((point_A[0] + point_B[0]) / 2, (point_A[1] + point_B[1]) / 2)
    ax.text(label_position[0], label_position[1], label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

# Set axis labels and limits
plt.text(4.511, 8.117, '4477 M$_\odot$', fontsize = 18)

ax.set_xlabel('$\log(T_{eff})$', fontsize=22)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=22)
ax.tick_params(axis='both', labelsize=20)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 8.44)
fig.set_size_inches(8, 8)
# Show the plot
plt.show()

######## Luminosity wave
import numpy as np
from matplotlib import pyplot as plt
G=6.67428*10**(-8)                       #Gravitational constant
sigma=5.67040*10**(-5)
Lsol=3.8427*10**33

Mtot1 = 14.61756
T1 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',skip_header=259))[3]))
R1 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',skip_header=259))[4]))
Lr1 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',skip_header=259))[5]))
Mr1 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',skip_header=259))[49]))
M1 = Mr1/Mtot1
L_layers1 = 4 * np.pi * (R1 ** 2) * sigma * (T1 ** 4)
L_sum1 = np.sum(L_layers1)


#
Mtot2 = 16.65358
T2 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031731.gz',skip_header=260))[3]))
R2 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031731.gz',skip_header=260))[4]))
Lr2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031731.gz',skip_header=260))[5]))
Mr2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031731.gz',skip_header=260))[49]))
M2 = Mr2/Mtot2
L_layers2 = 4 * np.pi * (R2 ** 2) * sigma * (T2 ** 4)
L_sum2 = np.sum(L_layers2)

#
Mtot3 = 18.87165
T3 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033951.gz',skip_header=3))[3]))
R3 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033951.gz',skip_header=3))[4]))
Lr3 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031731.gz',skip_header=260))[5]))
Mr3 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033951.gz',skip_header=3))[49]))
M3 = Mr3/Mtot3
L_layers3 = 4 * np.pi * (R3 ** 2) * sigma * (T3 ** 4)
L_sum3 = np.sum(L_layers3)

#
Mtot4 = 19.32657
T4 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0034391.gz',skip_header=3))[3]))
R4 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0034391.gz',skip_header=3))[4]))
Lr4 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0034391.gz',skip_header=3))[5]))
L_layers4 = 4 * np.pi * (R1 ** 4) * sigma * (T4 ** 4)
Mr4 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0034391.gz',skip_header=3))[49]))
M4 = Mr4/Mtot4
L_sum4 = np.sum(L_layers4)

#
Mtot5 = 54.54429
T5 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0041931.gz',skip_header=242))[3]))
R5 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0041931.gz',skip_header=242))[4]))
Lr5 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0041931.gz',skip_header=242))[5]))
L_layers5 = 4 * np.pi * (R5 ** 2) * sigma * (T5 ** 4)
Mr5 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0041931.gz',skip_header=242))[49]))
M5 = Mr5/Mtot5
L_sum5 = np.sum(L_layers5)





#T2 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031731.gz',skip_header=260))[3]))
#T3 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033951.gz',skip_header=3))[3]))
#T4 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0034391.gz',skip_header=3))[3]))
#T5 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0041931.gz',skip_header=242))[3]))

import numpy as np
import os
from matplotlib import pyplot as plt

G = 6.67428e-8  # Gravitational constant
sigma = 5.67040e-5
Lsol = 3.8427e33


def read_data(filename, skip_header):
    data = np.genfromtxt(filename, skip_header=skip_header)
    T = 10**(data[:, 3])
    R = 10**(data[:, 4])
    Mr = data[:, 49]
    return T, R, Mr


def calculate_luminosity(T, R):
    return (4 * np.pi * (R ** 2) * sigma * (T ** 4)) / Lsol


file_base_path = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/'

file_data = [
    ('P002z0S0.v0029481.gz', 259, 14.61756),
    ('P002z0S0.v0031731.gz', 260, 16.65358),
    ('P002z0S0.v0033951.gz', 3, 18.87165),
    ('P002z0S0.v0034391.gz', 3, 19.32657),
    ('P002z0S0.v0041931.gz', 242, 54.54429)
]

Ls_normalized = []
Ms = []

for file, skip_header, Mtot in file_data:
    file_path = os.path.join(file_base_path, file)
    T, R, Mr = read_data(file_path, skip_header)
    L = calculate_luminosity(T, R)
    total_luminosity = np.sum(L)
    L_normalized = L / total_luminosity
    M = Mr / Mtot
    Ls_normalized.append(L_normalized)
    Ms.append(M)

plt.figure()
color_map = plt.get_cmap('viridis')
colors = color_map(np.linspace(0, 1, len(file_data)))

for i, (L_normalized, M, color) in enumerate(zip(Ls_normalized, Ms, colors), 1):
    plt.plot(M, L_normalized, linestyle='-', linewidth=2.0, label=f'L{i}', color=color)
plt.xlabel('M')
plt.ylabel('Normalized Luminosity')
plt.legend()
plt.show()

###############
import numpy as np

# Your provided arrays
T1 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',skip_header=259))[3]))
R1 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',skip_header=259))[4]))
Lr1 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',skip_header=259))[5]))

# Calculate the luminosity of each layer using T1 and R1 arrays
sigma = 5.67040e-5
L_layers = 4 * np.pi * (R1 ** 2) * sigma * (T1 ** 4)

# Sum up the luminosity of all the layers
L_sum = np.sum(L_layers)

###########

import numpy as np
import os
from matplotlib import pyplot as plt

G = 6.67428e-8  # Gravitational constant
sigma = 5.67040e-5
Lsol = 3.8427e33


def read_data(filename, skip_header):
    data = np.genfromtxt(filename, skip_header=skip_header)
    T = 10**(data[:, 3])
    R = 10**(data[:, 4])
    Mr = data[:, 49]
    return T, R, Mr


def calculate_luminosity(T, R):
    return (4 * np.pi * (R ** 2) * sigma * (T ** 4)) / Lsol


file_base_path = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/'

file_data = [
    ('P002z0S0.v0029481.gz', 259, 14.61756),
    ('P002z0S0.v0031731.gz', 260, 16.65358),
    ('P002z0S0.v0033951.gz', 3, 18.87165),
    ('P002z0S0.v0034391.gz', 3, 19.32657),
    ('P002z0S0.v0041931.gz', 242, 54.54429),
    ('P002z0S0.v0044201.gz', 247, 71.79776),
]

Ls = []
Ms = []

for file, skip_header, Mtot in file_data:
    file_path = os.path.join(file_base_path, file)
    T, R, Mr = read_data(file_path, skip_header)
    L = calculate_luminosity(T, R)
    M = Mr / Mtot
    Ls.append(L)
    Ms.append(M)

colorblind_friendly_colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628']

plt.figure()
for i, (L, M, color) in enumerate(zip(Ls, Ms, colorblind_friendly_colors), 1):
    plt.plot(M, L, label=f'L{i}', linewidth=2.0, color=color)
plt.xlabel('M')
plt.ylabel('Luminosity')
plt.legend()
plt.show()


##########
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029481.gz',1)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0030571.gz',2)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0030591.gz',3)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026001.gz',1)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026101.gz',2)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026201.gz',3)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026301.gz',4)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026401.gz',1)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026501.gz',2)

#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0027501.gz',3)


#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0028501.gz',4)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029501.gz',5)


#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0030101.gz',6)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031651.gz',7)


#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0031731.gz',8)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0032071.gz',9)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0032471.gz',10)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0032971.gz',11)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033271.gz',12)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033471.gz',13) ### Highest L
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033671.gz',14)
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033871.gz',15)  ### Getting low

gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033981.gz',16)### wave has ended

###############
import numpy as np
import os
from matplotlib import pyplot as plt
Mtot1 = 12.20799
LLtot1 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026401.gz',skip_header=258))[5]))
M1 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0026401.gz',skip_header=258))[49]))/Mtot1

Mtot2 = 14.63490
LLtot2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029501.gz',skip_header=260))[5]))
M2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0029501.gz',skip_header=260))[49]))/Mtot2

Mtot3 = 18.41082
LLtot3 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033471.gz',skip_header=263))[5]))
M3 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033471.gz',skip_header=263))[49]))/Mtot3

Mtot4 = 18.89836
LLtot4 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033471.gz',skip_header=3))[5]))
M4 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0033981.gz',skip_header=3))[49]))/Mtot4


######### Plot of luminosity wave vr Mr/Mtot

import numpy as np
import os
import matplotlib.pyplot as plt

def read_data(filename, skip_header, Mtot):
    data = np.genfromtxt(filename, skip_header=skip_header)
    LLtot = data[:, 5]
    M = data[:, 49] / Mtot
    return LLtot, M

file_base_path = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/'

file_data = [
    ('P002z0S0.v0026401.gz', 258, 12.20799),
    ('P002z0S0.v0029501.gz', 260, 14.63490),
    ('P002z0S0.v0033471.gz', 263, 18.41082),
    ('P002z0S0.v0033981.gz', 3, 18.89836)
]

LLtots = []
Ms = []

for file, skip_header, Mtot in file_data:
    file_path = os.path.join(file_base_path, file)
    LLtot, M = read_data(file_path, skip_header, Mtot)
    LLtots.append(LLtot)
    Ms.append(M)

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['tab:blue', 'tab:orange', 'tab:purple', 'tab:brown']
labels = ['Start', 'Migration', 'Break', 'Aftermath']

for i, (LLtot, M) in enumerate(zip(LLtots, Ms)):
    ax.plot(M, LLtot, label=labels[i], color=colors[i])

ax.set_xlabel(r'$M_\mathrm{r}/M_\mathrm{tot}$', fontsize=22)
ax.set_ylabel(r'$L/L_{tot}$', fontsize=22)
ax.tick_params(axis='both', labelsize=20)
ax.legend(fontsize=20)
plt.show()

#In the script above, create a new array labelled r which exists as R = data[:, 4]. But this value is given in log scale and the units are in cm.
#Additionally, create another array named T which is the temperature inside the star given by T = data[:, 3] and is in log scale and units are Kelvin.
#From these two newly created arrays, take the very first value of T and R and use it to calculate luminosity using stefan boltzman law. Store this value
#indvidually for all four data files. Then multiply this value with Ltot, these new array, Lets call them Lr should ofcourse be in cgs units and then finally
#divide them by solar lumiosity and take the log. finally, plot Log(Lr/Lsol) versus M instead of what the code does now
####### Using the above changes, here is the modfifed code that works with changes to Luminosity.

import numpy as np
import os
import matplotlib.pyplot as plt

def read_data(filename, skip_header, Mtot):
    data = np.genfromtxt(filename, skip_header=skip_header)
    LLtot = data[:, 5]
    M = data[:, 49] / Mtot
    R = 10 ** data[:, 4]  # R in cm, converted from log scale
    T = 10 ** data[:, 3]  # T in Kelvin, converted from log scale
    return LLtot, M, R, T

file_base_path = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/'

file_data = [
    ('P002z0S0.v0026401.gz', 258, 12.20799),
    ('P002z0S0.v0029501.gz', 260, 14.63490),
    ('P002z0S0.v0033471.gz', 263, 18.41082),
    #('P002z0S0.v0033981.gz', 3, 18.89836)
    ('P002z0S0.v0034081.gz', 3, 19.04059)
]

LLtots = []
Ms = []
Lrs = []

stefan_boltzmann = 5.670374419e-5  # erg/(cm^2 K^4 s)
solar_luminosity = 3.828e33  # erg/s

for file, skip_header, Mtot in file_data:
    file_path = os.path.join(file_base_path, file)
    LLtot, M, R, T = read_data(file_path, skip_header, Mtot)
    L = 4 * np.pi * R[0] ** 2 * T[0] ** 4 * stefan_boltzmann  # Luminosity in erg/s
    Lr = L * LLtot  # Multiply L with LLtot
    Lr_solar = np.log10(Lr / solar_luminosity)  # Convert to solar units and take the log
    LLtots.append(LLtot)
    Ms.append(M)
    Lrs.append(Lr_solar)

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['k', 'tab:orange', 'tab:purple', 'tab:brown']
labels = ['Start', 'Migration', 'Break', 'Aftermath']

for i, (Lr, M) in enumerate(zip(Lrs, Ms)):
    ax.plot(M, Lr, label=labels[i], color=colors[i])

ax.set_xlabel(r'$M_\mathrm{r}/M_\mathrm{tot}$', fontsize=22)
ax.set_ylabel(r'$\log(L_\mathrm{r}/L_{\odot})$', fontsize=22)
ax.tick_params(axis='both', labelsize=20)
ax.legend(fontsize=20)
plt.show()



##### Mdot vs Teff, L, M for 1662

import numpy as np
from matplotlib import pyplot as plt
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[4]))
M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[2])
t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',skip_header=0))[1])
Teff2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4]))
M_Accr2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116]))
Lum2 = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3]))
Mr2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])

fig,ax=plt.subplots()

ax.plot(Lum,np.log(M_Accr),linewidth=1.5, color='black',label="1662 M$_\odot$")
ax.plot(Lum2,np.log(M_Accr2),linewidth=1.5, color='red',label="4477 M$_\odot$")

ax.set_xlabel('log $L/L_{\odot}$', fontsize = 20)
ax.set_ylabel('Accretion rate $[M_{\odot}/yr]$)', fontsize = 20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.show()

##### Mdot vs Teff, L, M for 4477

import numpy as np
from matplotlib import pyplot as plt
Teff = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4]))
M_Accr = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116]))
Lum = ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3]))
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])
fig,ax=plt.subplots()

ax.plot(Teff,M_Accr,linewidth=1.5, color='black',label="$K_{ther}$")

#ax.plot(R,Dconv,linewidth=1.5, color='blue',label="$D_{conv}$")

#plt.text(0.308, 13.06, 'Dconv', fontsize = 13)

#ax.set_xlabel('M$[M_{\odot}]$', fontsize = 20)
ax.set_xlabel('log T$_{eff}$[K]', fontsize = 20)
#ax.set_xlabel('log $L/L_{\odot}$', fontsize = 20)

ax.set_ylabel('Accretion rate $[M_{\odot}/yr]$)', fontsize = 20)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.show()
