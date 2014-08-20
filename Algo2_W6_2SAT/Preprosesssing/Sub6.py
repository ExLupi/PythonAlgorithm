#!/usr/bin/env python

##########################################################################
# Emma Yu Aug 2014
#
##########################################################################
# this is not complete, we need to change the number of elements to begin with
# or we need to find the range in the subroutine
def PreProcessing(Big, Small):
    dim = len(Big)
    pos = np.zeros(1000000)
    neg = np.zeros(1000000)
    for i in range(0,dim):
        for j in range(0,2):
            if Big[i][j] > 0:
                pos[Big[i][j]-1]=1
            else:
                neg[abs(Big[i][j])-1]=1

    for i in range(0,dim):
        if (pos[abs(Big[i][0])-1] + neg[abs(Big[i][0])-1]) == 2:
            if (pos[abs(Big[i][1])-1] + neg[abs(Big[i][1])-1]) == 2:
                Small.append(Big[i])


##########################################################################
import numpy as np

# read in data
data = np.loadtxt('2sat6.txt',skiprows=1)

# prepare the initial list for size reduction
init = []
for i in range (0,np.size(data)/2):
    init.append(data[i])

# run the preprocessing program multiple times to reduce the size of clauses to the mimimum.
for i in range(0,500):
    out = []
    PreProcessing(init,out)
    init = out
    print len(init)

# write the data out
fileout = open('2sat6_processed.txt', 'w')
nn = len(init)
s = 'Final number of clauses is     '+ str(nn)+'\n'
fileout.write(s)
for i in xrange(nn):
    s = str(init[i][0])+'      '+str(init[i][1])+'\n'
    fileout.write(s)
fileout.close()

##########################################################################
#In [89]: init
#Out[89]: 
#[array([ 95476., -15789.]),
# array([-98193.,  79715.]),
# array([ 58504.,  98193.]),
# array([-95476.,  73096.]),
# array([-79715., -73096.]),
# array([ 15789., -58504.])]
