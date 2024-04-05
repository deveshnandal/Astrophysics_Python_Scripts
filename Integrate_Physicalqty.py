######### Optical depth calculation from the parameters obtained from physicalquantities.py ####################

import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
Mass = 112680.929202*M_sun
Lum = 3.846e+33*(10**9.613091)
Teff = (10**3.907829)**4
M_dot = (0.1*M_sun)/3.154e+7
#r = np.array(list(np.arange(2.040e12,2.040e20,100000e12)))
r=np.linspace(2.040e15,2.040e20,2000)
velocity = (2*G*Mass/(r))**0.5
rho_array = M_dot/(4*pi*(np.power(r,2))*velocity)
Teff = (Lum/(4*pi*(np.power(r,2))*sigma))**0.25
D = (rho_array*6.023e23)
O_array = np.empty(2000)  # This created an empty list with 2040 spaces
O_array.fill(0.088354)   # This filled the empty spaces wth desired values

int = np.empty(2000)
int[0] = 0
for i in range(1,len(O_array)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + O_array[i]*rho_array[i]*(r[i]-r[i-1])

kapp1 = O_array[0]*rho_array[0]*r[0]
#####################
#opac =
#opaclist = []
#for i in range(2,len(opac)):
#    opaclist=np.append(opaclist,np.trapz(rho_array[0:i],r[0:i]))
opac = np.cumsum(O_array*rho_array*r)
#opac = np.cumsum(O_array*rho_array*r[1]-r[0])

# for i in range(0,len(opac)):
#     print(i,opac[i+1]-opac[i])

v
fig,ax=plt.subplots()
ax.plot(r,int,color='tab:blue',linewidth=4., label="Optical depth")


ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Opacity')

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()
######################
def f(r, O, rho):
    return O*rho*r
opac = [[O,rho, quad(f, 2e12, 2e20, args=(O,rho))[0]] for O in O_array for rho in rho_array]

np.array(opac).T[2]



########################
Int = quad(opac,2e12,2e20)
print (Int)




kr = np.array((len(density)))
for i,r in enumerate(density):
    kr[i] = opacity*r
opac = integrate.cumtrapz(kr,Radius)
print(opac)

############
# using scipy.integrate.simps() method
gfg = integrate.simps(density, opacity)

print(gfg)





########################
y = opacity*density
scipy.integrate.simps(y, x=None, dx=1, axis=-1, even='avg')


########################
# function we want to integrate
def f(x):
    return opacity*density

# call quad to integrate f from -2 to 2
res, err = quad(f, 2.04e19, 2.04e12)

print("The numerical result is {:f} (+-{:g})"
    .format(res, err))





########################
D = (density*6.023e23)
opacity = 0.088354


def function(x):
    return opacity,density


y = function(x)

y
####################
def function(x):
    return opacity*density
x = np.arange(2.04e19,2.040e12,-1e4)
y = function(x)
x
y

########## works I guess ##############
def integrand(density,opacity):
    return density*opacity

opacity = 0.088354
I = quad(integrand, 0, 100, args=(opacity))
I



###################
def f(x):
    return opacity*density
def trap(f,n,a,b):
    h = (b - a) / float(n)
    intgr=0.5*h*(f(a)+f(b))
    for i in range(1,int(n)):
        intgr=intgr+h*f(a+i*h)
    return intgr

a=-10
b=10
n=100

while(abs(trap(f,n,a,b)-trap(f,n*4,a*2,b*2))> 1e-6):
    n*=4
    a*=2
    b*=2
print(trap(f,n,a,b))
#####################
def f(x):
    return opacity*density
def trap (func,n,a,b):
    h = (b-a)/n
    intgr = 0.5*h*(func(a)+func(b))
    for i in range(1,int(n)):
        intgr = intgr + h*func(a+i*h)
    return intgr

a,b = 0,1e6
n= 1e6


#while (abs(trap(f,n,a,b)-trap(f,n*4,a,b*2)) > 1e-6):
#    n*=2
#    b*=2
#    print("increased n,b to {0},{1}".format(n,b))


########## Plotting from physical quantities.py############
fig,ax=plt.subplots()
ax.plot(Radius,density,color='tab:blue',linewidth=4., label="Density")
ax.plot(Radius,Teff,color='tab:red',linewidth=4., label="Temperature")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Physical quantities')

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

############# Final calculation for different masses at 0.1Msun/yr accretion rate #######################
###### 10
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M = 10*M_sun
L = 3.846e+33*(10**2.7573)
Teff = (10**3.7362)**4
M_dot = (0.1*M_sun)/3.154e+7

R_ini= (L/(4*pi*sigma*(Teff)))**0.5 # which equates to 1872163852449.0388 or 1.87e12
R = np.linspace(1.87e12,2.040e20,2000)
v = (2*G*M/(R))**0.5
rho = M_dot/(4*pi*(np.power(R,2))*v)
k = np.empty(2000)  # This created an empty list with 2040 spaces
k.fill(3.46e-4)
l = 1/(k*rho)
for i in range(1,len(k)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + k[i]*rho[i]*(R[i]-R[i-1])
###### 100
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M = 100*M_sun
L = 3.846e+33*(10**6.2271)
Teff = (10**3.7237)**4
M_dot = (0.1*M_sun)/3.154e+7

R_ini= (L/(4*pi*sigma*(Teff)))**0.5 # which equates to 107706981689295.39 or 1.07e14
R = np.linspace(1.07e14,2.040e20,2000)
v = (2*G*M/(R))**0.5
rho = M_dot/(4*pi*(np.power(R,2))*v)
k = np.empty(2000)  # This created an empty list with 2040 spaces
k.fill(1.9e-4)
l = 1/(k*rho)
for i in range(1,len(k)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + k[i]*rho[i]*(R[i]-R[i-1])
###### 1000
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M = 1000*M_sun
L = 3.846e+33*(10**7.4951)
Teff = (10**3.7467)**4
M_dot = (0.1*M_sun)/3.154e+7

R_ini= (L/(4*pi*sigma*(Teff)))**0.5 # which equates to 417103520706122.3 or 4.17e14
R = np.linspace(4.17e14,2.040e20,2000)
v = (2*G*M/(R))**0.5
rho = M_dot/(4*pi*(np.power(R,2))*v)
k = np.empty(2000)  # This created an empty list with 2040 spaces
k.fill(6.9e-4)
l = 1/(k*rho)
for i in range(1,len(k)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + k[i]*rho[i]*(R[i]-R[i-1])
###### 10000
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M = 10000*M_sun
L = 3.846e+33*(10**8.5410)
Teff = (10**3.7815)**4
M_dot = (0.1*M_sun)/3.154e+7

R_ini= (L/(4*pi*sigma*(Teff)))**0.5 # which equates to 1184660357084571.8 or 1.18e15
R = np.linspace(1.18e15,2.040e20,2000)
v = (2*G*M/(R))**0.5
rho = M_dot/(4*pi*(np.power(R,2))*v)
k = np.empty(2000)  # This created an empty list with 2040 spaces
k.fill(8e-3)
l = 1/(k*rho)
for i in range(1,len(k)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + k[i]*rho[i]*(R[i]-R[i-1])
#### 100000
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M = 100000*M_sun
L = 3.846e+33*(10**9.5580)
Teff = (10**3.8890)**4
M_dot = (0.1*M_sun)/3.154e+7

R_ini= (L/(4*pi*sigma*(Teff)))**0.5 # which equates to 2328594437407622.5 2.32e15
R = np.linspace(2.32e15,2.040e20,2000)
v = (2*G*M/(R))**0.5
rho = M_dot/(4*pi*(np.power(R,2))*v)
k = np.empty(2000)  # This created an empty list with 2040 spaces
k.fill(0.275)
l = 1/(k*rho)
int = np.empty(2000)
int[0] = 0
for i in range(1,len(k)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + k[i]*rho[i]*(R[i]-R[i-1])
###
#### 100000 with Maccr= 1
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M = 100000*M_sun
L = 3.846e+33*(10**9.5580)
Teff = (10**3.8890)**4
M_dot = (1*M_sun)/3.154e+7

R_ini= (L/(4*pi*sigma*(Teff)))**0.5 # which equates to 2328594437407622.5 2.32e15
R = np.linspace(2.32e15,2.040e20,2000)
v = (2*G*M/(R))**0.5
rho = M_dot/(4*pi*(np.power(R,2))*v)
k = np.empty(2000)  # This created an empty list with 2040 spaces
k.fill(0.0136)
l = 1/(k*rho)
int = np.empty(2000)
int[0] = 0
for i in range(1,len(k)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + k[i]*rho[i]*(R[i]-R[i-1])
###
#### 100000 with Maccr= 10000
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M = 100000*M_sun
L = 3.846e+33*(10**9.5580)
Teff = (10**3.8890)**4
M_dot = (10000*M_sun)/3.154e+7

R_ini= (L/(4*pi*sigma*(Teff)))**0.5 # which equates to 2328594437407622.5 2.32e15
R = np.linspace(2.32e15,2.040e20,2000)
v = (2*G*M/(R))**0.5
rho = M_dot/(4*pi*(np.power(R,2))*v)
k = np.empty(2000)  # This created an empty list with 2040 spaces
k.fill(0.0136)
l = 1/(k*rho)
int = np.empty(2000)
int[0] = 0
for i in range(1,len(k)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int[i] = int[i-1] + k[i]*rho[i]*(R[i]-R[i-1])
###
################# 1Msun/yr test ##################
#### 10 ###

import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M_10 = 10*M_sun
L_10 = 3.846e+33*(10**4.0806)
Teff_10 = (10**3.6790)**4
M_dot_10 = (1*M_sun)/3.154e+7

R_ini_10= (L_10/(4*pi*sigma*(Teff_10)))**0.5 # which equates to 11178765750673.912 or 1.11e13
R_10 = np.linspace(1.11e13,2.040e18,200000)
v_10 = (2*G*M_10/(R_10))**0.5
rho_10 = M_dot_10/(4*pi*(np.power(R_10,2))*v_10)
k_10 = np.empty(200000)  # This created an empty list with 2040 spaces
k_10.fill(1.547e-3)
l_10 = 1/(k_10*rho_10)
int_10 = np.empty(200000)
int_10[0] = 0
for i in range(1,len(k_10)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_10[i] = int_10[i-1] + k_10[i]*rho_10[i]*(R_10[i]-R_10[i-1])

##### 100 ###

M_100 = 100*M_sun
L_100 = 3.846e+33*(10**6.0641)
Teff_100 = (10**3.7040)**4
M_dot_100 = (1*M_sun)/3.154e+7

R_ini_100= (L_100/(4*pi*sigma*(Teff_100)))**0.5 # which equates to 97756097456129.72 or 9.77e13
R_100 = np.linspace(9.77e13,2.040e18,200000)
v_100 = (2*G*M_100/(R_100))**0.5
rho_100 = M_dot_100/(4*pi*(np.power(R_100,2))*v_100)
k_100 = np.empty(200000)  # This created an empty list with 2040 spaces
k_100.fill(1.15e-3)
l_100 = 1/(k_100*rho_100)
int_100 = np.empty(200000)
int_100[0] = 0
for i in range(1,len(k_100)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_100[i] = int_100[i-1] + k_100[i]*rho_100[i]*(R_100[i]-R_100[i-1])

#### 1000 ###

M_1000 = 1000*M_sun
L_1000 = 3.846e+33*(10**7.4214)
Teff_1000 = (10**3.7516)**4
M_dot_1000 = (1*M_sun)/3.154e+7

R_ini_1000 = (L_1000/(4*pi*sigma*(Teff_1000)))**0.5 # which equates to 374622498209563.7 or 3.74e14
R_1000 = np.linspace(3.74e14,2.040e18,200000)
v_1000 = (2*G*M_1000/(R_1000))**0.5
rho_1000 = M_dot_1000/(4*pi*(np.power(R_1000,2))*v_1000)
k_1000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_1000.fill(0.0340)
l_1000 = 1/(k_1000*rho_1000)
int_1000 = np.empty(200000)
int_1000[0] = 0
for i in range(1,len(k_1000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_1000[i] = int_1000[i-1] + k_1000[i]*rho_1000[i]*(R_1000[i]-R_1000[i-1])

#### 10000 ###

M_10000 = 10000*M_sun
L_10000 = 3.846e+33*(10**8.5193)
Teff_10000 = (10**3.7877)**4
M_dot_10000 = (1*M_sun)/3.154e+7

R_ini_10000 = (L_10000/(4*pi*sigma*(Teff_10000)))**0.5 # which equates to 1122907171987070.0 or 1.12e15
R_10000 = np.linspace(1.122e15,2.040e18,200000)
v_10000 = (2*G*M_10000/(R_10000))**0.5
rho_10000 = M_dot_10000/(4*pi*(np.power(R_10000,2))*v_10000)
k_10000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_10000.fill(0.076)
l_10000 = 1/(k_10000*rho_10000)
int_10000 = np.empty(200000)
int_10000[0] = 0
for i in range(1,len(k_10000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_10000[i] = int_10000[i-1] + k_10000[i]*rho_10000[i]*(R_10000[i]-R_10000[i-1])

#### 100000 ###

M_100000 = 100000*M_sun
L_100000 = 3.846e+33*(10**9.552)
Teff_100000 = (10**3.9164)**4
M_dot_100000 = (1*M_sun)/3.154e+7

R_ini_100000 = (L_100000/(4*pi*sigma*(Teff_100000)))**0.5 # which equates to 2038420863198279.2 or 2.03e15
R_100000 = np.linspace(2.03e15,2.040e18,200000)
v_100000 = (2*G*M_100000/(R_100000))**0.5
rho_100000 = M_dot_100000/(4*pi*(np.power(R_100000,2))*v_100000)
k_100000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_100000.fill(0.307)
l_100000 = 1/(k_100000*rho_100000)
int_100000 = np.empty(200000)
int_100000[0] = 0
for i in range(1,len(k_100000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_100000[i] = int_100000[i-1] + k_100000[i]*rho_100000[i]*(R_100000[i]-R_100000[i-1])


fig,ax=plt.subplots()
ax.plot(R_10,int_10,linewidth=3., label="10M$_{\odot}$")
ax.plot(R_100,int_100,linewidth=3., label="100M$_{\odot}$")
ax.plot(R_1000,int_1000,linewidth=3., label="1000M$_{\odot}$")
ax.plot(R_10000,int_10000,linewidth=3., label="10000M$_{\odot}$")
ax.plot(R_100000,int_100000,linewidth=3., label="100000M$_{\odot}$")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Optical depth')

leg = plt.legend(loc='upper left', shadow=True,prop={'size': 8})

ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()
####### For 1Msun/yr at 100000, T and rho plot vs R
Teff_100000 = (L_100000/(4*pi*(np.power(R_100000,2))*sigma))**0.25



fig,ax=plt.subplots()
ax.plot(R_100000,rho_100000,color='tab:blue',linewidth=3., label="Density")
ax.plot(R_100000,Teff_100000,color='tab:red',linewidth=3., label="Temperature")
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Physical quantities')

leg = plt.legend(loc='center right', shadow=True,prop={'size': 8})

plt.show()
################## 10-3 Msun/yr ############################
#### 10 Msun #####

import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from scipy import integrate
import numpy as np

G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
M_10 = 10*M_sun
L_10 = 3.846e+33*(10**4.3623)
Teff_10 = (10**4.188)**4
M_dot_10 = (0.001*M_sun)/3.154e+7

R_ini_10= (L_10/(4*pi*sigma*(Teff_10)))**0.5 # which equates to 1483350750484.8474 or 1.48e12
R_10 = np.linspace(1.48e12,2.040e18,200000)
v_10 = (2*G*M_10/(R_10))**0.5
rho_10 = M_dot_10/(4*pi*(np.power(R_10,2))*v_10)
k_10 = np.empty(200000)  # This created an empty list with 2040 spaces
k_10.fill(0.790)
l_10 = 1/(k_10*rho_10)
int_10 = np.empty(200000)
int_10[0] = 0
for i in range(1,len(k_10)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_10[i] = int_10[i-1] + k_10[i]*rho_10[i]*(R_10[i]-R_10[i-1])

##### 100 ###

M_100 = 100*M_sun
L_100 = 3.846e+33*(10**6.196)
Teff_100 = (10**4.976)**4
M_dot_100 = (0.001*M_sun)/3.154e+7

R_ini_100= (L_100/(4*pi*sigma*(Teff_100)))**0.5 # which equates to 325157559812.6852or 3.25e11
R_100 = np.linspace(3.25e11,2.040e18,200000)
v_100 = (2*G*M_100/(R_100))**0.5
rho_100 = M_dot_100/(4*pi*(np.power(R_100,2))*v_100)
k_100 = np.empty(200000)  # This created an empty list with 2040 spaces
k_100.fill(0.358)
l_100 = 1/(k_100*rho_100)
int_100 = np.empty(200000)
int_100[0] = 0
for i in range(1,len(k_100)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_100[i] = int_100[i-1] + k_100[i]*rho_100[i]*(R_100[i]-R_100[i-1])

#### 1000 ###

M_1000 = 1000*M_sun
L_1000 = 3.846e+33*(10**7.4832)
Teff_1000 = (10**4.986)**4
M_dot_1000 = (0.001*M_sun)/3.154e+7

R_ini_1000 = (L_1000/(4*pi*sigma*(Teff_1000)))**0.5 # which equates to 1366765021337.6099 or 3.74e14
R_1000 = np.linspace(1.36e12,2.040e18,200000)
v_1000 = (2*G*M_1000/(R_1000))**0.5
rho_1000 = M_dot_1000/(4*pi*(np.power(R_1000,2))*v_1000)
k_1000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_1000.fill(0.0348)
l_1000 = 1/(k_1000*rho_1000)
int_1000 = np.empty(200000)
int_1000[0] = 0
for i in range(1,len(k_1000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_1000[i] = int_1000[i-1] + k_1000[i]*rho_1000[i]*(R_1000[i]-R_1000[i-1])

#### 2000 ###

M_2000 = 10000*M_sun
L_2000 = 3.846e+33*(10**7.8306)
Teff_2000 = (10**4.843)**4
M_dot_2000 = (0.001*M_sun)/3.154e+7

R_ini_2000 = (L_2000/(4*pi*sigma*(Teff_2000)))**0.5 # which equates to 3939071424744.887 or 1.12e15
R_2000 = np.linspace(3.93e12,2.040e18,200000)
v_2000 = (2*G*M_2000/(R_2000))**0.5
rho_2000 = M_dot_2000/(4*pi*(np.power(R_2000,2))*v_2000)
k_2000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_2000.fill(0.350)
l_2000 = 1/(k_2000*rho_2000)
int_2000 = np.empty(200000)
int_2000[0] = 0
for i in range(1,len(k_2000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_2000[i] = int_2000[i-1] + k_2000[i]*rho_2000[i]*(R_2000[i]-R_2000[i-1])

#### 2797 ###

M_2797 = 2797*M_sun
L_2797 = 3.846e+33*(10**7.987)
Teff_2797 = (10**3.765)**4
M_dot_2797 = (0.001*M_sun)/3.154e+7

R_ini_2797 = (L_2797/(4*pi*sigma*(Teff_2797)))**0.5 # which equates to 675451010396974.4 or 2.03e15
R_2797 = np.linspace(6.75e14,2.040e18,200000)
v_2797 = (2*G*M_2797/(R_2797))**0.5
rho_2797 = M_dot_2797/(4*pi*(np.power(R_2797,2))*v_2797)
k_2797 = np.empty(200000)  # This created an empty list with 2040 spaces
k_2797.fill(0.053)
l_2797 = 1/(k_2797*rho_2797)
int_2797 = np.empty(200000)
int_2797[0] = 0
for i in range(1,len(k_2797)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_2797[i] = int_2797[i-1] + k_2797[i]*rho_2797[i]*(R_2797[i]-R_2797[i-1])


fig,ax=plt.subplots()
ax.plot(R_10,int_10,linewidth=3., label="10M$_{\odot}$")
ax.plot(R_100,int_100,linewidth=3., label="100M$_{\odot}$")
ax.plot(R_1000,int_1000,linewidth=3., label="1000M$_{\odot}$")
ax.plot(R_2000,int_2000,linewidth=3., label="2000M$_{\odot}$")
ax.plot(R_2797,int_2797,linewidth=3., label="2797M$_{\odot}$")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Optical depth')

leg = plt.legend(loc='upper left', shadow=True,prop={'size': 8})

ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

################## Better resolution of R

M_1000 = 1000*M_sun
L_1000 = 3.846e+33*(10**7.4832)
Teff_1000 = (10**4.986)**4
M_dot_1000 = (0.001*M_sun)/3.154e+7

R_ini_1000 = (L_1000/(4*pi*sigma*(Teff_1000)))**0.5 # which equates to 1366765021337.6099
R_1000 = np.linspace(1.36e13,2.040e18,200000)
v_1000 = (2*G*M_1000/(R_1000))**0.5
rho_1000 = M_dot_1000/(4*pi*(np.power(R_1000,2))*v_1000)
k_1000 = np.empty(200000)  # This created an empty list with 2040 spaces
k_1000.fill(0.0348)
l_1000 = 1/(k_1000*rho_1000)
int_1000 = np.empty(200000)
int_1000[0] = 0
for i in range(1,len(k_1000)):
#    int = np.append(int, O_array[i]*rho_array[i]*(r[i]-r[i-1]))
    int_1000[i] = int_1000[i-1] + k_1000[i]*rho_1000[i]*(R_1000[i]-R_1000[i-1])
fig,ax=plt.subplots()
ax.plot(R_1000,int_1000,linewidth=3., label="1000M$_{\odot}$")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Optical depth')

leg = plt.legend(loc='upper left', shadow=True,prop={'size': 8})

ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()
