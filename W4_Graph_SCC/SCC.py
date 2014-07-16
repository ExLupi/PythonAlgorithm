import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_edgelist('SCC.txt',create_using=nx.DiGraph())


#len(G)    875714 number of nodes
#G.size()  5105043  <= remember to read in as a directed graph, or not gonna match
