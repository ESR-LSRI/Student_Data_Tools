"""
Created on Wed Jul 19 08:42:58 2023

@author: sarah
"""



# libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os
import pickle as pickle
from sklearn.linear_model import LinearRegression

# location of data
fileLoc = 'C:\\Users\\sarah\\OneDrive\\Documents\\GitHub\\2023_SarahC\\data\\New folder\\'
fileNames = os.listdir(fileLoc)
# colNames = [c[:-4] for f in fileNames]
os.chdir(fileLoc)

# read the file
dfegp = pd.read_csv(fileNames[0],header= 0)
df= pd.read_pickle('C:\\Users\\sarah\\OneDrive\\Documents\\GitHub\\2023_SarahC\\data\\Accumulation data\\accumulationDataSonic (1).pkl')
dfegp=pd.read_csv('C:\\Users\\sarah\\OneDrive\\Documents\\GitHub\\2023_SarahC\\data\\New folder\\EGP_hour.csv')
# create datetime variable, set as index
dfegp['datetime'] = pd.to_datetime(dfegp['time'])



#Making sure that all datasets have the same number of datapoints, and that the datapoints are 
#from the same times
dfegp = dfegp.set_index('datetime')
dfegp=dfegp[dfegp.index.day==17]
dfegp=dfegp[dfegp.index.hour==00]
dfegp=dfegp[dfegp.index.year<2019]
dfegp=dfegp[dfegp.index.year>2016]

df=df[df.index.year>2016]
df=df[df.index.year<2019]




# drop useless columns from dataset 1
df.drop(['Julian_Sonic_mean', 'Sonic_num',
       'Sonic_cumsum_snow_height', 'year', 'dayOfYearStr','dayOfYear' ],axis = 'columns',inplace = True)


#drop cusless columns from dataset 2
dfegp.drop(['z_boom_u','qh_u', 'wspd_u','wdir_u','p_u', 't_u',
       'dsr', 'dsr_cor', 'usr', 'usr_cor', 'albedo', 'dlr', 'ulr', 'cc',
       't_surf', 'dlhf_u', 'dshf_u', 'z_stake', 'z_pt', 'z_pt_cor',
       'precip_u', 'precip_u_cor', 't_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5',
       't_i_6', 't_i_7', 't_i_8', 'tilt_x', 'tilt_y', 'rot', 'gps_lat',
       'gps_lon', 'gps_alt', 'gps_time', 'gps_geoid', 'gps_geounit',
       'gps_hdop', 'gps_numsat', 'gps_q', 'batt_v', 'batt_v_ini', 'batt_v_ss',
       'fan_dc_u', 'freq_vw', 't_log', 't_rad', 'msg_lat', 'msg_lon' ],axis = 'columns',inplace = True)
#Defining time as index
dfegp.drop(['time'],axis = 'columns',inplace = True)
dfegp.drop
# plotting the x and y axises
##To be clear, the labes and points do not have to be in light coral for this to work
plt.figure()
df3 = dfegp.dropna(subset=["rh_u"])
df4 = df.dropna(subset=["Sonic_mean"])
plt.plot(dfegp.rh_u,df.Sonic_mean, '.',alpha=(0.6), color='lightcoral')
#Labels!
plt.xlabel('Relitive Humidity (%)',color='lightcoral',size=16)
plt.ylabel('Sonic Mean',color='lightcoral',size=16)
