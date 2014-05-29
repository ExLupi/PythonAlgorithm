#!/usr/bin/env python

##########################################################################
# Impliment MergeSort to sort an array in O(nlog n) time
# Emma Yu May 2014
##########################################################################


#import numpy as np
#import matplotlib.pyplot as plt
#a = np.loadtxt('IntegerArray.txt')

def MergeSort(alist):

    if len(alist) > 1:
        mid = len(alist)//2
        leftlist = alist[:mid]
        rightlist = alist[mid:]

        MergeSort(leftlist)
        MergeSort(rightlist)


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

#The code jumps to here if either i or j is no longer smaller than the full size.
        while i<len(leftlist):
                alist[k]=leftlist[i]
                i=i+1
                k=k+1


        while j<len(rightlist):
                alist[k]=rightlist[j]
                j=j+1
                k=k+1

# Alist in alist out, the key is stored in the lower levels

alist = [54,26,93,17,77,31,44,55,20]
MergeSort(alist)
print(alist)

