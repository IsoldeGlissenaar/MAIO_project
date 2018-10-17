# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:05:26 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (12, 10),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
pylab.rcParams.update(params)

# =============================================================================
#%% Ulvebreen
# =============================================================================
fig=plt.figure()
PR = np.load('Ulvebreen/BAP[hPa].npy')
WD = np.load('Ulvebreen/HWDavg[deg].npy')
WS = np.load('Ulvebreen/HWSavg[m_s].npy')

plt.scatter(WD, WS, c=PR, cmap='seismic')
cbar = plt.colorbar()
cbar.set_label('Pressure [hPa]', labelpad=-40, y=1.05, rotation=0)
plt.xlabel('Wind Direction [$^\circ$]')
plt.ylabel('Wind Speed [m/s]')
plt.xlim(0,360)
plt.ylim(0,27)
plt.title('Ulvebreen')
plt.grid()
plt.show()
fig.savefig('Figures/compare/WD-WS-PR-Ulvebreen.png')

# =============================================================================
#%% Nordeskioldbreen
# =============================================================================

fig=plt.figure()
PR = np.load('Nordenskioldbreen/P.npy')
WD = np.load('Nordenskioldbreen/WD.npy')
WS = np.load('Nordenskioldbreen/WS.npy')

plt.scatter(WD, WS, c=PR, cmap='seismic')
cbar = plt.colorbar()
cbar.set_label('Pressure [hPa]', labelpad=-40, y=1.05, rotation=0)
plt.xlabel('Wind Direction [$^\circ$]')
plt.ylabel('Wind Speed [m/s]')
plt.xlim(0,360)
plt.ylim(0,32)
plt.title('Nordenskioldbreen')
plt.grid()
plt.show()
fig.savefig('Figures/compare/WD-WS-PR-Nordenskioldbreen.png')

# =============================================================================
#%% Ulvebreen
# =============================================================================
fig=plt.figure()
DT = np.load('Ulvebreen/Date.npy')
Lin = np.load('Ulvebreen/THUT2m[K].npy')
#RH = np.load('Ulvebreen/RHWavg[%].npy')
RH = np.load('Ulvebreen/SPECHUM[g_kg].npy')

plt.scatter(DT, Lin, c=RH, cmap='seismic')
cbar = plt.colorbar()
#cbar.set_label('Pressure [hPa]', labelpad=-40, y=1.05, rotation=0)
#plt.xlabel('Wind Direction [$^\circ$]')
#plt.ylabel('Wind Speed [m/s]')
plt.title('Ulvebreen')
plt.grid()
plt.show()
#fig.savefig('Figures/compare/WD-WS-PR-Ulvebreen.png')

