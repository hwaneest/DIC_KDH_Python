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


#pandas package

#pd.cut()
ages = [20, 22, 25, 27, 32]
bins = [18, 25, 30]
cats = pd.cut(ages, bins)
cats





