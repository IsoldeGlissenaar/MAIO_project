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
#fig.savefig('Figures/compare/WD-WS-PR-Nordenskioldbreen.png')

# =============================================================================
#%% Nordenskioldbreen
# =============================================================================

fig=plt.figure()
THUT = np.load('Nordenskioldbreen/T.npy')
SIN = np.load('Nordenskioldbreen/SIN.npy')
WS = np.load('Nordenskioldbreen/WS.npy')
THUT = T_nomask[:,2]
SIN = T_nomask[:,0]
WS = T_nomask[:,1]
dates=np.load('avgNordenskioldbreen/dates.npy')
dates_year=np.array(dates, dtype='datetime64[Y]')
dates_day=dates-dates_year
print(dates_day)

        
plt.scatter(WS, SIN, c=THUT, vmin=-10, vmax=12, cmap='seismic')
cbar = plt.colorbar()
cbar.set_label('Hut Temperature [$^\circ$ Celcius]', labelpad=-40, y=1.05, rotation=0)
plt.ylabel('Shortwave radiation In [W/m$^2$]')
plt.xlim(0,32)
plt.ylim(0,800)
plt.xlabel('Wind Speed [m/s]')
plt.title('Nordenskioldbreen')
plt.grid()
plt.show()
fig.savefig('Figures/compare/THUT-SIN-WS-Nordenskioldbreen.png')

# =============================================================================
#%% Nordenskioldbreen dT2m and dTsurf
# =============================================================================

fig=plt.figure()
T2M= np.load('Nordenskioldbreen/T2m.npy')
Tsurf = np.load('Nordenskioldbreen/Tsurf.npy')
WD = np.load('Nordenskioldbreen/WD.npy')
WS = np.load('Nordenskioldbreen/WS.npy')
        
plt.scatter(WD, WS, c=(T2M-Tsurf), vmin=-1, vmax=1, cmap='seismic')
cbar = plt.colorbar()
cbar.set_label('Temperature [$^\circ$]', labelpad=-40, y=1.05, rotation=0)
plt.xlabel('Wind Direction [$^\circ$]')
plt.ylabel('Wind Speed [m/s]')
plt.xlim(0,360)
plt.ylim(0,32)
plt.title('Nordenskioldbreen difference between T$_2m$ and T$_{surface}$')
plt.grid()
plt.show()
fig.savefig('Figures/compare/THUT-T2m-WD-WS-Nordenskioldbreen.png')

# =============================================================================
#%% Ulvebreen dT2m and dTsurf
# =============================================================================

fig=plt.figure()
T2M= np.load('Ulvebreen/THUT2m[K].npy')
Tsurf = np.load('Ulvebreen/TSURF[C].npy')
WD = np.load('Ulvebreen/HWDavg[deg].npy')
WS = np.load('Ulvebreen/HWSavg[m_s].npy')
        
plt.scatter(WD, WS, c=(T2M-Tsurf), vmin=-1, vmax=1, cmap='seismic')
cbar = plt.colorbar()
cbar.set_label('Temperature [$^\circ$]', labelpad=-40, y=1.05, rotation=0)
plt.xlabel('Wind Direction [$^\circ$]')
plt.ylabel('Wind Speed [m/s]')
plt.title('Ulvebreen difference between T$_2m$ and T$_{surface}$')
plt.xlim(0,360)
plt.ylim(0,26)
plt.grid()
plt.show()
fig.savefig('Figures/compare/THUT-T2m-WD-WS-Ulvebreen.png')


# =============================================================================
#%% Nordeskioldbreen WS - T2m
# =============================================================================

fig=plt.figure()
WS = T_nomask[:,2]
TN = T_nomask[:,0]
TU = T_nomask[:,1]

plt.scatter(TU, TN, c=WS, vmin=0, vmax=15, cmap='hsv')
cbar = plt.colorbar()
cbar.set_label('Wind Speed [m/s]', labelpad=-40, y=1.05, rotation=0)
plt.xlabel('Temperature Ulvebreen [$^\circ$C]')
plt.ylabel('Temperature Nordenskioldbreen [$^\circ$C]')
plt.title('Surface Temperature')
plt.grid()
plt.show()



