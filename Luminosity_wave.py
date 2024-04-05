############ Luminosity wave inside a 1 Msun/yr model at three different masses in early evolution##########

#########First at 20 Msun ###########


gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0017511',1)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0012871',2)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0007481',3)


Ltot1=6.234

Lr1=gtb.Get_Var('L',1)
Lr1=(Lr1*Ltot1)
gtb.Set_Var(Lr1,'Lnew',1,label="$L_r\ [L_\odot]$",category="energy")
gtb.defX('Mr')
gtb.Plot('Lnew')

gtb.keep_plot(True)
Ltot2=3.8315

Lr2=gtb.Get_Var('L',2)
Lr2=(Lr2*Ltot2)
gtb.Set_Var(Lr2,'Lnew',2,label="$L_r\ [L_\odot]$",category="energy")

gtb.Plot('Lnew')

gtb.keep_plot(True)
Ltot3=3.956

Lr3=gtb.Get_Var('L',3)
Lr3=(Lr3*Ltot3)
gtb.Set_Var(Lr3,'Lnew',3,label="$L_r\ [L_\odot]$",category="energy")

gtb.Plot('Lnew')


######################


gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0007481',1)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0012871',2)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0017511',3)
gtb.set_lineWidth(2.5)
gtb.defX('Mr')
gtb.Plot('L')










Ltot = 6.690447663E+39

Lr = 6.690447663E+39*(gtb.Get_Var('L',2))

gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0028051',1)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0024461',2)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0012781',3)

######### Useless #######
