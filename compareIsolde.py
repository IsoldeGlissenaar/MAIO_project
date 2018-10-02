# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:30:22 2018

@author: Isolde
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

T_ulve=np.load("Ulvebreen/THUTavg[C].npy")
T_ulveday=np.load("Ulvebreen/Date.npy")

T_norden=np.load("Nordenskioldbreen/Tsurf.npy")
T_nordenday=np.load("Nordenskioldbreen/Date.npy")

plt.plot(T_ulveday,T_ulve,'.')
plt.plot(T_nordenday,T_norden,'.')
plt.show()

minday = np.min(T_ulveday)
maxday = np.max(T_nordenday)

minnord = np.where(T_nordenday == minday)[0][0]
maxulv  = np.where(T_ulveday   == maxday)[0][0]

T_ulve_c =  T_ulve[:maxulv]
T_ulveday_c = T_ulveday[:maxulv]

T_norden_c =  T_norden[minnord:]
T_nordenday_c = T_nordenday[minnord:]

plt.plot(T_ulveday_c,T_ulve_c,'.')
plt.plot(T_nordenday_c,T_norden_c,'.')
plt.show()


#%%
dates = np.arange('2015-08-22T17:00:00', '2016-12-03T17:00:00', dtype='datetime64[30m]')

#miss_ulv = list(set(T_nordenday_c)-set(T_ulveday_c))
#miss_nord = list(set(T_ulveday_c)-set(T_nordenday_c))

T_c = np.empty([len(dates),2])
T_c[:,:] = np.nan

for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc = np.where(T_nordenday_c == dates[i])[0][0]
        T_c[i,0] = T_norden_c[loc]
    except IndexError: # catch the error
        continue
    
for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc_ulv  = np.where(T_ulveday_c == dates[i])[0][0]
        T_c[i,1] = T_ulve_c[loc_ulv]
    except IndexError: # catch the error
        continue

plt.plot(dates, T_c[:,0],'.')
plt.plot(dates, T_c[:,1],'.')
plt.show()




#pca = PCA()

