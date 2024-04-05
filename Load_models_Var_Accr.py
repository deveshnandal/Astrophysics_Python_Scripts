# SMS Var_accr - SMS models with varaiable accretion rate
#  With accretion rate printed in final column
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test2_491M_SS71/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/771M_SS40/P002z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/778M_SS39/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/932M_SS27/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1135M_S20/P002z0S0.dat',5)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1331M_SS14/P002z0S0.dat',6)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1662M_SS10/P002z0S0.dat',7)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1923M_SS6/P002z0S0.dat',8)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',9)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/Test1_6127M_SS0/P002z0S0.dat',10)

# No accretion rate
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/Test2_491M_SS71/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/771M_SS40/P002z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/778M_SS39/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/932M_SS27/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1135M_S20/P002z0S0.dat',5)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1331M_SS14/P002z0S0.dat',6)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1662M_SS10/P002z0S0.dat',7)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/1923M_SS6/P002z0S0.dat',8)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/4477M_SS1/P002z0S0.dat',9)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files_2/Test1_6127M_SS0/P002z0S0.dat',10)



gtb.put_legend(4,label=['491M$_\odot$','771M$_\odot$','778M$_\odot$','932M$_\odot$','1135M$_\odot$','1331M$_\odot$','1662M$_\odot$','1923M$_\odot$','4477M$_\odot$','6127M$_\odot$'],fontsize=14)

gtb.put_legend(4,label=['1331M','1662M','1923M','4477M','6127M'],fontsize=14)

# Tests
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Ascending_Maccr/P002z0S0.dat',1)

# Tests polytropic models
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Poly_491M/P491Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Poly_932M/P932Z0S0.dat',2)
#gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Poly_6127M/P6127Z0S0.wg',3)

##### 1e-2 fitm0.99
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-2Msun_yr_0.99/P002z0S0.dat',10)


############
from numpy import *
from matplotlib import *

import numpy as np
from matplotlib import pyplot as plt

t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[1])
M = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/4477M_SS1/P002z0S0.dat',skip_header=0))[2])

d=len(M)
dM=[]

for i in arange(0,d-1):
  dM=np.append(dM,(M[i+1]-M[i])/(t[i+1]-t[i]))


np.savetxt('/Users/hermit/desktop/File_save/Data.txt', dM, delimiter=' ')
