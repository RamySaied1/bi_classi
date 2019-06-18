import pandas as  pd
import matplotlib as mpl
import numpy as np
import seaborn as sns


train = pd.read_csv("training.csv",sep=';')

###### see basics about the data
print (train.head())
print (train.describe())

########## see how many data are missing

## 1- see if there any rows with all values of it are missing

print ("total number of rows")
print(train.shape[0])
print ("number of rows have  null values ")
print(train.shape[0]-(train.dropna(how="all")).shape[0])

# no row with all values are missing 

## 2- see if there any rows with all values of it are missing

print("total number of rows")
print(train.shape[0])
print("number of rows have  null values ")
print(train.shape[0]-(train.dropna(how="any")).shape[0])

# 2237 of 3700 have null values so we cant simply delete this rows

## 3- see which columns have missing values

print(train.isnull().sum())

# we noticed that variable18 have many nulls so we choose saw the correlaction between it and class label

corr=train.apply(lambda x: x.factorize()[0]).corr()
corr.to_csv("correlations")



