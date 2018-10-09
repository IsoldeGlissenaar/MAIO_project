# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:29:20 2018

@author: Isolde
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

# =============================================================================
#%% Ulvebreen
# =============================================================================
listulven= ['TC1avg[C]', 'TC2avg[C]', 'TSURF[C]', 'TSTR1[C]', 'TSTR2[C]', 'TSTR3[C]', 'TSTR4[C]', 'TSTR5[C]', 'TSTR6[C]', 'TSTR7[C]', 'TSTR8[C]', 'THUTavg[C]', 'THUT2m[K]', 'THUTpot[K]', 'RHWavg[%]', 'SPECHUM[g_kg]', 'HWSavg[m_s]', 'HWSmax[m_s]', 'HWDavg[deg]', 'Stoa[W_m2]', 'NRUavg[W_m2]', 'NRLavg[W_m2]', 'NRIUavg[W_m2]', 'NRILavg[W_m2]', 'NRTavg[C]', 'BAP[hPa]', 'SSH[m]', 'ADW[m]', 'MCH[deg]', 'TILTX[deg]', 'TILTY[deg]', 'LON[deg]', 'LAT[deg]', 'HMSL[m]', 'VBAT[V]', 'LBUT[days]', 'Qual', 'AWSid']
dateu = np.load('Ulvebreen/Date.npy')

days = 1117

for number, name in enumerate(listulven):
    T_surf = np.load('Ulvebreen/'+name+'.npy')
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
        startindex=np.where(dateu==start)
        stopindex=np.where(dateu==stop)    
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
    np.save('avgUlvebreen/'+name+'.npy', store)
    np.save('avgUlvebreen/'+name+'day.npy', day)
    
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(day, store, '.', markersize= 5 ); 
    plt.title('Ulvebreen average '+name); plt.grid(True); plt.show()
    fig.savefig('Figures/ulvebreen/avg_' + name)

# =============================================================================
#%% Nordenskioldbreen
# =============================================================================
listnorden=['WD', 'WS', 'WSm', 'Sin', 'Sout', 'Lin', 'Lout', 'Trad', 'Tsurf', 'Tpot', 'T', 'T2m', 'q', 'RH', 'P', 'H1', 'Q1', 'H2', 'Q2', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'A1', 'A2', 'Bat', 'Tint', 'Stoa', 'Qual', 'AWSid']
daten=np.load("Nordenskioldbreen/Date.npy")

days = 2577

for number, name in enumerate(listnorden):
    T_surf = np.load('Nordenskioldbreen/'+name+'.npy')
    store=[]
    day=[]
    td=np.timedelta64(1,'D')
    start=np.datetime64('2009-03-25T00:00')
    stop=start+td
    year=2010
    k=0
    minvalue=20 #hoeveel niet nan data punten binnen 1 dag minimaal?
    nonan=minvalue
    
    for i in range(days):
        if start == np.datetime64('2010-03-18T00:00'):
            start=np.datetime64('2010-03-20T00:00')
            stop=start+td
        if start == np.datetime64('2012-09-16T00:00'):
            start=np.datetime64('2013-04-24T00:00')
            stop=start+td
        if start == np.datetime64('2016-04-10T00:00'):
            start=np.datetime64('2016-04-12T00:00')
            stop=start+td
        if start == np.datetime64('2016-11-25T00:00'):
            start=np.datetime64('2016-11-30T00:00')
            stop=start+td
            
        startindex=np.where(daten==start)
        stopindex=np.where(daten==stop) 
        if start == np.datetime64('2010-03-19T00:00'):
            startindex=np.where(daten==start)
            
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
    np.save('avgNordenskioldbreen/'+name+'.npy', store)
    np.save('avgNordenskioldbreen/'+name+'day.npy', day)
    
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(day, store, '.', markersize= 5 ); 
    plt.title('Nordenskioldbreen average '+name); plt.grid(True); plt.show()
    fig.savefig('Figures/nordenskioldbreen/avg_' + name)

# =============================================================================
#%% Lufthavn
# =============================================================================
listluft= ['DD','FF', 'PO','RR_12','RR_24','Stno','TA','TSS']
dateu = np.load('Lufthavn2/Date.npy')

days = 3459

for number, name in enumerate(listluft):
    T_surf = np.load('Lufthavn/'+name+'.npy')
    store=[]
    day=[]
    td=np.timedelta64(1,'D')
    start=np.datetime64('2009-03-25T00:00')
    stop=start+td
    year=2010
    k=0
    minvalue=3 #hoeveel niet nan data punten binnen 1 dag minimaal?
    nonan=minvalue
    
    for i in range(days):
        startindex=np.where(dateu==start)
        stopindex=np.where(dateu==stop)
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

    np.save('avgLufthavn/'+name+'.npy', store)
    np.save('avgLufthavn/'+name+'day.npy', day)
    
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(day, store, '.', markersize= 5 ); 
    plt.title('Lufthavn average '+name); plt.grid(True); plt.show()
    fig.savefig('Figures/lufthavn/avg_' + name)
    

# =============================================================================
#%% Isfjord
# =============================================================================
listisfjord= ['DD', 'FF', 'PO','RR_12','RR_24','Stno','TA','TSS']
dateu = np.load('avgIsfjord/Date.npy')

days = 1464

for number, name in enumerate(listisfjord):
    T_surf = np.load('Isfjord/'+name+'.npy')
    store=[]
    day=[]
    td=np.timedelta64(1,'D')
    start=np.datetime64('2014-09-10T00:00')
    stop=start+td
    year=2015
    k=0
    minvalue=3 #hoeveel niet nan data punten binnen 1 dag minimaal?
    nonan=minvalue
    
    for i in range(days):
        startindex=np.where(dateu==start)
        stopindex=np.where(dateu==stop)
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
        
    np.save('avgIsfjord/'+name+'.npy', store)
    np.save('avgIsfjord/'+name+'day.npy', day)
    
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(day, store, '.', markersize= 5 ); 
    plt.title('Isfjord average '+name); plt.grid(True); plt.show()
    fig.savefig('Figures/isfjord/avg_' + name)
    



