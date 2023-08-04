# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:21:03 2023

@author: felicity
"""

import pandas as pd
import numpy as np
import os as os
import matplotlib.pyplot as plt


fileLoc = 'C:/Users/felicity/Documents/GitHub/2023_FelicityW/editedDATA'

os.chdir(fileLoc)

dfBIG = []
i = 0

#read in the files

#2018-2019
df1 = pd.read_csv("MBCP2018-2019_iButton1.csv")
df2 = pd.read_csv("MBCP2018-2019_iButton6.csv")

#2019-2020
df3 = pd.read_csv("MBCP2019-2020_iButton1.csv")
df4 = pd.read_csv("MBCP2019-2020_iButton6.csv")

#2020-2021
df5 = pd.read_csv("MBCP2020-2021_iButton1.csv")
df6 = pd.read_csv("MBCP2020-2021_iButton7.csv")

#2021-2022
df7 = pd.read_csv("MBCP2021-2022_iButton2.csv")
df8 = pd.read_csv("MBCP2021-2022_iButton11.csv")


#list of all dataframes
dflist = (df1, df2, df3, df4, df5, df6)

dflist2 = (df7,df8)

#organize dataframes
x = 1
for df in dflist:
    df["datetime"] = pd.to_datetime(df['Date/Time'])
    df = df.set_index ('datetime')
    df.drop(["Date/Time", "Unit"], axis = 'columns', inplace = True)
    df = df.resample('D').mean()
    if x == 1:
        df1 = df
    elif x == 2:
        df2 = df
    elif x == 3:
        df3 = df
    elif x == 4:
        df4 = df
    elif x == 5:
        df5 = df
    else:
        df6 = df
    x += 1
    #print (df)

#different function for organizing the dataframes with different collumns names (2021-2022)
for df in dflist2:
    df["ndt"] = df["Date/Time"].astype(str) + df["Unit"].astype(str)
    df["datetime"] = pd.to_datetime(df['ndt'])
    df = df.set_index ('datetime')
    df.drop(["Date/Time", "Unit", "ndt"], axis = 'columns', inplace = True)
    df = df.resample('D').mean()
    if x == 7:
        df7 = df
    else:
        df8 = df
    x += 1
    #print(df)
    
#calculate lapse rates
ldiff = df1["Value"] - df2["Value"]
adiff = 1341 - 1066
lapse_rate1 = 1000*ldiff/adiff

ldiff = df3["Value"] - df4["Value"]
adiff = 1341 - 1067
lapse_rate2 = 1000*ldiff/adiff

ldiff = df5["Value"] - df6["Value"]
adiff = 1341 - 1067
lapse_rate3 = 1000*ldiff/adiff

ldiff = df7["Value"] - df8["Value"]
adiff = 1227 - 1066
lapse_rate4 = 1000*ldiff/adiff

#lapse rate dataframes + organizing
#2018-2019 lapse rates dataframe
df_lapse_rates1 = df1
df_lapse_rates1["Temp_Lower"] = df_lapse_rates1["Value"]
df_lapse_rates1["Temp_Higher"] = df2["Value"]
df_lapse_rates1["Lapserate"] = lapse_rate1
df_lapse_rates1.drop(["Value", "Temp_Lower", "Temp_Higher"], axis = 'columns', inplace = True)  
df_lapse_rates1.dropna(inplace = True)
#print(df_lapse_rates1)

#2019-2020 lapse rates dataframe
df_lapse_rates2 = df3
df_lapse_rates2["Temp_Lower"] = df_lapse_rates2["Value"]
df_lapse_rates2["Temp_Higher"] = df4["Value"]
df_lapse_rates2["Lapserate"] = lapse_rate2
df_lapse_rates2.drop(["Value", "Temp_Lower", "Temp_Higher"], axis = 'columns', inplace = True)  
#print(df_lapse_rates2)
   
#2020-2021 lapse rates dataframe
df_lapse_rates3 = df5
df_lapse_rates3["Temp_Lower"] = df_lapse_rates3["Value"]
df_lapse_rates3["Temp_Higher"] = df6["Value"]
df_lapse_rates3["Lapserate"] = lapse_rate3
df_lapse_rates3.drop(["Value", "Temp_Lower", "Temp_Higher"], axis = 'columns', inplace = True)  
#print(df_lapse_rates3)
   
#2021-2022 lapse rates dataframe
df_lapse_rates4 = df7
df_lapse_rates4["Temp_Lower"] = df_lapse_rates4["Value"]
df_lapse_rates4["Temp_Higher"] = df8["Value"]
df_lapse_rates4["Lapserate"] = lapse_rate4
df_lapse_rates4.drop(["Value", "Temp_Lower", "Temp_Higher"], axis = 'columns', inplace = True)  
#print(df_lapse_rates4)


"""
#plot years seperate
#graph of df_lapse_rates1
plt.figure()
plt.plot(df_lapse_rates1.index,df_lapse_rates1.Lapserate)
plt.xlabel("Time")
plt.ylabel("Lapserate")

#graph of df_lapse_rates2
plt.figure()
plt.plot(df_lapse_rates2.index,df_lapse_rates2.Lapserate)
plt.xlabel("Time")
plt.ylabel("Lapserate")

#graph of df_lapse_rates3
plt.figure()
plt.plot(df_lapse_rates3.index,df_lapse_rates3.Lapserate)
plt.xlabel("Time")
plt.ylabel("Lapserate")

#graph of df_lapse_rates4
plt.figure()
plt.plot(df_lapse_rates4.index,df_lapse_rates4.Lapserate)
plt.xlabel("Time")
plt.ylabel("Lapserate")
"""


   
#print(df_lapse_rates3)

#big dataframe with all the years in one long graph
df_long = df_lapse_rates1
df_long = pd.concat([df_long, df_lapse_rates2,df_lapse_rates3,df_lapse_rates4])


#graph of df_long
plt.figure()
plt.plot(df_long.index,df_long.Lapserate)
plt.xlabel("Time (month)")
plt.ylabel("Lapserate (C/km)")


