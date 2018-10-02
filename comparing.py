# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:27:23 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt


listnorden=['Tsurf', 'T2m']
listulven= ['TSURF[C]', 'THUT2m[K]']

# =============================================================================
# Raw data
# =============================================================================
daten=np.load("Nordenskioldbreen/Date.npy")
dateu=np.load("Ulvebreen/Date.npy")

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

ulve={}
for k, i in enumerate(listulven):
        ulve["{0}".format(i)]=np.load("avgUlvebreen/"+i+".npy")   
        ulve["{0}day".format(i)]=np.load("avgUlvebreen/"+i+"day.npy")  
# =============================================================================
#  average   
# =============================================================================
norden={}
for k, j in enumerate(listnorden):
        norden["{0}".format(j)]=np.load("avgNordenskioldbreen/"+j+".npy")   
        norden["{0}day".format(j)]=np.load("avgNordenskioldbreen/"+j+"day.npy")   

for l in range(2):
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(norden[listnorden[l]+'day'], norden[listnorden[l]], '.', color='red', markersize = 2, label="nordenskioldbreen "+listnorden[l])
    plt.plot(ulve[listulven[l]+'day'], ulve[listulven[l]], '.', color='blue', markersize = 2, label="ulvebreen "+listulven[0])
    plt.title("Comparing average ulvebreen:"+listulven[l]+" and nordenskioldbreen:"+listnorden[l])
    plt.grid(True); plt.legend(); plt.show();# show plot on screen
    fig.savefig("Figures/compare/compare_avg_n"+listnorden[l]+"_u"+listulven[l]+".png")
