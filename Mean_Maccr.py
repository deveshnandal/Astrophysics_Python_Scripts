#491M_SS71#

import numpy as np
from matplotlib import pyplot as plt

a_rate = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt',skip_header=3))[0])
t_lim = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt',skip_header=3))[1])
t_lim_sum = np.sum((10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt',skip_header=3))[1]))

Pond_mean = (a_rate*(t_lim/t_lim.sum())).sum()
print(Pond_mean)


T = np.sum(a_rate*t_lim/(t_lim_sum))
print(T)

######################
 #6127M_SS0#
 import numpy as np
 from matplotlib import pyplot as plt

 a_rate = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt',skip_header=3))[0])
 t_lim = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt',skip_header=3))[1])
 t_lim_sum = np.sum((10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt',skip_header=3))[1]))

 Pond_mean = (a_rate*(t_lim/t_lim.sum())).sum()
 print(Pond_mean)


 T = np.sum(a_rate*t_lim/(t_lim_sum))
 print(T)

 # 5.55e-3 Msun/yr
 ########################
 # 856M_SS36 #

  import numpy as np
  from matplotlib import pyplot as plt

  a_rate = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_856M_SS36.txt',skip_header=3))[0])
  t_lim = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_856M_SS36.txt',skip_header=3))[1])
  t_lim_sum = np.sum((10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_856M_SS36.txt',skip_header=3))[1]))

  Pond_mean = (a_rate*(t_lim/t_lim.sum())).sum()
  print(Pond_mean)


  T = np.sum(a_rate*t_lim/(t_lim_sum))
  print(T)
# 1.496251922670283e-05

  ############################
  # 1177M_SS19 #

    import numpy as np
    from matplotlib import pyplot as plt

    a_rate = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1177M_SS19.txt',skip_header=3))[0])
    t_lim = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1177M_SS19.txt',skip_header=3))[1])
    t_lim_sum = np.sum((10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1177M_SS19.txt',skip_header=3))[1]))

    Pond_mean = (a_rate*(t_lim/t_lim.sum())).sum()
    print(Pond_mean)


    T = np.sum(a_rate*t_lim/(t_lim_sum))
    print(T)

# 0.013796174773775113
################################
# 1331M_SS14 #

    import numpy as np
    from matplotlib import pyplot as plt

    a_rate = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[0])
    t_lim = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[1])
    t_lim_sum = np.sum((10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[1]))

    Pond_mean = (a_rate*(t_lim/t_lim.sum())).sum()
    print(Pond_mean)


    T = np.sum(a_rate*t_lim/(t_lim_sum))
    print(T)

    # 0.00010613801698650956


#################################

    import numpy as np
    from matplotlib import pyplot as plt

    a_rate = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[0])
    t_lim = (10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[1])
    t_lim_sum = np.sum((10**3)*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt',skip_header=3))[1]))

    Pond_mean = (a_rate*(t_lim/t_lim.sum())).sum()
    print(Pond_mean)


    T = np.sum(a_rate*t_lim/(t_lim_sum))
    print(T)

    # 0.00010613801698650956

##############################
##############################
###### Yoshida end Si ########
import numpy as np

# Define input arrays
data = np.genfromtxt('/Users/hermit/Observatory/Starcalc/SMS/Yoshida_case4/P002z0S0.dat')
time = np.abs(data[:, 1])  # time in years
mass = np.abs(data[:, 2])  # mass in solar masses

# Calculate accretion rate
accretion_rate = np.gradient(mass, time)
small_number = 1e-12

# Replace NaN values with small number
accretion_rate = np.nan_to_num(accretion_rate, nan=small_number)
accretion_rate = np.where(accretion_rate == 0, np.finfo(float).eps, accretion_rate)  # replace zeros with a small number

# Calculate weighted mean accretion rate
weights = np.diff(time)
mean_accretion_rate = np.average(accretion_rate[:-1], weights=weights)

# Print the results
print("Time (years):", time)
print("Mass (solar masses):", mass)
print("Accretion rate (solar masses per year):", accretion_rate)
print("Weighted mean accretion rate (solar masses per year):", mean_accretion_rate)
 # The answer is  0.000371226
