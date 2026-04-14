import sys
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

#DNS1000
#DNS5200
#EXP535
#EXP770

nus = [5e-5, 8e-6, 1.515e-5, 1.515e-5]
hs  = [1.00, 1.00, 0.025000, 0.025000]
models = ['spalart-allmaras','kep','kepRNG','kw','kwSST']

i=0 #BITCH HUSK Å ENDRE

nu = nus[i]  # Set your kinematic viscosity value
h  = hs[i]      # For pipes the length scale is typically your pipe diameter and half-height for channels



# Reading u_tau value
with open(r'\\wsl$\Ubuntu\home\fermilian\turb_openfoam_V25\wallShearStress.dat', 'r') as file:
    last_line = file.readlines()[-1]
    u_tau = np.sqrt(abs(float(last_line.split()[2].strip('()'))))

# Function to calculate Y+ and U+
def y_plus(y, u_tau, nu):
    return y * u_tau / nu   

def u_plus(u, u_tau):
    return u / u_tau

# Reading the data file
data = np.loadtxt(r'\\wsl$\Ubuntu\home\fermilian\turb_openfoam_V25\yLine_U_non_uniform.xy', delimiter='\t')
y_plus_values_1 = y_plus(data[:, 0], u_tau, nu)
u_plus_values_1 = u_plus(data[:, 1], u_tau)

Re_tau_OpenFOAM = round((u_tau*h)/(nu),0) # https://www.cfd-online.com/Forums/main/201822-viscous-reynolds-math-re_-tau-math-estimation-streak-size-tcf.html

print(Re_tau_OpenFOAM)

turbulence_model = models[1]

# Plotting
plt.figure(figsize=(10, 6))
plt.semilogx(y_plus_values_1, u_plus_values_1, marker='o', linestyle='-', label=f"OpenFOAM {turbulence_model} Re_tau = {Re_tau_OpenFOAM}")
plt.xlabel('y+')
plt.ylabel('U+')
plt.title('Comparison of y+ vs U+')
plt.legend()
plt.grid(True)

n=1


if n:
    data_to_save = np.column_stack((y_plus_values_1, u_plus_values_1))
    data_filename = f'dataset_OpenFOAM_{turbulence_model}_re_tau_{Re_tau_OpenFOAM}.txt'
    np.savetxt(data_filename, data_to_save, header='y_plus_values_1, u_plus_values_1', fmt='%f', delimiter=', ')

    # Save the plot
    filename = f'comparison_plot_{turbulence_model}_re_tau_{Re_tau_OpenFOAM}.png'
    plt.savefig(filename)
    plt.show()

