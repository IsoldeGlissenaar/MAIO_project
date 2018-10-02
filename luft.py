# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:22:32 2018

@author: d-vz
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt




a=np.load("Lufthavn/TA.npy")
b=np.load("Lufthavn/Year.npy")
c=np.load("Lufthavn/Mnth.npy")
d=np.load("Lufthavn/Date.npy")
e=np.load("Lufthavn/Time(UTC).npy")

b=b.tolist()
c=c.tolist()
d=d.tolist()
e=e.tolist()

plt.scatter(b, a)
new=[]
for i in range(13843):
    b[i]=str(int(b[i]))
    if c[i] < 10: c[i] = str(0)+str(int(c[i]))
    else: c[i] = str(int(c[i]))
    if d[i] < 10: d[i] = str(0)+str(int(d[i]))
    else: d[i] = str(int(d[i]))    
    if e[i] < 10: e[i] = str(0)+str(int(e[i]))
    else: e[i] = str(int(e[i]))
    date=np.datetime64(b[i]+"-"+c[i]+"-"+d[i]+"T"+e[i]+":00")
    new.append(date)
    
new=np.asarray(new)
print(new)
print(a)
plt.plot(new,a)
