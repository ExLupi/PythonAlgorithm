#!/usr/bin/env python

##########################################################################
# Emma Yu Aug 2014
#
##########################################################################
# A subroutin to check if the accurent asignment is valid or not.
# If valid, return jud =1.
# If not, jud = 0, and we flip one sign of the element in the false statement
# which one is randomly decided, in this case, assign would be one digit different
# from the original one.

def TestandFlip(var, clause, assign, jud):
    nclause=np.size(clause)/2
    jud = 1 # 1 means valid so far
    npass = 0
    # set the var according to the assignment
    for i in range(0,len(var)):
        if assign[i] == 0:
            var[i] = -var[i]

    for i in range(0,nclause):
        if (clause[i,0] in var) or (clause[i,1] in var):
            npass = npass+1
        else:
            jud = 0
            # flip sign. Use a random variable to decide which one to flip.
            which=random.random()
            if which >= 0.5:
                assign[var.index(-clause[i,1])] = 1- assign[var.index(-clause[i,1])] 
            else:
                assign[var.index(-clause[i,0])] = 1- assign[var.index(-clause[i,0])]
            break
##########################################################################
import numpy as np
import random

# read in data
# find out how many variables we have 
clause = np.loadtxt('2sat5_processed.txt',skiprows=1)
nclause=np.size(clause)/2

var = []
repeat = 0
for i in range(0,nclause):
    for j in range(0,2):
        if abs(clause[i,j]) in var:
            repeat = repeat +1
        else:
            var.append(abs(clause[i,j]))
nvar = len(var)        
assign = np.zeros(len(var))


# run the outer loop log2(n) time 
# 1 means true and 0 means false
jud = 0  # store the result for individual iteration
valid = 0  # store the overall result

niter = int(np.log2(nvar)+0.5)
for i in range(0,niter):
    print i
    for i in range(0,nvar):
        assign[i]=random.random()
        if assign[i] >= 0.5:
            assign[i] = 1
        else:
            assign[i] =0
            #print assign
            for i in range(0, 2*nvar**2):
                TestandFlip(var, clause, assign, jud)
                if jud > 0:
                    valid = jud
                
print valid

