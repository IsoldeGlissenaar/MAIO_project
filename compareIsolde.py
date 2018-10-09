# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:30:22 2018

@author: Isolde
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd

direc = ""

T_ulve=np.load(direc+"Ulvebreen/THUTavg[C].npy")
T_ulveday=np.load(direc+"Ulvebreen/Date.npy")

T_norden=np.load(direc+"Nordenskioldbreen/Tsurf.npy")
T_nordenday=np.load(direc+"Nordenskioldbreen/Date.npy")

T_luft=np.load(direc+"Lufthavn/TA.npy")
T_luftday=np.load(direc+"Lufthavn2/Date.npy")


''' This code cuts the data to the overlapping length'''

plt.plot(T_ulveday,T_ulve,'.')
plt.plot(T_nordenday,T_norden,'.')
plt.plot(T_luftday,T_luft,'.')
plt.show()

minday = np.min(T_ulveday)
maxday = np.max(T_nordenday)

delta = np.timedelta64(1,'30m')
newminday = minday+2*delta

minnord = np.where(T_nordenday == minday)[0][0]
#minulve = np.where(T_ulveday   == minday)[0][0]
maxulv  = np.where(T_ulveday   == maxday)[0][0]

#minluft = np.where(T_luftday   == newminday)[0][0]

T_ulve_c =  T_ulve[:maxulv]
T_ulveday_c = T_ulveday[:maxulv]

T_norden_c =  T_norden[minnord:]
T_nordenday_c = T_nordenday[minnord:]

#T_luft_c = T_luft[minnord:maxulv]

plt.plot(T_nordenday_c,T_norden_c,'b.')
plt.plot(T_ulveday_c,T_ulve_c,'g.')
plt.show()


#%%
'''INCLUDE DATES THAT WERE SKIPPED IN THE MEASUREMENTS
This part of the code creates an array with values for the nordenskiold
and the ulvebreen for every half hour, even when there were no measurements for both.
When there is no value, this is masked.'''

dates = np.arange('2015-08-22T17:00:00', '2016-12-03T17:00:00', dtype='datetime64[30m]')

#miss_ulv = list(set(T_nordenday_c)-set(T_ulveday_c))
#miss_nord = list(set(T_ulveday_c)-set(T_nordenday_c))

T_c = np.empty([len(dates),2])
T_c[:,:] = 999   
    

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


plt.plot(dates, T_c[:,0],'b.') #nordenskioldbreen
plt.plot(dates, T_c[:,1],'g.') #ulvebreen
plt.show()

for i in range (0,len(dates)):
    for j in range(0,2):
        if np.isnan(T_c[i,j]):
            T_c[i,0]=999
            T_c[i,1]=999
            
T_mask = np.ma.masked_equal(T_c, 999)

plt.plot(dates, T_mask[:,0],'b.') #nordenskioldbreen
plt.plot(dates, T_mask[:,1],'g.') #ulvebreen
plt.show()

#%%

'''PC ANALYSIS TWO METHODS'''
    
'''maio method''' 
    
#pca = PCA()
#pc = pca.fit(T_c).transform(T_c)
#exp_var = pca.explained_variance_ratio_
#
#proj = pca.components_
#proj1 = proj[0,:]
#proj2 = proj[1,:]
  
    
'''DM method'''
ulvNorm = T_c[:,1]/np.std(T_c[:,1])
nordNorm = T_c[:,0]/np.std(T_c[:,0])


mat = np.matrix([ulvNorm,nordNorm])
Covmatrix = np.cov(mat)/np.cov(mat)[1,1]
eig = np.linalg.eig(Covmatrix)
print(eig)
print('-------')
print(Covmatrix)
print('-------')
print(np.corrcoef(ulvNorm, nordNorm), 'ulven vs norden')        #Geeft Correlatiecoefficiënten
print('-------')




regressie = np.polyfit(T_c[:,1],T_c[:,0],1)
tnao = np.arange(-25.,5.,1)

plt.plot(T_c[:,1],T_c[:,0],'bo')        #plot NAO-index tegen Neerslag Servie
plt.plot(tnao, tnao*regressie[0] + regressie[1],'r--')
plt.xlabel('Nordenskioldbreen')
plt.ylabel('Ulvebreen')
#plt.title('NAO-index versus Madrid precipitation')
#plt.text(0.75, 0.26, 'r = -0.72', fontsize=14, color='black')
#plt.text(0.75, 0.235, 's = -0.05', fontsize=14, color='black')
#plt.savefig("NaoMadrid.png",dpi=300)
plt.show()  


projectiematrix = np.transpose(np.dot(np.matrix.transpose(mat),(np.linalg.eig(Covmatrix)[1]))) #Projecteert de data op de eigenvectoren
princ1 = (projectiematrix[0].getA1()-np.mean(projectiematrix[0].getA1()))
princ2 = (projectiematrix[1].getA1()-np.mean(projectiematrix[1].getA1()))



plt.plot(dates, princ1,"bo", label = 'First PC', color = "blue")           #Plot de principal components
plt.plot(dates, princ2,"bo", label = 'Second PC', color = "green")
plt.xlabel('Years')
plt.ylabel('Amplitude of principal component')
plt.legend(numpoints=1,prop={'size':11},loc=3)
plt.savefig("Princomp.png",dpi=300)
plt.show()
