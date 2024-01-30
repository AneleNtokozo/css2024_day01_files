# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 06:02:25 2024

@author: AneleMahlangu
"""



"""
Extract files
"""

import pandas as pd

df = pd.read_csv('country_data_index.csv')

print(df)

###This data has no header information for each columns, i.e no column names. Let us add some:
    
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

print(df)

"""
Types of files
1. text files(csv)- ## text file with a semi colon::::df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")
2.Excel- ##df = pd.read_excel("data_02/residentdoctors.xlsx")
3. Json- ##df = pd.read_json("data_02/student_data.json")
"""



















