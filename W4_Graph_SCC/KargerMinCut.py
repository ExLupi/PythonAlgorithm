#Following Karger's method to find a minimum cut of a graph
#No randomization used in the GraphCut subroutine. However we run it multiple times to find a min of the GraphCut
#Emma Yu June 1 2014


import networkx as nx
import matplotlib.pyplot as plt
import random

# ipython -pylab  <= to test ploting in an interactive mode
G1 = nx.read_adjlist('kargerMinCut.txt')
numcut = [] # store the number of cuts for the above choices


def GraphCut(G1):    
    G = nx.MultiGraph(G1)
    while len(G) > 2:
        edges = G.edges()
        edgechosen = random.choice(edges)
        adjlist1 = G.edges(edgechosen[1])  #the adjlist of the node to be shrinked (second node chosen)
        G.remove_node(edgechosen[1])     #remove the second node chosen
        for x in adjlist1:                 #add the list removed back in, allow parallel edge, but eliminate self-loops
            if x[1] != edgechosen[0]:
                G.add_edge(edgechosen[0],x[1])
    print len(G)
    numcut.append(G.number_of_edges())
    
for x in range (0,100):
    GraphCut(G1)
    

mincut = min(numcut)
print "possible number of cut", numcut
print "mincut =", mincut

#possible number of cut [25, 21, 17, 26, 25, 20, 23, 20, 26, 24, 21, 26, 26, 17, 20, 21, 26, 20, 30, 20, 24, 32, 24, 25, 27, 20, 26, 20, 21, 20, 20, 20, 30, 24, 43, 22, 21, 21, 21, 25, 20, 21, 21, 21, 20, 24, 28, 21, 20, 22, 46, 20, 20, 26, 20, 21, 20, 30, 20, 22, 24, 21, 25, 22, 30, 23, 25, 17, 21, 48, 28, 22, 38, 20, 20, 17, 28, 22, 20, 20, 25, 30, 23, 23, 26, 26, 21, 23, 21, 22, 22, 26, 23, 21, 25, 20, 20, 20, 20, 24]
#mincut = 17
