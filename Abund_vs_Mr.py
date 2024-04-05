import numpy as np
from matplotlib import pyplot as plt

H2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[93])
Li6 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[94])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[95])
Y3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[31])
X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[6])
Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[7])
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[9])
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[34])
M_tot = 139171.11504
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[49])



fig,ax=plt.subplots()
ax.plot(Mfrac,H2,linewidth=2., label="H2")
ax.plot(Mfrac,Li6,linewidth=2., label="Li6")
ax.plot(Mfrac,Li7,linewidth=2., label="Li7")
ax.plot(Mfrac,Y3,linewidth=2., label="He3")
ax.plot(Mfrac,X,linewidth=2., label="H1")
ax.plot(Mfrac,Y,linewidth=2., label="He4")
ax.plot(Mfrac,C12,linewidth=2., label="C12")
ax.plot(Mfrac,N14,linewidth=2., label="N14")
ax.plot(Mfrac,O16,linewidth=2., label="O16")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=12)
ax.set_ylabel('Abundance profile',fontsize=12)


leg = plt.legend(loc='lower left', shadow=True,prop={'size': 9})

#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
