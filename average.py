# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:29:20 2018

@author: Isolde
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

listnorden=['Date', 'Hour', 'Day', 'WD', 'WS', 'WSm', 'Sin', 'Sout', 'Lin', 'Lout', 'Trad', 'Tsurf', 'Tpot', 'T', 'T2m', 'q', 'RH', 'P', 'H1', 'Q1', 'H2', 'Q2', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'A1', 'A2', 'Bat', 'Tint', 'Stoa', 'Qual', 'AWSid']
listulven= ['Date', 'Day', 'TC1avg[C]', 'TC2avg[C]', 'TSURF[C]', 'TSTR1[C]', 'TSTR2[C]', 'TSTR3[C]', 'TSTR4[C]', 'TSTR5[C]', 'TSTR6[C]', 'TSTR7[C]', 'TSTR8[C]', 'THUTavg[C]', 'THUT2m[K]', 'THUTpot[K]', 'RHWavg[%]', 'SPECHUM[g_kg]', 'HWSavg[m_s]', 'HWSmax[m_s]', 'HWDavg[deg]', 'Stoa[W_m2]', 'NRUavg[W_m2]', 'NRLavg[W_m2]', 'NRIUavg[W_m2]', 'NRILavg[W_m2]', 'NRTavg[C]', 'BAP[hPa]', 'SSH[m]', 'ADW[m]', 'MCH[deg]', 'TILTX[deg]', 'TILTY[deg]', 'LON[deg]', 'LAT[deg]', 'HMSL[m]', 'VBAT[V]', 'LBUT[days]', 'Qual', 'AWSid']

    
date = np.load('Ulvebreen/Date.npy')
T_surf = np.load('Ulvebreen/TSURF[C].npy')

# Calculate daily values
days = 1117

store=[]
day=[]
td=np.timedelta64(1,'D')
start=np.datetime64('2015-08-23T00:00')
stop=start+td
year=2016
k=0
minvalue=20 #hoeveel niet nan data punten binnen 1 dag minimaal?
nonan=minvalue

for i in range(days):
    startindex=np.where(date==start)
    stopindex=np.where(date==stop)    
    if k == 1:
        for uur in range(int(stopyear[0]),int(stopindex[0])):
            if m.isnan(T_surf[uur]): nonan=nonan-1
        if nonan >= 0: 
            x=np.nanmean(T_surf[int(stopyear[0]):int(stopindex[0])])  
            store.append(x)
            day.append(start) 
        nonan=minvalue
        year=year+1
        k=0
        
    elif stop ==  np.datetime64(str(year)+'-01-01T00:00'):
        stopyear=startindex[0]+48
        for uur in range(int(startindex[0]),int(stopyear[0])):
            if m.isnan(T_surf[uur]): nonan=nonan-1
        if nonan >= 0: 
            x=np.nanmean(T_surf[int(startindex[0]):int(stopyear[0])])
            store.append(x)
            day.append(start)
        nonan=minvalue
        k=1
        
    else:
        for uur in range(int(startindex[0]),int(stopindex[0])):
            if m.isnan(T_surf[uur]): nonan=nonan-1
        if nonan >= 0:
            x=np.nanmean(T_surf[int(startindex[0]):int(stopindex[0])])
            store.append(x)
            day.append(start)
        nonan=minvalue

    stop=stop+td
    start=start+td

fig=plt.figure(1, figsize=(11, 4))
plt.plot(day, store, '.', markersize= 5 ); 
plt.title('ulvebreen average T_Surf'); plt.grid(True); plt.show()

