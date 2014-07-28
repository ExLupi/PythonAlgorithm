#!/usr/bin/env python

##########################################################################
# Emma Yu July 2014
# Finding Minimum Spanning Tree (MST) with Prim's greedy algorithms
# Speed the code up with heaps
##########################################################################

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import choice

# read in edge list with weight
G = nx.read_edgelist('edges.txt', data=(('weight',float),))

# To store the total cost
n = 0 

# create a graph to store the node explored
X=nx.Graph()

#randomly choose a node to start from   
firstnode = choice(G.nodes()) 
X.add_node(firstnode)

# Let's first do it through a brute-force way:

for v in G.nodes()
    if v is not in X.nodes()
    

# define a list then turn it into a heap
#h = []
# Iterate over nodes, find the local mininum in the crossing edge, and push that into a heap

#Set up the initial condition 
#for v in G.nodes():
#    if v != X.nodes():
#        for j in G.neighbors(i): 
#    heappush(h,(weight, the other vertex))


