from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

L = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/P002z0S0.dat',skip_header=0))[3])
T = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/P002z0S0.dat',skip_header=0))[4])
M_dot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/P002z0S0.dat',skip_header=0))[116])
# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
#norm = plt.Normalize(M_dot.min(), M_dot.max())
#lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
#lc.set_array(M_dot)
#lc.set_linewidth(2.)
#line = axs[0].add_collection(lc)
#fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = 'gist_ncar'#ListedColormap(["cyan", "gold", 'm', 'w', 'k'])''
#norm = BoundaryNorm([1e-5, 1e-4, 1e-3, 1e-2, 1.e-1], cmap.N)
lc = LineCollection(segments, cmap=cmap)#, norm=norm)

lc.set_array(M_dot)
lc.set_linewidth(2)
line = axs.add_collection(lc)
fig.colorbar(line, ax=axs)

axs.set_xlim(3.6, 5.2)
axs.set_ylim(2, 7.8)
axs.set_xlabel('$log(Teff)$',fontsize=12)
axs.set_ylabel('$log(L/L_{\odot}$)',fontsize=12)
axs.invert_xaxis()
plt.show()

################

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

L = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1923.dat',skip_header=0))[3])
T = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1923.dat',skip_header=0))[4])
M_dot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1923.dat',skip_header=0))[116])
# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
#norm = plt.Normalize(M_dot.min(), M_dot.max())
#lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
#lc.set_array(M_dot)
#lc.set_linewidth(2.)
#line = axs[0].add_collection(lc)
#fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = 'tab20'#ListedColormap(["cyan", "gold", 'm', 'w', 'k'])''
#norm = BoundaryNorm([1e-5, 1e-4, 1e-3, 1e-2, 1.e-1], cmap.N)
lc = LineCollection(segments, cmap=cmap)#, norm=norm)

lc.set_array(M_dot)
lc.set_linewidth(2)
line = axs.add_collection(lc)
fig.colorbar(line, ax=axs)

axs.set_xlim(3.6, 5.2)
axs.set_ylim(2, 8.8)
axs.set_xlabel('$log(Teff)$',fontsize=12)
axs.set_ylabel('$log(L/L_{\odot}$)',fontsize=12)
axs.invert_xaxis()
plt.show()

############

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

L = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[3])
T = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[4])
M_dot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',skip_header=0))[116])
# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
#norm = plt.Normalize(M_dot.min(), M_dot.max())
#lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
#lc.set_array(M_dot)
#lc.set_linewidth(2.)
#line = axs[0].add_collection(lc)
#fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = 'tab20'#ListedColormap(["cyan", "gold", 'm', 'w', 'k'])''
#norm = BoundaryNorm([1e-5, 1e-4, 1e-3, 1e-2, 1.e-1], cmap.N)
lc = LineCollection(segments, cmap=cmap)#, norm=norm)

lc.set_array(M_dot)
lc.set_linewidth(2)
line = axs.add_collection(lc)
fig.colorbar(line, ax=axs)

axs.set_xlim(3.6, 5.2)
axs.set_ylim(2, 8.8)
axs.set_xlabel('$log(Teff)$',fontsize=12)
axs.set_ylabel('$log(L/L_{\odot}$)',fontsize=12)
axs.invert_xaxis()
plt.show()



####################


############ Try with a critical accretion Create

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

L = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[3])
T = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[4])
M_dot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[116])
# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
M_lim = np.where(M_dot > 7.0e-3,1,0)
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
#norm = plt.Normalize(M_dot.min(), M_dot.max())
#lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
#lc.set_array(M_dot)
#lc.set_linewidth(2.)
#line = axs[0].add_collection(lc)
#fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = 'jet'#ListedColormap(["cyan", "gold", 'm', 'w', 'k'])''
#norm = BoundaryNorm([1e-5, 1e-4, 1e-3, 1e-2, 1.e-1], cmap.N)
lc = LineCollection(segments, cmap=cmap)#, norm=norm)

lc.set_array(M_lim)
lc.set_linewidth(2)
line = axs.add_collection(lc)
fig.colorbar(line, ax=axs)

axs.set_xlim(3.6, 5.2)
axs.set_ylim(2, 8.8)
axs.set_xlabel('$log(Teff)$',fontsize=12)
axs.set_ylabel('$log(L/L_{\odot}$)',fontsize=12)
axs.invert_xaxis()
plt.show()


########### GPT 4 code
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, radius, T_min, T_max, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified radius,
    log(T_eff) range, and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    log_L = 2 * np.log10(radius) + log_T_range
    ax.plot(log_T_range, log_L, linestyle='--', label=f'$R/R_\odot = {radius}$')

# Load the data
data_file = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat'
data = np.genfromtxt(data_file, skip_header=0)
L = np.transpose(data[:, 3])
T = np.transpose(data[:, 4])
M_dot = np.transpose(data[:, 116])

# Create line segments for individual coloring
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Prepare the figure and axis
fig, ax = plt.subplots()

# Set colormap and create LineCollection
cmap = 'tab20'
lc = LineCollection(segments, cmap=cmap)
lc.set_array(M_dot)
lc.set_linewidth(2)
line = ax.add_collection(lc)

# Add colorbar
cbar = fig.colorbar(line, ax=ax)
cbar.set_label('Accretion Rate')

# Plot isoradius lines
isoradius_values = [1, 10, 100, 1000, 10000]  # List of isoradius values
T_min, T_max = 3.6, 5.2

for radius in isoradius_values:
    isoradius_line(ax, radius, T_min, T_max)

ax.legend()

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=12)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=12)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 8.8)
ax.invert_xaxis()

# Show the plot
plt.show()

#########
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, radius, T_min, T_max, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified radius,
    log(T_eff) range, and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (7.280 - 5.280) / (4.301 - 3.810)
    log_L = slope * (log_T_range - 4.301) + 5.280 - 2 * np.log10(radius)
    ax.plot(log_T_range, log_L, linestyle='--', label=f'$R/R_\odot = {radius}$')

# Load the data
data_file = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat'
data = np.genfromtxt(data_file, skip_header=0)
L = np.transpose(data[:, 3])
T = np.transpose(data[:, 4])
M_dot = np.transpose(data[:, 116])

# Create line segments for individual coloring
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Prepare the figure and axis
fig, ax = plt.subplots()

# Set colormap and create LineCollection
cmap = 'tab20'
lc = LineCollection(segments, cmap=cmap)
lc.set_array(M_dot)
lc.set_linewidth(2)
line = ax.add_collection(lc)

# Add colorbar
cbar = fig.colorbar(line, ax=ax)
cbar.set_label('Accretion Rate')

# Plot isoradius lines
isoradius_values = [1, 10, 100, 1000, 10000]  # List of isoradius values
T_min, T_max = 3.6, 5.2

for radius in isoradius_values:
    isoradius_line(ax, radius, T_min, T_max)

ax.legend()

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=12)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=12)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 7.46)
ax.invert_xaxis()

# Show the plot
plt.show()


############ WORKS with manual ticks for isoradius lines
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified points A and B,
    and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    ax.plot(log_T_range, log_L, linestyle='--')

# Load the data
data_file = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat'
data = np.genfromtxt(data_file, skip_header=0)
L = np.transpose(data[:, 3])
T = np.transpose(data[:, 4])
M_dot = np.transpose(data[:, 116])

# Create line segments for individual coloring
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Prepare the figure and axis
fig, ax = plt.subplots()

# Set colormap and create LineCollection
cmap = 'tab20'
lc = LineCollection(segments, cmap=cmap)
lc.set_array(M_dot)
lc.set_linewidth(2)
line = ax.add_collection(lc)

# Add colorbar
cbar = fig.colorbar(line, ax=ax)
cbar.set_label('Accretion Rate', fontsize=16)
cbar.ax.tick_params(labelsize=16)

# Plot isoradius lines
isoradius_points = [
    ((5.079, 3.278), (4.809, 2.196)),  # 0.1 Rsol
    ((5.079, 5.279), (4.309, 2.196)),  # 1 Rsol
    ((5.079, 7.297), (3.809, 2.196)),  # 10 Rsol
    ((4.621, 7.464), (3.629, 3.477)),  # 100 Rsol
    ((4.1258, 7.464), (3.629, 5.477)),  # 1000 Rsol
    ((3.9696, 8.8409), (3.6322, 7.4880)),  # 10000 Rsol
]

T_min, T_max = 5.2, 3.6

for point_A, point_B in isoradius_points:
    isoradius_line(ax, point_A, point_B, T_min, T_max)

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=16)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=16)
ax.tick_params(axis='both', labelsize=16)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 7.46)

# Show the plot
plt.show()


############### shading the region between isoradius lines
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def isoradius_line(ax, point_A, point_B, T_min, T_max, num_points=100):
    """
    Plot an isoradius line on the given axis with the specified points A and B,
    and number of points.
    """
    log_T_range = np.linspace(T_min, T_max, num_points)
    slope = (point_A[1] - point_B[1]) / (point_A[0] - point_B[0])
    intercept = point_A[1] - slope * point_A[0]
    log_L = slope * log_T_range + intercept
    return log_T_range, log_L

def shade_area(ax, log_T_range, log_L1, log_L2, alpha=0.2):
    ax.fill_between(log_T_range, log_L1, log_L2, alpha=alpha)

# Load the data
data_file = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat'
data = np.genfromtxt(data_file, skip_header=0)
L = np.transpose(data[:, 3])
T = np.transpose(data[:, 4])
M_dot = np.transpose(data[:, 116])

# Create line segments for individual coloring
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Prepare the figure and axis
fig, ax = plt.subplots()

# Set colormap and create LineCollection
cmap = 'tab20'
lc = LineCollection(segments, cmap=cmap)
lc.set_array(M_dot)
lc.set_linewidth(2)
line = ax.add_collection(lc)

# Add colorbar
cbar = fig.colorbar(line, ax=ax)
cbar.set_label('Accretion Rate', fontsize=16)
cbar.ax.tick_params(labelsize=16)

# Plot isoradius lines
isoradius_points = [
    ((5.079, 3.278), (4.809, 2.196)),  # 0.1 Rsol
    ((5.079, 5.279), (4.309, 2.196)),  # 1 Rsol
    ((5.079, 7.297), (3.809, 2.196)),  # 10 Rsol
    ((4.621, 7.464), (3.629, 3.477)),  # 100 Rsol
    ((4.1258, 7.464), (3.629, 5.477))  # 1000 Rsol
]

T_min, T_max = 5.2, 3.6

log_L_prev = None
for point_A, point_B in isoradius_points:
    log_T_range, log_L = isoradius_line(ax, point_A, point_B, T_min, T_max)
    if log_L_prev is not None:
        shade_area(ax, log_T_range, log_L_prev, log_L)
    log_L_prev = log_L

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=16)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=16)
ax.tick_params(axis='both', labelsize=16)
ax.set_xlim(T_min, T_max)
ax.set_ylim(2, 7.46)

# Show the plot
plt.show()

########## Merging two codes and shading the isoradius lines: not working correctly
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Function to create isoradius lines
def isoradius_line(ax, logL, logT, logR, alpha=0.7, cmap='cubehelix'):
    contour = ax.contourf(logT, logL, logR, alpha=alpha, cmap=cmap, levels=np.log10([1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 1e4, 1e5, 1e6, 1e7]))
    return contour

# Load the data
data_file = '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat'
data = np.genfromtxt(data_file, skip_header=0)
L = np.transpose(data[:, 3])
T = np.transpose(data[:, 4])
M_dot = np.transpose(data[:, 116])

# Create line segments for individual coloring
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Prepare the figure and axis
fig, ax = plt.subplots()

# Set colormap and create LineCollection
cmap = 'tab20'
lc = LineCollection(segments, cmap=cmap)
lc.set_array(M_dot)
lc.set_linewidth(2)
line = ax.add_collection(lc)

# Add colorbar
cbar = fig.colorbar(line, ax=ax)
cbar.set_label('Accretion Rate', fontsize=16)
cbar.ax.tick_params(labelsize=16)

# Define logT and logL ranges
logT_range = np.linspace(5.5, 3.2, 100)
logL_range = np.linspace(0, 11, 100)

# Calculate logR
L_sun = 3.827e26
R_sun = 696340e3
R = np.array([[np.sqrt((10**Li)*L_sun/(4*np.pi*5.67e-8*(10**Ti)**4)) for Li in logL_range] for Ti in logT_range]) / R_sun
logR = np.log10(R)

# Plot isoradius lines
isoradius_line(ax, logL_range, logT_range, logR)

# Set axis labels and limits
ax.set_xlabel('$\log(T_{eff})$', fontsize=16)
ax.set_ylabel('$\log(L/L_{\odot})$', fontsize=16)
ax.tick_params(axis='both', labelsize=16)
ax.set_xlim(5.2, 3.6)
ax.set_ylim(2, 7.46)

# Show the plot
plt.show()
