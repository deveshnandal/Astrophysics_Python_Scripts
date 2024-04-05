import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rc('text',usetex=True)
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern'],'size':14})
matplotlib.rcParams['text.latex.preamble']=r"\usepackage{amsmath}"
matplotlib.rcParams['xtick.top']=True
matplotlib.rcParams['ytick.right']=True
matplotlib.rcParams['ytick.minor.visible']=True
matplotlib.rcParams['xtick.minor.visible']=True
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.colors as colors

%matplotlib qt
columnwidth=240
pagewidth=513

def get_figsize(width,wf=1,hf=(5.**0.5-1.0)/2.0):
    '''
    BEAUTIFUL FIGURES

    Usage: fig,ax=plt.subplots(i,j,figsize=get_figsize(width,wf=1.0,hf=.5))
    Get the width in point from \the\textwidth or \the\pagewidth in the latex document
    '''
    fig_width_pt=width*wf
    inches_per_pt=1.0/72.27
    fig_width=fig_width_pt*inches_per_pt
    fig_height=fig_width*hf
    return [fig_width,fig_height]

L_sun = 3.827e26
R_sun = 696340e3
xmin = 5.5
xmax = 3.2
ymin = 0
ymax = 11

exes = [4.1293, 4.2790, 4.3790, 4.4521, 4.5563, 4.6303, 4.6788, 4.7306, 4.7942, 4.8633, 4.8983, 4.9361, 4.9604, 4.9773]
whys = [1.4694, 2.1333, 2.5751, 2.9016, 3.3746, 3.7150, 4.0754, 4.3346, 4.6600, 5.0928, 5.3706, 5.7251, 5.9992, 6.2475]
ZAMS = [2, 3, 4, 5, 7, 9, 12, 15, 20, 30, 40, 60, 85, 120]
logT = np.linspace(xmin,xmax,100)
logL = np.linspace(ymin,ymax,100)
R = np.array([[np.sqrt((10**Li)*L_sun/(4*np.pi*5.67e-8*(10**Ti)**4)) for Li in logL] for Ti in logT]) / R_sun
plt.figure(figsize=get_figsize(pagewidth,wf=1.0,hf=1))
plt.contourf(logT, logL, np.log10(R), alpha=.7, cmap='rainbow', levels=np.log10([1e-4,1e-3,1e-2,1e-1,1,10,100,1000,1e4,1e5,1e6,1e7]))
for model, linestyle in zip(['1e-0','1e-1','1e-2','1e-3','1e-4','1e-5','1e-6','CH','Yoshida'],3*['-','--',':','-.']):
    try:
        print(globals()['{}_logT'.format(model)])
    except:
        globals()['{}_logT'.format(model)] = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/WG_files/{}.wg'.format(model)))[4]
        globals()['{}_logL'.format(model)] = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/WG_files/{}.wg'.format(model)))[3]
    plt.plot(globals()['{}_logT'.format(model)],globals()['{}_logL'.format(model)],c='k', ls=linestyle)
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.scatter(exes, whys, s=10)
    [plt.text(exes[i],whys[i],s='${:n}M_\\odot$'.format(ZAMS[i]),ha = "right",va = "top", fontsize = 6) for i in range(len(exes))]
plt.xlabel("$\\log{T_{\\rm eff}~\\rm{[K]}}$")
plt.ylabel("$\\log{L~\\rm{[L_\\odot]}}$")
plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()


np.max(R)

##################################
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rc('text',usetex=True)
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern'],'size':14})
matplotlib.rcParams['text.latex.preamble']=r"\usepackage{amsmath}"
matplotlib.rcParams['xtick.top']=True
matplotlib.rcParams['ytick.right']=True
matplotlib.rcParams['ytick.minor.visible']=True
matplotlib.rcParams['xtick.minor.visible']=True
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.colors as colors

%matplotlib qt
columnwidth=240
pagewidth=513

def get_figsize(width,wf=1,hf=(5.**0.5-1.0)/2.0):
    '''
    BEAUTIFUL FIGURES

    Usage: fig,ax=plt.subplots(i,j,figsize=get_figsize(width,wf=1.0,hf=.5))
    Get the width in point from \the\textwidth or \the\pagewidth in the latex document
    '''
    fig_width_pt=width*wf
    inches_per_pt=1.0/72.27
    fig_width=fig_width_pt*inches_per_pt
    fig_height=fig_width*hf
    return [fig_width,fig_height]

L_sun = 3.827e26
R_sun = 696340e3
xmin = 5.5
xmax = 3.2
ymin = 0
ymax = 11

#exes = [4.1293, 4.2790, 4.3790, 4.4521, 4.5563, 4.6303, 4.6788, 4.7306, 4.7942, 4.8633, 4.8983, 4.9361, 4.9604, 4.9773]
#whys = [1.4694, 2.1333, 2.5751, 2.9016, 3.3746, 3.7150, 4.0754, 4.3346, 4.6600, 5.0928, 5.3706, 5.7251, 5.9992, 6.2475]
#ZAMS = [2, 3, 4, 5, 7, 9, 12, 15, 20, 30, 40, 60, 85, 120]
logT = np.linspace(xmin,xmax,100)
logL = np.linspace(ymin,ymax,100)
R = np.array([[np.sqrt((10**Li)*L_sun/(4*np.pi*5.67e-8*(10**Ti)**4)) for Li in logL] for Ti in logT]) / R_sun
plt.figure(figsize=get_figsize(pagewidth,wf=1.0,hf=1))
plt.contourf(logT, logL, np.log10(R), alpha=.7, cmap='cubehelix', levels=np.log10([1e-4,1e-3,1e-2,1e-1,1,10,100,1000,1e4,1e5,1e6,1e7]))
for model, linestyle in zip(['1e1','1e-0','1e-1','1e-2','1e-3'],2*['-','--',':','-.']):
    try:
        print(globals()['{}_logT'.format(model)])
    except:
        globals()['{}_logT'.format(model)] = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/WG_files_2/{}.wg'.format(model)))[4]
        globals()['{}_logL'.format(model)] = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/WG_files_2/{}.wg'.format(model)))[3]
    plt.plot(globals()['{}_logT'.format(model)],globals()['{}_logL'.format(model)],c='k', ls=linestyle)
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
#    plt.scatter(exes, whys, s=10)
#    [plt.text(exes[i],whys[i],s='${:n}M_\\odot$'.format(ZAMS[i]),ha = "right",va = "top", fontsize = 6) for i in range(len(exes))]
plt.xlabel("$\\log{T_{\\rm eff}~\\rm{[K]}}$")
plt.ylabel("$\\log{L~\\rm{[L_\\odot]}}$")
plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()

#######gpt 3.5

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 14})
matplotlib.rcParams['text.latex.preamble'] = r"\usepackage{amsmath}"
matplotlib.rcParams['xtick.top'] = True
matplotlib.rcParams['ytick.right'] = True
matplotlib.rcParams['ytick.minor.visible'] = True
matplotlib.rcParams['xtick.minor.visible'] = True
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.colors as colors

%matplotlib qt
columnwidth = 240
pagewidth = 513

def get_figsize(width, wf=1, hf=(5.**0.5-1.0)/2.0):
    '''
    BEAUTIFUL FIGURES

    Usage: fig,ax=plt.subplots(i,j,figsize=get_figsize(width,wf=1.0,hf=.5))
    Get the width in point from \the\textwidth or \the\pagewidth in the latex document
    '''
    fig_width_pt = width*wf
    inches_per_pt = 1.0/72.27
    fig_width = fig_width_pt*inches_per_pt
    fig_height = fig_width*hf
    return [fig_width, fig_height]

L_sun = 3.827e26
R_sun = 696340e3
xmin = 5.5
xmax = 3.2
ymin = 0
ymax = 11

logT = np.linspace(xmin, xmax, 100)
logL = np.linspace(ymin, ymax, 100)

# Calculate radii
R = np.array([[np.sqrt((10**Li)*L_sun/(4*np.pi*5.67e-8*(10**Ti)**4)) for Li in logL] for Ti in logT]) / R_sun

# Define contour levels
levels = np.log10([1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 1e4, 1e5, 1e6, 1e7])

# Define colormap and normalization
cmap = 'cubehelix'
norm = colors.Normalize(vmin=np.min(levels), vmax=np.max(levels))

# Create figure
fig, ax = plt.subplots(figsize=get_figsize(pagewidth, wf=1.0, hf=1))
contourf = ax.contourf(logT, logL, np.log10(R), alpha=.7, cmap=cmap, levels=levels, norm=norm)

# Add colorbar
cbar = fig.colorbar(contourf)
cbar.set_label(r"$\log_{10}\left(\frac{R}{R_{\odot}}\right)$")

# Plot isochrones
for model, linestyle in zip(['1e1', '1e-0', '1e-1', '1e-2', '1e-3'], 2*['-', '--', ':', '-.']):
    try:
        print(globals()['{}_logT'.format(model)])
    except:
        globals()['{}_logT'.format(model)] = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/WG_files_2/{}.wg'.format(model)))[4]
        globals()['{}_logL'.format(model)] = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/WG_files_2/{}.wg'.format(model)))[3]

    # Plot isochrone
    plt.plot(globals()['{}_logT'.format(model)],globals()['{}_logL'.format(model)], c='k', ls=linestyle)
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)

plt.xlabel(r"$\log_{10}(T_{\rm eff}\,\mathrm{[K]})$")
plt.ylabel(r"$\log_{10}(L/\mathrm{L_{\odot}})$")
plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)

plt.show()
