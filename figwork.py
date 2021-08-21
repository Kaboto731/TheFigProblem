#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:58:04 2021

@author: manuel
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'/home/manuel/Downloads/FAOSTAT_data_8-20-2021.csv')

# df.head()
# word = df.Area
# countdf = df[df['Area']==Area].sort_values('Year')
Areaharvdf = df.loc[lambda df: df['Element'] == 'Area harvested']
for Area in Areaharvdf['Area'].unique():
    globaldf=Areaharvdf[Areaharvdf['Area']==Area].sort_values('Year').plot.line(x='Year',y='Value',title=Area)
