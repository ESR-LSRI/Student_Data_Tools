# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:38:22 2023

@author: felicity
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:21:03 2023
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:21:03 2023

@author: felicity
"""

import pandas as pd
import numpy as np
#import xarray as xr
import os as os
#find a way to use this operating system to sort a list of all the spreadsheets to concat all
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


fileLoc = 'C:/Users/felicity/Documents/GitHub/2023_FelicityW/editedDATA'

os.chdir(fileLoc)

dfBIG = []
i = 0

#read in the files

#2018-2019
day = df1 = df1_3 = pd.read_csv("MBCP2018-2019_iButton1.csv")
df2 = df2_3 = pd.read_csv("MBCP2018-2019_iButton6.csv")

#2019-2020
df3 = pd.read_csv("MBCP2019-2020_iButton1.csv")
df4 = pd.read_csv("MBCP2019-2020_iButton6.csv")

#2020-2021
df5 = pd.read_csv("MBCP2020-2021_iButton1.csv")
df6 = pd.read_csv("MBCP2020-2021_iButton7.csv")

#2021-2022
df7 = pd.read_csv("MBCP2021-2022_iButton2.csv")
df8 = pd.read_csv("MBCP2021-2022_iButton11.csv")

fileLoc = 'C:/Users/felicity/Documents/GitHub/2023_FelicityW/editedDATA/pkl'

os.chdir(fileLoc)

df9 = pd.read_pickle("MBCP2022-2023_iButton2.pkl")
df9 = df9.resample('M').mean()

df10 = pd.read_pickle("MBCP2022-2023_iButton11.pkl")
df10 = df10.resample('M').mean()

#list of all dataframes
dflist = (df1, df2, df3, df4, df5, df6)

dflist2 = (df7,df8)

#organize dataframes
x = 1

for df in dflist:
    df["datetime"] = pd.to_datetime(df['Date/Time'])
    df = df.set_index ('datetime')
    df.drop(["Date/Time", "Unit"], axis = 'columns', inplace = True)
    df = df.resample('M').mean()
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

    
    
    
#different function for organizing the dataframes with different collumns names (2021-2022)
for df in dflist2:
    df["ndt"] = df["Date/Time"].astype(str) + df["Unit"].astype(str)
    df["datetime"] = pd.to_datetime(df['ndt'])
    df = df.set_index ('datetime')
    df.drop(["Date/Time", "Unit", "ndt"], axis = 'columns', inplace = True)
    df = df.resample('M').mean()
    if x == 7:
        df7 = df
    else:
        df8 = df
    x += 1
    #print(df)
    

    
    
#calculate lapse rates
#2018-2019
ldiff = df1["Value"] - df2["Value"]
adiff = 1341 - 1066
lapse_rate1 = 1000*ldiff/adiff

#2019-2020
ldiff = df3["Value"] - df4["Value"]
adiff = 1341 - 1067
lapse_rate2 = 1000*ldiff/adiff

#2020-2021
ldiff = df5["Value"] - df6["Value"]
adiff = 1341 - 1067
lapse_rate3 = 1000*ldiff/adiff

#2021-2022
ldiff = df7["Value"] - df8["Value"]
adiff = 1227 - 1066
lapse_rate4 = 1000*ldiff/adiff

#2022-2023
ldiff = df9["Value"] - df10["Value"]
adiff = 1227 - 1066
lapse_rate5 = 1000*ldiff/adiff


#lapse rate dataframes + organizing
#2018-2019 lapse rates dataframe
df_lapse_rates1 = df1
df_lapse_rates1["Temp_Lower"] = df_lapse_rates1["Value"]
df_lapse_rates1["Temp_Higher"] = df2["Value"]
df_lapse_rates1[2018] = lapse_rate1
df_lapse_rates1_2 = df_lapse_rates1
df_lapse_rates1_2.reset_index(inplace = True)
df_lapse_rates1_2.drop(["Value", "Temp_Lower", "Temp_Higher"], axis = 'columns', inplace = True)  
#print(df_lapse_rates1_2)

#2019-2020 lapse rates dataframe
df_lapse_rates2 = df3
df_lapse_rates2["Temp_Lower"] = df_lapse_rates2["Value"]
df_lapse_rates2["Temp_Higher"] = df4["Value"]
df_lapse_rates2[2019] = lapse_rate2
df_lapse_rates2_2 = df_lapse_rates2
df_lapse_rates2_2.reset_index(inplace = True)
df_lapse_rates2.drop(["Value", "Temp_Lower", "Temp_Higher", "datetime"], axis = 'columns', inplace = True)  
#print(df_lapse_rates2_2)
   
#2020-2021 lapse rates dataframe
df_lapse_rates3 = df5
df_lapse_rates3["Temp_Lower"] = df_lapse_rates3["Value"]
df_lapse_rates3["Temp_Higher"] = df6["Value"]
df_lapse_rates3[2020] = lapse_rate3
df_lapse_rates3_2 = df_lapse_rates3
df_lapse_rates3_2.reset_index(inplace = True)
df_lapse_rates3_2.drop(["Value", "Temp_Lower", "Temp_Higher", "datetime"], axis = 'columns', inplace = True)  
#print(df_lapse_rates3_2)
   
#2021-2022 lapse rates dataframe
df_lapse_rates4 = df7
df_lapse_rates4["Temp_Lower"] = df_lapse_rates4["Value"]
df_lapse_rates4["Temp_Higher"] = df8["Value"]
df_lapse_rates4[2021] = lapse_rate4
df_lapse_rates4_2 = df_lapse_rates4
df_lapse_rates4_2.reset_index(inplace = True)
df_lapse_rates4_2.drop(["Value", "Temp_Lower", "Temp_Higher", "datetime"], axis = 'columns', inplace = True)  
#print(df_lapse_rates4_2)

df_lapse_rates5 = df9
df_lapse_rates5["Temp_Lower"] = df_lapse_rates5["Value"]
df_lapse_rates5["Temp_Higher"] = df10["Value"]
df_lapse_rates5[2022] = lapse_rate5
df_lapse_rates5_2 = df_lapse_rates5
df_lapse_rates5_2.reset_index(inplace = True)
df_lapse_rates5_2.drop(["Value", "Temp_Lower", "Temp_Higher", "datetime"], axis = 'columns', inplace = True)  

#year over year dataframe
dfBIG = df_lapse_rates1_2
dfBIG[2019] = df_lapse_rates2_2[2019]
dfBIG[2020] = df_lapse_rates3_2[2020]
dfBIG[2021] = df_lapse_rates4_2[2021]
dfBIG[2022] = df_lapse_rates5_2[2022]
dfBIG = dfBIG.set_index ('datetime')
#print(dfBIG)

#year over year plot

dfBIG.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time(month)")
plt.show()
