M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
sigma = 5.670374e-05
h=6.62606896*10**(-27)
M = 1.391713135E+05
R_sun=1.066966852E+15
k=1.3806504*10**(-16)

Teff = 10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[4])
M = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])

L = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[3]))
R= (L/(4*pi*sigma*(Teff)**4))**0.5
S_ion = 8*(pi**2)*(R**2)/((c**2)*(h**2))


S_LW_list = []
for i in range(0,len(Teff)):
    h_nu = np.linspace(11.18,13.6,100)
    S_LW = 8*(pi**2)*(R[i]**2)/((c**2)*(h**2))*(np.trapz((h_nu**2)/exp(h_nu/k*Teff[i])-1,h_nu))
    S_LW_list = np.append(S_LW_list,S_LW)
fig,ax=plt.subplots()
ax.plot(M,S_LW_list)
ax.set_xscale('log')
ax.set_yscale('symlog')
plt.show()
