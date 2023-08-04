# -*- coding: utf-8 -*-
"""
This program creates overall and seasonal wind roses from csv files containing wind speed + direction data.

Created on Mon Jul 17 12:12:21 2023

@author: laelg

"""

# libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os

# location of data
# to insert different data, include your own data path
fileLoc = 'C:\\Users\\laelg\\OneDrive\\Documents\\GitHub\\2023_LaelG_LSRI_EastGRIP\\data\\'
fileNames = os.listdir(fileLoc)
# colNames = [c[:-4] for f in fileNames]
os.chdir(fileLoc)

# read the file
df = pd.read_csv(fileNames[0],header= 0)

# create datetime variable, set as index
df['datetime'] = pd.to_datetime(df['time'])
df = df.set_index('datetime')

# drop useless columns
# to access all the columns in your dataset, run df.columns
df.drop(['time', 'p_u', 't_u', 'rh_u', 'rh_u_cor', 'qh_u', 'dsr',
       'dsr_cor', 'usr', 'usr_cor', 'albedo', 'dlr', 'ulr', 'cc', 't_surf',
       'dlhf_u', 'dshf_u', 'z_boom_u', 'z_stake', 'z_pt', 'z_pt_cor',
       'precip_u', 'precip_u_cor', 't_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5',
       't_i_6', 't_i_7', 't_i_8', 'tilt_x', 'tilt_y', 'rot', 'gps_lat',
       'gps_lon', 'gps_alt', 'gps_time', 'gps_geoid', 'gps_geounit',
       'gps_hdop', 'gps_numsat', 'gps_q', 'batt_v', 'batt_v_ini', 'batt_v_ss',
       'fan_dc_u', 'freq_vw', 't_log', 't_rad', 'msg_lat', 'msg_lon'],axis = 'columns',inplace = True)

# import wind rose libraries
from windrose import WindroseAxes
import matplotlib.cm as cm
def windPlot(df,ind,title):
    fig1 = plt.figure()
    axWr = WindroseAxes(fig1,[1,1,1,1])
    fig1.add_axes(axWr)
    # graphing data points 
    # setting graph qualities (can change graph and edge colors, increments of speed, etc.)
    if len(ind) == 0:
        axWr.bar(df.wdir_u, df.wspd_u,  normed = False,
                 edgecolor='white',bins=np.arange(0, 12, 2),cmap=cm.YlGnBu)
    else:
        axWr.bar(df[ind].wdir_u, df[ind].wspd_u,  normed = False,
                 edgecolor='white',bins=np.arange(0, 12, 2),cmap=cm.YlGnBu)
    axWr.set_yticks(np.arange(0, 12, step=2))
    plt.legend(loc = 'upper right', fontsize = 12)
    plt.title(title)

# ALL DATA wind rose
ind = ()
fig1 = windPlot(df,ind,'EastGRIP, all winds, all seasons - 2016-2023')

# sorting months into seasons
# to plot different seasons, change the seasons list to your own classification of months
seasons = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 1]
month_to_season = dict(zip(range(1,13), seasons))
df.index.month.map(month_to_season) 

# SEASONS wind roses
# to plot another interval of time, change the df.index from month to year, day, etc.
ind = (df.index.month.map(month_to_season) == 1)
fig1 = windPlot(df,ind,'EastGRIP, all winds, Winter - 2016-2023')

ind = (df.index.month.map(month_to_season) == 2)
fig1 = windPlot(df,ind,'EastGRIP, all winds, Spring - 2016-2023')

ind = (df.index.month.map(month_to_season) == 3)
fig1 = windPlot(df,ind,'EastGRIP, all winds, Summer - 2016-2023')

ind = (df.index.month.map(month_to_season) == 4)
fig1 = windPlot(df,ind,'EastGRIP, all winds, Autumn - 2016-2023')
