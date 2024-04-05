import GENEC_toolBox as gtb
import os
import glob
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Arguments for the extraction of stellar models data', \
                                 usage='ExtractData.py #starpath #starname' \
                                 '\n--------------------------------------------------------\n')

parser.add_argument('StarPath',help='Path to the directory containing the .wg file(s), with or without final "/"',type=str)
parser.add_argument('StarName',help='Name of the star(s), with commas between stars',type=str)

args = parser.parse_args()

dirpath = args.StarPath

base_dir = os.getcwd()

os.chdir(dirpath)

if ',' in args.StarName:
    filelist=args.StarName.split(',')
    for i,star in enumerate(filelist):
        if '.wg' not in star:
            filelist[i]+='.wg'
else:
    if '.wg' not in args.StarName:
        args.StarName+='.wg'
    filelist=list(reversed(sorted(glob.glob(args.StarName))))


print('File list: ',filelist,len(filelist),'files.')
if input('Continue? [y/n] ') in ['n','N','no','No']:
    exit()

N_same_mass=eval(input('For each mass, how many stars have that initial mass? '))

zero_threshold=eval(input('Under what value do you want to approximate quantities to 0? '))

print('Base directory: ',base_dir)
#GENERATE A TABLE WITHOUT OVERWRITING EXISTING ONE (IF APPLICABLE)
if len(glob.glob(base_dir+'/DataTable_Latex.dat'))!=0:
    DataTableName=input('DataTable_Latex.dat already exists in '+base_dir+', please specify name for the new table: ')
    if '.' not in DataTableName:
        DataTableName+='.dat'
else:
    DataTableName='DataTable_Latex.dat'
with open(base_dir+'/'+DataTableName,'w') as DataTable:
    DataTable.writelines('\\begin{landscape}\n')
    DataTable.writelines('\\begin{table}\n')
    DataTable.writelines('\\caption{Properties of the stellar models at the end of H-, He-, and C- burning phases}\n')
    DataTable.writelines('\\centering\n')
    DataTable.writelines('\\scalebox{0.7}{\\begin{tabular}{|ccccc|ccccccc|cccccccc|cccccccc|}\n')
    DataTable.writelines('\\hline\\hline\n')
    DataTable.writelines('\\multicolumn{5}{|c|}{} & \\multicolumn{7}{c|}{End of H-burning} & \\multicolumn{8}{c|}{End of He-burning} & \\multicolumn{8}{c|}{End of C-burning}\\\  \n')
    DataTable.writelines('Criterion & $M_\\text{ini}$ & $v_\\text{ini}$ & $v_\\text{tot}/v_\\text{crit}$ & $\\bar{v}_\\text{MS}$ & $\\tau_\\text{H}$ & $M$ & $v_\\text{surf}$ & $v_\\text{eq}/v_\\text{crit}$ & $Y_\\text{surf}$ & $\\text{N}/\\text{C}$ & $\\text{N}/\\text{O}$ & $\\tau_\\text{He}$ & $M$ & $v_\\text{surf}$ & $P_\\text{rot}$ & $\\Omega_\\text{C}/\\Omega_\\text{S}$ & $Y_\\text{surf}$ & $\\text{N}/\\text{C}$ & $\\text{N}/\\text{O}$ & $\\tau_\\text{C}$ & $M$ & $v_\\text{surf}$ & $P_\\text{rot}$ & $\\Omega_\\text{C}/\\Omega_\\text{S}$ & $Y_\\text{surf}$ & $\\text{N}/\\text{C}$ & $\\text{N}/\\text{O}$ \\\  \n')
    DataTable.writelines('& $M_{\\sun}$ && \\multicolumn{2}{c|}{km s$^{-1}$} & Myr & $M_{\\sun}$ & km s$^{-1}$ && \\multicolumn{3}{c|}{mass fract.} & Myr & $M_{\\sun}$ & km s$^{-1}$ & d & & \\multicolumn{3}{c|}{mass fract.} & kyr & $M_{\\sun}$ & km s$^{-1}$ & d & & \\multicolumn{3}{c|}{mass fract.}\\\ \n')
    DataTable.writelines('\\hline\n')

for i,file in enumerate(filelist):
    gtb.loadE(file,i)
    print('File loaded: '+file)
    #NC and NO are filled with 0 by GENEC_toolBox, so we redefine them
    gtb.Del_Var('NC',i)
    gtb.Set_Var(gtb.Get_Var('N14s',i)/gtb.Get_Var('C12s',i),'NC',i,label='N/C (mass frac.)')
    gtb.Del_Var('NO',i)
    gtb.Set_Var(gtb.Get_Var('N14s',i)/gtb.Get_Var('O16s',i),'NO',i,label='N/O (mass frac.)')
    gtb.Set_Var(gtb.Get_Var('Omega_cen',i)/gtb.Get_Var('Omega_surf',i),'OcOs',i)
    gtb.Del_Var('VVc',i)
    VVc = gtb.Get_Var('Vsurf',i)/gtb.Get_Var('Vcrit1',i)
    gtb.Set_Var(VVc,'VVc',i,label='$V/V_\mathrm{crit}$',category='rotation')
    gtb.Del_Var('period',i)
    period = 2*np.pi*gtb.Get_Var('R',i)*1.989e30/gtb.Get_Var('Omega_surf',i)
    gtb.Set_Var(period,'period',i,category='rotation')
    if 'Ledoux' in gtb.Get_Var('FileName',i).split('/')[-1]:
        criterion='Ledoux'
    else:
        criterion='Schwarzschild'
    if i%N_same_mass==0:
        M_ini=gtb.Get_Var('M',i)[0]
    else:
        M_ini=''

    MS_start=np.where(gtb.Get_Var('phase',i)=='H')[0][0]
    MS_end=np.where(gtb.Get_Var('phase',i)=='H')[0][-1]
    He_start=np.where(gtb.Get_Var('phase',i)=='He')[0][0]
    He_end=np.where(gtb.Get_Var('phase',i)=='He')[0][-1]
    v_ini=gtb.Get_Var('Vsurf',i)[MS_start]
    y=gtb.Get_Var('Vsurf',i)[MS_start:MS_end]
    x=gtb.Get_Var('t',i)[MS_start:MS_end]
    v_MS=np.trapz(y,x)/(x[-1]-x[0])
    VVc_ini=gtb.Get_Var('VVc',i)[MS_start]
    #END OF H BURNING
    tau_H=gtb.Get_Var('tau',i)[0]/1e6
    M_H=gtb.Get_Var('M',i)[MS_end]
    v_H=gtb.Get_Var('Vsurf',i)[MS_end]
    Y_H=gtb.Get_Var('He4s',i)[MS_end]
    NC_H=gtb.Get_Var('NC',i)[MS_end]
    NO_H=gtb.Get_Var('NO',i)[MS_end]
    VVc_H=gtb.Get_Var('VVc',i)[MS_end]
    #END OF He BURNING
    tau_He=gtb.Get_Var('tau',i)[1]/1e6
    M_He=gtb.Get_Var('M',i)[He_end]
    v_He=gtb.Get_Var('Vsurf',i)[He_end]
    Y_He=gtb.Get_Var('He4s',i)[He_end]
    NC_He=gtb.Get_Var('NC',i)[He_end]
    NO_He=gtb.Get_Var('NO',i)[He_end]
    Prot_He=gtb.Get_Var('period',i)[He_end]
    OcOs_He=gtb.Get_Var('OcOs',i)[He_end]
    #END OF C BURNING
    try:
        C_start=np.where(gtb.Get_Var('phase',i)=='C')[0][0]
        C_end=np.where(gtb.Get_Var('phase',i)=='C')[0][-1]
        tau_C=gtb.Get_Var('tau',i)[2]/1e3
        M_C=gtb.Get_Var('M',i)[C_end]
        v_C=gtb.Get_Var('Vsurf',i)[C_end]
        Y_C=gtb.Get_Var('He4s',i)[C_end]
        NC_C=gtb.Get_Var('NC',i)[C_end]
        NO_C=gtb.Get_Var('NO',i)[C_end]
        Prot_C=gtb.Get_Var('period',i)[C_end]
        OcOs_C=gtb.Get_Var('OcOs',i)[C_end]
        C_burn=True
    except:
        C_burn=False

    #FORMATTING EXPORT
    if C_burn:
        variable_list=[criterion,M_ini,v_ini,VVc_ini,v_MS,tau_H,M_H,v_H,VVc_H,Y_H,NC_H,NO_H,tau_He,M_He,v_He,Prot_He,OcOs_He,Y_He,NC_He,NO_He,tau_C,M_C,v_C,Prot_C,OcOs_C,Y_C,NC_C,NO_C]
    else:
        variable_list=[criterion,M_ini,v_ini,VVc_ini,v_MS,tau_H,M_H,v_H,VVc_H,Y_H,NC_H,NO_H,tau_He,M_He,v_He,Prot_He,Y_He,NC_He,NO_He]
    outstring=''
    print(len(variable_list),variable_list)
    for i,variable in enumerate(variable_list):
        print(i,variable)
        if variable==variable_list[0]:
            outstring+=variable+' & '
        else:
            if not variable==variable_list[-1]:
                if variable=='':
                    outstring+='& '
                elif variable<=zero_threshold:
                    outstring+='0 & '
                elif np.isnan(variable) or np.isinf(variable):
                    outstring+= '-- & '
                else:
                    if '{:.3f}'.format(variable)=='0.000':
                        stringvar='${:.3E}$ & '.format(variable)
                        outstring+=('${:.3E}$ & '.format(variable)).replace(stringvar[-8:-4],'\\times 10^{'+stringvar[-7:-4]+'}')
                    else:
                        if i in [1,2,3,4,6,7,8,13,14,21,22]:
                            outstring+='${:.1f}$ & '.format(variable)
                        elif i in [15,16,23,24]:
                            if variable<1000:
                                outstring+='${:.3f}$ & '.format(variable)
                            else:
                                stringvar='${:.3E}$ & '.format(variable)
                                outstring+=('${:.3E}$ & '.format(variable)).replace(stringvar[-8:-4],'\\times 10^{'+stringvar[-7:-4]+'}')
                        else:
                            outstring+='${:.3f}$ & '.format(variable)
            else:
                if variable<=zero_threshold:
                    outstring+='0 \\\ '
                elif np.isnan(variable) or np.isinf(variable):
                    outstring+= '-- & '
                else:
                    if '{:.3f}'.format(variable)=='0.000':
                        stringvar='${:.3E}$ \\\ '.format(variable)
                        outstring+=('${:.3E}$ \\\ '.format(variable)).replace(stringvar[-10:-6],'\\times 10^{'+stringvar[-9:-6]+'}')
                    else:
                        outstring+='${:.3f}$ \\\ '.format(variable)
    print('Line to add to the table:')
    print(outstring)
    with open(base_dir+'tempDataTable.dat','w') as tempout:
        tempout.write(outstring)

    #APPEND TO EXISTING TABLE
    with open(base_dir+'/'+DataTableName,'a') as DataTable:
        DataTable.writelines(outstring+'\n')

    os.remove(base_dir+'tempDataTable.dat')

#REMOVE REDUNDANT INFORMATION


#FORMAT THE END OF THE TABLE
with open(base_dir+'/'+DataTableName,'a') as DataTable:
    DataTable.writelines('\\hline \n')
    DataTable.writelines('\\end{tabular}} \n')
    DataTable.writelines('\\label{TabListModels} \n')
    DataTable.writelines('\\end{table} \n')
    DataTable.writelines('\\end{landscape} \n')
