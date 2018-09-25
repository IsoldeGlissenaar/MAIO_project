# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:36:10 2018

@author: Isolde Glissenaar
"""

#import modules
import numpy as np
import matplotlib.pyplot as plt

#Open files
f = open( "aws_ulvebreen.txt" )

ulve = []
for line in f.readlines():
    y = [value for value in line.split()]
    ulve.append( y )

f.close()


f = open( "aws_nordenskioldbreen.txt" )

norden = []
for line in f.readlines():
    y = [value for value in line.split()]
    norden.append( y )

f.close()

#%%

#Create array with only values (no headings or dates)
ulve_values=[]      
ulve_notitle = ulve[1:len(ulve)][:]

for i in range (0,len(ulve)-1):
    z = ulve_notitle[i][2:len(ulve[0])]
    y = [value for value in z]
    ulve_values.append(y)


#make nan
ulve_float = []

for i in range(0,len(ulve_values)):
    y = [float(k) for k in ulve_values[i]]
    ulve_float.append(y)
    for j in range(0,len(ulve[0])-2):
        if ulve_float[i][j]==(-999.5) or ulve_float[i][j]==(-999.3):
            ulve_float[i][j] = np.nan
            
#%%

direc = 'C:/Users/Isolde/Documents/GitHub/MAIO_project/Ulvebreen/'

# Plot a value
for j in range(0,len(ulve_float[0])):
    len_ = len(ulve)
    temp_file = np.zeros(shape= (len(ulve_float)-1) )

    for i in range(0,len(ulve_float)-1):
        temp_file[i] = ulve_float[i][j]
    
    np.save(direc+ ulve[0][j+2] +'.npy', temp_file)

#plt.plot(T_surf, '.', markersize = 2)
#plt.ylim([-40,20])
#plt.show

#%%

len_ = len(ulve)
date_file = np.zeros(shape=(len(ulve)-2), dtype='datetime64[s]')

for i in range(1,len(ulve)-1):
    date_file[i-1] = ulve[i][0] + 'T'+ulve[i][1]
    
np.save(direc+ 'Date.npy', date_file)


#%%


# pick variable
column = 2
temp = np.zeros(shape=(len(ulve_float)))
for i in range(0,len(ulve_float)):
    temp[i] = ulve_float[i][column]

# Calculate daily values
store = temp[0]
days = 1.
nomeasure = 0
daily = np.zeros(shape=0)
for i in range(1,len(temp)):
    if ulve_notitle[i][0]==ulve_notitle[i-1][0]:
        if np.isnan(temp[i]):
            nomeasure = nomeasure +1
        else:
            store = store + temp[i]
            days = days + 1.
    else:
        daily = np.append(daily, [store/days])
        if np.isnan(temp[i]):
            nomeasure = nomeasure+1
            days = 0.
            store = 0
        else:
            store = temp[i]
            days = 1.
            
plt.plot(daily, '.', markersize= 2 )
plt.show()


