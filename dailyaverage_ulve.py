# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:29:20 2018

@author: Isolde
"""

import numpy as np
import matplotlib.pyplot as plt
#x=np.load('Ulvebreen/TSURF[C].npy')
#print(x)

listnorden=['Date', 'Hour', 'Day', 'WD', 'WS', 'WSm', 'Sin', 'Sout', 'Lin', 'Lout', 'Trad', 'Tsurf', 'Tpot', 'T', 'T2m', 'q', 'RH', 'P', 'H1', 'Q1', 'H2', 'Q2', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'A1', 'A2', 'Bat', 'Tint', 'Stoa', 'Qual', 'AWSid']

T_surf = np.load('Ulvebreen/TSURF[C].npy')

len_ = len(T_surf)

listulven= ['Day', 'TC1avg[C]', 'TC2avg[C]', 'TSURF[C]', 'TSTR1[C]', 'TSTR2[C]', 'TSTR3[C]', 'TSTR4[C]', 'TSTR5[C]', 'TSTR6[C]', 'TSTR7[C]', 'TSTR8[C]', 'THUTavg[C]', 'THUT2m[K]', 'THUTpot[K]', 'RHWavg[%]', 'SPECHUM[g_kg]', 'HWSavg[m_s]', 'HWSmax[m_s]', 'HWDavg[deg]', 'Stoa[W_m2]', 'NRUavg[W_m2]', 'NRLavg[W_m2]', 'NRIUavg[W_m2]', 'NRILavg[W_m2]', 'NRTavg[C]', 'BAP[hPa]', 'SSH[m]', 'ADW[m]', 'MCH[deg]', 'TILTX[deg]', 'TILTY[deg]', 'LON[deg]', 'LAT[deg]', 'HMSL[m]', 'VBAT[V]', 'LBUT[days]', 'Qual', 'AWSid']

Dateulve=np.load("Ulvebreen/Date.npy")


# Calculate daily values

ulve={}
for j in listulven:
       
        ulve["{0}".format(j)]=np.load("Ulvebreen/"+j+".npy") 
        store = ulve[j][0]
        days = 1.
        nomeasure = 0
        daily = np.zeros(shape=0)
 
        for i in range(1,len_):
            if np.datetime64(Dateulve[i], 'D')==np.datetime64(Dateulve[i-1], 'D'):
                if np.isnan(ulve[j][i]):
                    nomeasure = nomeasure +1
                else:
                    store = store + ulve[j][i]
                    days = days + 1.
            else:
                if store==0:
                    daily = np.append(daily, np.nan)
                else:
                    daily = np.append(daily, [store/days])
                    if np.isnan(ulve[j][i]):
                        nomeasure = nomeasure+1
                        days = 0.
                        store = 0
                    else:
                        store = ulve[j][i]
                        days = 1.
        fig=plt.figure()
        plt.plot(daily,'.')
        plt.title(j + ' daily average')
        plt.grid(True); plt.show() # show plot on screen
        fig.savefig("Figures/dailyaverage_"+j+".png")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        