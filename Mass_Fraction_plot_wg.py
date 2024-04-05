# Abundances vs time/etc for the entire evolution from .wg file
# 1. Surface abundance versus time
import numpy as np
from matplotlib import pyplot as plt

H1s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[5])
He4s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[6])
C12s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[8])
N14s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[10])
O16s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[11])
Ne20s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[14])

t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[1])
M = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[2])

fig,ax=plt.subplots()
ax.plot(t,H1s,linewidth=2., label="$H^{1}_{s}$")
ax.plot(t,He4s,linewidth=2., label="$He^{4}_{s}$")
ax.plot(t,C12s,linewidth=2., label="$C^{12}_{s}$")
ax.plot(t,N14s,linewidth=2., label="$N^{14}_{s}$")
ax.plot(t,O16s,linewidth=2., label="$O^{16}_{s}$")
ax.plot(t,Ne20s,linewidth=2., label="$Ne^{20}_{s}$")

#ax.set_xlabel('Mr [M$_{\odot}$]')
ax.set_xlabel('Time [$seconds$]')
ax.set_ylabel('Surface Abundance')
#plt.xlim([0, 104050])

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

# 2. Surface abundance versus Mass
import numpy as np
from matplotlib import pyplot as plt

H1s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[5])
He4s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[6])
C12s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[8])
N14s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[10])
O16s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[11])
Ne20s = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[14])

t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[1])
M = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[2])

fig,ax=plt.subplots()
ax.plot(M,H1s,linewidth=2., label="$H^{1}_{s}$")
ax.plot(M,He4s,linewidth=2., label="$He^{4}_{s}$")
ax.plot(M,C12s,linewidth=2., label="$C^{12}_{s}$")
ax.plot(M,N14s,linewidth=2., label="$N^{14}_{s}$")
ax.plot(M,O16s,linewidth=2., label="$O^{16}_{s}$")
ax.plot(M,Ne20s,linewidth=2., label="$Ne^{20}_{s}$")

ax.set_xlabel('M [M$_{\odot}$]')
#ax.set_xlabel('Time [$seconds$]')
ax.set_ylabel('Surface Abundance')
#plt.xlim([0, 104050])

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

####################################################################
# 3. Central abundance versus time
import numpy as np
from matplotlib import pyplot as plt

H1c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[21])
He4c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[22])
C12c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[24])
N14c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[26])
O16c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[27])
Ne20c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[30])

t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[1])
M = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[2])

fig,ax=plt.subplots()
ax.plot(t,H1c,linewidth=2., label="$H^{1}_{c}$")
ax.plot(t,He4c,linewidth=2., label="$He^{4}_{c}$")
ax.plot(t,C12c,linewidth=2., label="$C^{12}_{c}$")
ax.plot(t,N14c,linewidth=2., label="$N^{14}_{c}$")
ax.plot(t,O16c,linewidth=2., label="$O^{16}_{c}$")
ax.plot(t,Ne20c,linewidth=2., label="$Ne^{20}_{c}$")

#ax.set_xlabel('Mr [M$_{\odot}$]')
ax.set_xlabel('Time [$seconds$]')
ax.set_ylabel('Surface Abundance')
#plt.xlim([0, 104050])

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

# 4. Central abundance versus Mass
import numpy as np
from matplotlib import pyplot as plt

H1c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[21])
He4c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[22])
C12c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[24])
N14c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[26])
O16c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[27])
Ne20c = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[30])

t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[1])
M = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[2])

fig,ax=plt.subplots()
ax.plot(M,H1c,linewidth=2., label="$H^{1}_{c}$")
ax.plot(M,He4c,linewidth=2., label="$He^{4}_{c}$")
ax.plot(M,C12c,linewidth=2., label="$C^{12}_{c}$")
ax.plot(M,N14c,linewidth=2., label="$N^{14}_{c}$")
ax.plot(M,O16c,linewidth=2., label="$O^{16}_{c}$")
ax.plot(M,Ne20c,linewidth=2., label="$Ne^{20}_{c}$")

ax.set_xlabel('M [M$_{\odot}$]')
#ax.set_xlabel('Time [$seconds$]')
ax.set_ylabel('Surface Abundance')
#plt.xlim([0, 104050])

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()
