######## HRD from Dexter_Data
##### HRD_
# gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',1)
from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]

    extended_T_min = T_min + 1.0  # Extend the lower limit
    extended_T_max = T_max - 1.0  # Extend the upper limit

    log_T_range = np.linspace(extended_T_min, extended_T_max, num_points)
    ax.plot(log_T_range, slope * log_T_range + intercept, linestyle='--', color='grey', alpha=alpha)


L_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[3])
T_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[4])
L_D = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/Dexter_Data/Data.txt',skip_header=0))[1])
T_D = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/Dexter_Data/Data.txt',skip_header=0))[0])
fig,ax=plt.subplots()
ax.plot(T_Y,L_Y,linewidth=2.6, color='red',linestyle='solid',label="Our Model")
ax.plot(T_D,L_D,linewidth=2.6, color='blue',linestyle='dotted',label="Ohkubo 2009")
ax.tick_params(axis='x', labelsize=26)
ax.tick_params(axis='y', labelsize=26)

ax.set_xlabel('log$(T_{\mathrm{eff}}[K])$',fontsize=26)
ax.set_ylabel('log$(L/L_{\odot}$)',fontsize=26)

# Add the markers
marker_coords = [(4.1293,1.4694),
                (4.2790,2.1333),
                (4.3790,2.5751),
                (4.4521,2.9016),
                (4.5563,3.3746),
                (4.6303,3.7150),
                (4.6788,4.0754),
                (4.7306,4.3346),
                (4.7942,4.6600),
                (4.8633,5.0928),
                (4.8983,5.3706),
                (4.9361,5.7251),
                (4.9604,5.9992),
                (4.9773,6.2475)]

# Create array for marker sizes
marker_sizes = np.full((len(marker_coords),), 20)  # Note the comma after len(marker_coords)
marker_sizes[-1] = 40  # Last marker twice as big

for (x, y), size in zip(marker_coords, marker_sizes):
    ax.scatter(x, y, color='black', zorder=5, s=size)  # zorder=5 to make sure markers are on top

# Connect the markers
marker_coords_arr = np.array(marker_coords)
ax.plot(marker_coords_arr[:,0], marker_coords_arr[:,1], color='black', label='ZAMS')

# Add the labels
label_coords_texts = [(4.1780,1.4194, '2'),
                      (4.3300,1.9300, '3'),
                      (4.4280,2.3451, '4'),
                      (4.5000,2.6556, '5'),
                      (4.6000,3.0646, '7'),
                      (4.6850,3.4950, '9'),
                      (4.7700,3.8504, '12'),
                      (4.82000,4.1500, '15'),
                      (4.8800,4.4800, '20'),
                      (4.9350,4.8600, '30'),
                      (4.9780,5.1706, '40'),
                      (5.0100,5.4900, '60'),
                      (5.0380,5.7492, '85'),
                      (5.0790,6.0375, '120')]

for x, y, text in label_coords_texts:
    ax.text(x, y-0.1, text, fontsize=14, color='black', ha='center', va='center')  # Adjust label position to not overlap

# Add the isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max, alpha = 5.2, 3.6, 0.7

for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    ax.text(*(np.array(point_A) + np.array(point_B)) / 2, label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

leg = plt.legend(loc='lower left', shadow=True, prop={'size': 18})
ax.set_ylim(0.5, 8)
ax.set_xlim(3.5, 5.2)
ax.invert_xaxis()

fig.set_size_inches(8, 8)
plt.show()


######## HRD Yoshida versus time average accretion rate #######################
##### HRD_
# gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',1)
# gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/3.712e-4Msun_yr/P002z0S0.dat',2)
from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]

    extended_T_min = T_min + 1.0  # Extend the lower limit
    extended_T_max = T_max - 1.0  # Extend the upper limit

    log_T_range = np.linspace(extended_T_min, extended_T_max, num_points)
    ax.plot(log_T_range, slope * log_T_range + intercept, linestyle='--', color='grey', alpha=alpha)


L_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[3])
T_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[4])
L_D = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/3.712e-4Msun_yr/P002z0S0.dat',skip_header=0))[3])
T_D = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/3.712e-4Msun_yr/P002z0S0.dat',skip_header=0))[4])
fig,ax=plt.subplots()
ax.plot(T_Y,L_Y,linewidth=2.6, color='red',linestyle='solid',label=r"Variable $\dot{M}$")
ax.plot(T_D,L_D,linewidth=2.6, color='cyan',linestyle='solid',label="Constant $\dot{M}$")
ax.tick_params(axis='x', labelsize=26)
ax.tick_params(axis='y', labelsize=26)

ax.set_xlabel('log$(T_{\mathrm{eff}}[K])$',fontsize=26)
ax.set_ylabel('log$(L/L_{\odot}$)',fontsize=26)

# Add the markers
marker_coords = [(4.1293,1.4694),
                (4.2790,2.1333),
                (4.3790,2.5751),
                (4.4521,2.9016),
                (4.5563,3.3746),
                (4.6303,3.7150),
                (4.6788,4.0754),
                (4.7306,4.3346),
                (4.7942,4.6600),
                (4.8633,5.0928),
                (4.8983,5.3706),
                (4.9361,5.7251),
                (4.9604,5.9992),
                (4.9773,6.2475)]

# Create array for marker sizes
marker_sizes = np.full((len(marker_coords),), 20)  # Note the comma after len(marker_coords)
marker_sizes[-1] = 40  # Last marker twice as big

for (x, y), size in zip(marker_coords, marker_sizes):
    ax.scatter(x, y, color='black', zorder=5, s=size)  # zorder=5 to make sure markers are on top

# Connect the markers
marker_coords_arr = np.array(marker_coords)
ax.plot(marker_coords_arr[:,0], marker_coords_arr[:,1], color='black', label='ZAMS')

# Add the labels
label_coords_texts = [(4.1780,1.4194, '2'),
                      (4.3300,1.9300, '3'),
                      (4.4280,2.3451, '4'),
                      (4.5000,2.6556, '5'),
                      (4.6000,3.0646, '7'),
                      (4.6850,3.4950, '9'),
                      (4.7700,3.9704, '12'),
                      (4.82000,4.2500, '15'),
                      (4.8800,4.5800, '20'),
                      (4.9350,4.9900, '30'),
                      (4.9780,5.3706, '40'),
                      (5.0100,5.7900, '60'),
                      (5.0380,6.0002, '85'),
                      (5.0790,6.317, '120')]

for x, y, text in label_coords_texts:
    ax.text(x, y-0.1, text, fontsize=14, color='black', ha='center', va='center')  # Adjust label position to not overlap

# Add the isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max, alpha = 5.2, 3.6, 0.7

for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    ax.text(*(np.array(point_A) + np.array(point_B)) / 2, label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

leg = plt.legend(loc='lower left', shadow=True, prop={'size': 14})
ax.set_ylim(1.235, 8)
ax.set_xlim(3.5, 5.2)
ax.invert_xaxis()

fig.set_size_inches(8, 8)
plt.show()



######## HRD 1e-3 for three metallicities #######################
##### HRD_
# gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',1)
# gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/3.712e-4Msun_yr/P002z0S0.dat',2)
from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]

    extended_T_min = T_min + 1.0  # Extend the lower limit
    extended_T_max = T_max - 1.0  # Extend the upper limit

    log_T_range = np.linspace(extended_T_min, extended_T_max, num_points)
    ax.plot(log_T_range, slope * log_T_range + intercept, linestyle='--', color='grey', alpha=alpha)


L_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',skip_header=0))[3])
T_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',skip_header=0))[4])
L_D = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.dat',skip_header=0))[3])
T_D = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.dat',skip_header=0))[4])
L_E = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.dat',skip_header=0))[3])
T_E = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.dat',skip_header=0))[4])
fig,ax=plt.subplots()
ax.plot(T_Y,L_Y,linewidth=2.6, color='black',linestyle='solid',label="Z = $0$")
ax.plot(T_D,L_D,linewidth=2.6, color='magenta',linestyle='solid',label="Z = $1x10^{-6}$")
ax.plot(T_E,L_E,linewidth=2.6, color='orange',linestyle='solid',label="Z = $0.014$")
ax.tick_params(axis='x', labelsize=26)
ax.tick_params(axis='y', labelsize=26)

ax.set_xlabel('log$(T_{\mathrm{eff}}[K])$',fontsize=26)
ax.set_ylabel('log$(L/L_{\odot}$)',fontsize=26)

# Add the markers
marker_coords = [(4.1293,1.4694),
                (4.2790,2.1333),
                (4.3790,2.5751),
                (4.4521,2.9016),
                (4.5563,3.3746),
                (4.6303,3.7150),
                (4.6788,4.0754),
                (4.7306,4.3346),
                (4.7942,4.6600),
                (4.8633,5.0928),
                (4.8983,5.3706),
                (4.9361,5.7251),
                (4.9604,5.9992),
                (4.9773,6.2475)]

# Create array for marker sizes
#marker_sizes = np.full((len(marker_coords),), 20)  # Note the comma after len(marker_coords)
#marker_sizes[-1] = 40  # Last marker twice as big

#for (x, y), size in zip(marker_coords, marker_sizes):
#    ax.scatter(x, y, color='black', zorder=5, s=size)  # zorder=5 to make sure markers are on top

# Connect the markers
#marker_coords_arr = np.array(marker_coords)
#ax.plot(marker_coords_arr[:,0], marker_coords_arr[:,1], color='black', label='ZAMS')

# Add the labels
label_coords_texts = [(4.1780,1.4194, '2'),
                      (4.3300,1.9300, '3'),
                      (4.4280,2.3451, '4'),
                      (4.5000,2.6556, '5'),
                      (4.6000,3.0646, '7'),
                      (4.6850,3.4950, '9'),
                      (4.7700,3.9704, '12'),
                      (4.82000,4.2500, '15'),
                      (4.8800,4.5800, '20'),
                      (4.9350,4.9900, '30'),
                      (4.9780,5.3706, '40'),
                      (5.0100,5.7900, '60'),
                      (5.0380,6.0002, '85'),
                      (5.0790,6.317, '120')]

#for x, y, text in label_coords_texts:
#    ax.text(x, y-0.1, text, fontsize=14, color='black', ha='center', va='center')  # Adjust label position to not overlap

# Add the isoradius lines
isoradius_lines = [
    ((5.079, 3.278), (4.809, 2.196), "0.1 R$_\odot$"),
    ((5.079, 5.279), (4.309, 2.196), "1 R$_\odot$"),
    ((5.079, 7.297), (3.809, 2.196), "10 R$_\odot$"),
    ((4.621, 7.464), (3.629, 3.477), "100 R$_\odot$"),
    ((4.1258, 7.464), (3.629, 5.477), "1000 R$_\odot$"),
    ((3.9696, 8.8409), (3.6322, 7.4880), "10000 R$_\odot$")
]

T_min, T_max, alpha = 5.2, 3.6, 0.7

for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    ax.text(*(np.array(point_A) + np.array(point_B)) / 2, label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

leg = plt.legend(loc='lower left', shadow=True, prop={'size': 18})
ax.set_ylim(2, 8.5)
ax.set_xlim(3.5, 5.2)
ax.invert_xaxis()

fig.set_size_inches(8, 8)
plt.show()
