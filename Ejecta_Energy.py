#Calculation of binding energy of envelope which extends from 600 Msun to 3050Msun
####
import scipy
from scipy import integrate
from scipy.integrate import quad
from math import *
import numpy as np

G=6.67428*10**(-8)                       #Gravitational constant
R1 = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294, skip_footer=93))[4]))
M1 = (1.9884*10**33)*((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294, skip_footer=93))[49]))
y1=np.empty(195)
for i in range(1,len(M1)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    y1[i] = ((G*M1[i]))/R1[i]**2
y1_int = integrate.cumtrapz(y1,R1,initial=0)
y1_tot1= np.sum(y1_int)
y1_tot1
# Envelope Energy = 8.2e+18
#6.76e51
#### Check for Mass for above test
import scipy
from scipy import integrate
from scipy.integrate import quad
from math import *
import numpy as np

G=6.67428*10**(-8)                       #Gravitational constant
rho = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294, skip_footer=93))[14]))
R = 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294, skip_footer=93))[4]))
y=np.empty(195)
for i in range(1,len(R)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    y[i] = (4*3.1415*R[i]**2*rho[i])
y_int = integrate.cumtrapz(y,R,initial=0)
y_tot2 = np.sum(y_int)

#### Gravitational potential energy of the core from 0 to 660 Msun
####
import scipy
from scipy import integrate
from scipy.integrate import quad
from math import *
import numpy as np

G=6.67428*10**(-8)                       #Gravitational constant
R3= 10**((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=488))[4]))
M3 = (1.9884*10**33)*((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=488))[49]))
y3=np.empty(94)
for i in range(1,len(M3)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    y3[i] = ((G*M3[i]))/(R3[i]**2)
y_int3 = integrate.cumtrapz(y3,R3,initial=0)
y_tot3 = np.sum(y_int3)
y_tot3
### GPE of core with mass 660 is 2.73e+20
# 3.83e53
#### Core with Mass 660 is now contracted to the schwarzschild radius, how much GPE is released
import scipy
from scipy import integrate
from scipy.integrate import quad
from math import *
import numpy as np

G=6.67428*10**(-8)
c=2.99792458*10**10
M_s = 1.31234e+36

r_s = (2.0*G*(M_s))/c**2
# r_s = 194912359 cm
U_r = (G*M_s)/r_s
## Potential energy at the r_s = 4.493e+20
#7.54e57


##################
import scipy
from scipy import integrate
from scipy.integrate import quad
from math import *
import numpy as np

G=6.67428*10**(-8)                       #Gravitational constant
T= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[3]))
rho= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[14]))
