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
listulven= ['Date', 'Day', 'TC1avg[C]', 'TC2avg[C]', 'TSURF[C]', 'TSTR1[C]', 'TSTR2[C]', 'TSTR3[C]', 'TSTR4[C]', 'TSTR5[C]', 'TSTR6[C]', 'TSTR7[C]', 'TSTR8[C]', 'THUTavg[C]', 'THUT2m[K]', 'THUTpot[K]', 'RHWavg[%]', 'SPECHUM[g_kg]', 'HWSavg[m_s]', 'HWSmax[m_s]', 'HWDavg[deg]', 'Stoa[W_m2]', 'NRUavg[W_m2]', 'NRLavg[W_m2]', 'NRIUavg[W_m2]', 'NRILavg[W_m2]', 'NRTavg[C]', 'BAP[hPa]', 'SSH[m]', 'ADW[m]', 'MCH[deg]', 'TILTX[deg]', 'TILTY[deg]', 'LON[deg]', 'LAT[deg]', 'HMSL[m]', 'VBAT[V]', 'LBUT[days]', 'Qual', 'AWSid']

    
date = np.load('Ulvebreen/Date.npy')
T_surf = np.load('Ulvebreen/TSURF[C].npy')

# Calculate daily values
days = 1117

store=[]
td=np.timedelta64(1,'D')
start=np.datetime64('2015-08-23T00:00')
stop=start+td
year=2016
k=0

for i in range(days):
    print(i, year)
    startindex=np.where(date==start)
    stopindex=np.where(date==stop)    
    print(start,stop)
    print(startindex, stopindex)
    if k == 1:
        x=np.nanmean(T_surf[int(stopyear[0]):int(stopindex[0])])  
        year=year+1
        k=0
    elif stop ==  np.datetime64(str(year)+'-01-01T00:00'):
        stopyear=startindex[0]+48
        x=np.nanmean(T_surf[int(startindex[0]):int(stopyear[0])])
        k=1
    else:
        x=np.nanmean(T_surf[int(startindex[0]):int(stopindex[0])])
    stop=stop+td
    start=start+td
    store.append(x)
            
plt.plot(store, '.', markersize= 5 ); 
plt.title(); plt.grid(True); plt.show()







