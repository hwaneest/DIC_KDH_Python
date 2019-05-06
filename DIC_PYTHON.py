# -*- coding: utf-8 -*-

#######################################################
##### This is Python CODES Dictionary             #####
##### produced by Donghwan Kim                    #####
##### from Republic of Korea (Seoul, South Korea) #####
#######################################################

# check current working directory (wd)
import os
os.getcwd()

#print(os.path.realpath(__file__)) #'file'
#print(os.path.dirname(os.path.realpath(__file__)) ) #directory which has 'file'


#change working directory
import os
from os import chdir
os.getcwd()  # show current wd         
chdir('./Desktop/dir_name')   #relatively
chdir('C:\\Users\\username\\Desktop')  # change wd
os.getcwd()  # show changed wd

 
## reading files in current wd
df = pd.read_csv("filename.txt", sep=",")
df.head(3)  

## reading data using relative path
df = pd.read_csv(".\data\filename.csv", sep=",")
df.head(3)


##see all objects on memory now
globals()


## loops

# for loop
for i in range(1,5) :   #i=1,2,3,4
    print('before', i)
    print(i)
    print('after',i)












#pandas package

#pd.cut()
import pandas as pd
ages = [20, 22, 25, 27, 32]
bins = [18, 25, 30]
cats = pd.cut(ages, bins)
cats

cats.categories
cats.codes
cats.value_counts()


#dimension of dataframe or series
df.shape
