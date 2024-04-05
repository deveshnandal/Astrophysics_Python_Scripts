# First 5 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_493M_SS70.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_493M_SS70.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_497M_SS69.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_497M_SS69.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_507M_SS67.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_507M_SS67.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_507M_SS68.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_507M_SS68.txt',skip_header=3))[1])

a_6 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1923M_SS6.txt',skip_header=3))[0])
t_6 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1923M_SS6.txt',skip_header=3))[1])
fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M$_{\odot}SS71$')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='493M$_{\odot}SS70$')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='497M$_{\odot}SS69$')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='507M$_{\odot}SS67$')
#ax.plot(t_5,a_5,color='tab:yellow',linewidth=2.,label='507M$_{\odot}SS68$')
ax.plot(t_6,a_6,color='tab:green',linewidth=2.,label='1923M$_{\odot}SS68$')

ax.legend(loc='upper left', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 6-10 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_510M_SS66.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_510M_SS66.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_511M_SS65.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_511M_SS65.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_515M_SS64.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_515M_SS64.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_536M_SS63.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_536M_SS63.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_549M_SS62.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_549M_SS62.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M$_{\odot}SS71$')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='493M$_{\odot}SS70$')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='497M$_{\odot}SS69$')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='507M$_{\odot}SS67$')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='507M$_{\odot}SS68$')

ax.legend(loc='upper left', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 11-15 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_565M_SS61.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_565M_SS61.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_567M_SS60.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_567M_SS60.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_580M_SS59.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_580M_SS59.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_616M_SS58.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_616M_SS58.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_620M_SS57.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_620M_SS57.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M$_{\odot}SS71$')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='493M$_{\odot}SS70$')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='497M$_{\odot}SS69$')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='507M$_{\odot}SS67$')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='507M$_{\odot}SS68$')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 16-20 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_625M_SS56.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_625M_SS56.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_631M_SS55.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_631M_SS55.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_646M_SS54.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_646M_SS54.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_666M_SS53.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_666M_SS53.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_667M_SS52.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_667M_SS52.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M$_{\odot}SS71$')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='493M$_{\odot}SS70$')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='497M$_{\odot}SS69$')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='507M$_{\odot}SS67$')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='507M$_{\odot}SS68$')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 21-25 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_682M_SS51.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_682M_SS51.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_683M_SS50.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_683M_SS50.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_686M_SS49.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_686M_SS49.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_689M_SS48.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_689M_SS48.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_696M_SS47.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_696M_SS47.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M$_{\odot}SS71$')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='493M$_{\odot}SS70$')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='497M$_{\odot}SS69$')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='507M$_{\odot}SS67$')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='507M$_{\odot}SS68$')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 26-30 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_709M_SS46.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_709M_SS46.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_726M_SS45.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_726M_SS45.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_732M_SS44.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_732M_SS44.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_739M_SS43.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_739M_SS43.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_740M_SS42.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_740M_SS42.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M$_{\odot}SS71$')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='493M$_{\odot}SS70$')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='497M$_{\odot}SS69$')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='507M$_{\odot}SS67$')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='507M$_{\odot}SS68$')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 31-35 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_748M_SS41.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_748M_SS41.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_771M_SS40.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_771M_SS40.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_778M_SS39.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_778M_SS39.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_808M_SS38.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_808M_SS38.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_834M_SS37.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_834M_SS37.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M$_{\odot}SS71$')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='748M_SS41')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='778M_SS39')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='808M_SS38')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='834M_SS37')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 36-40 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_856M_SS36.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_856M_SS36.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_858M_SS35.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_858M_SS35.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_862M_SS34.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_862M_SS34.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_886M_SS33.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_886M_SS33.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_887M_SS32.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_887M_SS32.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='856M_SS36')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='858M_SS35')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='778M_SS39')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='886M_SS33')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='887M_SS32')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 41-45 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_912M_SS30.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_912M_SS30.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_912M_SS31.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_912M_SS31.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_921M_SS29.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_921M_SS29.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_924M_SS28.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_924M_SS28.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_932M_SS27.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_932M_SS27.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='912M_SS30')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='912M_SS31')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='921M_SS29')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='924M_SS28')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='932M_SS27')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 46-50 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_946M_SS26.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_946M_SS26.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_956M_SS25.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_956M_SS25.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_965M_SS24.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_965M_SS24.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_969M_SS23.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_969M_SS23.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_986M_SS22.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_986M_SS22.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='946M_SS26')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='956M_SS25')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='965M_SS24')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='969M_SS23')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='986M_SS22')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 51-55 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1008M_SS21.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1008M_SS21.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1135M_SS20.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1135M_SS20.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1177M_SS19.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1177M_SS19.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1186M_SS18.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1186M_SS18.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1236M_SS17.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1236M_SS17.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='1008M_SS21')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='1135M_SS20')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='1177M_SS19')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='1186M_SS18')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='1236M_SS17')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 56-60 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1274M_SS16.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1274M_SS16.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1294M_SS15.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1294M_SS15.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1489M_SS13.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1489M_SS13.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1514M_SS12.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1514M_SS12.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='1274M_SS16')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='1294M_SS15')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='1331M_SS14')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='1489M_SS13')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='1514M_SS12')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 61-65 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1596M_SS11.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1596M_SS11.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1662M_SS10.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1662M_SS10.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1717M_SS9.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1717M_SS9.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1845M_SS8.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1845M_SS8.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1892M_SS7.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1892M_SS7.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='1596M_SS11')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='1662M_SS10')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='1717M_SS9')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='1845M_SS8')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='1892M_SS7')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show

# 66-70 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1923M_SS6.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1923M_SS6.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1924M_SS5.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1924M_SS5.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_2479M_SS4.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_2479M_SS4.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_2612M_SS3.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_2612M_SS3.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_2630M_SS2.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_2630M_SS2.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='1923M_SS6')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='1924M_SS5')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='2479M_SS4')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='2612M_SS3')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='2630M_SS2')

ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# 71-72 #

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_4477M_SS1.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_4477M_SS1.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt',skip_header=3))[1])


fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='4477M_SS1')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='6127M_SS0')


ax.legend(loc='upper right', shadow=True,prop={'size': 7})
ax.set_xlabel('Time [M$_{\odot}$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

############# Select Ten models ###############
############# First five ######################

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_771M_SS40.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_771M_SS40.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_778M_SS39.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_778M_SS39.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_932M_SS27.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_932M_SS27.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1135M_SS20.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1135M_SS20.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='491M_SS71')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='771M_SS40')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='778M_SS39')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='932M_SS27')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='1135M_SS20')

ax.legend(loc='lower left', shadow=True,prop={'size': 9})
ax.set_xlabel('Time [$years$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

############# Last five ######################

import numpy as np
from matplotlib import pyplot as plt

a_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[0])
t_1 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[1])

a_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1662M_SS10.txt',skip_header=3))[0])
t_2 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1662M_SS10.txt',skip_header=3))[1])

a_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1923M_SS6.txt',skip_header=3))[0])
t_3 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1923M_SS6.txt',skip_header=3))[1])

a_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_4477M_SS1.txt',skip_header=3))[0])
t_4 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_4477M_SS1.txt',skip_header=3))[1])

a_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt',skip_header=3))[0])
t_5 = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt',skip_header=3))[1])

fig,ax=plt.subplots()
ax.plot(t_1,a_1,color='k',linewidth=2.,label='1331M_SS14')
ax.plot(t_2,a_2,color='tab:blue',linewidth=2.,label='1662M_SS10')
ax.plot(t_3,a_3,color='tab:red',linewidth=2.,label='1923M_SS6')
ax.plot(t_4,a_4,color='tab:cyan',linewidth=2.,label='4477M_SS1')
ax.plot(t_5,a_5,color='tab:orange',linewidth=2.,label='6127M_SS0')

ax.legend(loc='lower left', shadow=True,prop={'size': 9})
ax.set_xlabel('Time [$years$]')
ax.set_ylabel('Accretion rate [M$_{\odot}/yr$]')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
