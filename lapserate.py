# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:30:22 2018

@author: Isolde Glissenaar

This script opens the daily mean values of given data for the Ulvebreen, Nordenskioldbreen
and Svalbard Lufthavn. The data is then cut to the overlapping length 
(where all three of them have measurements). In the next block the arrays are put
together and the dates with nan values are deleted.
"""

import numpy as np
import matplotlib.pyplot as plt

direc = ""
data_ulve = "THUT2m[K]" 
data_norden = "T2m"
data_luft = "TA"

T_ulve=np.load(direc+"avgUlvebreen/"+data_ulve+".npy")
T_ulveday=np.load(direc+"avgUlvebreen/"+data_ulve+"day.npy")

T_norden=np.load(direc+"avgNordenskioldbreen/"+data_norden+".npy")
T_nordenday=np.load(direc+"avgNordenskioldbreen/"+data_norden+"day.npy")

T_luft=np.load(direc+"avgLufthavn/"+data_luft+".npy")
T_luftday=np.load(direc+"avgLufthavn/"+data_luft+"Day.npy")


''' This code cuts the data to the overlapping length'''

plt.plot(T_ulveday,T_ulve,'g.')
plt.plot(T_nordenday,T_norden,'b.')
plt.plot(T_luftday,T_luft,'y.')
plt.show()

minday = T_ulveday[1]
maxday = np.max(T_nordenday)


minnord = np.where(T_nordenday == minday)[0][0]
maxnord  = np.where(T_nordenday   == maxday)[0][0]

minulv  = np.where(T_ulveday   == minday)[0][0]
maxulv  = np.where(T_ulveday   == maxday)[0][0]

minluft = np.where(T_luftday   == minday)[0][0]
maxluft = np.where(T_luftday   == maxday)[0][0]


T_ulve_c =  T_ulve[minulv:maxulv]
T_ulveday_c = T_ulveday[minulv:maxulv]

T_norden_c =  T_norden[minnord:maxnord]
T_nordenday_c = T_nordenday[minnord:maxnord]

T_luft_c = T_luft[minluft:maxluft]
T_luftday_c = T_luftday[minluft:maxluft]

#plt.plot(T_nordenday_c,T_norden_c,'b.')
#plt.plot(T_ulveday_c,T_ulve_c,'g.')
#plt.plot(T_luftday_c,T_luft_c,'y.')
#plt.show()


#%%
'''
INCLUDE DATES THAT WERE SKIPPED IN THE MEASUREMENTS
This part of the code creates an array with values for the nordenskiold
and the ulvebreen for every half hour, even when there were no measurements for both.
When there is no value, this is masked or cut.
'''

dates = np.arange(minday, maxday, dtype='datetime64[1D]')

T_c = np.empty([len(dates),3])
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
    
for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc_luft  = np.where(T_luftday_c == dates[i])[0][0]
        T_c[i,2] = T_luft_c[loc_luft]
    except IndexError: # catch the error
        continue


#plt.plot(dates, T_c[:,0],'b.') #nordenskioldbreen
#plt.plot(dates, T_c[:,1],'g.') #ulvebreen
#plt.plot(dates, T_c[:,2],'y.') #lufthavn
#plt.show()


#check how many days with data
nomask_dates = []
for i in range (0,len(dates)):
    if np.isnan(T_c[i,0]) or np.isnan(T_c[i,1]) or np.isnan(T_c[i,2]):
        temp=1
    else:
        nomask_dates.append(dates[i])
    
days = len(nomask_dates)  # number of days with data (for other data find this by making list + append)

# Make array without mask
T_nomask = np.zeros((days,3))
nomask_dates = np.empty(shape=(days), dtype='datetime64[D]')
count = 0

for i in range (0,len(dates)):
    if np.isnan(T_c[i,0]) or np.isnan(T_c[i,1]) or np.isnan(T_c[i,2]):
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

plt.plot(nomask_dates, T_nomask[:,0],'b.', label='Nordenskioldbreen')
plt.plot(nomask_dates, T_nomask[:,1],  'g.',label='Ulvebreen')
plt.plot(nomask_dates, T_nomask[:,2], 'y.', label='Lufthavn')
plt.ylabel('Temperature [$^\circ$C]')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.0,0.5), loc="center left")
plt.grid(linestyle='dotted')
plt.title('T2m [$^\circ$C]')
#plt.xlim([np.datetime64('2015-08-01'),np.datetime64('2016-08-01') ])
#plt.savefig('Figures/T2m/Tall.png', bbox_inches="tight", dpi=500)
plt.show()

'''
T_nomask is an array with the data for overlapping dates. nomask_dates is the companionaning
time array. First column: Nordenskioldbreen, second column: Ulvebreen, third column:
Svalbard Lufthavn.
T_mask is the array where the dates with no data are masked. dates is the companionaning time 
array.
'''



#%%

'''LAPSE RATE'''

plt.scatter(nomask_dates, T_nomask[:,1])
plt.scatter(nomask_dates, T_nomask[:,2]-lapse_rate)
plt.show()

TU = (T_nomask[:,1])
TL = (T_nomask[:,2])

lapse_rate = 1.12 * 0.6

TL_shift = TL - lapse_rate

import scipy.stats

c=scipy.stats.ttest_ind(TU, TL_shift)
print(np.mean(TU), np.mean(TL_shift))
print(c)

 
