#!/usr/bin/env python

##########################################################################
# Emma Yu July 2014
# Optimization with KnapSack's algorithm
# Find the highest value within allowed capacity

# Tricks to speed up the algorithm:
# 1) Sort by density = value/weight
# 2) Remember only two column of the matrix
# 3) Only check the cells when update is possible (weight < capacity)

# Possible improvement:
# Use an even sparse grid since the value is a monotonic increasing function of the weight
# Step function happens only when:
# 1) there is a step in the last iteration
# 2) adding the current data value and create a new step
# Need to store both the value and the weight for each step.

#Problem 1
#2493893.0

#Problem 2
# I've been gettting the wrong answer because I'm been missing the first term.
#4243395  (only after looking at 64/2000 terms)

##########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Read in data into a numpy array
# first row: knspsack_size; number of items
# first column value; second column weight
#data = np.loadtxt('knapsack1.txt',skiprows=1)
data = np.loadtxt('knapsack_big.txt',skiprows=1)

# 1st problem: we know the total size is 1e4, and the total number of elements is 100.
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

for i in range(0,nn):
    for j in range(int(data[i,1]),capacity):
        Value[1,j]=max(Value[0,j], Value[0,j-data[i,1]]+data[i,0])
    Value[0,0:]=Value[1,0:]
    print i, Value[0, capacity-1]
    

print Value[0,capacity-1]

