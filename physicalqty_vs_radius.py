################# Estimation of Opacity from density, temperature and abundances ###########################

################# Step 1: Calculation of velocity #######################

################# The radius of the star at this time is 2.04e12 cm ##################
################# Mass of the star at this point in the evolution is chosen to be 1.59823360955e+34 ###################

import math
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
Mass = 1.59823360955e+34
Lum = 3.846e+33*(10**2.797175)
#Teff = (10**3.727498)**4
M_dot = (0.1*M_sun)/3.154e+7
#Radius = 3.086e+19  # 10 Parsec #
#velocity = (2*G*Mass/(Radius))**0.5
#

#Radius= (Lum/(4*pi*sigma*(Teff)))**0.5


Radius = [2.040e12,2.040e13,2.040e14,2.040e15,2.040e16,2.040e17,2.040e18,2.040e19]

#const = 2.133411723109475e+27
#velocity = (2*G*Mass/(Radius))**0.5 in cm/sec
velocity = (2.*G*Mass/(2.040e12))**0.5
velocity = [32336622.803774197,10226387.73149044,3233867.746751221,1022638.773149044,323386.7746751221,102263.8773149044,32338.67746751221,10226.38773149044]

density = M_dot/(4*pi*(np.power(Radius,2))*velocity)
#Teff = (Lum/(4*pi*(np.power(Radius,2))*sigma))**0.25
Teff = [5.33980742e+03, 1.68859537e+03, 5.33980742e+02, 1.68859537e+02, 5.33980742e+01, 1.68859537e+01, 5.33980742e+00, 1.68859537e+00]



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


##################
for x in Radius:
    velocity.append(const/x)

density = M_dot/(4*pi*(np.power(Radius,2))*velocity)


################# Test of values for P120Z0S0 1e-3 at Mass 120 Msun ############
import math
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
Mass = 2.3862e+35
Lum = 3.846e+33*(10**6.307285)
Teff = (10**4.968607  )**4
M_dot = (0.001*M_sun)/3.154e+7
#Radius = 3.086e+19  # 10 Parsec #
#velocity = (2*G*Mass/(Radius))**0.5
#

#Radius= (Lum/(4*pi*sigma*(Teff)))**0.5


Radius = [382403937715.74554]

#const = 2.133411723109475e+27
#velocity = (2*G*Mass/(Radius))**0.5 in cm/sec
#velocity = (2.*G*Mass/(382403937715.74554))**0.5
velocity = [288608722.0720082]

density = M_dot/(4*pi*(np.power(Radius,2))*velocity)
Teff = (Lum/(4*pi*(np.power(Radius,2))*sigma))**0.25
Teff = [5.33980742e+03, 1.68859537e+03, 5.33980742e+02, 1.68859537e+02, 5.33980742e+01, 1.68859537e+01, 5.33980742e+00, 1.68859537e+00]



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

############# 0.1 Msun: A list with many more elements ####################
import math
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
Mass = 112680.929202*M_sun
Lum = 3.846e+33*(10**9.613091)
Teff = (10**3.907829)
M_dot = (0.001*M_sun)/3.154e+7

Radius = np.array(list(np.arange(2.040e12,2.040e20,100000e12)))  ## Remember this::::: just by typing np.array, you converted a list
# into an array that can work when putting its value in a formula
velocity = (2*G*Mass/(Radius))**0.5
density = M_dot/(4*pi*(np.power(Radius,2))*velocity)
Teff = (Lum/(4*pi*(np.power(Radius,2))*sigma))**0.25

D = (density*6.023e23)


fig,ax=plt.subplots()
ax.plot(Radius,density,color='tab:blue',linewidth=4., label="Density")
ax.plot(Radius,Teff,color='tab:red',linewidth=4., label="Temperature")
ax.plot(Radius,D,color='tab:green',linewidth=4., label="Density")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Physical quantities')

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
