############# Works !!!!!!!!!
############# Z0_1e1_0.999 model





import os
import numpy as np
import matplotlib.pyplot as plt

name = 'Z0_1e1_0.999'
path = '/Users/hermit/Observatory/StarCalc/SMS/'+name

# Directory where to find the vfiles
dir_list = os.listdir(path)

# Sort the dir_list in ascending order
dir_list.sort()

# Initialize the lists to store the values of I+, I-, and other quantities
I1_list=[]
I2_a_list=[]
I2_b_list=[]
I2_tot_list=[]
I0_list=[]
Mtot=[]

# Loop over the data files
for y in dir_list:
    # Retrieve only the vfiles
    if '.v' in y:
        # Retrieve only the vfiles finishing by 01
        if y.endswith("01"):
            print('current file:', y)
            pathfile = path+'/'+y

            data = np.loadtxt(pathfile, skiprows=1, max_rows=2)
            age = data[1]
            m = int(data[3])
            Mr = np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=49)
            beta = np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=30)
            P = 10**(np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=2))
            r = 10**(np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=4))
            rho = 10**(np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=14))

            # Calculate the integrals I+, I-, and I0 using the trapezoidal rule
            Mr = Mr*np.float64(1.9889e33) # Convert to grams
            Mtot.append(Mr[0]/np.float64(1.9889e33)) # Convert to solar masses
            G = np.float64(6.6743e-8)
            c = np.float64(2.9979e10)
            I1 = np.trapz(1.5*beta*P*r**2, r)
            I2_a = np.trapz(-3.*G**2/c**2*rho*Mr**2, r)
            I2_b = np.trapz(-4.*G/c**2*P*Mr*r, r)
            I0 = np.trapz(2./3.*r**2, Mr)

            # Append the values of I+, I-, and I0 to the corresponding lists
            I1_list.append(I1)
            I2_a_list.append(I2_a)
            I2_b_list.append(I2_b)
            I2_tot_list.append(I2_a+I2_b)
            I0_list.append(I0)

# Plot the values of I+ and I-
fig, ax = plt.subplots()
ax.plot(Mtot, np.array(I1_list) / np.array(I0_list), color='tab:blue', linewidth=2., label='I$_+$')
ax.plot(Mtot, np.array(I2_tot_list) / -np.array(I0_list), color='tab:red', linewidth=2., label='I$_-$')

# Modify the x-axis label and tick labels
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GR Integrals')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(loc='upper center', shadow=True, prop={'size': 8})
plt.show()


########## For wimps model

############# Works !!!!!!!!!
############# Z0_1e1_0.999 model





import os
import numpy as np
import matplotlib.pyplot as plt

name = '1e-3Msun_yr_Wimp_rho14_sig-40'
path = '/Users/hermit/Observatory/StarCalc/SMS_Wimp/' + name

# Directory where to find the vfiles
dir_list = os.listdir(path)

# Sort the dir_list in ascending order
dir_list.sort()

# Initialize the lists to store the values of I+, I-, and other quantities
I1_list=[]
I2_a_list=[]
I2_b_list=[]
I2_tot_list=[]
I0_list=[]
Mtot=[]

# Loop over the data files
for y in dir_list:
    # Retrieve only the vfiles
    if '.v' in y:
        # Retrieve only the vfiles finishing by 01
        if y.endswith("01"):
            print('current file:', y)
            pathfile = path+'/'+y

            data = np.loadtxt(pathfile, skiprows=1, max_rows=2)
            age = data[1]
            m = int(data[3])
            Mr = np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=49)
            beta = np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=30)
            P = 10**(np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=2))
            r = 10**(np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=4))
            rho = 10**(np.genfromtxt(pathfile, skip_header=3, max_rows=m, usecols=14))

            # Calculate the integrals I+, I-, and I0 using the trapezoidal rule
            Mr = Mr*np.float64(1.9889e33) # Convert to grams
            Mtot.append(Mr[0]/np.float64(1.9889e33)) # Convert to solar masses
            G = np.float64(6.6743e-8)
            c = np.float64(2.9979e10)
            I1 = np.trapz(1.5*beta*P*r**2, r)
            I2_a = np.trapz(-3.*G**2/c**2*rho*Mr**2, r)
            I2_b = np.trapz(-4.*G/c**2*P*Mr*r, r)
            I0 = np.trapz(2./3.*r**2, Mr)

            # Append the values of I+, I-, and I0 to the corresponding lists
            I1_list.append(I1)
            I2_a_list.append(I2_a)
            I2_b_list.append(I2_b)
            I2_tot_list.append(I2_a+I2_b)
            I0_list.append(I0)

# Plot the values of I+ and I-
fig, ax = plt.subplots()
ax.plot(Mtot, np.array(I1_list) / np.array(I0_list), color='tab:blue', linewidth=2., label='I$_+$')
ax.plot(Mtot, np.array(I2_tot_list) / -np.array(I0_list), color='tab:red', linewidth=2., label='I$_-$')

# Modify the x-axis label and tick labels
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GR Integrals')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(loc='upper center', shadow=True, prop={'size': 8})
plt.show()

############## Faster loading when using .gz files
###################### Works ++
import os
import numpy as np
import matplotlib.pyplot as plt
import gzip

name = '1e-3Msun_yr_Wimp'
path = '/Users/hermit/Observatory/StarCalc/SMS_Wimp/' + name

# Directory where to find the vfiles
dir_list = os.listdir(path)

# Sort the dir_list in ascending order
dir_list.sort()

# Initialize the lists to store the values of I+, I-, and other quantities
I1_list=[]
I2_a_list=[]
I2_b_list=[]
I2_tot_list=[]
I0_list=[]
Mtot=[]

# Loop over the data files
for y in dir_list:
    # Retrieve only the vfiles with the desired prefix and suffix
    if y.startswith("P002z0S0.v") and y.endswith("01.gz"):
        print('current file:', y)
        pathfile = path+'/'+y

        with gzip.open(pathfile, 'rt') as file:
            data1 = np.loadtxt(file, max_rows=1)
            data2 = np.loadtxt(file, max_rows=1)
            age = data2[0]
            m = int(data2[2])
            file.seek(0)  # Reset the file pointer to the beginning
            _ = file.readline()  # Skip the first row
            _ = file.readline()  # Skip the second row
            data_table = np.loadtxt(file, max_rows=m)
            Mr = data_table[:, 49]
            beta = data_table[:, 30]
            P = 10**(data_table[:, 2])
            r = 10**(data_table[:, 4])
            rho = 10**(data_table[:, 14])

        # Calculate the integrals I+, I-, and I0 using the trapezoidal rule
        Mr = Mr * np.float64(1.9889e33)  # Convert to grams
        Mtot.append(Mr[0] / np.float64(1.9889e33))  # Convert to solar masses
        G = np.float64(6.6743e-8)
        c = np.float64(2.9979e10)
        I1 = np.trapz(1.5 * beta * P * r ** 2, r)
        I2_a = np.trapz(-3. * G ** 2 / c ** 2 * rho * Mr ** 2, r)
        I2_b = np.trapz(-4. * G / c ** 2 * P * Mr * r, r)
        I0 = np.trapz(2. / 3. * r ** 2, Mr)

        # Append the values of I+, I-, and I0 to the corresponding lists
        I1_list.append(I1)
        I2_a_list.append(I2_a)
        I2_b_list.append(I2_b)
        I2_tot_list.append(I2_a + I2_b)
        I0_list.append(I0)

# Plot the values of I+ and I-
fig, ax = plt.subplots()
ax.plot(Mtot, np.array(I1_list) / np.array(I0_list), color='tab:blue', linewidth=2., label='I$_+$')
ax.plot(Mtot, np.array(I2_tot_list) / -np.array(I0_list), color='tab:red', linewidth=2., label='I$_-$')

# Modify the x-axis label and tick labels

ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GR Integrals')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(loc='upper center', shadow=True, prop={'size': 8})
plt.show()


############## Faster loading when using .vfiles
###################### Works ++
import os
import numpy as np
import matplotlib.pyplot as plt

name = '1e-1Msun_yr_Wimp_rho14_sig-40'
path = '/Users/hermit/Observatory/StarCalc/SMS_Wimp/' + name

# Directory where to find the vfiles
dir_list = os.listdir(path)

# Sort the dir_list in ascending order
dir_list.sort()

# Initialize the lists to store the values of I+, I-, and other quantities
I1_list=[]
I2_a_list=[]
I2_b_list=[]
I2_tot_list=[]
I0_list=[]
Mtot=[]

# Loop over the data files
for y in dir_list:
    # Retrieve only the vfiles with the desired prefix and suffix
    if y.startswith("P002z0S0.v") and y.endswith("01"):  # Changed here
        print('current file:', y)
        pathfile = path+'/'+y

        with open(pathfile, 'rt') as file:  # Changed here
            data1 = np.loadtxt(file, max_rows=1)
            data2 = np.loadtxt(file, max_rows=1)
            age = data2[0]
            m = int(data2[2])
            file.seek(0)  # Reset the file pointer to the beginning
            _ = file.readline()  # Skip the first row
            _ = file.readline()  # Skip the second row
            data_table = np.loadtxt(file, max_rows=m)
            Mr = data_table[:, 49]
            beta = data_table[:, 30]
            P = 10**(data_table[:, 2])
            r = 10**(data_table[:, 4])
            rho = 10**(data_table[:, 14])

        # Calculate the integrals I+, I-, and I0 using the trapezoidal rule
        Mr = Mr * np.float64(1.9889e33)  # Convert to grams
        Mtot.append(Mr[0] / np.float64(1.9889e33))  # Convert to solar masses
        G = np.float64(6.6743e-8)
        c = np.float64(2.9979e10)
        I1 = np.trapz(1.5 * beta * P * r ** 2, r)
        I2_a = np.trapz(-3. * G ** 2 / c ** 2 * rho * Mr ** 2, r)
        I2_b = np.trapz(-4. * G / c ** 2 * P * Mr * r, r)
        I0 = np.trapz(2. / 3. * r ** 2, Mr)

        # Append the values of I+, I-, and I0 to the corresponding lists
        I1_list.append(I1)
        I2_a_list.append(I2_a)
        I2_b_list.append(I2_b)
        I2_tot_list.append(I2_a + I2_b)
        I0_list.append(I0)

# Plot the values of I+ and I-
fig, ax = plt.subplots()
ax.plot(Mtot, np.array(I1_list) / np.array(I0_list), color='tab:blue', linewidth=2., label='I$_+$')
ax.plot(Mtot, np.array(I2_tot_list) / -np.array(I0_list), color='tab:red', linewidth=2., label='I$_-$')

# Modify the x-axis label and tick labels
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GR Integrals')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(loc='upper center', shadow=True, prop={'size': 8})
plt.show()


############## Faster loading when using .vfiles
###################### Works ++ for 1e-1 baryonic sms
import os
import numpy as np
import matplotlib.pyplot as plt
import gzip

name = '0.1Msun_yr_rho14_sig-40'
path = '/Users/hermit/Observatory/StarCalc/SMS_Wimps/' + name

# Directory where to find the vfiles
dir_list = os.listdir(path)

# Sort the dir_list in ascending order
dir_list.sort()

# Initialize the lists to store the values of I+, I-, and other quantities
I1_list=[]
I2_a_list=[]
I2_b_list=[]
I2_tot_list=[]
I0_list=[]
Mtot=[]

# Loop over the data files
for y in dir_list:
    # Retrieve only the vfiles with the desired prefix and suffix
    if y.startswith("P002z0S0.v") and y.endswith("01.gz"):
        print('current file:', y)
        pathfile = path+'/'+y

        with gzip.open(pathfile, 'rt') as file:
            data1 = np.loadtxt(file, max_rows=1)
            data2 = np.loadtxt(file, max_rows=1)
            age = data2[0]
            m = int(data2[2])
            file.seek(0)  # Reset the file pointer to the beginning
            _ = file.readline()  # Skip the first row
            _ = file.readline()  # Skip the second row
            data_table = np.loadtxt(file, max_rows=m)
            Mr = data_table[:, 49]
            beta = data_table[:, 30]
            P = 10**(data_table[:, 2])
            r = 10**(data_table[:, 4])
            rho = 10**(data_table[:, 14])

        # Calculate the integrals I+, I-, and I0 using the trapezoidal rule
        Mr = Mr * np.float64(1.9889e33)  # Convert to grams
        Mtot.append(Mr[0] / np.float64(1.9889e33))  # Convert to solar masses
        G = np.float64(6.6743e-8)
        c = np.float64(2.9979e10)
        I1 = np.trapz(1.5 * beta * P * r ** 2, r)
        I2_a = np.trapz(-3. * G ** 2 / c ** 2 * rho * Mr ** 2, r)
        I2_b = np.trapz(-4. * G / c ** 2 * P * Mr * r, r)
        I0 = np.trapz(2. / 3. * r ** 2, Mr)

        # Append the values of I+, I-, and I0 to the corresponding lists
        I1_list.append(I1)
        I2_a_list.append(I2_a)
        I2_b_list.append(I2_b)
        I2_tot_list.append(I2_a + I2_b)
        I0_list.append(I0)

# Plot the values of I+ and I-
fig, ax = plt.subplots()
ax.plot(Mtot, np.array(I1_list) / np.array(I0_list), color='tab:blue', linewidth=2., label='I$_+$')
ax.plot(Mtot, np.array(I2_tot_list) / -np.array(I0_list), color='tab:red', linewidth=2., label='I$_-$')

# Modify the x-axis label and tick labels

ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GR Integrals')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(loc='upper center', shadow=True, prop={'size': 8})
plt.show()


###############
###############
import os
import numpy as np
import matplotlib.pyplot as plt
import gzip

name = '0.1Msun_yr_rho14_sig-40'
path = '/Users/hermit/Observatory/StarCalc/SMS_Wimps/' + name

# Directory where to find the vfiles
dir_list = os.listdir(path)

# Sort the dir_list in ascending order
dir_list.sort()

# Initialize the lists to store the values of I+, I-, and other quantities
I1_list=[]
I2_a_list=[]
I2_b_list=[]
I2_tot_list=[]
I0_list=[]
Mtot=[]

# Constants
G = 6.6743e-8
c = 2.9979e10
Msol = 1.9889e33

# Loop over the data files
for y in dir_list:
    # Retrieve only the vfiles with the desired prefix and suffix
    if y.startswith("P002z0S0.v") and y.endswith("01.gz"):
        print('current file:', y)
        pathfile = path + '/' + y

        with gzip.open(pathfile, 'rt') as file:
            data1 = np.loadtxt(file, max_rows=1)
            data2 = np.loadtxt(file, max_rows=1)
            age = data2[0]
            m = int(data2[2])
            file.seek(0)  # Reset the file pointer to the beginning
            _ = file.readline()  # Skip the first row
            _ = file.readline()  # Skip the second row
            data_table = np.loadtxt(file, max_rows=m)
            Mr = data_table[:, 49]
            beta = data_table[:, 30]
            P = 10**(data_table[:, 2])
            r = 10**(data_table[:, 4])
            rho = 10**(data_table[:, 14])

        # Calculations
        Mtot.append(Mr[0])
        Mr = Mr * Msol
        I1 = np.trapz(1.5 * beta * P * r ** 2, r)
        I2_a = np.trapz(-3. * G ** 2 / c ** 2 * rho * Mr ** 2, r)
        I2_b = np.trapz(-4. * G / c ** 2 * P * Mr * r, r)
        I0 = np.trapz(2. / 3. * r ** 2, Mr)
        I1_list.append(I1)
        I2_a_list.append(I2_a)
        I2_b_list.append(I2_b)
        I2_tot_list.append(I2_a + I2_b)
        I0_list.append(I0)

# Plotting
fig, ax = plt.subplots()
ax.plot(Mtot, np.array(I1_list) / np.array(I0_list), color='tab:blue', linewidth=2., label='I$_+$')
ax.plot(Mtot, np.array(I2_tot_list) / -np.array(I0_list), color='tab:red', linewidth=2., label='I$_-$')
ax.legend(loc='upper center', shadow=True, prop={'size': 8})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('GR Integrals')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
