################  GR integral script #############

#Be in the star folder and launch ipython
# You can stay in ipython but change folders to load other models by doing cd

# 10 Msun/yr***
listfiles_10=!ls *.v*
I1_10_list=[]
I2_10_a_list=[]
I2_10_b_list=[]
I2_10_tot_list=[]
I0_10_list=[]
cut_list_10=[]
Mtot_10=[]
cut_list_10=np.append(cut_list_10,listfiles_10[0])
m=0
for k in listfiles_10:
  if m==10:
    cut_list_10=np.append(cut_list_10,k)
    m=0
  else:
    m=m+1
for i in cut_list_10:
  gtb.loadS(i,1,forced=True)
  beta_10=gtb.Get_Var('beta',1)
  P_10=gtb.Get_Var('P',1)
  r_10=gtb.Get_Var('r_cm',1)
  rho_10=gtb.Get_Var('rho',1)
  Mr_10=gtb.Get_Var('Mr',1)
  Mtot_10=np.append(Mtot_10,Mr_10[0])
  Mr_10=Mr_10*gtb.Cst.Msol
  G=gtb.Cst.G
  c=gtb.Cst.c
  I1_10=np.trapz(1.5*beta_10*P_10*r_10**2,r_10)
  I2_10_a=np.trapz(-3.*G**2/c**2*rho_10*Mr_10**2,r_10)
  I2_10_b=np.trapz(-4.*G/c**2*P_10*Mr_10*r_10,r_10)
  I0_10=np.trapz(2./3.*r_10**2,Mr_10)
  I1_10_list=np.append(I1_10_list,I1_10)
  I2_10_a_list=np.append(I2_10_a_list,I2_10_a)
  I2_10_b_list=np.append(I2_10_b_list,I2_10_b)
  I2_10_tot_list=np.append(I2_10_tot_list,I2_10_a+I2_10_b)
  I0_10_list=np.append(I0_10_list,I0_10)


# 1 Msun/yr***

listfiles_1=!ls *.v*
I1_1_list=[]
I2_1_a_list=[]
I2_1_b_list=[]
I2_1_tot_list=[]
I0_1_list=[]
cut_list_1=[]
Mtot_1=[]
cut_list_1=np.append(cut_list_1,listfiles_1[0])
m=0
for k in listfiles_1:
  if m==10:
    cut_list_1=np.append(cut_list_1,k)
    m=0
  else:
    m=m+1
for i in cut_list_1:
  gtb.loadS(i,1,forced=True)
  beta_1=gtb.Get_Var('beta',1)
  P_1=gtb.Get_Var('P',1)
  r_1=gtb.Get_Var('r_cm',1)
  rho_1=gtb.Get_Var('rho',1)
  Mr_1=gtb.Get_Var('Mr',1)
  Mtot_1=np.append(Mtot_1,Mr_1[0])
  Mr_1=Mr_1*gtb.Cst.Msol
  G=gtb.Cst.G
  c=gtb.Cst.c
  I1_1=np.trapz(1.5*beta_1*P_1*r_1**2,r_1)
  I2_1_a=np.trapz(-3.*G**2/c**2*rho_1*Mr_1**2,r_1)
  I2_1_b=np.trapz(-4.*G/c**2*P_1*Mr_1*r_1,r_1)
  I0_1=np.trapz(2./3.*r_1**2,Mr_1)
  I1_1_list=np.append(I1_1_list,I1_1)
  I2_1_a_list=np.append(I2_1_a_list,I2_1_a)
  I2_1_b_list=np.append(I2_1_b_list,I2_1_b)
  I2_1_tot_list=np.append(I2_1_tot_list,I2_1_a+I2_1_b)
  I0_1_list=np.append(I0_1_list,I0_1)

# 0.1 Msun/yr***

listfiles_01=!ls *.v*
I1_01_list=[]
I2_01_a_list=[]
I2_01_b_list=[]
I2_01_tot_list=[]
I0_01_list=[]
cut_list_01=[]
Mtot_01=[]
cut_list_01=np.append(cut_list_01,listfiles_01[0])
m=0
for k in listfiles_01:
  if m==10:
    cut_list_01=np.append(cut_list_01,k)
    m=0
  else:
    m=m+1
for i in cut_list_01:
  gtb.loadS(i,1,forced=True)
  beta_01=gtb.Get_Var('beta',1)
  P_01=gtb.Get_Var('P',1)
  r_01=gtb.Get_Var('r_cm',1)
  rho_01=gtb.Get_Var('rho',1)
  Mr_01=gtb.Get_Var('Mr',1)
  Mtot_01=np.append(Mtot_01,Mr_01[0])
  Mr_01=Mr_01*gtb.Cst.Msol
  G=gtb.Cst.G
  c=gtb.Cst.c
  I1_01=np.trapz(1.5*beta_01*P_01*r_01**2,r_01)
  I2_01_a=np.trapz(-3.*G**2/c**2*rho_01*Mr_01**2,r_01)
  I2_01_b=np.trapz(-4.*G/c**2*P_01*Mr_01*r_01,r_01)
  I0_01=np.trapz(2./3.*r_01**2,Mr_01)
  I1_01_list=np.append(I1_01_list,I1_01)
  I2_01_a_list=np.append(I2_01_a_list,I2_01_a)
  I2_01_b_list=np.append(I2_01_b_list,I2_01_b)
  I2_01_tot_list=np.append(I2_01_tot_list,I2_01_a+I2_01_b)
  I0_01_list=np.append(I0_01_list,I0_01)

# 0.01 Msun/yr***

listfiles_001=!ls *.v*
I1_001_list=[]
I2_001_a_list=[]
I2_001_b_list=[]
I2_001_tot_list=[]
I0_001_list=[]
cut_list_001=[]
Mtot_001=[]
cut_list_001=np.append(cut_list_001,listfiles_001[0])
m=0
for k in listfiles_001:
  if m==10:
    cut_list_001=np.append(cut_list_001,k)
    m=0
  else:
    m=m+1
for i in cut_list_001:
  gtb.loadS(i,1,forced=True)
  beta_001=gtb.Get_Var('beta',1)
  P_001=gtb.Get_Var('P',1)
  r_001=gtb.Get_Var('r_cm',1)
  rho_001=gtb.Get_Var('rho',1)
  Mr_001=gtb.Get_Var('Mr',1)
  Mtot_001=np.append(Mtot_001,Mr_001[0])
  Mr_001=Mr_001*gtb.Cst.Msol
  G=gtb.Cst.G
  c=gtb.Cst.c
  I1_001=np.trapz(1.5*beta_001*P_001*r_001**2,r_001)
  I2_001_a=np.trapz(-3.*G**2/c**2*rho_001*Mr_001**2,r_001)
  I2_001_b=np.trapz(-4.*G/c**2*P_001*Mr_001*r_001,r_001)
  I0_001=np.trapz(2./3.*r_001**2,Mr_001)
  I1_001_list=np.append(I1_001_list,I1_001)
  I2_001_a_list=np.append(I2_001_a_list,I2_001_a)
  I2_001_b_list=np.append(I2_001_b_list,I2_001_b)
  I2_001_tot_list=np.append(I2_001_tot_list,I2_001_a+I2_001_b)
  I0_001_list=np.append(I0_001_list,I0_001)

# 0.001 Msun/yr***

listfiles_0001=!ls *.v*
I1_0001_list=[]
I2_0001_a_list=[]
I2_0001_b_list=[]
I2_0001_tot_list=[]
I0_0001_list=[]
cut_list_0001=[]
Mtot_0001=[]
cut_list_0001=np.append(cut_list_0001,listfiles_0001[0])
m=0
for k in listfiles_0001:
  if m==10:
    cut_list_0001=np.append(cut_list_0001,k)
    m=0
  else:
    m=m+1
for i in cut_list_0001:
  gtb.loadS(i,1,forced=True)
  beta_0001=gtb.Get_Var('beta',1)
  P_0001=gtb.Get_Var('P',1)
  r_0001=gtb.Get_Var('r_cm',1)
  rho_0001=gtb.Get_Var('rho',1)
  Mr_0001=gtb.Get_Var('Mr',1)
  Mtot_0001=np.append(Mtot_0001,Mr_0001[0])
  Mr_0001=Mr_0001*gtb.Cst.Msol
  G=gtb.Cst.G
  c=gtb.Cst.c
  I1_0001=np.trapz(1.5*beta_0001*P_0001*r_0001**2,r_0001)
  I2_0001_a=np.trapz(-3.*G**2/c**2*rho_0001*Mr_0001**2,r_0001)
  I2_0001_b=np.trapz(-4.*G/c**2*P_0001*Mr_0001*r_0001,r_0001)
  I0_0001=np.trapz(2./3.*r_0001**2,Mr_0001)
  I1_0001_list=np.append(I1_0001_list,I1_0001)
  I2_0001_a_list=np.append(I2_0001_a_list,I2_0001_a)
  I2_0001_b_list=np.append(I2_0001_b_list,I2_0001_b)
  I2_0001_tot_list=np.append(I2_0001_tot_list,I2_0001_a+I2_0001_b)
  I0_0001_list=np.append(I0_0001_list,I0_0001)


fig,ax=plt.subplots()
ax.plot(Mtot_10,-I1_10_list/-I0_10_list,color='k',linewidth=2.,label='10M$_{\odot}/yr I{_+}$')
ax.plot(Mtot_10,I2_10_tot_list/-I0_10_list,color='k',linestyle='dashdot',linewidth=2.,label='10M$_{\odot}/yr I{_-}$')
ax.plot(Mtot_1,-I1_1_list/-I0_1_list,color='tab:red',linewidth=2.,label='1M$_{\odot}/yr I{_+}$')
ax.plot(Mtot_1,I2_1_tot_list/-I0_1_list,color='tab:red',linestyle='dashdot',linewidth=2.,label='1M$_{\odot}/yr I{_-}$')
ax.plot(Mtot_01,-I1_01_list/-I0_01_list,color='tab:green',linewidth=2.,label='0.1M$_{\odot}/yr I{_+}$')
ax.plot(Mtot_01,I2_01_tot_list/-I0_01_list,color='tab:green',linestyle='dashdot',linewidth=2.,label='0.1M$_{\odot}/yr I{_-}$')
ax.plot(Mtot_001,-I1_001_list/-I0_001_list,color='tab:blue',linewidth=2.,label='0.01M$_{\odot}/yr I{_+}$')
ax.plot(Mtot_001,I2_001_tot_list/-I0_001_list,color='tab:blue',linestyle='dashdot',linewidth=2.,label='0.01M$_{\odot}/yr I{_-}$')
ax.plot(Mtot_0001,-I1_0001_list/-I0_0001_list,color='tab:cyan',linewidth=2.,label='0.001M$_{\odot}/yr I{_+}$')
ax.plot(Mtot_0001,I2_0001_tot_list/-I0_0001_list,color='tab:cyan',linestyle='dashdot',linewidth=2.,label='0.001M$_{\odot}/yr I{_-}$')


ax.legend(loc='upper right', shadow=True,prop={'size': 6})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GRIntegrals')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

x1 = [449661]
y1 = [7.1752e-15]
plt.plot(x1, y1, marker="o", markersize=6, markeredgecolor="orange", markerfacecolor="yellow")
plt.annotate("449661M$_{\odot}$", (267040, 2.172e-15),fontsize='6')

x2 = [214092]
y2 = [7.8842e-14]
plt.plot(x2, y2, marker="o", markersize=6, markeredgecolor="orange", markerfacecolor="yellow")
plt.annotate("214092M$_{\odot}$", (174515, 3.5567e-14),fontsize='6')

x3 = [104046]
y3 = [1.2154e-13]
plt.plot(x3, y3, marker="o", markersize=6, markeredgecolor="orange", markerfacecolor="yellow")
plt.annotate("104046M$_{\odot}$", (63791, 2.5368e-13),fontsize='6')

####### Without labels

fig,ax=plt.subplots()

#ax.tick_params(axis='both', which='major', labelsize=16)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.plot(Mtot_10,-I1_10_list/-I0_10_list,color='k',linewidth=2.)
ax.plot(Mtot_10,I2_10_tot_list/-I0_10_list,color='k',linestyle='dashdot',linewidth=2.)
ax.plot(Mtot_1,-I1_1_list/-I0_1_list,color='tab:red',linewidth=2.)
ax.plot(Mtot_1,I2_1_tot_list/-I0_1_list,color='tab:red',linestyle='dashdot',linewidth=2.)
ax.plot(Mtot_01,-I1_01_list/-I0_01_list,color='tab:green',linewidth=2.)
ax.plot(Mtot_01,I2_01_tot_list/-I0_01_list,color='tab:green',linestyle='dashdot',linewidth=2.)
ax.plot(Mtot_001,-I1_001_list/-I0_001_list,color='tab:blue',linewidth=2.)
ax.plot(Mtot_001,I2_001_tot_list/-I0_001_list,color='tab:blue',linestyle='dashdot',linewidth=2.)
ax.plot(Mtot_0001,-I1_0001_list/-I0_0001_list,color='tab:cyan',linewidth=2.)
ax.plot(Mtot_0001,I2_0001_tot_list/-I0_0001_list,color='tab:cyan',linestyle='dashdot',linewidth=2.)
x1 = [449661]
y1 = [7.1752e-15]
plt.plot(x1, y1, marker="o", markersize=6, markeredgecolor="orange", markerfacecolor="yellow")
#plt.annotate("449661M$_{\odot}$", (267040, 2.172e-15),fontsize='6')

x2 = [214092]
y2 = [7.8842e-14]
plt.plot(x2, y2, marker="o", markersize=6, markeredgecolor="orange", markerfacecolor="yellow")
#plt.annotate("214092M$_{\odot}$", (174515, 3.5567e-14),fontsize='6')

x3 = [104046]
y3 = [1.2154e-13]
plt.plot(x3, y3, marker="o", markersize=6, markeredgecolor="orange", markerfacecolor="yellow")
#plt.annotate("104046M$_{\odot}$", (63791, 2.5368e-13),fontsize='6')

#ax.legend(loc='upper right', shadow=True,prop={'size': 6})
ax.set_xlabel('Mass [M$_{\odot}$]', fontsize=16)
ax.set_ylabel('GRIntegrals', fontsize=16)
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
