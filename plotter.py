import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat
import os

from read_of23_file import read_cfd_sim
from read_yLineUdata import read_yLineUdata
from read_reference import read_ref


nus = [5e-5, 8e-6, 1.515e-5, 1.515e-5]
hs  = [1.00, 1.00, 0.025000, 0.025000]

def u1u1(TKE):
    return 2/3 * TKE

def u2u2(TKE, V, x_2, nu_tau):
     return 2/3 * TKE - 2 * nu_tau * np.gradient(V, x_2)

def u1u2(U, x_2, nu_tau):
     return - nu_tau * np.gradient(U, x_2)


def plotter_same_mesh(modelpaths, models, refpath, case, H, nu):
     '''
     This function does some stuff
     '''
     fig, axs = plt.subplots(2,2)

     i=0
     while(i<len(modelpaths)):
          U1, U2, U3, nut, k, u_tau = read_cfd_sim(modelpaths[i])
          y = np.linspace(0,H,1000)
          print(np.shape(nut), np.shape(u_tau))

          y_plus = y * u_tau/nu

          axs[0,0].semilogx(y_plus, U1/u_tau, label=models[i])

          axs[0,1].semilogx(y_plus, u1u1(k)/u_tau**2,  label=models[i])

          axs[1,0].semilogx(y_plus, u2u2(k, U2, y, nut)/u_tau**2,  label=models[i])

          axs[1,1].semilogx(y_plus, -u1u2(U1, y, nut)/u_tau**2,  label=models[i])
     
          i+=1

     #printing reference data

     y_plus_ref, U_plus, uu_plus, vv_plus, uv_plus = read_ref(refpath)
     axs[0,0].semilogx(y_plus_ref, U_plus, label="ref", linestyle="--", color="#000000")
     axs[0,1].semilogx(y_plus_ref, uu_plus, label="ref", linestyle="--", color="#000000")
     axs[1,0].semilogx(y_plus_ref, vv_plus, label="ref", linestyle="--", color="#000000")
     axs[1,1].semilogx(y_plus_ref, -uv_plus, label="ref", linestyle="--", color="#000000")


     #labels
     axs[0,0].set_ylabel(r'$U_1^\plus$')
     axs[0,0].set_xlabel(r'$x_2^\plus$')
     axs[0,0].set_xlim(10**(-2), 10**(4))
     axs[0,0].set_ylim(bottom=0)
     axs[0,0].legend()

     axs[0,1].set_ylabel(r"$\overline{u_1' u_1'}^\plus$")
     axs[0,1].set_xlabel(r'$x_2^\plus$')
     axs[0,1].set_xlim(10**(-2), 10**(4))
     axs[0,1].set_ylim(bottom=0)
     axs[0,1].legend()

     axs[1,0].set_ylabel(r"$\overline{u_2' u_2'}^\plus$")
     axs[1,0].set_xlabel(r'$x_2^\plus$')
     axs[1,0].set_xlim(10**(-2), 10**(4))
     axs[1,0].set_ylim(bottom=0)
     axs[1,0].legend()

     axs[1,1].set_ylabel(r"$- \overline{u_1' u_2'}^\plus$")
     axs[1,1].set_xlabel(r'$x_2^\plus$')
     axs[1,1].set_xlim(10**(-2), 10**(4))
     axs[1,1].set_ylim(bottom=0)
     axs[1,1].legend()

     #room for aesthetic changes here, probably needed
     fig.suptitle(case)
     fig.set_size_inches(11.69, 8.27)
     fig.tight_layout()
     fig.savefig("grid1000_plots.svg")
     fig.show()

#testing function

paths_1 = ["DNS1000/kep", "DNS1000/kepRNG", "DNS1000/kw", "DNS1000/kwsst"] #, "DNS1000/spalart-allmaras"
models_1 = [r"$k$-$\epsilon$", 
            r"$k$-$\epsilon$ RNG",
            r"$k$-$\omega$", 
            r"$k$-$\omega$ SST",
            ]

ref_path_1 = "Reference data/DNS_1000_dataset.mat"
data_dict = loadmat(ref_path_1)
print(data_dict.keys())
plotter_same_mesh(paths_1, models_1, ref_path_1, r"$Re = 1000$", 2, nus[1])


def plotter_same_model(grid_model_paths, grids, models, case):

     fig, axs = plt.subplots(len(models))

     for i in len(models):
          a = 1

     fig.savefig(case + "__plots.svg")
     fig.show()
     fig.clear()
     return 0