# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:29:26 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

data=[0, 3, 0.2, np.nan, 40293,0, 3, 0.2, np.nan, 40293,0, 3, 0.2, np.nan, 40293]
print(np.all(np.isnan(data)))

nonan=6
for uur in range(len(data)):
    if m.isnan(data[uur]): nonan=nonan-1
    print(uur, nonan)
