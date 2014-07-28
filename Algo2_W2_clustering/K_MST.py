#!/usr/bin/env python

##########################################################################
# Emma Yu July 2014
# K-clustering algorithm (same as Krugal's MST algorithm)
# Speed the code up with union find data structure
##########################################################################

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_edgelist('clustering1.txt', data=(('weight',float),))
T=nx.minimum_spanning_tree(G)
print(sorted(T.edges(data=True)))
