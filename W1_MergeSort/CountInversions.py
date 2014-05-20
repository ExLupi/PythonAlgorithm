#!/usr/bin/env python

##################### How to run a script ########################
# (1) run the code by typing "python xxx.py" in the terminal
# (2) To make it excutable:
# chmod 755 thescript.py
# ./thescript.py
# (3)To use Ipython shell, type "ipython --pylab", start with ipython  and run with "run xxx.py"

#Be careful: Python is case sensitive - if and while
# indension matters - how to automatically setup?
# : after each statement
##################### Goal: plot, do interpolation, build a new grid #############


import numpy as np
import matplotlib.pyplot as plt



ncount = 0

def CountInversion(alist):
    global ncount #number of inversion
   
    if len(alist) > 1:
        mid = len(alist)//2
        leftlist = alist[:mid]
        rightlist = alist[mid:]

        CountInversion(leftlist)
        CountInversion(rightlist)

# We're not doing anything for the base condition.
# It will just be ignored

        i=0
        j=0
        k=0
        
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                alist[k]=leftlist[i]
                i=i+1
                k=k+1
            else:
                alist[k]=rightlist[j]
                j=j+1
                k=k+1
                ncount = ncount +len(leftlist)-i
                #print(rightlist[j], leftlist[i])
                

#The code jumps to here if either i or j is no longer smaller than the full size.
        while i<len(leftlist):
                alist[k]=leftlist[i]
                i=i+1
                k=k+1


        while j<len(rightlist):
                alist[k]=rightlist[j]
                j=j+1
                k=k+1


# Worked with all text cases. However I still have problem reading in the arrary correctly.
                
#alist = [54,26,93,17,77,31,44,55,20]
#alist=[6,5,4,3,2,1,0]
#alist=[9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 ] -56

                
#alist = np.loadtxt('IntegerArray.txt')
#alist=int(alist)
#, dtype=np.int64
f = open('IntegerArray.txt')
alist = f.readlines()
f.close()

alist = [int(i) for i in alist] # NEED TO CONVERT TO INT BEFORE COMPARISION
                                # THE NP.LOADTXT THING IS TILL NOT WORKING CORRECTLY :(

#alist=load('IntegerArray.txt')                
#alist=alist[0:5]

CountInversion(alist)
print(alist[0:10])
print(ncount)

