# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:07:29 2023

@author: felicity
"""

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


# read in the files

# 2018-2019
df1 = pd.read_pickle("MBCP2022-2023_iButton2.pkl")
df1 = df1.resample("H").mean()
df1 = df1.dropna()
df1 = df1.reset_index()

august = df1.loc[71:246]
august = august.set_index('datetime')

september = df1.loc[247:415]
september = september.set_index('datetime')

october = df1.loc[416:590]
october = october.set_index('datetime')

november = df1.loc[591:761]
november = november.set_index('datetime')

december = df1.loc[761:935]
december = december.set_index('datetime')

january = df1.loc[936:1110]
january = january.set_index('datetime')

february = df1.loc[1111:1268]
february = february.set_index('datetime')

march = df1.loc[1269:1443]
march = march.set_index('datetime')

april = df1.loc[1444:1612]
april = april.set_index('datetime')

may = df1.loc[1613:1787]
may = may.set_index('datetime')

june = df1.loc[1788:1957]
june = june.set_index('datetime')

july1 = df1.loc[1957:2048]
july2 = df1.loc[0:70]
july3 = pd.concat([july2,july1])
july3 = july3.set_index('datetime')

df2 = pd.read_pickle("MBCP2022-2023_iButton11.pkl")
df2 = df2.resample("H").mean()
df2 = df2.dropna()
df2 = df2.reset_index()

august2 = df2.loc[71:246]
august2 = august2.set_index('datetime')

september2 = df2.loc[247:415]
september2 = september2.set_index('datetime')

october2 = df2.loc[416:590]
october2 = october2.set_index('datetime')

november2 = df2.loc[591:761]
november2 = november2.set_index('datetime')

december2 = df2.loc[761:935]
december2 = december2.set_index('datetime')

january2 = df2.loc[936:1110]
january2 = january2.set_index('datetime')

february2 = df2.loc[1111:1268]
february2 = february2.set_index('datetime')

march2 = df2.loc[1269:1443]
march2 = march2.set_index('datetime')

april2 = df2.loc[1444:1612]
april2 = april2.set_index('datetime')

may2 = df2.loc[1613:1787]
may2 = may2.set_index('datetime')

june2 = df2.loc[1788:1957]
june2 = june2.set_index('datetime')

july1 = df2.loc[1957:2048]
july2 = df2.loc[0:70]
july4 = pd.concat([july2,july1])
july4 = july4.set_index('datetime')


#august
a_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    a_diurnal.loc[n,"Temp"] = np.mean(august[august.index.hour == n].Value)
   
#september    
s_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s_diurnal.loc[n,"Temp"] = np.mean(september[september.index.hour == n].Value)

#october    
o_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    o_diurnal.loc[n,"Temp"] = np.mean(october[october.index.hour == n].Value)
   
#november
n_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    n_diurnal.loc[n,"Temp"] = np.mean(november[november.index.hour == n].Value)

#december    
d_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    d_diurnal.loc[n,"Temp"] = np.mean(december[december.index.hour == n].Value)

#january    
j_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    j_diurnal.loc[n,"Temp"] = np.mean(january[january.index.hour == n].Value)
 
#february
f_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    f_diurnal.loc[n,"Temp"] = np.mean(february[february.index.hour == n].Value)

#march    
m_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    m_diurnal.loc[n,"Temp"] = np.mean(march[march.index.hour == n].Value)

#april    
a_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    a_diurnal.loc[n,"Temp"] = np.mean(april[april.index.hour == n].Value)

#may    
ma_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    ma_diurnal.loc[n,"Temp"] = np.mean(may[may.index.hour == n].Value)

#june    
ju_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    ju_diurnal.loc[n,"Temp"] = np.mean(june[june.index.hour == n].Value)

#july    
jul_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    jul_diurnal.loc[n,"Temp"] = np.mean(july3[july3.index.hour == n].Value)
 
    #2
    
#august2
a2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    a2_diurnal.loc[n,"Temp"] = np.mean(august2[august2.index.hour == n].Value)
   
#september    
s2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    s2_diurnal.loc[n,"Temp"] = np.mean(september2[september2.index.hour == n].Value)

#october    
o2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    o2_diurnal.loc[n,"Temp"] = np.mean(october2[october2.index.hour == n].Value)
   
#november
n2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    n2_diurnal.loc[n,"Temp"] = np.mean(november2[november2.index.hour == n].Value)

#december    
d2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    d_diurnal.loc[n,"Temp"] = np.mean(december2[december2.index.hour == n].Value)

#january    
j2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    j2_diurnal.loc[n,"Temp"] = np.mean(january2[january2.index.hour == n].Value)
 
#february
f2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    f2_diurnal.loc[n,"Temp"] = np.mean(february2[february2.index.hour == n].Value)

#march    
m2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    m_diurnal.loc[n,"Temp"] = np.mean(march2[march2.index.hour == n].Value)

#april    
a2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    a2_diurnal.loc[n,"Temp"] = np.mean(april2[april2.index.hour == n].Value)

#may    
ma2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    ma_diurnal.loc[n,"Temp"] = np.mean(may2[may2.index.hour == n].Value)

#june    
ju2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    ju2_diurnal.loc[n,"Temp"] = np.mean(june2[june2.index.hour == n].Value)

#july    
jul2_diurnal = pd.DataFrame(index = [np.arange(0,24,1)], columns = ["Temp"])

x = []
for n in np.arange(0,24,1):
    jul2_diurnal.loc[n,"Temp"] = np.mean(july4[july4.index.hour == n].Value)
 

# calculate lapse rates
ldiff = a_diurnal - a2_diurnal
adiff = 1341 - 1066
aug_lapse_rate1 = 1000*ldiff/adiff

ldiff = s_diurnal - s2_diurnal
adiff = 1341 - 1066
sep_lapse_rate1 = 1000*ldiff/adiff

ldiff = o_diurnal - o2_diurnal
adiff = 1341 - 1066
oct_lapse_rate1 = 1000*ldiff/adiff

ldiff = n_diurnal - n2_diurnal
adiff = 1341 - 1066
nov_lapse_rate1 = 1000*ldiff/adiff

ldiff = d_diurnal - d2_diurnal
adiff = 1341 - 1066
dec_lapse_rate1 = 1000*ldiff/adiff

ldiff = j_diurnal - j2_diurnal
adiff = 1341 - 1066
jan_lapse_rate1 = 1000*ldiff/adiff

ldiff = f_diurnal - f2_diurnal
adiff = 1341 - 1066
feb_lapse_rate1 = 1000*ldiff/adiff

ldiff = m_diurnal - m2_diurnal
adiff = 1341 - 1066
mar_lapse_rate1 = 1000*ldiff/adiff

ldiff = a_diurnal - a2_diurnal
adiff = 1341 - 1066
apr_lapse_rate1 = 1000*ldiff/adiff

ldiff = d_diurnal - d2_diurnal
adiff = 1341 - 1066
may_lapse_rate1 = 1000*ldiff/adiff

ldiff = ju_diurnal - ju2_diurnal
adiff = 1341 - 1066
jun_lapse_rate1 = 1000*ldiff/adiff

ldiff = jul_diurnal - jul2_diurnal
adiff = 1341 - 1066
jul_lapse_rate1 = 1000*ldiff/adiff

df2018 = pd.DataFrame(index = [np.arange(0,24,1)], columns=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug','Sep','Oct','Nov','Dec'])
df2018["Jan"] = jan_lapse_rate1
df2018["Feb"] = feb_lapse_rate1
df2018["Mar"] = mar_lapse_rate1
df2018["Apr"] = apr_lapse_rate1
df2018["May"] = may_lapse_rate1
df2018["Jun"] = jun_lapse_rate1
df2018["Jul"] = jul_lapse_rate1
df2018["Aug"] = aug_lapse_rate1
df2018["Sep"] = sep_lapse_rate1
df2018["Oct"] = oct_lapse_rate1
df2018["Nov"] = nov_lapse_rate1
df2018["Dec"] = dec_lapse_rate1



df2018.plot.line()
plt.ylabel("Lapse Rate (C/km)")
plt.xlabel("Time of Day (hours)")
plt.show()





