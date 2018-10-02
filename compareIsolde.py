# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:30:22 2018

@author: Isolde
"""

import numpy as np
import matplotlib.pyplot as plt

T_ulve=np.load("avgUlvebreen/THUTavg[C].npy")
T_ulveday=np.load("avgUlvebreen/THUTavg[C]day.npy")

T_norden=np.load("avgNordenskioldbreen/Tsurf.npy")
T_nordenday=np.load("avgNordenskioldbreen/Tsurfday.npy")

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