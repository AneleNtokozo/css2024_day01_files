# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:29:56 2024

@author: AneleMahlangu
"""

import pandas

file = pandas.read_csv('country_data.csv')

print(file)

print(file.info())

print(file.describe())


####file = pandas.read_csv('country_data.csv', skiprows=5)


import pandas as pd

file2 = pandas.read_csv('housing_data.csv')

print(file2)

###column_names = ["A", "B", "C"....]

###file2 = pandas.read_csv('housing_data.csv', names = column_names) #to give column names

column_names = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K","L", "M", "N"]

file2 = pd.read_csv('housing_data.csv', names = column_names)

print(file2)

print(file2.info())

print(file2.describe())


####file3 = pandas.read_csv('insurance_data.csv')

file3 = pandas.read_csv('insurance_data.csv', skiprows=5)

print(file3)

print(file3.info())



file4 = pandas.read_csv('iris.csv')

print(file4)

print(file4.info())


file5 = pandas.read_csv('diab_data.csv')

print(file5)

print(file5.info())































