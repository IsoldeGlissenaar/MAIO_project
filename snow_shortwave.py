# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:35:46 2018

@author: Isolde
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

Sin_U = np.load("sneeuwhoogte/Ulve/NRUavg[W_m2].npy")
Sin_Uday = np.load("sneeuwhoogte/Ulve/NRUavg[W_m2]day.npy")
Sout_U = np.load("sneeuwhoogte/Ulve/NRLavg[W_m2].npy")
Sout_Uday = np.load("sneeuwhoogte/Ulve/NRLavg[W_m2]day.npy")
SSH_U = np.load("sneeuwhoogte/Ulve/SSH[m].npy")
SSH_Uday = np.load("sneeuwhoogte/Ulve/SSH[m]day.npy")

#%%
minday = Sin_Uday[0]
maxday = Sin_Uday[-1]

dates = np.arange(minday, maxday, dtype='datetime64[1D]')

T_c = np.empty([len(dates),2])
T_c[:,:] = np.nan   
    

for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc = np.where((Sin_Uday == dates[i]))[0][0]
        T_c[i,0] = Sin_U[loc]
    except IndexError: # catch the error
        continue

for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc_ulv  = np.where(Sout_Uday == dates[i])[0][0]
        T_c[i,1] = Sout_U[loc_ulv]
    except IndexError: # catch the error
        continue
#%%

albedo = np.zeros((len(T_c[:,0])))
for i in range (len(T_c[:,0])):
    if T_c[i,0]<10:
        albedo[i] = np.nan
    else:
        albedo[i] = T_c[i,1]/T_c[i,0]






params = {'legend.fontsize': 'large',
          'figure.figsize': (8, 4),
         'axes.labelsize': 'large',
         'axes.titlesize':'large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

#fig, ax1 = plt.subplots()
#plt.scatter(Sin_Uday,Sin_U , label='Sin', s=10, c='r')
#plt.scatter(Sout_Uday,Sout_U, label='Sout', s=10, c='b')
#ax1.set_xlabel('date')
## Make the y-axis label, ticks and tick labels match the line color.
#ax1.set_ylabel('radiation [W/m2]')
#ax1.tick_params('y')

fig, ax1 = plt.subplots()
plt.scatter(dates , albedo , label='albedo', s=10, c='r')
ax1.set_xlabel('date')
ax1.set_ylim([0,1])
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('radiation [W/m2]')
ax1.tick_params('y')

ax2 = ax1.twinx()
plt.scatter(SSH_Uday,SSH_U, label='SSH',  s=10, c= 'y')
ax2.set_ylabel('snow height [m]')
ax2.tick_params('y')

fig.tight_layout()
fig.legend()
#plt.savefig('Figures/Sout_ssh.png')
plt.show()


