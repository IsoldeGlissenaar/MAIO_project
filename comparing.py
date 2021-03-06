# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:27:23 2018

@author: d-vz
"""

import numpy as np
import matplotlib.pyplot as plt
'''
For Raw data or Average data:
Input: .npy files and defined variables in list for different sources.
Output: Plot of to compare different sources with corresponding variables
'''

listnorden= ['T2m',      "WD",          "WS",          "P", "WSm",  'RH',]
listulven=  ['THUT2m[K]','HWDavg[deg]', "HWSavg[m_s]", "BAP[hPa]",  "HWSmax[m_s]", 'RHWavg[%]', ]
listluft=   ['TA',       'DD',          "FF",          "PO"]

# =============================================================================
#%% Raw data
# =============================================================================

dateu=np.load("Ulvebreen/Date.npy")
ulve={}
for k, i in enumerate(listulven): ulve["{0}".format(i)]=np.load("Ulvebreen/"+i+".npy")   

datel=np.load("avgLufthavn/Date.npy")
luft={}
for k, j in enumerate(listluft):  luft["{0}".format(j)]=np.load("Lufthavn/"+j+".npy")

datei=np.load("avgIsfjord/Date.npy")
isfj={}
for k, j in enumerate(listluft):  isfj["{0}".format(j)]=np.load("Isfjord/"+j+".npy")

daten=np.load("Nordenskioldbreen/Date.npy")       
norden={}
for k, j in enumerate(listnorden): norden["{0}".format(j)]=np.load("Nordenskioldbreen/"+j+".npy")   
        
for l in range(k+1):
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(daten, norden[listnorden[l]], '.', color='red', markersize = 2, label="nordenskioldbreen "+listnorden[l])
    plt.plot(dateu, ulve[listulven[l]], '.', color='blue', markersize = 2, label="ulvebreen "+listulven[l])
    if l < (len(listluft)):
        plt.plot(datel, luft[listluft[l]], '.', color='green', markersize = 2, label="lufthavn "+listluft[l])
        plt.plot(datei, isfj[listluft[l]], '.', color='purple', markersize = 2, label="isfjord "+listluft[l])
        plt.title("Comparing lufthavn:"+listluft[l]+" and ulvebreen:"+listulven[l]+" and nordenskioldbreen:"+listnorden[l])
    else: plt.title("Comparing ulvebreen:"+listulven[l]+" and nordenskioldbreen:"+listnorden[l])
    plt.grid(True); plt.legend(); plt.show();# show plot on screen
    fig.savefig("Figures/compare/compare_n"+listnorden[l]+"_u"+listulven[l]+".png")

# =============================================================================
#%%  average   
# =============================================================================
ulve={}
for k, i in enumerate(listulven):
        ulve["{0}".format(i)]=np.load("avgUlvebreen/"+i+".npy")   
        ulve["{0}day".format(i)]=np.load("avgUlvebreen/"+i+"day.npy")  

luft={}
for k, j in enumerate(listluft):  
        luft["{0}".format(j)]=np.load("avgLufthavn/"+j+".npy")   
        luft["{0}day".format(j)]=np.load("avgLufthavn/"+j+"day.npy")   
        
isfj={}
for k, j in enumerate(listluft):  
        isfj["{0}".format(j)]=np.load("avgIsfjord/"+j+".npy")   
        isfj["{0}day".format(j)]=np.load("avgIsfjord/"+j+"day.npy")   

norden={}
for k, j in enumerate(listnorden):
        norden["{0}".format(j)]=np.load("avgNordenskioldbreen/"+j+".npy")   
        norden["{0}day".format(j)]=np.load("avgNordenskioldbreen/"+j+"day.npy")   


for l in range(k+1):
    fig=plt.figure(1, figsize=(11, 4))
    plt.plot(norden[listnorden[l]+'day'], norden[listnorden[l]], '.', color='red', markersize = 2, label="nordenskioldbreen "+listnorden[l])
    plt.plot(ulve[listulven[l]+'day'], ulve[listulven[l]], '.', color='blue', markersize = 2, label="ulvebreen "+listulven[l])
    if l < (len(listluft)):
        plt.plot(isfj[listluft[l]+'day'], isfj[listluft[l]], '.', color='purple', markersize = 2, label="isfjord "+listluft[l])
        plt.plot(luft[listluft[l]+'day'], luft[listluft[l]], '.', color='green', markersize = 2, label="lufthavn "+listluft[l])
        plt.title("Comparing average ulvebreen:"+listulven[l]+" and nordenskioldbreen:"+listnorden[l]+"  luft/isfjord:"+listluft[l])
    else: plt.title("Comparing average ulvebreen:"+listulven[l]+" and nordenskioldbreen:"+listnorden[l])
    plt.grid(True); plt.legend(); plt.show();# show plot on screen
    fig.savefig("Figures/compare/compare_avg_n"+listnorden[l]+"_u"+listulven[l]+".png")



