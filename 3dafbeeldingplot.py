# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:26:19 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 10),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
pylab.rcParams.update(params)
  
def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

# =============================================================================
#%% T2m
# =============================================================================
fig=plt.figure()
c = mcolors.ColorConverter().to_rgb
rvb = make_colormap([c('red'), c('violet'),
                     0.08, c('violet'), c('blue'), 
                     0.37, c('blue'), c('violet'), 
                     0.65, c('violet'), c('red') ])
N=272
array_dg = np.linspace(0, 10, N)
colors = np.linspace(0,N,N)
plt.scatter(T_nomask[:,1],T_nomask[:,0], c=colors, cmap=rvb)
plt.plot(T_nomask[:,0]+2.334,T_nomask[:,0], color='black',  linewidth=2.0)
plt.xlabel('Temperature Ulvebreen [ $^\circ$C]')
plt.ylabel('Temperature Nordenskioldbreen  [$^\circ$C]')
plt.title('Temperature 2 meter')
cbar = plt.colorbar()
cbar.ax.set_yticklabels(['26-08-2015','21-09-2015', '21-12-2015', '21-03-2016', '21-06-2016', '21-07-2016'])
cbar.set_label('date', rotation=360)
plt.grid()
plt.show()
fig.savefig('Figures/compare/T2mUlve-T2mNorde.png')

# =============================================================================
#%% Tsurface
# =============================================================================
fig=plt.figure()
c = mcolors.ColorConverter().to_rgb
rvb = make_colormap([c('red'), c('violet'),
                     0.08, c('violet'), c('blue'), 
                     0.37, c('blue'), c('violet'), 
                     0.65, c('violet'), c('red') ])
N=451
array_dg = np.linspace(0, 10, N)
colors = np.linspace(0,N,N)
plt.scatter(T_nomask[:,1],T_nomask[:,0], c=colors, cmap=rvb)
plt.plot(T_nomask[:,0]+2.334,T_nomask[:,0], color='black',  linewidth=2.0)
plt.xlabel('Temperature Ulvebreen [$^\circ$C]')
plt.ylabel('Temperature Nordenskioldbreen [$^\circ$C]')
plt.title('Surface Temperature')
cbar = plt.colorbar()
cbar.ax.set_yticklabels(['26-08-2015','21-09-2015', '21-12-2015', '21-03-2016', '21-06-2016', '21-07-2016'])
cbar.set_label('date', rotation=360)
plt.grid()
plt.show()
fig.savefig('Figures/compare/TsurfU-N.png')