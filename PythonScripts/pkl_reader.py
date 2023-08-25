# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:45:18 2023

@author: Zara
"""

import pandas as pd
import pickle

file_path = '' # put your pickle file path here

with open(file_path, 'rb') as file:
    data = pickle.load(file)

df = pd.DataFrame(data) # df is your dataframe, you can work with this directly