
import numpy as np
import pandas as pd
import datetime

dateu = np.load('Ulvebreen/Date.npy')
daten = np.load("Nordenskioldbreen/Date.npy")
datel = np.load('Lufthavn2/Date.npy')
datei = np.load('avgIsfjord/Date.npy')

new=[]

for i in range(10):
    print(daten[i])
    pdt= pd.to_datetime(daten[i])
    if pdt.strftime('%S') != '00':
        daten[i]=pd.to_datetime(daten[i]) + pd.to_timedelta([1], unit='s')
        #dtype='datetime64[30m]'
        