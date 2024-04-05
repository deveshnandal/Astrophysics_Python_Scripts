
import math
import pandas as pd
import matplotlib.pyplot as plt

M_eq = [9,12,15,20,30,40,60,85,120]
Time_H = [1.77097e7,1.78575e7,1.29865e7,9.50960e6,6.16050e6,4.79495e6,3.66825e6,3.07592e6,2.73616e6]
Time_M_H = [17.7097,17.8575,12.9865,9.50960,6.16050,4.79495,3.66825,3.07592,2.73616]
Time_M_KH = [0.11959601031463714e6,0.12028039799771725e6,0.09771535195097131e6,0.07568678015787887e6,0.050245619730054925e6,0.039762161583578634e6,0.031222827442315186e6,0.027247214499731477e6,0.025142008661050923e6]

Time_KH = [2.60524075e+08,3.50767623e+08,4.86414778e+08,7.42381152e+08,1.22162262e+09,1.73796211e+09,2.89591148e+09,4.53339496e+09,7.11521010e+09]
Time_accr_2 = [900,1200,1500,2000,3000,4000,6000,8500,12000]
Time_accr_3 = [9000,12000,15000,20000,30000,40000,60000,85000,120000]
Time_accr_4 = [90000,120000,150000,200000,300000,400000,600000,850000,1200000]
Time_accr_5 = [900000,1200000,1500000,2000000,3000000,4000000,6000000,8500000,12000000]
Time_accr_6 = [9000000,12000000,15000000,20000000,30000000,40000000,60000000,85000000,120000000]
Time_accr_CH = [42857.14,34285.71,35714.28,31746.03,36585.36,42105.26,44776.11,44270.83,51282.05]
plt.plot(M_eq,Time_H, label='MS lifetime')
plt.plot(M_eq,Time_M_KH, label='KH contraction')
plt.plot(M_eq,Time_accr_2, label='10 -2 Accretion Time')
plt.plot(M_eq,Time_accr_3, label='10 -3 Accretion Time')
plt.plot(M_eq,Time_accr_4, label='10 -4 Accretion Time')
plt.plot(M_eq,Time_accr_5, label='10 -5 Accretion Time')
plt.plot(M_eq,Time_accr_6, label='10 -6 Accretion Time')
plt.plot(M_eq,Time_accr_CH, label='CH Accretion Time')
plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Various timescales versus Mass")
plt.xlabel("log(Mass when accretion stops)")
plt.ylabel("Log(Time in years)")
plt.legend(fontsize = 6)
plt.show()



M = [Msol * M_eq for Msol, M_eq  in zip(Msol, M_eq)]
R = [Rsol * R_eq for Rsol, R_eq  in zip(Rsol, R_eq)]
L = [Lsol * L_eq for Lsol, L_eq  in zip(Lsol, L_eq)]
print(L)


Time_KH = []
print(len(M))
for i in range(len(M)):
    Time_KH = (G*M**2/(R*L))**0.5
print(Time_KH)


for i in range(len(M)):
    KH = G*M
    Time_KH.append(KH)
print(Time_KH)


T_KH = (G*M**2/(R*L))**0.5
print(T_KH)




R_eq = [1.3068,1.5729,1.6663,1.8054,2.2588,2.6766,3.3905,4.1481,5.0582]
L_eq = [3.715023,4.075448,4.334670,4.660077,5.092853,5.370685,5.725151,5.999272,6.247586]
G = [6.6738e-8,6.6738e-8,6.6738e-8,6.6738e-8,6.6738e-8,6.6738e-8,6.6738e-8,6.6738e-8,6.6738e-8]
Msol = [1.9885e33,1.9885e33,1.9885e33,1.9885e33,1.9885e33,1.9885e33,1.9885e33,1.9885e33,1.9885e33]
Rsol = [6.9951e10,6.9951e10,6.9951e10,6.9951e10,6.9951e10,6.9951e10,6.9951e10,6.9951e10,6.9951e10]
Lsol = [3.828e33,3.828e33,3.828e33,3.828e33,3.828e33,3.828e33,3.828e33,3.828e33,3.828e33]
M_eq = [9,12,15,20,30,40,60,85,120]



G = 6.6738e-8
M= 1.78965e+34, 2.3862000000000003e+34, 2.98275e+34, 3.977e+34, 5.9655e+34, 7.954e+34, 1.1931e+35, 1.690225e+35, 2.3862e+35
R = 91411966800.0, 110025927900.0, 116559351300.0, 126289535400.0, 158005318800.0, 187230846600.0, 237168865500.0, 290163743100.0, 353826148200.0
L = 3.0978801154246974e+37, 4.549586526628909e+37, 8.2598455982364e+37, 1.749733589845742e+38, 4.739930012111032e+38, 8.986114108603798e+38, 2.032693643642935e+39, 3.820955054038321e+39, 6.76818044948697e+39

import math
import pandas as pd
import matplotlib.pyplot as plt

KH_formula = 0.5*(6.6738e-8*2.3862e+35**2/(353826148200.0*2.3915759208000003e+34))
print(KH_formula)

import numpy as np
Time_M_years = 31556952000000.0
KH_seconds = [8221345737919108.0, 1.106915705573795e+16,1.5349767785803836e+16,2.3427286381709612e+16,3.855068643672307e+16,5.484478699126073e+16,9.138613971890459e+16,1.4306012729057541e+17,2.2453434361491603e+17]

KH_years = np.divide(KH_seconds, Time_years)
print(KH_years)
Time_KH = [2.60524075e+08,3.50767623e+08,4.86414778e+08,7.42381152e+08,1.22162262e+09,1.73796211e+09,2.89591148e+09,4.53339496e+09,7.11521010e+09]
Time_M_KH = [0.11959601031463714,0.12028039799771725,0.09771535195097131,0.07568678015787887,0.050245619730054925,0.039762161583578634,0.031222827442315186,0.027247214499731477,0.025142008661050923]
import numpy as np
M_eq = [9,12,15,20,30,40,60,85,120]
Accr_rate = 1.00e-3
Accr_yr = np.divide(M_eq,Accr_rate)
print(Accr_yr)

G = 6.6738e-8
M = 1.9885e33
R = 6.9951e10
L = 3.828e33

KH = 0.5*(G*M**2/(R*L))
print(KH)
Time_years = 31556952
KH_years = np.divide(KH, Time_years)
print(KH_years)
Answer is 492752147918119.44

###############################Mass versus accretion rate ###########################
import math
import pandas as pd
import matplotlib.pyplot as plt
M_eq = [22.951,82.127,406.75,2797.4,22146.3,139127]
Accr_rate = [1.00e-6,1.00e-5,1.00e-4,1.00e-3,1.00e-2,1.00e-1]

plt.plot(Accr_rate,M_eq)
plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Mass at Xc=0 versus accretion rate")
plt.xlabel("log(accretion rate)")
plt.ylabel("Log(Mass)")
plt.legend(fontsize = 6)
plt.show()
