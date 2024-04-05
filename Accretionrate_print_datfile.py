from numpy import *
from matplotlib import *

import numpy as np
from matplotlib import pyplot as plt

t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/P002z0S0.dat',skip_header=0))[1])
M = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/P002z0S0.dat',skip_header=0))[2])

d=len(M)
dM=[]

for i in arange(0,d-1):
  dM=np.append(dM,(M[i+1]-M[i])/(t[i+1]-t[i]))


np.savetxt('/Users/hermit/desktop/File_save/Data.txt', dM, delimiter=' ')


# copy

from numpy import *
from matplotlib import *

import numpy as np
from matplotlib import pyplot as plt

t = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1923.dat',skip_header=0))[1])
M = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Load_files/1923.dat',skip_header=0))[2])

d=len(M)
dM=[]

for i in arange(0,d-1):
  dM=np.append(dM,(M[i+1]-M[i])/(t[i+1]-t[i]))


np.savetxt('/Users/hermit/desktop/File_save/Data.txt', dM, delimiter=' ')
