# Trapezium integration method
# Copy and paste individual section of code into ipython and press enter


# When the limits are finite: in this case 0 to 1
import math
def f(x):
  return x**4*(1-x)**4/(1+x**2)
def trap(f,n):
  h=1/float(n)
  intgr=0.5*h*f((0)+f(1))
  for i in range(1,int(n)):
    intgr=intgr+h*f(i*h)
  return intgr
print(trap(f,100))

#When the limits are infinite
import math
def f(x):
    return math.exp(-x**2)
def trap(f,n,a,b):
    h = (b - a) / float(n)
    intgr=0.5*h*(f(a)+f(b))
    for i in range(1,int(n)):
        intgr=intgr+h*f(a+i*h)
    return intgr

a=-10
b=10
n=100

while(abs(trap(f,n,a,b)-trap(f,n*4,a*2,b*2))> 1e-6):
    n*=4
    a*=2
    b*=2
print(trap(f,n,a,b))

# Integrate using scipy.integrate
    # Example 1
import scipy
from scipy.integrate import quad
from math import *

def f(x):
    return x**4*log(x+sqrt(x**2+1))

print(quad(f,0,2))#here 0 and 2 are the limits of the function

    #Example 2
from pylab import *
from math import *
import scipy
from scipy.integrate import quad

def f(x, a):
    return(2/pi)/sqrt(1-sin(a/2)**2*sin(x)**2)

print("%15s%15s%15s" % ("A (degrees)", "A (radians)", "T/T0"))
for i in range(0, 91):
    angle = pi * i / 180
    print("%15d%15.10f%15.10f" % (i, angle, quad(f,0,pi/2,args=(angle))[0]))


# Plotting integrated functions: Sin versus integrated cos

from pylab import *
from math import *
import scipy
from scipy.integrate import quad

def f(x):
    return cos(x)

x = arange(-pi,pi+0.1,0.1)
y_sin = []
y_cos_integrated = []

for element in x:
    y_sin.append(sin(element))
    y_cos_integrated.append(quad(f,-pi,element)[0]-sin(pi))

plot(x,y_sin)
plot(x,y_cos_integrated)
show()

# Integrating ODE with odeint

from scipy import *
from scipy.integrate import odeint
from pylab import *

def damped_osc(u,t):
    x,v = u
    return(v,-k*(x-L)/m-b*v)

t = arange(0,20.1,0.1)
u0 = array([1,0])

b=0.4
k=8.0
L=0.5
m=1.0

u = odeint(damped_osc,u0,t)

figure(1)
plot(t,u[:,0],t,u[:,1]) #u[:,0] is x; u[:,1] is v
xlabel('Time')
title('Damped Oscillator')

figure(2)
plot(u[:,0],u[:,1])
title('Phase-space')
xlabel('Position')
ylabel('Velocity')
show()

# Questions and solutions, Look in python_scripts on desktop and the problems
# and solutions are in the learn_python folder

#1
from pylab import *
from math import log
import scipy
from scipy.integrate import quad

def f(x):
    return x*log(x)
print(quad(f,1,2)[0])


#2 btw quad means quadrature, an old name for integration
from pylab import *
from math import *
import scipy
from scipy.integrate import quad

def f(x):
    return 1./(x**6+1)
print(quad(f,-pi,pi)[0])

#3
import scipy
from scipy.integrate import quad
def f(x):
    return x**x
print(quad(f,1,2)[0])

#4
from math import sin
def f(x):
    return 1 if x==0 else sin(x)/x
print(quad(f,1,100)[0])

###############
import numpy as np
from scipy.integrate import quad
from scipy.integrate import dblquad
def f(x):
    return x

area = quad(f, 0, 2)
print(area)

def f(x,y):
    return x*y

area = dblquad(f, 0, 2, 0, 5)
