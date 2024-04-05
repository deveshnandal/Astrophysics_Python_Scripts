
import numpy as np
import matplotlib.pyplot as plt
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',5)
gtb.set_lineWidth(3)
gtb.CBLimits(min=0,max=0.7512)
gtb.Limits(xmax=5.2)
gtb.mark_phase('H',colour='0.10')
gtb.set_colourMap('jet')
gtb.HRD_plot(zcol='H1c')
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')
x1 = [3.7518]
y1 = [1.8345]
plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
plt.text(3.813, 1.45, 'I L', fontsize = 18, fontweight="bold")
x2 = [4.1315]
y2 = [4.1668]
plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
plt.text(4.082, 2.60, 'II L', fontsize = 18, fontweight="bold")
x3 = [4.948]
y3 = [5.84]
plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
plt.text(4.609, 4.56, 'III L', fontsize = 18, fontweight="bold")
plt.text(4.495, 8.15, 'IV L', fontsize = 18, fontweight="bold")
####
x1 = [3.713]
y1 = [5.812]
plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
plt.text(3.762, 3.03, 'I H', fontsize = 18, fontweight="bold")
x2 = [4.272]
y2 = [5.279]
plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
plt.text(4.228, 5.75, 'II H', fontsize = 18, fontweight="bold")
x3 = [3.763]
y3 = [8.08]
plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
plt.text(3.950, 7.28, 'III H', fontsize = 18, fontweight="bold")
plt.text(4.011, 8.47, 'IV H', fontsize = 18, fontweight="bold")
gtb.add_label(4.162,7.98,'$10^{-3}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.197,9.00,'$10^{-2}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.225,9.46,'$10^{-1}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.250,9.88,'$1M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.276,10.28,'$10M_{\odot}/yr$',fontsize=12)


########### without labels


import numpy as np
import matplotlib.pyplot as plt
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',5)
gtb.set_lineWidth(3)
gtb.CBLimits(min=0,max=0.7512)
gtb.Limits(xmax=5.2)
gtb.mark_phase('H',colour='0.10')
gtb.set_colourMap('jet')
gtb.HRD_plot(zcol='H1c')
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')
#x1 = [3.7518]
#y1 = [1.8345]
#plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
#plt.text(3.813, 1.45, 'I L', fontsize = 18, fontweight="bold")
#x2 = [4.1315]
#y2 = [4.1668]
#plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
#plt.text(4.082, 2.60, 'II L', fontsize = 18, fontweight="bold")
#x3 = [4.948]
#y3 = [5.84]
#plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
#plt.text(4.609, 4.56, 'III L', fontsize = 18, fontweight="bold")
#plt.text(4.495, 8.15, 'IV L', fontsize = 18, fontweight="bold")
####
#x1 = [3.713]
#y1 = [5.812]
#plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
#plt.text(3.762, 3.03, 'I H', fontsize = 18, fontweight="bold")
#x2 = [4.272]
#y2 = [5.279]
#plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
#plt.text(4.228, 5.75, 'II H', fontsize = 18, fontweight="bold")
#x3 = [3.763]
#y3 = [8.08]
#plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="black", markerfacecolor="white")
#plt.text(3.950, 7.28, 'III H', fontsize = 18, fontweight="bold")
#plt.text(4.011, 8.47, 'IV H', fontsize = 18, fontweight="bold")
gtb.add_label(4.162,7.98,'$10^{-3}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.197,9.00,'$10^{-2}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.225,9.46,'$10^{-1}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.250,9.88,'$1M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.276,10.28,'$10M_{\odot}/yr$',fontsize=12)


#################

import numpy as np
import matplotlib.pyplot as plt

# Define file paths
file_paths = [
    '/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',
    '/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat'
]

# Define plot markers
markers = [
    (3.7518, 1.8345, 'I L'),
    (4.1315, 4.1668, 'II L'),
    (4.948, 5.84, 'III L'),
    (4.495, 8.15, 'IV L'),
    (3.713, 5.812, 'I H'),
    (4.272, 5.279, 'II H'),
    (3.763, 8.08, 'III H'),
    (4.011, 8.47, 'IV H'),
]

# Function to set up plotting parameters
def setup_plots():
    gtb.set_lineWidth(3)
    gtb.CBLimits(min=0,max=0.7512)
    gtb.Limits(xmax=5.2)
    gtb.mark_phase('H',colour='0.10')
    gtb.set_colourMap('jet')

# Function to add markers and labels
def add_markers_labels():
    for x, y, label in markers:
        gtb.add_marker(x, y, markersize=8, markeredgecolor="black", markerfacecolor="white")

        gtb.add_label(x, y, label, fontsize=18, fontweight="bold")

#Load in data files
for i, file_path in enumerate(file_paths):
    gtb.loadE(file_path, i+1)

#Set up plotting parameters
setup_plots()

#Create HRD plot and isoradius lines
fig, ax = plt.subplots()
gtb.HRD_plot(zcol='H1c')
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')

#Add markers and labels
add_markers_labels()

#Add accretion rate labels
gtb.add_label(4.162,7.98,'$10^{-3}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.197,9.00,'$10^{-2}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.225,9.46,'$10^{-1}M_{\odot}/yr$',fontsize=12)

#########With 0.075Msun Model ###########
########### without labels


import numpy as np
import matplotlib.pyplot as plt
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/7.5e-2Msun_yr/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',5)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',6)
gtb.set_lineWidth(3)
gtb.CBLimits(min=0,max=0.7512)
gtb.Limits(xmax=5.2)
gtb.mark_phase('H',colour='0.10')
gtb.set_colourMap('jet')
gtb.HRD_plot(zcol='H1c')
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')
