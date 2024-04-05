#### 10 Msun/yr last model
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428*10**(-8)                       #Gravitational constant
Msun=1.9884*10**33


R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.v0108911',skip_header=294))[4])
M = Msun*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.v0108911',skip_header=294))[49])

g = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.v0108911',skip_header=294))[55])
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.v0108911',skip_header=294))[14])
V=1.33*np.pi*R**3
mean_rho=M/V
mean_rho
tff = 0.5*((G*mean_rho)**-0.5)
tff/86400

#### 1 Msun/yr last model
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428*10**(-8)                       #Gravitational constant
Msun=1.9884*10**33


R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0132471',skip_header=307))[4])
M = Msun*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0132471',skip_header=307))[49])

g = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0132471',skip_header=307))[55])
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0132471',skip_header=307))[14])
V=1.33*np.pi*R**3
mean_rho=M/V
mean_rho
tff = 0.5*((G*mean_rho)**-0.5)
tff/86400

#### 0.1 Msun/yr last model
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428*10**(-8)                       #Gravitational constant
Msun=1.9884*10**33


R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002Z0S0.v0198161',skip_header=1568))[4])
M = Msun*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002Z0S0.v0198161',skip_header=1568))[49])

g = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002Z0S0.v0198161',skip_header=1568))[55])
rho = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002Z0S0.v0198161',skip_header=1568))[14])
V=1.33*np.pi*R**3
mean_rho=M/V
mean_rho
tff = 0.5*((G*mean_rho)**-0.5)
tff/86400
