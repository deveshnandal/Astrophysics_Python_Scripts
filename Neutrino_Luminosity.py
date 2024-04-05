##### Neutrino luminosity versus nuclear luminosity
##### At end of computation
import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt

#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',1)
epsnu = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[16])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[4])
Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[49])

L = integrate.cumtrapz(epsnu,R, initial=0)

fig,ax=plt.subplots()
ax.plot(Mr,L,linewidth=2., label="$3053 M_{\odot}$")
ax.set_xlabel('Mass$[M_\odot]$',fontsize=24, fontweight='bold')
ax.set_ylabel('Luminosity',fontsize=24, fontweight='bold')
ax.set_yscale('log')
leg = plt.legend(loc='upper right', shadow=True,prop={'size': 9})
#fig.tight_layout()
plt.show()
################
##### At end Sib, v0177201
import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
Msol=1.9884*10**33
#gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',1)
epsnu = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[16])
epsC = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[12])
epsY = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[11])
epsX = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[10])
eps_grav = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[27])

eps_nucl = epsC+epsY+epsX
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[4])
Mr = Msol*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[49])

dMr = np.diff(-Mr)
dMr = np.insert(dMr,0,0)
L_neut = np.cumsum((dMr*epsnu)[::-1])[::-1]
L_nucl = np.cumsum((dMr*eps_nucl)[::-1])[::-1]
L_grav = np.cumsum((dMr*eps_grav)[::-1])[::-1]

fig,ax=plt.subplots()
ax.plot(Mr/Msol,-L_neut,linewidth=2., label="$-Neutrino$")# negative can be put in the end
ax.plot(Mr/Msol,L_nucl,linewidth=2., label="$Nuclear$")
ax.plot(Mr/Msol,L_grav,linewidth=2., label="$Gravitational$")

ax.set_xlabel('Mass$[M_\odot]$',fontsize=24, fontweight='bold')
ax.set_ylabel('Luminosity',fontsize=24, fontweight='bold')
ax.set_yscale('log')
leg = plt.legend(loc='lower right', shadow=True,prop={'size': 9})
#fig.tight_layout()
plt.show()

############################################
########## GPT generated code ######## WORKS
############################################
import numpy as np
from matplotlib import pyplot as plt

def read_star_data(filepath):
    data = []
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            if i < 293:
                continue
            data.append(list(map(float, line.strip().split())))
    data = np.array(data)
    return data

data = read_star_data('P002z0S0.v0170461')

Msol = 1.9884 * 10**33
R = 10**data[:, 4]
Mr = Msol * data[:, 49]

dMr = np.diff(-Mr)
dMr = np.insert(dMr, 0, 0)

epsnu = data[:, 16]
epsC = data[:, 12]
epsY = data[:, 11]
epsX = data[:, 10]
eps_grav = data[:, 27]
eps_nucl = epsC + epsY + epsX

L_neut = np.flip(np.cumsum(np.flip(dMr * epsnu)))
L_nucl = np.flip(np.cumsum(np.flip(dMr * eps_nucl)))
L_grav = np.flip(np.cumsum(np.flip(dMr * eps_grav)))

fig, ax = plt.subplots()
ax.plot(Mr / Msol, -L_neut, linewidth=2., label="$-Neutrino$")
ax.plot(Mr / Msol, L_nucl, linewidth=2., label="$Nuclear$")
ax.plot(Mr / Msol, L_grav, linewidth=2., label="$Gravitational$")

ax.set_xlabel('Mass $[M_\odot]$', fontsize=24, fontweight='bold')
ax.set_ylabel('Luminosity $[erg/s]$', fontsize=24, fontweight='bold')
ax.set_yscale('log')
ax.legend(loc='lower right', shadow=True, fontsize=9)
plt.show()

######## GPT attempt 2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def read_star_data(filepath):
    data = []
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            if i < 293:
                continue
            data.append(list(map(float, line.strip().split())))
    data = np.array(data)
    return data

data = read_star_data('P002z0S0.v0170461')

Msol = 1.9884 * 10**33
R = 10**data[:, 4]
Mr = Msol * data[:, 49]

dMr = np.diff(-Mr)
dMr = np.insert(dMr, 0, 0)

epsnu = data[:, 16]
epsC = data[:, 12]
epsY = data[:, 11]
epsX = data[:, 10]
eps_grav = data[:, 27]
eps_nucl = epsC + epsY + epsX

L_neut = np.flip(np.cumsum(np.flip(dMr * epsnu)))
L_nucl = np.flip(np.cumsum(np.flip(dMr * eps_nucl)))
L_grav = np.flip(np.cumsum(np.flip(dMr * eps_grav)))

fig, ax = plt.subplots()
ax.plot(Mr / Msol, -L_neut, linewidth=3., color='b', label="$-Neutrino$")
ax.plot(Mr / Msol, L_nucl, linewidth=3., color='g', label="$Nuclear$")
ax.plot(Mr / Msol, L_grav, linewidth=3., color='r', label="$Gravitational$")

ax.set_xlabel('Mass $[M_\odot]$', fontsize=24, fontweight='bold')
ax.set_ylabel('Luminosity $[erg/s]$', fontsize=24, fontweight='bold')
ax.set_yscale('log')
ax.legend(loc='lower right', shadow=True, fontsize=9)
ax.grid(True)
plt.title('Star Luminosity')
plt.gca().xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.set_yscale('log')
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.show()
