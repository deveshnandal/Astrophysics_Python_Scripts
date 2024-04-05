import numpy as np
from matplotlib import pyplot as plt
enuc = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[10])
egrav = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[27])
epsd12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[96])
epsd22 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[97])

Mr = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0211371',skip_header=3))[49])


fig,ax=plt.subplots()
ax.plot(Mr,enuc,linewidth=2., label="$eps nuc$")
ax.plot(Mr,egrav,linewidth=2., label="$eps grav$")
ax.plot(Mr,epsd12,linewidth=2., label="$epsd12$")
ax.plot(Mr,epsd22,linewidth=2., label="$epsd22$")
ax.set_xlabel('M [M$_{\odot}$]', fontsize = 18)
ax.set_ylabel('Energy [$erg{g^{-1}}{s^{-1}}$]', fontsize = 18)
leg = plt.legend(loc='lower left', shadow=True,prop={'size': 9})
ax.set_yscale('log')
#plt.text(0.44, 5.64e-15, 'D', fontsize = 18)
plt.show()


enuc = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/TP3_files/P010Z0S0.v0059331',skip_header=3))[10])
