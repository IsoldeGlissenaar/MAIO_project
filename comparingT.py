# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:27:23 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt


listnorden=['WD', 'WS', 'WSm', 'Sin', 'Sout', 'Lin', 'Lout', 'Trad', 'Tsurf', 'Tpot', 'T', 'T2m', 'q', 'RH', 'P', 'H1', 'Q1', 'H2', 'Q2', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'A1', 'A2', 'Bat', 'Tint', 'Stoa', 'Qual', 'AWSid']
listulven= ['Day', 'TC1avg[C]', 'TC2avg[C]', 'TSURF[C]', 'TSTR1[C]', 'TSTR2[C]', 'TSTR3[C]', 'TSTR4[C]', 'TSTR5[C]', 'TSTR6[C]', 'TSTR7[C]', 'TSTR8[C]', 'THUTavg[C]', 'THUT2m[K]', 'THUTpot[K]', 'RHWavg[%]', 'SPECHUM[g_kg]', 'HWSavg[m_s]', 'HWSmax[m_s]', 'HWDavg[deg]', 'Stoa[W_m2]', 'NRUavg[W_m2]', 'NRLavg[W_m2]', 'NRIUavg[W_m2]', 'NRILavg[W_m2]', 'NRTavg[C]', 'BAP[hPa]', 'SSH[m]', 'ADW[m]', 'MCH[deg]', 'TILTX[deg]', 'TILTY[deg]', 'LON[deg]', 'LAT[deg]', 'HMSL[m]', 'VBAT[V]', 'LBUT[days]', 'Qual', 'AWSid']

Datenorden=np.load("Nordenbreen/Date.npy")
Dateulve=np.load("Ulvebreen/Date.npy")

ulve={}
for i in listulven:
        ulve["{0}".format(i)]=np.load("Ulvebreen/"+i+".npy")   
        fig=plt.figure(i, figsize=(11, 4))
        plt.plot(ulve[i], '.', markersize = 2)
        plt.title("Raw data "+i)
        plt.grid(True); plt.show() # show plot on screen
        fig.savefig("Figures/ulvebreen/rawdata_"+i+".png")
        plt.show

norden={}
for i in listnorden:
        norden["{0}".format(i)]=np.load("Nordenskioldbreen/"+i+".npy")   
        fig=plt.figure(i, figsize=(11, 4))
        plt.plot(norden[i], '.', markersize = 2)
        plt.title("Raw data "+i)
        plt.grid(True); plt.show() # show plot on screen
        fig.savefig("Figures/nordenskioldbreen/rawdata_"+i+".png")
        plt.show