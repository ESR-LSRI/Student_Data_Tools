# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:14:52 2023

@author: felicity
"""

import pandas as pd
import numpy as np
import os as os
# find a way to use this operating system to sort a list of all the spreadsheets to concat all
import matplotlib.pyplot as plt
from datetime import datetime

fileLoc = 'C:/Users/felicity/Documents/GitHub/2023_FelicityW/editedDATA/pkl'

os.chdir(fileLoc)


# 2018-2019
#2018
df1 = pd.read_pickle("MBCP2018-2019_iButton1.pkl")
df1 = df1.resample("H").mean()
df1 = df1.dropna()
df1 = df1.reset_index()

#dataframe with only fall dates
fall = df1.loc[247:760]
fall = fall.set_index('datetime')

#dataframe with only winter dates
winter = df1.loc[761:1268]
winter = winter.set_index('datetime')

#dataframe with only spring dates
spring = df1.loc[1269:1787]
spring = spring.set_index('datetime')

#dataframe with only summer dates
summer1 = df1.loc[1788:2084]
summer = df1.loc[9:246]
summer3 = pd.concat([summer, summer1])
summer3 = summer3.set_index('datetime')

#2019
df2 = pd.read_pickle("MBCP2018-2019_iButton6.pkl")
df2 = df2.resample("H").mean()
df2 = df2.dropna()
df2 = df2.reset_index()

fall2 = df2.loc[235:748]
fall2 = fall2.set_index('datetime')

winter2 = df2.loc[749:1256]
winter2 = winter2.set_index('datetime')

spring2 = df2.loc[1258:1775]
spring2 = spring2.set_index('datetime')

summer1 = df2.loc[1775:2035]
summer = df2.loc[0:234]
summer2 = pd.concat([summer, summer1])
summer2 = summer2.set_index('datetime')

f_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    f_diurnal.loc[n,"Temp"] = np.mean(fall[fall.index.hour == n].Value)
    
w_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal.loc[n,"Temp"] = np.mean(winter[winter.index.hour == n].Value)
    
s_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal.loc[n,"Temp"] = np.mean(spring[spring.index.hour == n].Value)
    
su_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal.loc[n,"Temp"] = np.mean(summer3[summer3.index.hour == n].Value)



f_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])
for n in np.arange(0,24,1):
    f_diurnal2.loc[n,"Temp"] = np.mean(fall2[fall2.index.hour == n].Value)
    
w_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal2.loc[n,"Temp"] = np.mean(winter2[winter2.index.hour == n].Value)
    
s_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal2.loc[n,"Temp"] = np.mean(spring2[spring2.index.hour == n].Value)
    
su_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal2.loc[n,"Temp"] = np.mean(summer2[summer2.index.hour == n].Value)

# calculate lapse rates
ldiff = f_diurnal - f_diurnal2
adiff = 1341 - 1066
fall_lapse_rate1 = 1000*ldiff/adiff

ldiff = w_diurnal - w_diurnal2
adiff = 1341 - 1066
winter_lapse_rate1 = 1000*ldiff/adiff

ldiff = s_diurnal - s_diurnal2
adiff = 1341 - 1066
spring_lapse_rate1 = 1000*ldiff/adiff

ldiff = su_diurnal - su_diurnal2
adiff = 1341 - 1066
summer_lapse_rate1 = 1000*ldiff/adiff


df2018 = pd.DataFrame(index = [np.arange(0,24,1)], columns=['winter', 'summer', 'spring', 'fall'])
df2018["fall"] = fall_lapse_rate1
df2018["winter"] = winter_lapse_rate1
df2018["spring"] = spring_lapse_rate1
df2018["summer"] = summer_lapse_rate1

df2018.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()


f_diurnal.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()

w_diurnal.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()

s_diurnal.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()

su_diurnal.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()
"""
"""
"""
"""
# 2019-2020
df3 = pd.read_pickle("MBCP2019-2020_iButton1.pkl")
df3 = df3.resample("H").mean()
df3 = df3.dropna()
df3 = df3.reset_index()

fall = df3.loc[241:754]
fall = fall.set_index('datetime')

winter = df3.loc[755:1268]
winter = winter.set_index('datetime')

spring = df3.loc[1269:1787]
spring = spring.set_index('datetime')

summer1 = df3.loc[1788:2084]
summer = df3.loc[0:246]
summer3 = pd.concat([summer, summer1])
summer3 = summer3.set_index('datetime')


df4 = pd.read_pickle("MBCP2019-2020_iButton6.pkl")
df4 = df4.resample("H").mean()
df4 = df4.dropna()
df4 = df4.reset_index()

fall2 = df4.loc[241:754]
fall2 = fall2.set_index('datetime')

winter2 = df4.loc[755:1268]
winter2 = winter2.set_index('datetime')

spring2 = df4.loc[1269:1787]
spring2 = spring2.set_index('datetime')

summer1 = df4.loc[1788:2084]
summer = df4.loc[0:234]
summer2 = pd.concat([summer, summer1])
summer2 = summer2.set_index('datetime')

f_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    f_diurnal.loc[n,"Temp"] = np.mean(fall[fall.index.hour == n].Value)
    
w_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal.loc[n,"Temp"] = np.mean(winter[winter.index.hour == n].Value)
    
s_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal.loc[n,"Temp"] = np.mean(spring[spring.index.hour == n].Value)
    
su_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal.loc[n,"Temp"] = np.mean(summer3[summer3.index.hour == n].Value)



f_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])
for n in np.arange(0,24,1):
    f_diurnal2.loc[n,"Temp"] = np.mean(fall2[fall2.index.hour == n].Value)
    
w_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal2.loc[n,"Temp"] = np.mean(winter2[winter2.index.hour == n].Value)
    
s_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal2.loc[n,"Temp"] = np.mean(spring2[spring2.index.hour == n].Value)
    
su_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal2.loc[n,"Temp"] = np.mean(summer2[summer2.index.hour == n].Value)

# calculate lapse rates
ldiff = f_diurnal - f_diurnal2
adiff = 1341 - 1066
fall_lapse_rate1 = 1000*ldiff/adiff

ldiff = w_diurnal - w_diurnal2
adiff = 1341 - 1066
winter_lapse_rate1 = 1000*ldiff/adiff

ldiff = s_diurnal - s_diurnal2
adiff = 1341 - 1066
spring_lapse_rate1 = 1000*ldiff/adiff

ldiff = su_diurnal - su_diurnal2
adiff = 1341 - 1066
summer_lapse_rate1 = 1000*ldiff/adiff


df2019 = pd.DataFrame(index = [np.arange(0,24,1)], columns=['winter', 'summer', 'spring', 'fall'])
df2019["fall"] = fall_lapse_rate1
df2019["winter"] = winter_lapse_rate1
df2019["spring"] = spring_lapse_rate1
df2019["summer"] = summer_lapse_rate1

df2019.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()
"""

# 2020-2021

"""
df5 = pd.read_pickle("MBCP2020-2021_iButton1.pkl")
df5 = df5.resample("H").mean()
df5 = df5.dropna()
df5 = df5.reset_index()

fall = df5.loc[198:711]
fall = fall.set_index('datetime')

winter = df5.loc[712:1220]
winter = winter.set_index('datetime')

spring = df5.loc[1221:1739]
spring = spring.set_index('datetime')

summer1 = df5.loc[1740:2048]
summer = df5.loc[0:197]
summer3 = pd.concat([summer, summer1])
summer3 = summer3.set_index('datetime')

df6 = pd.read_pickle("MBCP2020-2021_iButton7.pkl")
df6 = df6.resample("H").mean()
df6 = df6.dropna()
df6 = df6.reset_index()

fall2 = df6.loc[198:711]
fall2 = fall2.set_index('datetime')

winter2 = df6.loc[712:1220]
winter2 = winter2.set_index('datetime')

spring2 = df6.loc[1221:1739]
spring2 = spring2.set_index('datetime')

summer1 = df6.loc[1740:2084]
summer = df6.loc[0:234]
summer2 = pd.concat([summer, summer1])
summer2 = summer2.set_index('datetime')

f_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    f_diurnal.loc[n,"Temp"] = np.mean(fall[fall.index.hour == n].Value)
    
w_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal.loc[n,"Temp"] = np.mean(winter[winter.index.hour == n].Value)
    
s_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal.loc[n,"Temp"] = np.mean(spring[spring.index.hour == n].Value)
    
su_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal.loc[n,"Temp"] = np.mean(summer3[summer3.index.hour == n].Value)



f_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])
for n in np.arange(0,24,1):
    f_diurnal2.loc[n,"Temp"] = np.mean(fall2[fall2.index.hour == n].Value)
    
w_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal2.loc[n,"Temp"] = np.mean(winter2[winter2.index.hour == n].Value)
    
s_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal2.loc[n,"Temp"] = np.mean(spring2[spring2.index.hour == n].Value)
    
su_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal2.loc[n,"Temp"] = np.mean(summer2[summer2.index.hour == n].Value)

# calculate lapse rates
ldiff = f_diurnal - f_diurnal2
adiff = 1341 - 1066
fall_lapse_rate1 = 1000*ldiff/adiff

ldiff = w_diurnal - w_diurnal2
adiff = 1341 - 1066
winter_lapse_rate1 = 1000*ldiff/adiff

ldiff = s_diurnal - s_diurnal2
adiff = 1341 - 1066
spring_lapse_rate1 = 1000*ldiff/adiff

ldiff = su_diurnal - su_diurnal2
adiff = 1341 - 1066
summer_lapse_rate1 = 1000*ldiff/adiff


df2020 = pd.DataFrame(index = [np.arange(0,24,1)], columns=['winter', 'summer', 'spring', 'fall'])
df2020["fall"] = fall_lapse_rate1
df2020["winter"] = winter_lapse_rate1
df2020["spring"] = spring_lapse_rate1
df2020["summer"] = summer_lapse_rate1


df2020.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()
"""


# 2021-2022
"""
df7 = pd.read_pickle("MBCP2021-2022_iButton2.pkl")
df7 = df7.resample("H").mean()
df7 = df7.dropna()
df7 = df7.reset_index()

fall = df7.loc[198:711]
fall = fall.set_index('datetime')

winter = df7.loc[712:1220]
winter = winter.set_index('datetime')

spring = df7.loc[1221:1739]
spring = spring.set_index('datetime')

summer1 = df7.loc[1740:2048]
summer = df7.loc[0:197]
summer3 = pd.concat([summer, summer1])
summer3 = summer3.set_index('datetime')

df8 = pd.read_pickle("MBCP2021-2022_iButton11.pkl")
df8 = df8.resample("H").mean()
df8 = df8.dropna()
df8 = df8.reset_index()

fall2 = df8.loc[198:711]
fall2 = fall2.set_index('datetime')

winter2 = df8.loc[712:1220]
winter2 = winter2.set_index('datetime')

spring2 = df8.loc[1221:1739]
spring2 = spring2.set_index('datetime')

summer1 = df8.loc[1740:2084]
summer = df8.loc[0:234]
summer2 = pd.concat([summer, summer1])
summer2 = summer2.set_index('datetime')

f_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    f_diurnal.loc[n,"Temp"] = np.mean(fall[fall.index.hour == n].Value)
    
w_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal.loc[n,"Temp"] = np.mean(winter[winter.index.hour == n].Value)
    
s_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal.loc[n,"Temp"] = np.mean(spring[spring.index.hour == n].Value)
    
su_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal.loc[n,"Temp"] = np.mean(summer3[summer3.index.hour == n].Value)



f_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])
for n in np.arange(0,24,1):
    f_diurnal2.loc[n,"Temp"] = np.mean(fall2[fall2.index.hour == n].Value)
    
w_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal2.loc[n,"Temp"] = np.mean(winter2[winter2.index.hour == n].Value)
    
s_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal2.loc[n,"Temp"] = np.mean(spring2[spring2.index.hour == n].Value)
    
su_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal2.loc[n,"Temp"] = np.mean(summer2[summer2.index.hour == n].Value)

# calculate lapse rates
ldiff = f_diurnal - f_diurnal2
adiff = 1341 - 1066
fall_lapse_rate1 = 1000*ldiff/adiff

ldiff = w_diurnal - w_diurnal2
adiff = 1341 - 1066
winter_lapse_rate1 = 1000*ldiff/adiff

ldiff = s_diurnal - s_diurnal2
adiff = 1341 - 1066
spring_lapse_rate1 = 1000*ldiff/adiff

ldiff = su_diurnal - su_diurnal2
adiff = 1341 - 1066
summer_lapse_rate1 = 1000*ldiff/adiff


df2021 = pd.DataFrame(index = [np.arange(0,24,1)], columns=['winter', 'summer', 'spring', 'fall'])
df2021["fall"] = fall_lapse_rate1
df2021["winter"] = winter_lapse_rate1
df2021["spring"] = spring_lapse_rate1
df2021["summer"] = summer_lapse_rate1


df2021.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()

# 2022-2023
#2022
df9 = pd.read_pickle("MBCP2022-2023_iButton2.pkl")
df9 = df9.resample("H").mean()
df9 = df9.dropna()
df9 = df9.reset_index()

fall = df9.loc[198:711]
fall = fall.set_index('datetime')

winter = df9.loc[712:1220]
winter = winter.set_index('datetime')

spring = df9.loc[1221:1739]
spring = spring.set_index('datetime')

summer1 = df9.loc[1740:2048]
summer = df9.loc[0:197]
summer3 = pd.concat([summer, summer1])
summer3 = summer3.set_index('datetime')

#2023
df10 = pd.read_pickle("MBCP2022-2023_iButton11.pkl")
df10 = df10.resample("H").mean()
df10 = df10.dropna()
df10 = df10.reset_index()

fall2 = df10.loc[198:711]
fall2 = fall2.set_index('datetime')

winter2 = df10.loc[712:1220]
winter2 = winter2.set_index('datetime')

spring2 = df10.loc[1221:1739]
spring2 = spring2.set_index('datetime')

summer1 = df10.loc[1740:2084]
summer = df10.loc[0:234]
summer2 = pd.concat([summer, summer1])
summer2 = summer2.set_index('datetime')

f_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    f_diurnal.loc[n,"Temp"] = np.mean(fall[fall.index.hour == n].Value)
    
w_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal.loc[n,"Temp"] = np.mean(winter[winter.index.hour == n].Value)
    
s_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal.loc[n,"Temp"] = np.mean(spring[spring.index.hour == n].Value)
    
su_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal.loc[n,"Temp"] = np.mean(summer3[summer3.index.hour == n].Value)



f_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])
for n in np.arange(0,24,1):
    f_diurnal2.loc[n,"Temp"] = np.mean(fall2[fall2.index.hour == n].Value)
    
w_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    w_diurnal2.loc[n,"Temp"] = np.mean(winter2[winter2.index.hour == n].Value)
    
s_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal2.loc[n,"Temp"] = np.mean(spring2[spring2.index.hour == n].Value)
    
su_diurnal2 = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    su_diurnal2.loc[n,"Temp"] = np.mean(summer2[summer2.index.hour == n].Value)

# calculate lapse rates
ldiff = f_diurnal - f_diurnal2
adiff = 1341 - 1066
fall_lapse_rate1 = 1000*ldiff/adiff

ldiff = w_diurnal - w_diurnal2
adiff = 1341 - 1066
winter_lapse_rate1 = 1000*ldiff/adiff

ldiff = s_diurnal - s_diurnal2
adiff = 1341 - 1066
spring_lapse_rate1 = 1000*ldiff/adiff

ldiff = su_diurnal - su_diurnal2
adiff = 1341 - 1066
summer_lapse_rate1 = 1000*ldiff/adiff


df2022 = pd.DataFrame(index = [np.arange(0,24,1)], columns=['winter', 'summer', 'spring', 'fall'])
df2022["fall"] = fall_lapse_rate1
df2022["winter"] = winter_lapse_rate1
df2022["spring"] = spring_lapse_rate1
df2022["summer"] = summer_lapse_rate1


df2022.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()

