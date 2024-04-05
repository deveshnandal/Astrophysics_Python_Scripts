import sys
sys.path.append('/Users/devesh/Observatory/GENEC_toolBox/')
import GENEC_toolBox as gtb
import matplotlib.pyplot as plt

def load12sims():
    gtb.loadE('/Users/devesh/Observatory/StarCalc/TutorialCalc/M015Z14V0.4/M015Z14V0.4.dat',1)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4/M015Zm8V0.4.dat',2)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4/M015Z0V0.4.dat',3)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod12/M015Z14V0.4Im0Cod12.dat',4)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod12/M015Zm8V0.4Im0Cod12.dat',5)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod12/M015Z0V0.4Im0Cod12.dat',6)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod21/M015Z14V0.4Im0Cod21.dat',7)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod21/M015Zm8V0.4Im0Cod21.dat',8)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod21/M015Z0V0.4Im0Cod21.dat',9)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod22/M015Z14V0.4Im0Cod22.dat',10)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod22/M015Zm8V0.4Im0Cod22.dat',11)
    gtb.loadE('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod22/M015Z0V0.4Im0Cod22.dat',12)
    gtb.Loaded()
    return

def plotAllGraphs(number):
    gtb.select_model(number)
    gtb.multiPlot(4)
    gtb.HRD_plot()
    gtb.YTeff(9)
    return
load12sims()


gtb.select_model()
gtb.defX('line')
gtb.Plot('H1c')

gtb.logVar('y')
gtb.Abund()


#10 % H burning
gtb.loadS('/Users/devesh/Observatory/StarCalc/TutorialCalc/M015Z14V0.4/M015Z14V0.4.v0000811',13)

gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4/M015Z0V0.4.v0000911',15)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod12/M015Z14V0.4Im0Cod12.v0000781.gz',16)

gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod12/M015Z0V0.4Im0Cod12.v0000871.gz',18)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod21/M015Z14V0.4Im0Cod21.v0000831.gz',19)

gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod21/M015Z0V0.4Im0Cod21.v0000921.gz',21)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod22/M015Z14V0.4Im0Cod22.v0000781.gz',22)

gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod22/M015Z0V0.4Im0Cod22.v0000871.gz',24)

# Halfway through H1c burning
gtb.loadS('/Users/devesh/Observatory/StarCalc/TutorialCalc/M015Z14V0.4/M015Z14V0.4.v0002341',13)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4/M015Zm8V0.4.v0002051',14)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4/M015Z0V0.4.v0001961',15)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod12/M015Z14V0.4Im0Cod12.v0002041.gz',16)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod12/M015Zm8V0.4Im0Cod12.v0002021.gz',17)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod12/M015Z0V0.4Im0Cod12.v0001821.gz',18)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod21/M015Z14V0.4Im0Cod21.v0002341.gz',19)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod21/M015Zm8V0.4Im0Cod21.v0002071.gz',20)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod21/M015Z0V0.4Im0Cod21.v0001931.gz',21)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod22/M015Z14V0.4Im0Cod22.v0002021.gz',22)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod22/M015Zm8V0.4Im0Cod22.v0001831.gz',23)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod22/M015Z0V0.4Im0Cod22.v0001691.gz',24)

# Halfway through He4c burning
gtb.loadS('/Users/devesh/Observatory/StarCalc/TutorialCalc/M015Z14V0.4/M015Z14V0.4.v0012271',25)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4/M015Zm8V0.4.v0009621',26)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4/M015Z0V0.4.v0008731',27)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod12/M015Z14V0.4Im0Cod12.v0012121.gz',28)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod12/M015Zm8V0.4Im0Cod12.v0099971.gz',29)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod12/M015Z0V0.4Im0Cod12.v0065081.gz',30)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod21/M015Z14V0.4Im0Cod21.v0013011.gz',31)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod21/M015Zm8V0.4Im0Cod21.v0009101.gz',32)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod21/M015Z0V0.4Im0Cod21.v0009221.gz',33)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod22/M015Z14V0.4Im0Cod22.v0012061.gz',34)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod22/M015Zm8V0.4Im0Cod22.v0007931.gz',35)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod22/M015Z0V0.4Im0Cod22.v0008421.gz',36)

# End of He4c burning
gtb.loadS('/Users/devesh/Observatory/StarCalc/TutorialCalc/M015Z14V0.4/M015Z14V0.4.v0024681',37)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4/M015Zm8V0.4.v0020511',38)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4/M015Z0V0.4.v0025311',39)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod12/M015Z14V0.4Im0Cod12.v0023981.gz',40)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod12/M015Zm8V0.4Im0Cod12.v0439531.gz',41)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod12/M015Z0V0.4Im0Cod12.v0188731.gz',42)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod21/M015Z14V0.4Im0Cod21.v0024431.gz',43)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod21/M015Zm8V0.4Im0Cod21.v0020021.gz',44)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod21/M015Z0V0.4Im0Cod21.v0020281.gz',45)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z14V0.4Im0Cod22/M015Z14V0.4Im0Cod22.v0026331.gz',46)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Zm8V0.4Im0Cod22/M015Zm8V0.4Im0Cod22.v0019121.gz',47)
gtb.loadS('/Users/devesh/Observatory/StarCalc/Rotation_prescription/M015Z0V0.4Im0Cod22/M015Z0V0.4Im0Cod22.v0017621.gz',48)
