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


def plotter_same_mesh(modelpaths: list[str], models: list[str], refpath: str, Re: int, H: float, mesh: int, nu: float):
     '''
     Creates and saves a figure containing 4 plots comparing RANS methods. 
     All plots include data from all given methods 
     as well as referance data. 
     Wall units are used in plots.
     small modification needed to be able to plot datasets with no k-file

     input:
     modelpaths: len=n, list of paths to data from all methods for a given Re
     models: len>=n, list of models to plot
     refpath: path to referance data
     Re: reynolds number
     H: total height of channel
     mesh: meshsize
     nu: viscosity
     '''
     fig, axs = plt.subplots(2,2)

     i=0
     while(i<len(modelpaths)):
     
          U1, U2, U3, nut, k, u_tau = read_cfd_sim(modelpaths[i])
          y = np.linspace(0,H, mesh)
          print(models[i])

          y_plus = y * u_tau/nu

          if np.array_equal(k, np.zeros_like(k)):
               axs[0,0].semilogx(y_plus, U1/u_tau, label=models[i])

          else:
               axs[0,0].semilogx(y_plus, U1/u_tau, label=models[i])

               axs[0,1].semilogx(y_plus, u1u1(k)/u_tau**2,  label=models[i])
          
               axs[1,0].semilogx(y_plus, u2u2(k, U2, y, nut)/u_tau**2,  label=models[i])

               axs[1,1].semilogx(y_plus, -u1u2(U1, y, nut)/u_tau**2,  label=models[i])
     
          i+=1

     #plotting reference data
     y_plus_ref, U_plus, uu_plus, vv_plus, uv_plus = read_ref(refpath)
     axs[0,0].semilogx(y_plus_ref, U_plus, label="ref", linestyle="--", color="#000000")
     axs[0,1].semilogx(y_plus_ref, uu_plus, label="ref", linestyle="--", color="#000000")
     axs[1,0].semilogx(y_plus_ref, vv_plus, label="ref", linestyle="--", color="#000000")
     axs[1,1].semilogx(y_plus_ref, -uv_plus, label="ref", linestyle="--", color="#000000")

     #labels
     axs[0,0].set_ylabel(r'$U_1^\plus$', fontsize=11)
     axs[0,0].set_xlabel(r'$x_2^\plus$', fontsize=11)
     axs[0,0].set_ylim(top = 30)
     
     axs[0,1].set_ylabel(r"$\overline{u_1' u_1'}^\plus$", fontsize=11)
     axs[0,1].set_xlabel(r'$x_2^\plus$', fontsize=11)

     axs[1,0].set_ylabel(r"$\overline{u_2' u_2'}^\plus$", fontsize=11)
     axs[1,0].set_xlabel(r'$x_2^\plus$', fontsize=11)

     axs[1,1].set_ylabel(r"$- \overline{u_1' u_2'}^\plus$", fontsize=11)
     axs[1,1].set_xlabel(r'$x_2^\plus$', fontsize=11)

     #limits, legends and grids
     for a in range(2):
          for b in range(2):
               axs[a,b].set_xlim(10**(-2), 10**(4))
               axs[a,b].set_ylim(bottom=0)
               axs[a,b].legend(title="Model")
               axs[a,b].grid()
               axs[a,b].grid(which="minor", axis="x")

     #aesthetics
     fig.suptitle(r"Re =" + str(Re))
     fig.set_size_inches(11.69, 8.27)
     fig.tight_layout()

     fig.savefig("Re" + str(Re) +"_grid" + str(mesh) +"_plots.svg")
     fig.show()

#creating plots
models_1 = [r"$k$-$\epsilon$", 
            r"$k$-$\epsilon$ RNG",
            r"$k$-$\omega$", 
            r"$k$-$\omega$ SST",
            "Spalart-Allmaras"] 

#creating plots for Re=1000
paths_1 = ["DNS1000/kep", "DNS1000/kepRNG", "DNS1000/kw", "DNS1000/kwsst", "DNS1000/spalart-allmaras"] #
ref_path_1 = "Reference data/DNS_1000_dataset.mat"
plotter_same_mesh(paths_1, models_1, ref_path_1, 1000, 2, 1000, nus[0])

#creating plots for Re=5200
paths_2 = ["DNS5200/kep", "DNS5200/kepRNG", "DNS5200/kw"] #"DNS5200/kwsst", "DNS5200/spalart-allmaras"
ref_path_2 = "Reference data/DNS_5200_dataset.mat"
#plotter_same_mesh(paths_2, models_1, ref_path_2, 5200, 2, 1000, nus[1])

#creating plots for Re=535
paths_3 = ["EXP535/kep", "EXP535/kepRNG", "EXP535/kw", "EXP535/kwsst"] #"EXP535/spalart-allmaras"
ref_path_3 = "Reference data/EXP_535_dataset.mat"
#plotter_same_mesh(paths_3, models_1, ref_path_3, 535, 0.05, 1000, nus[2])

#creating plots for Re=770
paths_4 = ["EXP770/kep", "EXP770/kepRNG", "EXP770/kw", "EXP770/kwsst"] #"EXP770/spalart-allmaras"
ref_path_4 = "Reference data/EXP_770_dataset.mat"
#plotter_same_mesh(paths_4, models_1, ref_path_4, 770, 0.05, 1000, nus[3])

def plotter_same_model(grid_paths: list[str], grids: list[int], modelpaths: list[str], models: list[str], refpath: str, Re: int, H: float, nu: float):
     '''
     Creates 10 plots comparing effect of meshsize for each RANS model.
     All plots include data from all given meshsizes 
     as well as referance data.

     input:
     grid_paths: len>=n, list of paths to data from all for a given Re
     grids: len=n, list of grids to plot
     refpath: path to referance data
     Re: reynolds number
     H: total height of channel
     mesh: meshsize
     nu: viscosity
     '''
     fig, axs = plt.subplots(len(models), 2)

     for i in range(len(grids)):
          if (i == len(grids) - 1):
               y_plus_ref, U_plus, uu_plus, vv_plus, uv_plus = read_ref(refpath)

          for j in range(len(models)):

               U1, U2, U3, nut, k, u_tau = read_cfd_sim(grid_paths[i]+"/"+modelpaths[j], length=grids[i])
               y = np.linspace(0,H, grids[i])

               y_plus = y * u_tau/nu

               axs[j,0].semilogx(y_plus, U1/u_tau, label=str(grids[i]))

               axs[j,1].semilogx(y_plus, -u1u2(U1, y, nut)/u_tau**2,  label=str(grids[i]))

               if (i == len(grids) - 1):
                    #modifing the looks of all graphs

                    axs[j,0].set_title(models[j])
                    axs[j,1].set_title(models[j])

                    axs[j,0].set_ylabel(r'$U_1^\plus$', fontsize=11)
                    axs[j,0].set_xlabel(r'$x_2^\plus$', fontsize=11)
                    axs[j,0].set_xlim(10**(-2), 10**(4))
                    axs[j,0].set_ylim(bottom=0)
                    axs[j,0].legend(title="Gridsize")
                    axs[j,0].grid()
                    axs[j,0].grid(which="minor", axis="x", linestyle="--")

                    axs[j,1].set_ylabel(r'$U_1^\plus$', fontsize=11)
                    axs[j,1].set_xlabel(r'$x_2^\plus$', fontsize=11)
                    axs[j,1].set_xlim(10**(-2), 10**(4))
                    axs[j,1].set_ylim(bottom=0)
                    axs[j,1].legend(title="Gridsize")
                    axs[j,1].grid()
                    axs[j,1].grid(which="minor", axis="x", linestyle="--")

                    #plotting referance data
                    axs[j,0].semilogx(y_plus_ref, U_plus, label="ref", linestyle="--", color="#000000")
                    axs[j,1].semilogx(y_plus_ref, -uv_plus, label="ref", linestyle="--", color="#000000")

     #making it look nice
     fig.suptitle(r"Re ="+str(Re))
     fig.set_size_inches(8.27, 11.69)
     fig.tight_layout()

     fig.savefig("Re" + str(Re) + "_vargrids_plots.svg")
     fig.show()
     return 0

#plotting for Re = 1000
paths_5 = ["DNS1000/kep", "DNS1000/kepRNG", "DNS1000/kw", "DNS1000/kwsst"] #, "DNS1000/spalart-allmaras"
grid_paths_1 = ["mesh/1000", "mesh/2000"] #"mesh/500"
grids_1 = [1000, 2000] #500
plotter_same_model(grid_paths_1, grids_1, paths_5, models_1, ref_path_1, 1000, 2, nus[0])