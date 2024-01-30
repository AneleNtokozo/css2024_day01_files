# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:42:48 2024

@author: AneleMahlangu
"""

"""Storing data in python

1. LIsts
2. Dictionaries
3. Data frames-specific to pandas
"""
"""
import pandas

file = pandas.read_csv('country_data.csv')

print(file)

age1 = 30
age2 = 25
age3 = 29   ##to do this quicker, we use diff ways in python, eg lists

age = [30,40,30,49,22,35,22,46,29,25,39]

print(age)

print(age[0]) #index starts at 0, to acces numbers in our list

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
##print(age[11])


# Basic Stats


print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

#storing data
C2 = "M"  #male
C3 = "M"
C4 = "F"   #female
print(C2)
print(C3)
print(C4)      
      
# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
      
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(age[0:3])

print(country)
print(country[0])
print(country[5])


#append is to add
##Lists uses square brackets

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

age.insert(0,100) #to insert 100 in the first position

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3]) #dont include the last one

"""
##Dictionaries-key:value pairs
##eg, age
##eg cat- a cute animal
###-unordered, unlike lists

"""

mammals = {"cat":"a cute animal", "lion": "king of the jungle", "elephant": "a gigantic herbivore"}

print(mammals["cat"])


"""

"""
Data frames

"""
# Creating a DataFrame
data_people = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}


import pandas
import pandas as pd
#df = data frame
df = pd.DataFrame(data_people)

# Displaying the DataFrame
print(df)



fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes': size_nm
}

"""
df = dataframe
"""

df = pandas.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'].min())

print(df['sizes'].mean())

print(df.describe())

print(df['sizes']>10)

print(df[1:3])



#how to remove a column

df.drop(columns=["sizes"], inplace = True) ##inplace mean  modification is made directly to the original DataFrame.


















      
      
      
      