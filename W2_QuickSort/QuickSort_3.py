#!/usr/bin/env python

##########################################################################
#Emma Yu May 19 2014 
#Goal: Inplement quick sort and count the number of comparisions
#For an array of m elements, (m-1) comparisons, etc.

#Explore three different pivoting rules
#(1) Always use the first element of the array as the pivot element.
#(2) Always use the final element of the given array as the pivot element
#(3) I haven't read it yet.
##########################################################################


ncompare = 0

import numpy as np
import matplotlib.pyplot as plt

def QuickSort(alist):
    global ncompare

    if len(alist) > 1:
        if  (len(alist)//2)*2 == len(alist):
            pivotm = alist[len(alist)//2-1]
            mm = len(alist)//2-1
        else:
            pivotm = alist[len(alist)//2]
            mm = len(alist)//2
        pivotf = alist[0]
        pivotl = alist[len(alist)-1]  #case 3, choose the middle number amoung the first, last, and middle elements as pivot.
        
        # Sort the three possible pivots and find the middle one
        if (pivotf > pivotl) and (pivotf > pivotm):
            if pivotl > pivotm:
                pivot = pivotl
                alist[len(alist)-1]=alist[0]
                alist[0] = pivot
            else:
                pivot= pivotm
                alist[mm] = alist[0]
                alist[0] = pivot

        if (pivotl > pivotm) and (pivotl > pivotf):
            if pivotm > pivotf:
                pivot = pivotm
                alist[mm]=alist[0]
                alist[0] = pivot
            else:
                pivot= pivotf

        if (pivotm > pivotl) and (pivotm > pivotf):
            if pivotl > pivotf:
                pivot = pivotl
                alist[len(alist)-1]=alist[0]
                alist[0] = pivot
            else:
                pivot= pivotf
        
        #rearrange, then fed the new arrays to the next level
        i=1
        alist, i = Partition(alist, i)

        #print i
        llist = alist[:i-1]
        rlist = alist[i:]

        #print 'llist=',llist
        QuickSort(llist)
        #print 'rlist=',rlist
        QuickSort(rlist)


#Always swap the pivot into the first position before doing the Partition        
def Partition(list, i):
    global ncompare
    l=0
    pivot = list[l]
    i= l + 1
    nlist = len(list)       
    for j in range (l+1,nlist):
        ncompare = ncompare + 1
        if list[j] < list[0]:
            temp = list[j]
            list[j] = list[i]
            list[i] = temp
            i = i+1
            
    #print "in the subroutine", i
    list[0] = list[i-1]  #Swap the pivot into the right position
    list[i-1] = pivot
    #print 'after partition', list
    #print 'ncompare =', ncompare
    return list, i


#alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#QuickSort(alist)
#print alist 
#print ncompare

#alist = np.loadtxt('IntegerArray.txt')
#alist=int(alist)
#, dtype=np.int64

f = open('QuickSort.txt')
alist = f.readlines()
f.close()
alist = [int(i) for i in alist] # NEED TO CONVERT TO INT BEFORE COMPARISION
                                # THE NP.LOADTXT THING IS TILL NOT WORKING CORRECTLY :(
QuickSort(alist)
print ncompare


#The algorithm works, even though the final alist is not updated correctly ?!
# (1) 162085
# (2) 164123
