# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:17:48 2019

@author: Kryzha Lei Aguilar
"""

import pandas as pd

df = pd.read_csv (r'C:\Users\Kryzha Lei Aguilar\Desktop\cars.csv')

a = df.head()
print (a)

b = df.tail()
print (b)
