#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:41:54 2021

@author: longlee
"""

'''
Bellman
'''
import networkx as nx
import numpy as np

###test
G1 =nx.DiGraph()
G1.add_weighted_edges_from([(0,1,7)])
G1.add_weighted_edges_from([(0,2,6)])
G1.add_weighted_edges_from([(1,3,-3)])
G1.add_weighted_edges_from([(1,4,9)])
G1.add_weighted_edges_from([(2,1,8)])
G1.add_weighted_edges_from([(2,3,5)])
G1.add_weighted_edges_from([(2,4,-4)])
G1.add_weighted_edges_from([(3,2,-2)])
G1.add_weighted_edges_from([(4,3,7)])
G1.add_weighted_edges_from([(4,0,2)])

D = [9999]*5
H = np.arange(5)
S = []
start_node = 0
D[start_node] = 0
S.append(start_node)
tmp_d = {}
for node in range(5):
    tmp_d[node] = D[node]

##Bellman_function
for iter in range(5):
    for edge in list(G1.edges):
        w = G1.get_edge_data(edge[0], edge[1])['weight']
        if D[edge[1]] > D[edge[0]] + w:
            D[edge[1]] = D[edge[0]] + w
            tmp_d[edge[1]] = D[edge[1]]

###negative_cycle
for edge in list(G1.edges):
    w = G1.get_edge_data(edge[0], edge[1])['weight']
    if D[edge[1]] > D[edge[0]] + w:
        print("exist negative cycle")
    else:
        print("no negative cycle")