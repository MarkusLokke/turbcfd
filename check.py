import sys
import numpy as np

case  = ['DNS1000','DNS5200','EXP535','EXP770']
nu   = [ 5e-5,     8e-6,    1.515e-5, 1.515e-5]
h    = [ 1.00,     1.00,    0.025000, 0.025000]
model = ['kep', 'kepRNG','kw','kwsst','spalart-allmaras']



for i in range(4):
    for j in range(5):

        with open(f'{case[i]}/{model[j]}/wallShearStress.dat', 'r') as file:
            last_line = file.readlines()[-1]
            u_tau = np.sqrt(abs(float(last_line.split()[2].strip('()'))))

        Re_tau_OpenFOAM = round((u_tau*h[i])/(nu[i]),0) # https://www.cfd-online.com/Forums/main/201822-viscous-reynolds-math-re_-tau-math-estimation-streak-size-tcf.html

        print(Re_tau_OpenFOAM)
    print('-')