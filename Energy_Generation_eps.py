import math
import matplotlib.pyplot as plt
import matplotlib.text as text

fig,ax=plt.subplots()

gtb.loadS('Observatory/StarCalc/Isochrones_preMS/1e-5_then_1e-3_Maccr/P120Z1e-6S0_Var_Maccr/P002z0S0.v0019761',1)

M=gtb.Get_Var('Mr',1)
gtb.Set_Var(M,'M',1,label="$Mass\ [g]$",category="energy")

E=gtb.Get_Var('eps_reac',1)+gtb.Get_Var('epsgrav',1)
gtb.Set_Var(E,'E',1,label="$eps_reac+epsgrav\ [ergs/g/s]$",category="energy")

E_reac=gtb.Get_Var('eps_reac',1)
gtb.Set_Var(E_reac,'E_reac',1,label="$eps_reac\ [ergs/g/s]$",category="energy")

E_grav=gtb.Get_Var('epsgrav',1)
gtb.Set_Var(E_grav,'E_grav',1,label="$eps_grav\ [ergs/g/s]$",category="energy")


plt.plot(M,E,color='black',linestyle='solid',linewidth=2,label='Total eps')
plt.plot(M,E_reac,color='red',linestyle='solid',linewidth=2,label='eps reac')
plt.plot(M,E_grav,color='blue',linestyle='solid',linewidth=2,label='eps grav')
plt.legend(loc='upper center', shadow=True,prop={'size': 6})

plt.xlabel('$M_r$')
plt.ylabel('Energy(ergs/g/s)')
plt.show()


plt.plot(M,E_reac,color='red',linestyle='solid',linewidth=2)
plt.plot(M,E_grav,color='blue',linestyle='solid',linewidth=2)

#fig,ax=plt.subplots(nrows=2,ncols=2)
#ax[0,0]

import math
import matplotlib.pyplot as plt
import matplotlib.text as text

gtb.loadS('Observatory/StarCalc/Isochrones_preMS/1e-5_then_1e-3_Maccr/P120Z2e-3S0_Var_Maccr/P002z0S0.v0019961',2)

M=gtb.Get_Var('Mr',2)
gtb.Set_Var(M,'M',2,label="$Mass\ [g]$",category="energy")

E=gtb.Get_Var('eps_reac',2)+gtb.Get_Var('epsgrav',2)
gtb.Set_Var(E,'E',2,label="$eps_reac+epsgrav\ [ergs/g/s]$",category="energy")

E_reac=gtb.Get_Var('eps_reac',2)
gtb.Set_Var(E_reac,'E_reac',2,label="$eps_reac\ [ergs/g/s]$",category="energy")

E_grav=gtb.Get_Var('epsgrav',2)
gtb.Set_Var(E_grav,'E_grav',2,label="$eps_grav\ [ergs/g/s]$",category="energy")

plt.plot(M,E,color='black',linestyle='solid',linewidth=2,label='Total eps')
plt.plot(M,E_reac,color='red',linestyle='solid',linewidth=2,label='eps reac')
plt.plot(M,E_grav,color='blue',linestyle='solid',linewidth=2,label='eps grav')
plt.legend(loc='upper center', shadow=True,prop={'size': 6})
plt.xlabel('$M_r$')
plt.ylabel('Energy(ergs/g/s)')
plt.show()
