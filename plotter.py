import numpy as np
import matplotlib.pyplot as plt

from read_of23_file import read_cfd_sim

def u1u1(TKE):
    return 2/3 * TKE

def u2u2(TKE, V, x_2, nu_tau):
     return 2/3 * TKE - 2 * nu_tau * np.gradient(V, x_2)

def u1u2(U, x_2, nu_tau):
     return - nu_tau * np.gradient(U, x_2)


def plotter_same_mesh(modelpaths, models, case):
     '''
     This function does some stuff
     '''
     fig, axs = plt.subplots(2,2)
     for i in range(len(modelpaths)):
          U1, U2, U3, nut, u_tau = read_cfd_sim(modelpaths[i])
          y = 0
          k = 0

          y_plus = y * u_tau/nut

          axs[0,0].plot(U1/u_tau, y_plus, label=models[i])

          axs[0,1].plot(u1u1(k)/u_tau**2, y_plus, label=models[i])

          axs[1,0].plot(u2u2(k)/u_tau**2, y_plus, label=models[i])

          axs[1,1].plot(u1u2(U1, y, nut)/u_tau**2, y_plus, label=models[i])


     #labels
     axs[0,0].setylabel(r'$U_1^\plus$')
     axs[0,0].setxlabel(r'$x_2^\plus$')
     axs[0,0].legend()
     axs[0,1].setylabel(r"$\overline{u_1' u_1'}^\plus$")
     axs[0,1].setxlabel(r'$x_2^\plus$')
     axs[0,1].legend()
     axs[1,0].setylabel(r"$\overline{u_2' u_2'}^\plus$")
     axs[1,0].setxlabel(r'$x_2^\plus$')
     axs[1,0].legend()
     axs[1,1].setylabel(r"$\overline{u_1' u_2'}^\plus$")
     axs[1,1].setxlabel(r'$x_2^\plus$')
     axs[1,1].legend()

     #room for aesthetic changes here

     fig.savefig(case + "_plots.py")
     fig.show()
     return 0


def plotter_same_model(gridpaths, grids):
     return 0