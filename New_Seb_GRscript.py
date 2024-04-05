#Be in the star folder and launch ipython


listfiles=!ls *.v*
I1_list=[]
I2_a_list=[]
I2_b_list=[]
I2_tot_list=[]
I0_list=[]
cut_list=[]
Mtot=[]
cut_list=np.append(cut_list,listfiles[0])
m=0
for k in listfiles:
  if m==10:
    cut_list=np.append(cut_list,k)
    m=0
  else:
    m=m+1
for i in cut_list:
  gtb.loadS(i,1,forced=True)
  beta=gtb.Get_Var('beta',1)
  P=gtb.Get_Var('P',1)
  r=gtb.Get_Var('r_cm',1)
  rho=gtb.Get_Var('rho',1)
  Mr=gtb.Get_Var('Mr',1)
  Mtot=np.append(Mtot,Mr[0])
  Mr=Mr*gtb.Cst.Msol
  G=gtb.Cst.G
  c=gtb.Cst.c
  I1=np.trapz(1.5*beta*P*r**2,r)
  I2_a=np.trapz(-3.*G**2/c**2*rho*Mr**2,r)
  I2_b=np.trapz(-4.*G/c**2*P*Mr*r,r)
  I0=np.trapz(2./3.*r**2,Mr)
  I1_list=np.append(I1_list,I1)
  I2_a_list=np.append(I2_a_list,I2_a)
  I2_b_list=np.append(I2_b_list,I2_b)
  I2_tot_list=np.append(I2_tot_list,I2_a+I2_b)
  I0_list=np.append(I0_list,I0)


fig,ax=plt.subplots()
ax.plot(Mtot,-I1_list/-I0_list,color='tab:blue',linewidth=4.,label='I$_+$')
ax.plot(Mtot,I2_tot_list/-I0_list,color='tab:red',linewidth=4.,label='I$_-$')
ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GRIntegrals')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
