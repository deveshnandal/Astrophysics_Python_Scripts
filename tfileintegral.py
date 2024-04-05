import matplotlib.pyplot as plt



def tfile(file):

  f= open(file)
  lines=f.readlines()
  nlines=len(lines)
  n=[]
  q=[]
  eps=[]
  h1=[]
  h2=[]
  h3=[]
  Mr=[]
  mr=[]

  for k in range(nlines):
    i=nlines-1-k
    x=lines[i]
    j=0

    var=''
    while j<6:
      var=var+x[j]
      j=j+1
    n=[int(var)]+n

    var=''
    while j<21:
      var=var+x[j]
      j=j+1
    q=[float(var)]+q

    var=''
    while j<37:
      var=var+x[j]
      j=j+1
    eps=[float(var)]+eps

    var=''
    while j<53:
      var=var+x[j]
      j=j+1
    h1=[float(var)]+h1

    var=''
    while j<69:
      var=var+x[j]
      j=j+1
    h2=[float(var)]+h2

    var=''
    while j<85:
      var=var+x[j]
      j=j+1
    h3=[float(var)]+h3

    var=''
    while j<101:
      var=var+x[j]
      j=j+1
    Mr=[float(var)]+Mr

    var=''
    while j<117:
      var=var+x[j]
      j=j+1
    mr=[float(var)]+mr

    dt=''
    while j<133:
      dt=dt+x[j]
      j=j+1
    dt=float(dt)

    if n[0]==1:
        break
    #print n[i],q[i],eps[i],h1[i],h2[i],h3[i],Mr[i],mr[i]
  return n,q,eps,h1,h2,h3,Mr,mr,dt


def vfile(file):

  f= open(file)
  lines=f.readlines()
  nlines=len(lines)

  eps=[]
  egrav=[]
  Mr=[]
  lr=[]
  n=[]
  X=[]
  for k in range(nlines):
    i=nlines-1-k
    x=lines[i]


    j=0
    var=''
    while j<5:
      var=var+x[j]
      j=j+1
    n=[int(var)]+n

    j=54
    var=''
    while j<67:
      var=var+x[j]
      j=j+1
    lr=[float(var)]+lr


    var=''
    while j<82:
      var=var+x[j]
      j=j+1
    X=[float(var)]+X


    j=130
    var=''
    while j<141:
      var=var+x[j]
      j=j+1
    eps=[float(var)]+eps

    j=341
    var=''
    while j<354:
      var=var+x[j]
      j=j+1
    egrav=[float(var)]+egrav

    j=679
    var=''
    while j<691:
      var=var+x[j]
      j=j+1
    Mr=[float(var)]+Mr

    if n[0]==1:
        break
    #print n[0],eps[0],Mr[0],lr[0],egrav[0]
    #print i,len(n),len(eps),len(lr),len(egrav),len(Mr)
  return n,Mr,lr,eps,egrav,X

def gfile(file):

  f= open(file)
  lines=f.readlines()
  x=lines[0]

  j=8
  t=''
  while j<30:
    t=t+x[j]
    j=j+1
  t=float(t)


  j=34
  M=''
  while j<48:
    M=M+x[j]
    j=j+1
  M=float(M)

  j=49
  L=''
  while j<58:
    L=L+x[j]
    j=j+1
  L=float(L)

  return t,M,L


def plotH(file):
  struc=tfile(file)
  q=struc[1]
  #print q
  h1=struc[3]
  h2=struc[4]
  h3=struc[5]
  plt.plot(q,h1,color='red',linewidth=2)
  plt.plot(q,h2,color='lightblue',linestyle='dashed',linewidth=2)
  plt.plot(q,h3,color='black',linestyle='dotted',linewidth=2)
  plt.ylim(0.65,0.652)
  plt.show()


def plotE(file):
  c=2.9979e10
  struc=tfile(file)
  q=struc[1]
  #print q
  eps=struc[2]
  h1=struc[3]
  h2=struc[4]
  dt=struc[8]
  #print dt
  d=len(q)
  zz7=range(d)
  for i in range(d):
     zz7[i]=.007*(c**2)*(h1[i]-h2[i])/dt#*1.602176487e-6*6.02214179e23
     eps[i]=eps[i]/dt


  plt.plot(q,eps,color='red',linewidth=2)
  plt.plot(q,zz7,color='black',linestyle='dotted',linewidth=2)
  #plt.ylim(0.65,0.652)
  plt.show()

def plotL(fileg,filev):
  Msol=1.9891e33
  Lsol=3.845e33
  mod=gfile(fileg)
  L=mod[2]
  struc=vfile(filev)
  Mr=struc[1]
  lr=struc[2]
  eps=struc[3]
  egrav=struc[4]
  d=len(Mr)
  Lr=range(d)
  Ln=range(d)
  Lg=range(d)
  Lt=range(d)
  Ln[d-1]=0.
  Lr[d-1]=0.
  Lg[d-1]=0.
  Lt[d-1]=0.
  for i in range(d-1):
      j=d-2-i
      Lr[j]=10**L*lr[j]
      Ln[j]=Ln[j+1]+0.5*(eps[j]+eps[j+1])*(Mr[j]-Mr[j+1])*(Msol/Lsol)
      Lg[j]=Lg[j+1]+0.5*(egrav[j]+egrav[j+1])*(Mr[j]-Mr[j+1])*(Msol/Lsol)
      Lt[j]=Ln[j]+Lg[j]
  plt.plot(Mr,Lr,color='red',linestyle='solid')
  plt.plot(Mr,Ln,color='green',linestyle='dashed')
  plt.plot(Mr,Lg,color='black',linestyle='dashed')
  plt.plot(Mr,Lt,color='blue',linestyle='dotted')
  plt.show()


def plotE2(fileg,filev,filet,filev2,fileg2):
  c=2.9979e10
  Msol=1.9891e33
  Yr=3.15576e7
  strucg=gfile(fileg)
  t1=strucg[0]
  M=strucg[1]

  strucg2=gfile(fileg2)
  t2=strucg2[0]

  dt2=(t2-t1)*Yr

  struct=tfile(filet)
  q=struct[1]
  eps=struct[2]
  h1=struct[3]
  h2=struct[4]
  dt=struct[8]

  strucv=vfile(filev)
  Mr=strucv[1]
  lr=strucv[2]
  epsv=strucv[3]
  egrav=strucv[4]
  X1=strucv[5]
  dv=len(Mr)

  strucv2=vfile(filev2)
  Mr2=strucv2[1]
  epsv2=strucv2[3]
  X2=strucv2[5]
  dv2=len(Mr2)

  #print dt
  d=len(q)
  zz7=range(d)
  Mt=range(d)
  for i in range(d):
     zz7[i]=.007*(c**2)*(h1[i]-h2[i])/dt#*1.602176487e-6*6.02214179e23
     Mt[i]=q[i]*M
  #print zz7
  ZZ7=range(d)
  ZZ7[d-1]=0.
  Lnt=range(d)
  Lnt[d-1]=0.

  for i in range(d-1):
     j=d-2-i
     ZZ7[j]=ZZ7[j+1]+0.5*(zz7[j+1]+zz7[j])*(Mt[j]-Mt[j+1])*Msol
     Lnt[j]=Lnt[j+1]+0.5*(eps[j]+eps[j+1])*(Mt[j]-Mt[j+1])*Msol/dt#/Lsol


  zz7b=range(dv)
  zz7b[dv-1]=0.
  k=0
  for i in range(dv):
     while Mr2[k]>Mr[i]: #changed from > to < on sun 28 march
         k=k+1
     #print Mr[i],Mr2[k]
     zz7b[i]=.007*(c**2)*(X1[i]-X2[k])/dt2

  ZZ7b=range(dv)
  ZZ7b[dv-1]=0.
  Ln=range(dv)
  Ln[dv-1]=0.
  for i in range(dv-1):
     j=dv-2-i
     Ln[j]=Ln[j+1]+0.5*(epsv[j]+epsv[j+1])*(Mr[j]-Mr[j+1])*Msol#/Lsol
     ZZ7b[j]=ZZ7b[j+1]+0.5*(zz7b[j+1]+zz7b[j])*(Mr[j]-Mr[j+1])*Msol

  Ln2=range(dv2)
  Ln2[dv2-1]=0.
  for i in range(dv2-1):
     j=dv2-2-i
     Ln2[j]=Ln2[j+1]+0.5*(epsv2[j]+epsv2[j+1])*(Mr2[j]-Mr2[j+1])*Msol#/Lsol

  plt.plot(Mr,Ln,color='red',linestyle='solid',linewidth=2)
  plt.plot(Mt,ZZ7,color='black',linestyle='dotted',linewidth=2)
  plt.plot(Mt,Lnt,color='blue',linestyle='dashed',linewidth=2)
  plt.plot(Mr,ZZ7b,color='green',linestyle='dotted',linewidth=2)
  #plt.ylim(0.65,0.652)
  plt.show()
