#!/usr/bin/env python

##########################################################################
#Emma Yu May 2014
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Read in Data: skip first line which indecated the number of rows
# first column is the weight, and the second column is the length
data = np.loadtxt('jobs.txt',skiprows=1)


# 1) first schedule jobs in decreasing order of the different (weight-length), higher weight first for ties
# Numpy sorting reminder:
# for sorting, the default is along the last axis
# np.sort returns the sorted array, np.argsort returns the sorted index, lexsort return index and can deal with multiple keys

difference = data[0:,1]-data[0:,0]  # since we want a decreasing order, let's just do (length - weight)
invweight = -data[0:,0] # since we want a decreasing order, we take the nagative
order1 = np.lexsort((invweight, difference))  # sort by the last column, then the second last column

time = 0.  # the accummulated time,
sum = 0.   # sum = sum + weight(i) * current accummulated time.

for x in order1:
    time = time + data[x, 1]
    sum = sum + time*data[x, 0]
    #print time, sum
    #print difference[x], data[x]
    #final sum:  69119377652 

#2) schedules jobs (optimally) in decreasing order of the ratio (weight/length)
ratio = -data[0:,0]/data[0:,1]
order2 = np.argsort(ratio)

time2 = 0.  # the accummulated time,
sum2 = 0.   # sum = sum + weight(i) * current accummulated time.

for x in order2:
    time2 = time2 + data[x, 1]
    sum2 = sum2 + time2*data[x, 0]
    print time2, sum2
    #final sum: 67311454237
