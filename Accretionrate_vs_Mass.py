gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_then_1e-3_Maccr/P120Z0S0_Var_Maccr/P002z0S0.wg',1)


import math
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

M=gtb.Get_Var('M',1)
T=gtb.Get_Var('t',1)

M=M[T>9.0]
T=T[T>9.0]
T=T[M<1000]
M=M[M<1000]

d=len(M)
dM=[]

for i in arange(0,d-1):
  dM=np.append(dM,(M[i+1]-M[i])/(T[i+1]-T[i]))

plt.plot(M[0:-1],dM,color='black',linestyle='solid',linewidth=2)
#plt.legend(loc='upper center', shadow=True,prop={'size': 6})
plt.xlabel('$M(Msolar)$')
plt.ylabel('$Accretion_rate(M/yr)$')
plt.show()
