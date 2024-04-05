###############################################
#### 4477 Global tkh and tacc verification ####
###############################################
####### Done at  L = 7.380 ####################
import numpy as np
from scipy.integrate import simps

# Load the data
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[4])[::-1]  # reverse the array

l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[5])[::-1]  # reverse the array
M_solar = 849.58853*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[1])[::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[3])[::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[14])[::-1]  # reverse the array

# Constants
G = 6.67*10**-8
Ltot_log = 7.3380
a=7.56576738*10**(-15)
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year
Mdot = (1.981369016655021298e-01)  # in gr per year
t_accr = M_solar/Mdot
# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs

Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate integrands
numerator = s_rad[1:] * T[1:] * dm
denominator = dl
tKH_global = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

t_accr_global = (np.sum(dm) / Mdot_cgs)/seconds_per_year


# Print the result
print("Global Kelvin-Helmholtz timescale:", tKH_global, "years")
print("Global Accretion timescale:", t_accr_global, "years")

############ same as above at 70% #############
############ Additional formula for tkh_local #
#### Calculated from center to 70% ############
###############################################
import numpy as np
from scipy.integrate import simps

# Load the data
l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[5])[78:][::-1]  # reverse the array
M_solar = 849.58853*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[1])[78:][::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[3])[78:][::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[14])[78:][::-1]  # reverse the array
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[4])[78:][::-1]  # reverse the array

# Constants
Mdot = (1.981369016655021298e-01)  # in gr per year
Ltot_log = 7.3380
a=7.56576738*10**(-15)
G = 6.67430 * 10**(-8)  # Gravitational constant in cgs units
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year

# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs
Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate tKH_local
numerator = s_rad[1:] * T[1:] * dm  # We use [1:] to make the arrays align with the size of dm and dl
denominator = dl
tKH_local = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

# Calculate t_accr_local
t_accr_local = (np.sum(dm) / Mdot_cgs)/seconds_per_year

# Calculate tKH_local_alt
numerator_alt = (G*M[1:]/r[1:])*dm  # We use [1:] to make the arrays align with the size of dm
denominator_alt = dl
tKH_local_alt = (np.sum(numerator_alt)/np.sum(denominator_alt))/seconds_per_year


# Print the result
print("Local Kelvin-Helmholtz timescale:", tKH_local, "years")
print("Local Accretion timescale:", t_accr_local, "years")
print("Alternative Local Kelvin-Helmholtz timescale:", tKH_local_alt, "years")



############ same as above at 70% #############
############ Additional formula for tkh_local #
#### Calculated from 70% to surface ###########
###############################################
import numpy as np
from scipy.integrate import simps

# Load the data
l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[5])[:-173][::-1]  # reverse the array
M_solar = 849.58853*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[1])[:-173][::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[3])[:-173][::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[14])[:-173][::-1]  # reverse the array
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[4])[:-173][::-1]  # reverse the array

# Constants
Mdot = (1.981369016655021298e-01)  # in gr per year
Ltot_log = 7.3380
a=7.56576738*10**(-15)
G = 6.67430 * 10**(-8)  # Gravitational constant in cgs units
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year

# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs
Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate tKH_local
numerator = s_rad[1:] * T[1:] * dm  # We use [1:] to make the arrays align with the size of dm and dl
denominator = dl
tKH_local = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

# Calculate t_accr_local
t_accr_local = (np.sum(dm) / Mdot_cgs)/seconds_per_year

# Calculate tKH_local_alt
numerator_alt = (G*M[1:]/r[1:])*dm  # We use [1:] to make the arrays align with the size of dm
denominator_alt = dl
tKH_local_alt = (np.sum(numerator_alt)/np.sum(denominator_alt))/seconds_per_year


# Print the result
print("Local Kelvin-Helmholtz timescale:", tKH_local, "years")
print("Local Accretion timescale:", t_accr_local, "years")
print("Alternative Local Kelvin-Helmholtz timescale:", tKH_local_alt, "years")


###############################################
#### 1662 Global tkh and tacc verification ####
###############################################
####### Done at  L = 7.380 ####################

import numpy as np
from scipy.integrate import simps

# Load the data
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[4])[::-1]  # reverse the array

l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[5])[::-1]  # reverse the array
M_solar = 733.33132*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[1])[::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[3])[::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[14])[::-1]  # reverse the array

# Constants
G = 6.67*10**-8
Ltot_log = 7.3380
a=7.56576738*10**(-15)
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year
Mdot = (8.632854024608935251e-03)  # in gr per year
t_accr = M_solar/Mdot
# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs

Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate integrands
numerator = s_rad[1:] * T[1:] * dm
denominator = dl
tKH_global = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

t_accr_global = (np.sum(dm) / Mdot_cgs)/seconds_per_year


# Print the result
print("Global Kelvin-Helmholtz timescale:", tKH_global, "years")
print("Global Accretion timescale:", t_accr_global, "years")


######## 1662 same as above at 70% ############
############ Additional formula for tkh_local #
#### Calculated from 70% to surface ###########
###############################################


import numpy as np
from scipy.integrate import simps

# Load the data
l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[5])[:-178][::-1]  # reverse the array
M_solar = 733.33132*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[1])[:-178][::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[3])[:-178][::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[14])[:-178][::-1]  # reverse the array
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059591.gz', skip_header=920))[4])[:-178][::-1]  # reverse the array

# Constants
Mdot = (8.632854024608935251e-03)  # in gr per year
Ltot_log = 7.3380
a=7.56576738*10**(-15)
G = 6.67430 * 10**(-8)  # Gravitational constant in cgs units
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year

# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs
Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate tKH_local
numerator = s_rad[1:] * T[1:] * dm  # We use [1:] to make the arrays align with the size of dm and dl
denominator = dl
tKH_local = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

# Calculate t_accr_local
t_accr_local = (np.sum(dm) / Mdot_cgs)/seconds_per_year

# Calculate tKH_local_alt
numerator_alt = (G*M[1:]/r[1:])*dm  # We use [1:] to make the arrays align with the size of dm
denominator_alt = dl
tKH_local_alt = (np.sum(numerator_alt)/np.sum(denominator_alt))/seconds_per_year


# Print the result
print("Local Kelvin-Helmholtz timescale:", tKH_local, "years")
print("Local Accretion timescale:", t_accr_local, "years")
print("Alternative Local Kelvin-Helmholtz timescale:", tKH_local_alt, "years")

###############################################################################################
#### The test will now be repeated at different time in the evolution related to L ############
###############################################################################################
######### L = 7.40456
import numpy as np
from scipy.integrate import simps

# Load the data
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070971', skip_header=261))[4])[::-1]  # reverse the array

l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070971', skip_header=261))[5])[::-1]  # reverse the array
M_solar = 862.18574*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070971', skip_header=261))[1])[::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070971', skip_header=261))[3])[::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070971', skip_header=261))[14])[::-1]  # reverse the array

# Constants
G = 6.67*10**-8
Ltot_log = 7.40456
a=7.56576738*10**(-15)
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year
Mdot = (1.981369016655021298e-01)  # in gr per year
t_accr = M_solar/Mdot
# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs

Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate integrands
numerator = s_rad[1:] * T[1:] * dm
denominator = dl
tKH_global = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

t_accr_global = (np.sum(dm) / Mdot_cgs)/seconds_per_year


# Print the result
print("Global Kelvin-Helmholtz timescale:", tKH_global, "years")
print("Global Accretion timescale:", t_accr_global, "years")
############ same as above at 70% #############
############ Additional formula for tkh_local #
#### Calculated from 70% to surface ###########
###############################################
import numpy as np
from scipy.integrate import simps

# Load the data
l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[5])[:-180][::-1]  # reverse the array
M_solar = 862.18574*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[1])[:-180][::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[3])[:-180][::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[14])[:-180][::-1]  # reverse the array
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[4])[:-180][::-1]  # reverse the array

# Constants
Mdot = (1.981369016655021298e-01)  # in gr per year
Ltot_log = 7.40456
a=7.56576738*10**(-15)
G = 6.67430 * 10**(-8)  # Gravitational constant in cgs units
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year

# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs
Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate tKH_local
numerator = s_rad[1:] * T[1:] * dm  # We use [1:] to make the arrays align with the size of dm and dl
denominator = dl
tKH_local = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

# Calculate t_accr_local
t_accr_local = (np.sum(dm) / Mdot_cgs)/seconds_per_year

# Calculate tKH_local_alt
numerator_alt = (G*M[1:]/r[1:])*dm  # We use [1:] to make the arrays align with the size of dm
denominator_alt = dl
tKH_local_alt = (np.sum(numerator_alt)/np.sum(denominator_alt))/seconds_per_year


# Print the result
print("Local Kelvin-Helmholtz timescale:", tKH_local, "years")
print("Local Accretion timescale:", t_accr_local, "years")
print("Alternative Local Kelvin-Helmholtz timescale:", tKH_local_alt, "years")

###############################################
#### 1662 Global tkh and tacc verification ####
###############################################
####### Done at  L = 7.40456 ####################

import numpy as np
from scipy.integrate import simps

# Load the data
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[4])[::-1]  # reverse the array

l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[5])[::-1]  # reverse the array
M_solar = 747.295963*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[1])[::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[3])[::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[14])[::-1]  # reverse the array

# Constants
G = 6.67*10**-8
Ltot_log = 7.40456
a=7.56576738*10**(-15)
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year
Mdot = (8.100355952868022388e-03)  # in gr per year
t_accr = M_solar/Mdot
# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs

Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate integrands
numerator = s_rad[1:] * T[1:] * dm
denominator = dl
tKH_global = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

t_accr_global = (np.sum(dm) / Mdot_cgs)/seconds_per_year


# Print the result
print("Global Kelvin-Helmholtz timescale:", tKH_global, "years")
print("Global Accretion timescale:", t_accr_global, "years")
############ same as above at 70% #############
############ Additional formula for tkh_local #
#### Calculated from 70% to surface ###########
###############################################
import numpy as np
from scipy.integrate import simps

# Load the data
l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[5])[:-179][::-1]  # reverse the array
M_solar = 747.295963*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[1])[:-179][::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[3])[:-179][::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[14])[:-179][::-1]  # reverse the array
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0059661.gz', skip_header=314))[4])[:-179][::-1]  # reverse the array

# Constants
Mdot = (8.100355952868022388e-03)  # in gr per year
Ltot_log = 7.40456
a=7.56576738*10**(-15)
G = 6.67430 * 10**(-8)  # Gravitational constant in cgs units
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year

# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs
Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate tKH_local
numerator = s_rad[1:] * T[1:] * dm  # We use [1:] to make the arrays align with the size of dm and dl
denominator = dl
tKH_local = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

# Calculate t_accr_local
t_accr_local = (np.sum(dm) / Mdot_cgs)/seconds_per_year

# Calculate tKH_local_alt
numerator_alt = (G*M[1:]/r[1:])*dm  # We use [1:] to make the arrays align with the size of dm
denominator_alt = dl
tKH_local_alt = (np.sum(numerator_alt)/np.sum(denominator_alt))/seconds_per_year


# Print the result
print("Local Kelvin-Helmholtz timescale:", tKH_local, "years")
print("Local Accretion timescale:", t_accr_local, "years")
print("Alternative Local Kelvin-Helmholtz timescale:", tKH_local_alt, "years")


###############################################
#### 1662 Global tkh and tacc verification ####
###############################################
####### Done at  L = 6.3406 ####################

import numpy as np
from scipy.integrate import simps

# Load the data
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0040641.gz', skip_header=274))[4])[::-1]  # reverse the array

l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0040641.gz', skip_header=274))[5])[::-1]  # reverse the array
M_solar = 99.810963*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0040641.gz', skip_header=274))[1])[::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0040641.gz', skip_header=274))[3])[::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0040641.gz', skip_header=274))[14])[::-1]  # reverse the array

# Constants
G = 6.67*10**-8
Ltot_log = 6.3406
a=7.56576738*10**(-15)
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year
Mdot = (2.706478139741398670e-02)  # in gr per year
t_accr = M_solar/Mdot
# Convert mass from solar masses to cgs
M = M_solar * solar_mass_cgs

Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

# Convert total luminosity from log base 10 scale to linear scale
Ltot = 10**Ltot_log * solar_luminosity_cgs

# Convert l from L/Ltot units to cgs units
l = l_Ltot * Ltot

# Calculate s_rad
s_rad = (4*a*(T**3))/(3*rho)

# Calculate dm and dl
dm = np.diff(M)
dl = np.diff(l)

# Calculate integrands
numerator = s_rad[1:] * T[1:] * dm
denominator = dl
tKH_global = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

t_accr_global = (np.sum(dm) / Mdot_cgs)/seconds_per_year


# Print the result
print("Global Kelvin-Helmholtz timescale:", tKH_global, "years")
print("Global Accretion timescale:", t_accr_global, "years")



###################################################################################################
################ Attempting to do this for all v files in 1662 model ##############################

import numpy as np
import pandas as pd
import os
import glob

# Constants
a=7.56576738*10**(-15)
G = 6.67430 * 10**(-8)  # Gravitational constant in cgs units
solar_mass_cgs = 1.989 * 10**33  # Mass of the Sun in grams
solar_luminosity_cgs = 3.828 * 10**33  # Luminosity of the Sun in erg/s
seconds_per_year = 60 * 60 * 24 * 365.25  # Number of seconds in a year
Mdot = (8.100355952868022388e-03)  # in gr per year
Ltot_log = 7.40456
Mdot_cgs = Mdot * solar_mass_cgs / seconds_per_year

def parse_vfile(v_filename):
    with open(v_filename, 'r') as f:
        vFile = f.readlines()

    first_character = [x[:10].strip()[0] for x in vFile][::-1]
    istart = len(first_character) - next((x[0] for x in enumerate(first_character) if x[1] == '#'), 0) - 1
    iskip = istart

    vf = np.genfromtxt(v_filename, skip_header=iskip)

    v_columns = [x for x in vFile[istart][:-1].split(' ') if x != '']
    v_columns[0] = v_columns[0][1:]

    df_vfile = pd.DataFrame(vf, columns=v_columns)
    return df_vfile

# Create an array to store the timescales for each file
tKH_locals = []
t_accr_locals = []
tKH_local_alts = []

# Sort the files by their number
vfiles = sorted(glob.glob('/path/to/vfiles/P002z0S0.v*.gz'), key=lambda x: int(x.split('.')[-2][1:]))

# Iterate over each file
for vfilename in vfiles:
    df_vfile = parse_vfile(vfilename)

    l_Ltot = df_vfile['L/Ltot'][::-1].values  # reverse the array
    M_solar = df_vfile['Mass'][::-1].values  # reverse the array
    T = 10**df_vfile['logT'][::-1].values  # reverse the array
    rho = 10**df_vfile['logRho'][::-1].values  # reverse the array
    r = 10**df_vfile['logR'][::-1].values  # reverse the array

    M = M_solar * solar_mass_cgs
    Ltot = 10**Ltot_log * solar_luminosity_cgs
    l = l_Ltot * Ltot
    s_rad = (4*a*(T**3))/(3*rho)
    dm = np.diff(M)
    dl = np.diff(l)

    # Calculate tKH_local
    numerator = s_rad[1:] * T[1:] * dm
    denominator = dl
    tKH_local = (np.sum(numerator)/np.sum(denominator))/seconds_per_year

    # Calculate t_accr_local
    t_accr_local = (np.sum(dm) / Mdot_cgs)/seconds_per_year

    # Calculate tKH_local_alt
    numerator_alt = (G*M[1:]/r[1:])*dm
    denominator_alt = dl
    tKH_local_alt = (np.sum(numerator_alt)/np.sum(denominator_alt))/seconds_per_year

    # Store the timescales in the arrays
    tKH_locals.append(tKH_local)
    t_accr_locals.append(t_accr_local)
    tKH_local_alts.append(tKH_local_alt)

# Convert the lists to arrays
tKH_locals = np.array(tKH_locals)
t_accr_locals = np.array(t_accr_locals)
tKH_local_alts = np.array(tKH_local_alts)

# Now you have three arrays with the timescales for each file
print("Local Kelvin-Helmholtz timescale array:", tKH_locals)
print("Local Accretion timescale array:", t_accr_locals)
print("Alternative Local Kelvin-Helmholtz timescale array:", tKH_local_alts)


l_Ltot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[5])[:-180][::-1]  # reverse the array
M_solar = 862.18574*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[1])[:-180][::-1]  # reverse the array
T = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[3])[:-180][::-1]  # reverse the array
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[14])[:-180][::-1]  # reverse the array
r = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0070661', skip_header=265))[4])[:-180][::-1]  # reverse the array
