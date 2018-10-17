# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:24:35 2018

@author: d-vz
"""

TU = np.load('avgUlvebreen/THUT2m[K].npy')
TN = np.load('avgNordenskioldbreen/T2m.npy')

import scipy.stats

c=scipy.stats.ttest_ind(TU, TN+2.334)
print(np.mean(TU))
print(np.mean(TN+2.334))
print(c)