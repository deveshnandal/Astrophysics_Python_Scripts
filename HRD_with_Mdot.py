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
    cmap = 'viridis'
    lc = LineCollection(segments, cmap=cmap)
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

# Add colorbar
ticks = np.linspace(0, 0.25, 10)
cbar = fig.colorbar(line, ax=ax, ticks=ticks)
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






################################################################################
########## Working code but shorter ##############

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    ax.plot(log_T_range, slope * log_T_range + intercept, linestyle='--', color='grey', alpha=alpha)

data_files = ['/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',
              '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat']

fig, ax = plt.subplots()

for data_file in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L, T, M_dot = data[:, [3, 4, 116]].T
    segments = np.array([T, L]).T.reshape(-1, 1, 2)
    lc = LineCollection(np.concatenate([segments[:-1], segments[1:]], axis=1), cmap='viridis')
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

cbar = fig.colorbar(line, ax=ax, ticks=np.linspace(0, 0.25, 10))
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

T_min, T_max, alpha = 5.2, 3.6, 0.7

for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    ax.text(*(np.array(point_A) + np.array(point_B)) / 2, label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

ax.set(xlabel='$\log(T_{eff})$', ylabel='$\log(L/L_{\odot})$', xlim=(T_min, T_max), ylim=(2, 8.44))
ax.tick_params(axis='both', labelsize=20)
fig.set_size_inches(8, 8)
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, alpha, num_points=100):
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    ax.plot(log_T_range, slope * log_T_range + intercept, linestyle='--', color='grey', alpha=alpha)

data_files = ['/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',
              '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat']

fig, ax = plt.subplots()

for data_file in data_files:
    data = np.genfromtxt(data_file, skip_header=0)
    L, T, M_dot = data[:, [3, 4, 116]].T
    segments = np.array([T, L]).T.reshape(-1, 1, 2)
    lc = LineCollection(np.concatenate([segments[:-1], segments[1:]], axis=1), cmap='Accent')
    lc.set_array(M_dot)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)

cbar = fig.colorbar(line, ax=ax, ticks=np.linspace(0, 0.25, 10))
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

T_min, T_max, alpha = 5.2, 3.6, 0.7

for point_A, point_B, label in isoradius_lines:
    isoradius_line(ax, point_A, point_B, T_min, T_max, alpha)
    ax.text(*(np.array(point_A) + np.array(point_B)) / 2, label, fontsize=14, color='grey', alpha=alpha, ha='center', va='center')

ax.set(xlabel='$\log(T_{eff})$', ylabel='$\log(L/L_{\odot})$', xlim=(T_min, T_max), ylim=(2, 8.44))
ax.xaxis.label.set_size(22)
ax.yaxis.label.set_size(22)
ax.tick_params(axis='both', labelsize=20)
fig.set_size_inches(8, 8)
plt.show()
