##### Mdot vs Mass #########
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.dat',3)

from numpy import *
from matplotlib import *

import math
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

M1=gtb.Get_Var('M',1)
T1=gtb.Get_Var('t',1)

M1=M1[T1>9.0]
T1=T1[T1>9.0]
T1=T1[M1<7000]
M1=M1[M1<7000]

d=len(M1)
dM1=[]

for i in arange(0,d-1):
  dM1=np.append(dM1,(M1[i+1]-M1[i])/(T1[i+1]-T1[i]))

M2=gtb.Get_Var('M',2)
T2=gtb.Get_Var('t',2)

M2=M2[T2>9.0]
T2=T2[T2>9.0]
T2=T2[M2<7000]
M2=M2[M2<7000]

d=len(M2)
dM2=[]

for i in arange(0,d-1):
  dM2=np.append(dM2,(M2[i+1]-M2[i])/(T2[i+1]-T2[i]))

M3=gtb.Get_Var('M',3)
T3=gtb.Get_Var('t',3)

M3=M3[T3>9.0]
T3=T3[T3>9.0]
T3=T3[M3<7000]
M3=M3[M3<7000]

d=len(M3)
dM3=[]

for i in arange(0,d-1):
  dM3=np.append(dM3,(M3[i+1]-M3[i])/(T3[i+1]-T3[i]))

plt.plot(M1[0:-1],dM1,color='black',linestyle='solid',linewidth=2,label="491M_SS71")
plt.plot(M2[0:-1],dM2,color='blue',linestyle='solid',linewidth=2,label="1331M_SS14")
plt.plot(M3[0:-1],dM3,color='red',linestyle='solid',linewidth=2,label="6271M_SS0")
#plt.legend(loc='upper center', shadow=True,prop={'size': 6})
plt.xlabel('Mass (M$_{\odot}$)')
plt.ylabel('Accretion rate (M$_{\odot}$/yr)')
leg = plt.legend(loc='lower left', shadow=True,prop={'size': 12})

plt.show()

##### Mdot vs time #########

gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.dat',3)

from numpy import *
from matplotlib import *

import math
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')

M1=gtb.Get_Var('M',1)
T1=gtb.Get_Var('t',1)

M1=M1[T1>9.0]
T1=T1[T1>9.0]
T1=T1[M1<7000]
M1=M1[M1<7000]

d=len(M1)
dM1=[]

for i in arange(0,d-1):
  dM1=np.append(dM1,(M1[i+1]-M1[i])/(T1[i+1]-T1[i]))

M2=gtb.Get_Var('M',2)
T2=gtb.Get_Var('t',2)

M2=M2[T2>9.0]
T2=T2[T2>9.0]
T2=T2[M2<7000]
M2=M2[M2<7000]

d=len(M2)
dM2=[]

for i in arange(0,d-1):
  dM2=np.append(dM2,(M2[i+1]-M2[i])/(T2[i+1]-T2[i]))

M3=gtb.Get_Var('M',3)
T3=gtb.Get_Var('t',3)

M3=M3[T3>9.0]
T3=T3[T3>9.0]
T3=T3[M3<7000]
M3=M3[M3<7000]

d=len(M3)
dM3=[]

for i in arange(0,d-1):
  dM3=np.append(dM3,(M3[i+1]-M3[i])/(T3[i+1]-T3[i]))

plt.plot(T1[0:-1],dM1,color='black',linestyle='solid',linewidth=2,label="491M_SS71")
plt.plot(T2[0:-1],dM2,color='blue',linestyle='solid',linewidth=2,label="1331M_SS14")
plt.plot(T3[0:-1],dM3,color='red',linestyle='solid',linewidth=2,label="6271M_SS0")
#plt.legend(loc='upper center', shadow=True,prop={'size': 6})
plt.xlabel('Time ($years$)')
plt.ylabel('Accretion rate (M$_{\odot}$/yr)')
leg = plt.legend(loc='lower left', shadow=True,prop={'size': 12})

plt.show()
