skip_header=3

data120S4=np.genfromtxt('/Users/devesh/Observatory/120.dat')
np.transpose(data120S4).shape ()
three = np.loadtxt("Users/devesh/Observatory/120.dat")[:, 3]


gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-4_Maccr/End_HBurning_ini_GeorgesTest/P002z0S0.dat',5)

clf()

plt.xlabel(r'Log T$_{\rm eff}$', fontsize=18)

plt.ylabel(r'Log L/L$_\odot$', fontsize=18)
#plt.axis([5.0,4.0, 6.2,6.7], fontsize=16)
plt.title(r'HRD', fontsize=16)
plt.grid(True)


#datam=data120S4
logL = gtb.Get_Var('L',1)
logT = gtb.Get_Var('Teff',1)
#LogL=datam['f3’]
#logT=datam['f4’]

plt.plot(logT,LogL,'r',lw=3)

x = np.linspace(4.0,5.0,101)

y = np.linspace(6.2,6.7,101)

z = np.array([10**(0.5*(j-4.*i+4.*3.761)) for j in y for i in x])

X, Y = np.meshgrid(x, y)

Z = z.reshape(101, 101)

plt.pcolor(X, Y, Z)


x = np.linspace(4.0,5.0,2)
y = 2.*1.+4.*x-4.*3.761
plt.plot(x, y,'w')


x = np.linspace(4.0,5.0,2)
y = 2.*2.+4.*x-4.*3.761
plt.plot(x, y,'w')


x = np.linspace(4.0,5.0,2)
y = 2.*3.+4.*x-4.*3.761
plt.plot(x, y,'w')

plt.show()
