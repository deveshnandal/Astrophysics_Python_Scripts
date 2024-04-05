##### Three axis Plot where Third axis is independent of the first two #####

import matplotlib.pyplot as plt
import numpy as np
t1 = [75, 76, 77, 78]
t2 = [75, 76, 77, 78]
v = [0.5, 0.5, 0.8, 0.8]

image_data = np.column_stack([t1, t2, v])
plt.imshow(image_data)
plt.colorbar()
plt.show()



import matplotlib.pyplot as plt
import numpy as np
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat',1)
for i in range(gtb.MyDriver.SelectedModels)

log_L = gtb.Get_Var('L', 1)
log_Teff = gtb.Get_Var('Teff', 1)
Radius = np.log10(gtb.Get_Var('R',1))
v = [0.5, 0.5, 0.8, 0.8]
plt.figure()
image_data = np.column_stack([log_Teff, log_L, Radius])
plt.imshow(image_data)
plt.colorbar()
plt.show()
