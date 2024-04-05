#############  Gr integral vs mass ############

# 1331M***

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

# 491M Msun/yr***

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

# 6127 Msun/yr***

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
a = 330
b = 492
plt.axvspan(a, b, color='c', alpha=0.2, lw=0)
a = 252
b = 1331
plt.axvspan(a, b, color='y', alpha=0.2, lw=0)
a = 1613
b = 6127
plt.axvspan(a, b, color='b', alpha=0.2, lw=0)
ax.plot(Mtot_001,-I1_001_list/-I0_001_list,color='k',linewidth=2.,label='491M$_{\odot} I{_+}$')
ax.plot(Mtot_001,I2_001_tot_list/-I0_001_list,color='k',linestyle='dashdot',linewidth=2.,label='491M$_{\odot} I{_-}$')
ax.plot(Mtot_01,-I1_01_list/-I0_01_list,color='tab:blue',linewidth=2.,label='1331M$_{\odot}/yr I{_+}$')
ax.plot(Mtot_01,I2_01_tot_list/-I0_01_list,color='tab:blue',linestyle='dashdot',linewidth=2.,label='1331M$_{\odot} I{_-}$')
ax.plot(Mtot_0001,-I1_0001_list/-I0_0001_list,color='tab:red',linewidth=2.,label='6127M$_{\odot} I{_+}$')
ax.plot(Mtot_0001,I2_0001_tot_list/-I0_0001_list,color='tab:red',linestyle='dashdot',linewidth=2.,label='6127M$_{\odot} I{_-}$')


ax.legend(loc='upper left', shadow=True,prop={'size': 7})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GRIntegrals')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
