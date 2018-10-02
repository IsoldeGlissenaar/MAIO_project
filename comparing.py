# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:27:23 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt

#listnorden=['WD', 'WS', 'WSm', 'Sin', 'Sout', 'Lin', 'Lout', 'Trad', 'Tsurf', 'Tpot', 'T', 'T2m', 'q', 'RH', 'P', 'H1', 'Q1', 'H2', 'Q2', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'A1', 'A2', 'Bat', 'Tint', 'Stoa', 'Qual', 'AWSid']
#listulven= ['TC1avg[C]', 'TC2avg[C]', 'TSURF[C]', 'TSTR1[C]', 'TSTR2[C]', 'TSTR3[C]', 'TSTR4[C]', 'TSTR5[C]', 'TSTR6[C]', 'TSTR7[C]', 'TSTR8[C]', 'THUTavg[C]', 'THUT2m[K]', 'THUTpot[K]', 'RHWavg[%]', 'SPECHUM[g_kg]', 'HWSavg[m_s]', 'HWSmax[m_s]', 'HWDavg[deg]', 'Stoa[W_m2]', 'NRUavg[W_m2]', 'NRLavg[W_m2]', 'NRIUavg[W_m2]', 'NRILavg[W_m2]', 'NRTavg[C]', 'BAP[hPa]', 'SSH[m]', 'ADW[m]', 'MCH[deg]', 'TILTX[deg]', 'TILTY[deg]', 'LON[deg]', 'LAT[deg]', 'HMSL[m]', 'VBAT[V]', 'LBUT[days]', 'Qual', 'AWSid']


listnorden=['Tsurf', 'T2m', 'RH', "WD", ]
listulven= ['TSURF[C]', 'THUT2m[K]', 'RHWavg[%]', 'HWDavg[deg]']

# =============================================================================
# Raw data
# =============================================================================
daten=np.load("Nordenskioldbreen/Date.npy")
dateu=np.load("Ulvebreen/Date.npy")

ulve={}
for k, i in enumerate(listulven):
        print(k)
        ulve["{0}".format(i)]=np.load("Ulvebreen/"+i+".npy")   

norden={}
for k, j in enumerate(listnorden):
        norden["{0}".format(j)]=np.load("Nordenskioldbreen/"+j+".npy")   

for l in range(k+1):
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

for l in range(k+1):
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(norden[listnorden[l]+'day'], norden[listnorden[l]], '.', color='red', markersize = 2, label="nordenskioldbreen "+listnorden[l])
    plt.plot(ulve[listulven[l]+'day'], ulve[listulven[l]], '.', color='blue', markersize = 2, label="ulvebreen "+listulven[0])
    plt.title("Comparing average ulvebreen:"+listulven[l]+" and nordenskioldbreen:"+listnorden[l])
    plt.grid(True); plt.legend(); plt.show();# show plot on screen
    fig.savefig("Figures/compare/compare_avg_n"+listnorden[l]+"_u"+listulven[l]+".png")
