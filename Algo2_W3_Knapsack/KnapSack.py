#!/usr/bin/env python

##########################################################################
# Emma Yu July 2014
#
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Read in data into a numpy array
# first row: knspsack_size; number of items
# first column value; second column weight
#data = np.loadtxt('knapsack1.txt',skiprows=1)
data = np.loadtxt('knapsack_big.txt',skiprows=1)
# we know the total size is 1e4, and the total number of elements is 100.
nn = 2000
capacity = 2000000 
Value = np.zeros([nn,capacity])
Value[0,0:]=0

for i in range(1,nn):
    for j in range(0,capacity):
        if data[i,1] > j:
            Value[i,j] = Value[i-1,j]
        else:
            Value[i,j]=max(Value[i-1,j], Value[i-1,j-data[i,1]]+data[i,0])

print Value[nn-1,capacity-1]

#Problem 1
#2493893.0


