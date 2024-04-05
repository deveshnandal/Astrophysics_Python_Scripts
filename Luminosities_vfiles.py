# Loading the values from last .v file #####
import numpy as np
from matplotlib import pyplot as plt

Msol=1.9884*10**33
# defining the path
path = '/Users/hermit/Observatory/StarCalc/Betelgeuse/P019Z0.02S0.2_fitm0.92/P019Z0.02S0.2_fitm0.92.v0136741.gz'

epsnu = (np.transpose(np.genfromtxt(path, skip_header=3))[16])
epsC = (np.transpose(np.genfromtxt(path, skip_header=3))[12])
epsY = (np.transpose(np.genfromtxt(path, skip_header=3))[11])
epsX = (np.transpose(np.genfromtxt(path, skip_header=3))[10])

eps_nucl = epsC+epsY+epsX
R = 10**(np.transpose(np.genfromtxt(path, skip_header=3))[4])
Mr = Msol*(np.transpose(np.genfromtxt(path, skip_header=3))[49])

dMr = np.diff(-Mr)
dMr = np.insert(dMr,0,0)
L_neut = np.cumsum((dMr*epsnu)[::-1])[::-1]
L_nucl = np.cumsum((dMr*eps_nucl)[::-1])[::-1]

fig, ax = plt.subplots()
ax.plot(Mr/Msol, -L_neut, linewidth=2., label="$-Neutrino$")
ax.plot(Mr/Msol, L_nucl, linewidth=2., label="$Nuclear$")

ax.set_xlabel('Mass$[M_\\odot]$', fontsize=24, fontweight='bold')
ax.set_ylabel('Luminosity', fontsize=24, fontweight='bold')
ax.set_yscale('log')
leg = plt.legend(loc='lower right', shadow=True, prop={'size': 9})

plt.show()


######################
## Loading from all .v vfiles

import os
import numpy as np
import gzip
from matplotlib import pyplot as plt
import re

def get_last_iteration(file_path, labels):
    with gzip.open(file_path, 'rt') as file:  # open the file as text with gzip module
        lines = file.readlines()
    lines.reverse()
    for i, line in enumerate(lines):
        if any(label in line for label in labels):
            break
    last_iteration = lines[:i+1]
    last_iteration.reverse()
    last_iteration = np.genfromtxt(last_iteration)
    return last_iteration

labels = ['epsc', 'epsy', 'epsx', 'epsnu']
folder_path = '/Users/hermit/Observatory/StarCalc/Betelgeuse/P019Z0.02S0.2_fitm0.92/'

# Use a regex to match only the expected file names
pattern = re.compile(r"P019Z0\.02S0\.2_fitm0\.92\.v\d+\.gz$")

files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if pattern.match(file)]

# Sorting function updated to handle file path correctly
files.sort(key=lambda x: int(x.split('/')[-1].split('v')[-1].split('.gz')[0]))

Msol = 1.9884*10**33
L_neut_list = []
L_nucl_list = []
mass_list = []

for file in files:
    data = get_last_iteration(file, labels)
    epsnu = data[16]
    epsC = data[12]
    epsY = data[11]
    epsX = data[10]
    eps_nucl = epsC + epsY + epsX
    Mr = Msol * data[49]
    dMr = np.diff(-Mr)
    dMr = np.insert(dMr,0,0)
    L_neut = np.sum(dMr * epsnu)
    L_nucl = np.sum(dMr * eps_nucl)
    L_neut_list.append(L_neut)
    L_nucl_list.append(L_nucl)
    mass_list.append(Mr[0]/Msol)

fig, ax = plt.subplots()
ax.plot(mass_list, -np.array(L_neut_list), linewidth=2., label="$-Neutrino$")
ax.plot(mass_list, np.array(L_nucl_list), linewidth=2., label="$Nuclear$")
ax.set_xlabel('Mass$[M_\\odot]$', fontsize=24, fontweight='bold')
ax.set_ylabel('Luminosity', fontsize=24, fontweight='bold')
ax.set_yscale('log')
leg = plt.legend(loc='best', shadow=True, prop={'size': 9})

plt.show()
