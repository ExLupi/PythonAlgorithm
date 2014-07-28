#!/usr/bin/env python

##########################################################################
# Emma Yu July 2014
# K-clustering algorithm (same as Krugal's MST algorithm)
# Speed the code up with union find data structure
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Read in data into a numpy array
data = np.loadtxt('clustering1.txt',skiprows=1, dtype={ 'names': ('Node1','Node2','Weight'),'formats':('i4','i4','i6')})

# Sort in place according to the weight
data = data[data['Weight'].argsort()]  

# Set up a pointer array for the Union-Find data structure
# The pointers are set to the locations themselves initially
# We know the number of vertices is 500
nvertices = 500
pointers = np.arange(nvertices)

# Let's try to loop throug the array, and terminate when K = 4
for x in np.nditer(data):
    if pointers(x['Node1']) ne pointers(x['Node2']): 
    
