# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:35:46 2018

@author: Isolde
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

Sin_U = np.load("sneeuwhoogte/Ulve/NRUavg[W_m2].npy")
Sin_Uday = np.load("sneeuwhoogte/Ulve/NRUavg[W_m2]day.npy")
Sout_U = np.load("sneeuwhoogte/Ulve/NRLavg[W_m2].npy")
Sout_Uday = np.load("sneeuwhoogte/Ulve/NRLavg[W_m2]day.npy")
SSH_U = np.load("sneeuwhoogte/Ulve/SSH[m].npy")
SSH_Uday = np.load("sneeuwhoogte/Ulve/SSH[m]day.npy")


Sin_N = np.load("sneeuwhoogte/Norden/Sin.npy")
Sin_Nday = np.load("sneeuwhoogte/Norden/Sinday.npy")
Sout_N = np.load("sneeuwhoogte/Norden/Sout.npy")
Sout_Nday = np.load("sneeuwhoogte/Norden/Soutday.npy")
H_N = np.load("sneeuwhoogte/Norden/H1.npy")
H_Nday = np.load("sneeuwhoogte/Norden/H1day.npy")

#%%
'''Ulvebreen'''

minday = Sin_Uday[0]
maxday = Sin_Uday[-1]

dates = np.arange(minday, maxday, dtype='datetime64[1D]')

T_c = np.empty([len(dates),2])
T_c[:,:] = np.nan   
    

for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc = np.where((Sin_Uday == dates[i]))[0][0]
        T_c[i,0] = Sin_U[loc]
    except IndexError: # catch the error
        continue

for i in range(0,len(dates)):
    try:
    # the code that can cause the error
        loc_ulv  = np.where(Sout_Uday == dates[i])[0][0]
        T_c[i,1] = Sout_U[loc_ulv]
    except IndexError: # catch the error
        continue
#%%

albedo = np.zeros((len(T_c[:,0])))
for i in range (len(T_c[:,0])):
    if T_c[i,0]<10:
        albedo[i] = np.nan
    else:
        albedo[i] = T_c[i,1]/T_c[i,0]


#Summer albedo Ulvebreen

dates_year = np.array(dates, dtype='datetime64[Y]')
dates_day = dates - dates_year

summ_albedoU=np.zeros((332))
count=0
for i in range ((len(albedo))):
    if dates_day[i]>np.timedelta64(202,'D') and dates_day[i]<np.timedelta64(307,'D') :
        summ_albedoU[count]=albedo[i]
        count = count+1

mean_summ_albedoU = np.nanmean(summ_albedoU)
print('Ulvebreen average summer albedo is', mean_summ_albedoU)

#%%

'''Nordenskioldbreen'''

minday = Sin_Nday[0]
maxday = Sin_Nday[-1]

datesN = np.arange(minday, maxday, dtype='datetime64[1D]')

TN_c = np.empty([len(datesN),2])
TN_c[:,:] = np.nan   
    

for i in range(0,len(datesN)):
    try:
    # the code that can cause the error
        loc = np.where((Sin_Nday == datesN[i]))[0][0]
        TN_c[i,0] = Sin_N[loc]
    except IndexError: # catch the error
        continue

for i in range(0,len(datesN)):
    try:
    # the code that can cause the error
        loc_ulv  = np.where(Sout_Nday == datesN[i])[0][0]
        TN_c[i,1] = Sout_N[loc_ulv]
    except IndexError: # catch the error
        continue
#%%

albedoN = np.zeros((len(TN_c[:,0])))
for i in range (len(TN_c[:,0])):
    if TN_c[i,0]<10:
        albedoN[i] = np.nan
    else:
        albedoN[i] = TN_c[i,1]/TN_c[i,0]


dates_year = np.array(datesN, dtype='datetime64[Y]')
dates_day = datesN - dates_year


summ_albedoN=[]
for i in range ((len(albedoN))):
    if dates_day[i]>np.timedelta64(202,'D') and dates_day[i]<np.timedelta64(307,'D') :
        summ_albedoN.append(albedoN[i])

mean_summ_albedoN = np.nanmean(summ_albedoN)
print('Nordenskiold average summer albedo is', mean_summ_albedoN)

#%%

params = {'legend.fontsize': 'large',
          'figure.figsize': (8, 4),
         'axes.labelsize': 'large',
         'axes.titlesize':'large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

fig, ax1 = plt.subplots()
plt.scatter(dates , albedo , label='albedo', s=10, c='r')
ax1.set_xlabel('date')
plt.xticks(rotation=45)
ax1.set_ylim([0,1])
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('albedo')
ax1.tick_params('y')

ax2 = ax1.twinx()
plt.scatter(SSH_Uday, -SSH_U, label='SSH',  s=10, c= 'y')
plt.axvline(x=SSH_Uday[248], color = 'black', linestyle='--')
plt.axvline(x=SSH_Uday[310], color = 'black', linestyle='--')
ax2.set_ylabel('snow height [m]')
ax2.tick_params('y')

fig.tight_layout()
fig.legend()
#plt.savefig('Figures/Sout_ssh.png')
plt.show()


#%%


fig = plt.figure()

ax1 = fig.add_subplot(211)
plt.title('Albedo and SSH Ulvebreen')
ax1.grid(linestyle='--')
ax1.scatter(dates , albedo , label='albedo', s=10, c='r')
ax1.set_ylim([0,1])
ax1.set_yticks([0,0.25,0.5,0.75,1])
ax1.set_ylabel('albedo')
ax1.tick_params('y')
ax1.xaxis.set_ticklabels([])

ax2 = fig.add_subplot(212)
ax2.grid(linestyle='--')
ax2.scatter(SSH_Uday, -SSH_U+SSH_U[0], label='SSH',  s=10, c= 'y')
ax2.set_ylabel('snow height [m]')
ax2.tick_params('y')
plt.xticks(rotation=45)

ax1.axvline(x=SSH_Uday[248],c="black", linestyle='--', linewidth=2,zorder=0, clip_on=False)
ax2.axvline(x=SSH_Uday[248],c="black", linestyle='--', linewidth=2, zorder=0,clip_on=False)

ax1.axvline(x=SSH_Uday[310],c="black", linestyle='--', linewidth=2,zorder=0, clip_on=False)
ax2.axvline(x=SSH_Uday[310],c="black", linestyle='--', linewidth=2, zorder=0,clip_on=False)

plt.draw()
fig.savefig('sneeuwhoogte/final.png', bbox_inches="tight", dpi=500)

#%%
'''Nordenskioldbreen plot'''

fig2 = plt.figure()

ax1 = fig2.add_subplot(211)
plt.title('Albedo and SSH Nordenskioldbreen')
ax1.grid(linestyle='--')
ax1.scatter(datesN [:2665] , albedoN [:2665] , label='albedo', s=10, c='r')
ax1.set_ylim([0,1])
ax1.set_yticks([0,0.25,0.5,0.75,1])
ax1.set_ylabel('albedo')
ax1.tick_params('y')
ax1.xaxis.set_ticklabels([])

ax2 = fig2.add_subplot(212)
ax2.grid(linestyle='--')
ax2.scatter(H_Nday, -H_N+np.max(H_N), label='SSH',  s=10, c= 'y')
ax2.set_ylabel('snow height [m]')
ax2.tick_params('y')
plt.xticks(rotation=45)

ax1.axvline(x=datesN[1916],c="black", linestyle='--', linewidth=2,zorder=0, clip_on=False)
ax2.axvline(x=H_Nday[1000],c="black", linestyle='--', linewidth=2, zorder=0,clip_on=False)

ax1.axvline(x=H_Nday[1080],c="black", linestyle='--', linewidth=2,zorder=0, clip_on=False)
ax2.axvline(x=H_Nday[1080],c="black", linestyle='--', linewidth=2, zorder=0,clip_on=False)

plt.draw()
fig2.savefig('sneeuwhoogte/NordenFinal.png', bbox_inches="tight", dpi=500)
