#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:24:49 2021

@author: longlee
"""

'''
Dijkstra Algorithm
'''
import networkx as nx
import numpy as np


###test
G1 =nx.DiGraph()
G1.add_weighted_edges_from([(0,1,5)])
G1.add_weighted_edges_from([(0,2,10)])
G1.add_weighted_edges_from([(1,2,3)])
G1.add_weighted_edges_from([(1,3,9)])
G1.add_weighted_edges_from([(1,4,2)])
G1.add_weighted_edges_from([(2,1,2)])
G1.add_weighted_edges_from([(2,3,1)])
G1.add_weighted_edges_from([(3,4,4)])
G1.add_weighted_edges_from([(4,3,6)])
G1.add_weighted_edges_from([(4,0,7)])

D = [9999]*5
H = np.arange(5)
S = []
start_node = 0
D[start_node] = 0
S.append(start_node)
# Dis_dic = {}
# for node in range(5):
#     Dis_dic[node] = D[node]


while len(H) != 0:
    tmp_d = {}
    for node in range(5):
        tmp_d[node] = D[node]
    u = S[-1]
    next_nodes = list(nx.neighbors(G1,u))
    for nei in next_nodes:
        w = G1.get_edge_data(u,nei)['weight']
        if D[nei] > D[u] + w:
            D[nei] = D[u] + w
            tmp_d[nei] = D[nei]
    for node in list(tmp_d.keys()):
        if node in S:
            del tmp_d[node]
    if not bool(tmp_d):
        break
    else:
        next_node = min(zip(tmp_d.values(),tmp_d.keys()))[1]
        S.append(next_node)
        H = list(set(H) -set(S))
