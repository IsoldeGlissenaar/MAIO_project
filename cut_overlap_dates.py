# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:30:22 2018

@author: Isolde Glissenaar

This script opens the daily mean values of the 2m temperature in degrees C for the
Ulvebreen, Nordenskioldbreen and Svalbard Lufthavn. The data is then cut to the overlapping
length (where all three of them have measurements). In the next block the arrays are put
together and the dates with nan values are deleted.
"""

import numpy as np
import matplotlib.pyplot as plt


direc = ""

T_ulve=np.load(direc+"avgUlvebreen/THUT2m[K].npy")
T_ulveday=np.load(direc+"avgUlvebreen/THUT2m[K]day.npy")

T_norden=np.load(direc+"avgNordenskioldbreen/T2m.npy")
T_nordenday=np.load(direc+"avgNordenskioldbreen/T2mday.npy")

T_luft=np.load(direc+"avgLufthavn/TA.npy")
T_luftday=np.load(direc+"avgLufthavn/TADay.npy")


''' This code cuts the data to the overlapping length'''

plt.plot(T_ulveday,T_ulve,'.')
plt.plot(T_nordenday,T_norden,'.')
plt.plot(T_luftday,T_luft,'.')
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

plt.plot(T_nordenday_c,T_norden_c,'b.')
plt.plot(T_ulveday_c,T_ulve_c,'g.')
plt.plot(T_luftday_c,T_luft_c,'y.')
plt.show()


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


plt.plot(dates, T_c[:,0],'b.') #nordenskioldbreen
plt.plot(dates, T_c[:,1],'g.') #ulvebreen
plt.plot(dates, T_c[:,2],'y.') #lufthavn
plt.show()

days = 272      # number of days with data (for other data find this by making list + append)
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

plt.plot(nomask_dates, T_nomask[:,0],'b.') #nordenskioldbreen
plt.plot(nomask_dates, T_nomask[:,1],'g.') #ulvebreen
plt.plot(nomask_dates, T_nomask[:,2],'y.') #lufthavn
plt.show()

'''
T_nomask is an array with the data for overlapping dates. nomask_dates is the companionaning
time array. First column: Nordenskioldbreen, second column: Ulvebreen, third column:
Svalbard Lufthavn.
T_mask is the array where the dates with no data are masked. dates is the companionaning time 
array.
'''











#%%

'''PC ANALYSIS TWO METHODS'''
    
'''maio method''' 
    
#pca = PCA()
#pc = pca.fit(T_mask).transform(T_mask)
#exp_var = pca.explained_variance_ratio_
#
#proj = pca.components_
#proj1 = proj[0,:]
#proj2 = proj[1,:]
#  
#    
#'''DM method'''
#    
#from sklearn.decomposition import PCA
#import pandas as pd
#ulvNorm = T_nomask[:,1]/np.std(T_nomask[:,1])
#nordNorm = T_nomask[:,0]/np.std(T_nomask[:,0])
#
#
#mat = np.array([ulvNorm,nordNorm])
#Covmatrix = np.cov(mat)#/np.ma.cov(mat)[1,1]
#eig = np.linalg.eig(Covmatrix)
#print(eig)
#print('-------')
#print(Covmatrix)
#print('-------')
#print(np.corrcoef(ulvNorm, nordNorm), 'ulven vs norden')        #Geeft Correlatiecoefficiënten
#print('-------')
#
#
#
#
#regressie = np.polyfit(T_nomask[:,1],T_nomask[:,0],1)
#tnao = np.arange(-25.,5.,1)
#
#plt.plot(T_nomask[:,1],T_nomask[:,0],'bo')        #plot NAO-index tegen Neerslag Servie
#plt.plot(tnao, tnao*regressie[0] + regressie[1],'r--')
#plt.xlabel('Nordenskioldbreen')
#plt.ylabel('Ulvebreen')
##plt.title('NAO-index versus Madrid precipitation')
##plt.text(0.75, 0.26, 'r = -0.72', fontsize=14, color='black')
##plt.text(0.75, 0.235, 's = -0.05', fontsize=14, color='black')
##plt.savefig("NaoMadrid.png",dpi=300)
#plt.show()  
#
#
#projectiematrix = np.transpose(np.dot(np.matrix.transpose(mat),(np.linalg.eig(Covmatrix)[1]))) #Projecteert de data op de eigenvectoren
#princ1 = (projectiematrix[0].getA1()-np.mean(projectiematrix[0].getA1()))
#princ2 = (projectiematrix[1].getA1()-np.mean(projectiematrix[1].getA1()))
#
#
#
#plt.plot(dates, princ1,"bo", label = 'First PC', color = "blue")           #Plot de principal components
#plt.plot(dates, princ2,"bo", label = 'Second PC', color = "green")
#plt.xlabel('Years')
#plt.ylabel('Amplitude of principal component')
#plt.legend(numpoints=1,prop={'size':11},loc=3)
#plt.show()
