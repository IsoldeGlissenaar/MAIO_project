# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:27:23 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt


listnorden=['Tsurf', 'T2m']
listulven= ['TSURF[C]', 'THUT2m[K]']

daten=np.load("Nordenskioldbreen/Date.npy")
dateu=np.load("Ulvebreen/Date.npy")

'''
Tsurf 		= Surface temperature derived from outgoing longwave radiation
T2m 		= 2m temperature based on T and H

TC1avg[C]		= THERMOCOUPLE 1 
TC2avg[C]		= THERMOCOUPLE 2

TSURF[C]		= Surface temperature derived from outgoing longwave radiation
TSTR1[C]		= SNOW TEMPERATURE STRING 1
TSTR2[C]		= SNOW TEMPERATURE STRING 2 
TSTR3[C]		= SNOW TEMPERATURE STRING 3
TSTR4[C]		= SNOW TEMPERATURE STRING 4
TSTR5[C]		= SNOW TEMPERATURE STRING 5
TSTR6[C]		= SNOW TEMPERATURE STRING 6
TSTR7[C]		= SNOW TEMPERATURE STRING 7
TSTR8[C]		= SNOW TEMPERATURE STRING 8
THUTavg[C]		= MAIN HUT TEMPERATURE = Temperature head Transmitter (HUT)
THUT2m[K]		= 2m temperature based on THUTavg and SSH
THUTpot[K]		= potential temperature based on THUTavg and BAP
'''

ulve={}
for k, i in enumerate(listulven):
        ulve["{0}".format(i)]=np.load("Ulvebreen/"+i+".npy")   

norden={}
for k, j in enumerate(listnorden):
        norden["{0}".format(j)]=np.load("Nordenskioldbreen/"+j+".npy")   

for l in range(2):
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(daten, norden[listnorden[l]], '.', color='red', markersize = 2, label="nordenskioldbreen "+listnorden[l])
    plt.plot(dateu, ulve[listulven[l]], '.', color='blue', markersize = 2, label="ulvebreen "+listulven[0])
    plt.title("Comparing ulvebreen:"+listulven[l]+" and nordenskioldbreen:"+listnorden[l])
    plt.grid(True); plt.legend(); plt.show();# show plot on screen
    fig.savefig("Figures/compare/compare_n"+listnorden[l]+"_u"+listulven[l]+".png")

