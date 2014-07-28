#!/usr/bin/env python

##########################################################################
# Emma Yu July 2014
# I try to speed up the algorith by implementing a sparse grid
# This code is not working yet.
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Read in data into a numpy array
# first row: knspsack_size; number of items
# first column value; second column weight
#data = np.loadtxt('knapsack1.txt',skiprows=1)
data = np.loadtxt('knapsack_big.txt',skiprows=1)

# we know the total size is 1e4, and the total number of elements is 100.
#nn=100
#capacity = 10000
nn = 2000
capacity = 2000000

# Sort the data by density
# Run it on the small data set, found the best solution after runing through 20% of the data
data2 = np.zeros([nn,3])
data2[0:,0]=data[0:,0]
data2[0:,1]=data[0:,1]
data2[0:,2]=-data[0:,0]/data[0:,1]
data2=data2[data2[0:,2].argsort()]
data[0:,0]=data2[0:,0]
data[0:,1]=data2[0:,1]


# only maintain two column, and update only when the weight is no larger than the capacity
Value = np.zeros([2,capacity])
# initialize [number, capacity]
old = [[0,0]]

# do i =1 by hand:
i = 1
new = old
new.append=([data[i,1], data[i,0]]) #I store [weight, value]
old = new

# think as a step function. Only step when there is previous one, or adding a new value
# AKA Value[0,j-data[i,1]]+data[i,0] is larger  

# should I scan through everything or not?
for i in range(0,nn):
    new = []
    for j in old:
        new = new.append(old[j])
        nweight = old[j][0]+data[i,1]
        nvalue = old[j][1]+data[i,0]
        if nweight < old[j+1][0]:
            new.append([nweight,nvalue])
                        
# for i =1, simple add one step at data[i,0] = capacity
# add one point - [data[i,0], ]

for i in range(1,nn):
    for j in range(int(data[i,1]),capacity):
        Value[1,j]=max(Value[0,j], Value[0,j-data[i,1]]+data[i,0])
    Value[0,0:]=Value[1,0:]
    print i, Value[0, capacity-1]
    

print Value[0,capacity-1]


#Problem 1
#2493893.0

#Problem 2
# I've been gettting the wrong answer because I'm been missing the first term.
#4243395  (only after looking at 64/2000 terms)
