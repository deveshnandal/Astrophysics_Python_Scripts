######### HRD Plot ##########
######### With H1c as z col #####
from numpy import *
from matplotlib import *

import math
import matplotlib.pyplot as plt
import numpy as np

gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.dat',3)

gtb.set_lineWidth(3)
gtb.CBLimits(min=0,max=0.7512)
gtb.Limits(xmax=5.2)
#gtb.mark_phase('H',colour='0.10')
gtb.HRD_plot()
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')

######### HRD Plot ##########
######### With He4c as z col #####
from numpy import *
from matplotlib import *

import math
import matplotlib.pyplot as plt
import numpy as np

gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.dat',3)

gtb.set_lineWidth(3)
gtb.CBLimits(min=0,max=0.7512)
gtb.Limits(xmax=5.2)
gtb.mark_phase('H',colour='0.10')
gtb.HRD_plot(zcol='He4c',plotif='phase=="He"')
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')

################################
##### Comparison HRDs ##########
from numpy import *
from matplotlib import *

import math
import matplotlib.pyplot as plt
import numpy as np

gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3/P002z0S0.dat',2)
gtb.set_lineWidth(2.5)
gtb.HRD_plot()
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')

###################################
##### Comparison HRDs #############
from numpy import *
from matplotlib import *

import math
import matplotlib.pyplot as plt
import numpy as np
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',2)
gtb.set_lineWidth(2.5)
gtb.HRD_plot()
gtb.isoRadius(fontsize=10,line='dashdot',colour='0.4')
