
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:30:22 2018

@author: Isolde Glissenaar

NO LUFTHAVN DATA
This script opens the daily mean values of given data for the Ulvebreen, Nordenskioldbreen
and Svalbard Lufthavn. The data is then cut to the overlapping length 
(where all three of them have measurements). In the next block the arrays are put
together and the dates with nan values are deleted.
"""

import numpy as np
import matplotlib.pyplot as plt

direc = ""
data_ulve = "NRLavg[W_m2]" 
data_norden = "Sout"

T_ulve=np.load(direc+"avgUlvebreen/"+data_ulve+".npy")
T_ulveday=np.load(direc+"avgUlvebreen/"+data_ulve+"day.npy")

T_norden=np.load(direc+"avgNordenskioldbreen/"+data_norden+".npy")
T_nordenday=np.load(direc+"avgNordenskioldbreen/"+data_norden+"day.npy")


''' This code cuts the data to the overlapping length'''

plt.plot(T_ulveday,T_ulve,'g.')
plt.plot(T_nordenday,T_norden,'b.')
plt.show()

minday = T_ulveday[1]
maxday = np.max(T_nordenday)


minnord = np.where(T_nordenday == minday)[0][0]
maxnord  = np.where(T_nordenday   == maxday)[0][0]

minulv  = np.where(T_ulveday   == minday)[0][0]
maxulv  = np.where(T_ulveday   == maxday)[0][0]



T_ulve_c =  T_ulve[minulv:maxulv]
T_ulveday_c = T_ulveday[minulv:maxulv]

T_norden_c =  T_norden[minnord:maxnord]
T_nordenday_c = T_nordenday[minnord:maxnord]


#plt.plot(T_nordenday_c,T_norden_c,'b.')
#plt.plot(T_ulveday_c,T_ulve_c,'g.')
#plt.show()


#%%
'''
INCLUDE DATES THAT WERE SKIPPED IN THE MEASUREMENTS
This part of the code creates an array with values for the nordenskiold
and the ulvebreen for every half hour, even when there were no measurements for both.
When there is no value, this is masked or cut.
'''

dates = np.arange(minday, maxday, dtype='datetime64[1D]')

T_c = np.empty([len(dates),2])
T_c[:,:] = np.nan   
    

for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc = np.where((T_nordenday_c == dates[i]))[0][0]
        T_c[i,0] = T_norden_c[loc]
    except IndexError: # catch the error
        continue

for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc_ulv  = np.where(T_ulveday_c == dates[i])[0][0]
        T_c[i,1] = T_ulve_c[loc_ulv]
    except IndexError: # catch the error
        continue


#plt.plot(dates, T_c[:,0],'b.') #nordenskioldbreen
#plt.plot(dates, T_c[:,1],'g.') #ulvebreen
#plt.plot(dates, T_c[:,2],'y.') #lufthavn
#plt.show()


#check how many days with data
nomask_dates = []
for i in range (0,len(dates)):
    if np.isnan(T_c[i,0]) or np.isnan(T_c[i,1]):
        temp=1
    else:
        nomask_dates.append(dates[i])
    
days = len(nomask_dates)  # number of days with data (for other data find this by making list + append)

# Make array without mask
T_nomask = np.zeros((days,2))
nomask_dates = np.empty(shape=(days), dtype='datetime64[D]')
count = 0

for i in range (0,len(dates)):
    if np.isnan(T_c[i,0]) or np.isnan(T_c[i,1]):
        temp=1
    else:
        T_nomask[count,:] = (T_c[i,:])
        nomask_dates[count] = dates[i]
        count = count+1

#for i in range (0,len(dates)):
#    for j in range(0,3):            
#            T_c[i,0]=999
#            T_c[i,1]=999
#            T_c[i,2]=999
            
#T_mask = np.ma.masked_equal(T_c, 999)
            
plt.scatter(nomask_dates, T_nomask[:,0], s=15 ,  c='b') #nordenskioldbreen
plt.scatter(nomask_dates, T_nomask[:,1], s=15 , c='g') #ulvebreen
plt.show()

#%%            
dates_snow = np.load('sneeuwhoogte/dates.npy')
ulve_snow = np.load('sneeuwhoogte/ulve.npy')
norden_snow = np.load('sneeuwhoogte/norden.npy')


import matplotlib.pylab as pylab
params = {'legend.fontsize': 'large',
          'figure.figsize': (8, 4),
         'axes.labelsize': 'large',
         'axes.titlesize':'large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

fig, ax1 = plt.subplots()
#ax1.scatter(nomask_dates, T_nomask[:,0], label='Sout Norden', s=10, c='b') #norden
#ax1.scatter(nomask_dates, T_nomask[:,1], label= 'Sout Ulve', s=10, c='g') #ulve
ax1.scatter(datesN[2345:2664], albedoN[2345:2664], label='Albedo Norden', s=10, c='b') #norden
ax1.scatter(dates[3:322], albedo[3:322], label= 'Albedo Ulve', s=10, c='g') #ulve
plt.xticks(rotation=45)
plt.grid(linestyle='--', color='grey')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('albedo')
ax1.set_ylim([0,1])
ax1.tick_params('y')

ax2 = ax1.twinx()
ax2.scatter(dates_snow, norden_snow, label= 'SSH Norden ', s=10, c='aquamarine', marker='v') #norden
ax2.scatter(dates_snow, ulve_snow , label= 'SSH Ulve',  s=10, c='lime', marker='v')   #ulve

ax2.scatter(np.nan, np.nan, label = 'Albedo Norden', s=30, color='b', marker = '.')
ax2.scatter(np.nan, np.nan, label = 'Albedo Ulve', s=30, color='g', marker = '.')

ax2.set_ylabel('snow height uncorrected [m]')
ax2.tick_params('y')
#ax2.set_ylim([0,3])

plt.legend(markerscale=4., bbox_to_anchor=(1.2,0.5), loc="center left")
fig.tight_layout()
#plt.savefig('Figures/Sout_ssh.png')
plt.show()


'''
T_nomask is an array with the data for overlapping dates. nomask_dates is the companionaning
time array. First column: Nordenskioldbreen, second column: Ulvebreen.
T_mask is the array where the dates with no data are masked. dates is the companionaning time 
array.
'''
