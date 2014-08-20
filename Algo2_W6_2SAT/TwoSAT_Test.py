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

def TestandFlip(var, clause, assign,jud):
    nclause=np.size(clause)/2
    # set the var according to the assignment
    #print 'assignment:  '+ str(assign)
    #print  'variables read in:  '+ str(var)    
    for i in range(0,len(var)):
        if assign[i] == 0:
            var[i] = -var[i]
            #print  'variable defined by assignment:  '+ str(var)
    
    for i in range(0,nclause):
        if (clause[i,0] in var) or (clause[i,1] in var):
            jud = 1.
            #print "change jud: " + str(jud)
        else:
            #print 'problematic clause is:  '+ str(clause[i])
            jud = 0.
            #print "change jud: " + str(jud)
            # flip sign. Use a random variable to decide which one to flip.
            which=random.random()
            if which >= 0.5:
                assign[var.index(-clause[i,1])] = 1- assign[var.index(-clause[i,1])] 
            else:
                assign[var.index(-clause[i,0])] = 1- assign[var.index(-clause[i,0])]
                #print 'new assignment:  '+ str(assign)
            print ' '
            break
    print "final jud: " + str(jud)
    return
 ##########################################################################
import numpy as np
import random

# read in data
# find out how many variables we have 
clause = np.loadtxt('2sat6_processed.txt',skiprows=1)

#1-valid 2- invalid.  3 -in 4 -valid   5-in  6-in

100100


#clause = np.array([[1,2],[-1,2]])
nclause=np.size(clause)/2

origvar = []
repeat = 0
for i in range(0,nclause):
    for j in range(0,2):
        if abs(clause[i,j]) in origvar:
            repeat = repeat +1
        else:
            origvar.append(abs(clause[i,j]))
nvar = len(origvar)        
assign = np.zeros(len(origvar))


# run the outer loop log2(n) time 
# 1 means true and 0 means false
jud = 1.  # store the result for individual iteration
valid = 1.  # store the overall result

niter = int(np.log2(nvar)+0.5)
for i in range(0,niter):
    #print i
    for i in range(0,nvar):
        assign[i]=random.random()
        if assign[i] >= 0.5:
            assign[i] = 1
        else:
            assign[i] =0
            #print assign
            
            for i in range(0, 2*nvar**2):
                var= []
                for j in range(0,nvar):  
                    var.append(origvar[j]) # can't use var = orivar or the orivar value will be changed as well
                TestandFlip(var, clause, assign, jud)
                #print assign
                print jud
                if jud == 1.:
                    print "VALID"
                    break
                
print valid

