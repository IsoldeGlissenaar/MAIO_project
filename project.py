# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:36:10 2018

@author: Isolde Glissenaar
"""

#import modules
import numpy as np


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


f = open("lufthavn_data.txt")

lufthavn = []
for line in f.readlines():
    y = [value for value in line.split()]
    lufthavn.append( y )

f.close()

lufthavn = lufthavn[23:][:]


#%%
'ULVEBREEN'

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
        if ulve_float[i][j]<-990:
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
'NORDENSKIOLD'

norden_values=[]      
norden_notitle = norden[1:len(norden)][:]

for i in range (0,len(norden)-1):
    z = norden_notitle[i][2:len(norden[0])]
    y = [value for value in z]
    norden_values.append(y)


#make nan
norden_float = []

for i in range(0,len(norden_values)):
    y = [float(k) for k in norden_values[i]]
    norden_float.append(y)
    for j in range(0,len(norden[0])-2):
        if norden_float[i][j]<-990:
            norden_float[i][j] = np.nan

#%%
direc = 'C:/Users/Isolde/Documents/GitHub/MAIO_project/Nordenskioldbreen/'

# Plot a value
for j in range(0,len(norden_float[0])):
    len_ = len(norden)
    temp_file = np.zeros(shape= (len(norden_float)-1) )

    for i in range(0,len(norden_float)-1):
        temp_file[i] = norden_float[i][j]
    
    np.save(direc+ norden[0][j+2] +'.npy', temp_file)


#%%

len_ = len(norden)
date_file = np.zeros(shape=(len(norden)-2), dtype='datetime64[s]')

for i in range(1,len(norden)-1):
    date_file[i-1] = norden[i][0] + 'T'+norden[i][1]
    
np.save(direc+ 'Date.npy', date_file)