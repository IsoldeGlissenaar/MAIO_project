# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:13:14 2018

@author: Isolde
"""


import numpy as np
import matplotlib.pyplot as plt

direc = ""
data_1 = "ADW[m]" 
data_2 = "SSH[m]"

T_ulve=np.load(direc+"avgUlvebreen/"+data_1+".npy")
T_ulveday=np.load(direc+"avgUlvebreen/"+data_1+"day.npy")

T_norden=np.load(direc+"avgUlvebreen/"+data_2+".npy")
T_nordenday=np.load(direc+"avgUlvebreen/"+data_2+"day.npy")


''' This code cuts the data to the overlapping length'''



fig, ax1 = plt.subplots()
ax1.scatter(T_ulveday, T_ulve, label='ice' , s=10, c='b') #norden
ax1.set_xlabel('date')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('ice')
ax1.tick_params('y')

ax2 = ax1.twinx()
ax2.scatter(T_nordenday, T_norden, label= 'snow', s=10, c='g') #ulve
ax2.set_ylabel('snow')
ax2.tick_params('y')

fig.tight_layout()
fig.legend()
#plt.savefig('Figures/Sout_ssh.png')
plt.show()
