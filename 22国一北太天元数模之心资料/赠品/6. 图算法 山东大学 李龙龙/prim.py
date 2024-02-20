#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:19:23 2021

@author: longlee
"""

'''
Prim
'''
import networkx as nx
import numpy as np
import copy

###test
G1 =nx.Graph()
G1.add_weighted_edges_from([(0,1,93)])
G1.add_weighted_edges_from([(0,2,107)])
G1.add_weighted_edges_from([(0,3,63)])
G1.add_weighted_edges_from([(0,9,187)])
G1.add_weighted_edges_from([(1,2,633)])
G1.add_weighted_edges_from([(2,8,998)])
G1.add_weighted_edges_from([(3,4,108)])
G1.add_weighted_edges_from([(4,5,152)])
G1.add_weighted_edges_from([(5,6,123)])
G1.add_weighted_edges_from([(6,7,136)])
G1.add_weighted_edges_from([(6,8,843)])
G1.add_weighted_edges_from([(7,9,126)])
G1.add_weighted_edges_from([(8,9,86)])
###initialization
n = 10
D = [9999]* n
H = list(np.arange(n))
S = []
start_node = 0
D[start_node] = 0

tmp_d = {}
for node in range(n):
    tmp_d[node] = D[node]

###prim_function
Node_set = set()

Check_edge = []
Node_set.add(start_node)

while len(Check_edge) != 9:

    ###集合的邻居
    Nei = copy.deepcopy(Node_set)
    for node in Node_set:
        Nei = Nei|set(nx.neighbors(G1, node))
    Nei = Nei.difference(Node_set)

    ###判断重边
    Nei_edges = []
    for nei in Nei:
        for node in list(nx.neighbors(G1, nei)):
            edge = {nei,node}

            if node in Node_set:
                Nei_edges.append(edge)

    ###找出最小的边和下一次搜寻的点
    Edge_set = {}
    for edge in Nei_edges:
        edge = list(edge)
        w = G1.get_edge_data(edge[0], edge[1])['weight']
        Edge_set[(edge[0],edge[1])] = w  ###添加边的权重
    tup = min(zip(Edge_set.values(),Edge_set.keys()))###最小权重的点
    for node in list(tup[1]):
        if node not in Node_set:
            next_node = node
    tmp_d[next_node] = tup[0]

    ###添加判断后的边和点
    for edge in Nei_edges:   ###list(nx.neighbors(G1, next_node)):
        edge = list(edge)
        if G1.get_edge_data(edge[0], edge[1])['weight'] == tup[0]:
            edge = {edge[0],edge[1]}
            Check_edge.append(edge)
    Node_set.add(next_node)

# prim_function
def prim_function(Check_edge,Node_set,n,tmp_d):

    while len(Check_edge) != n-1:

        ###集合的邻居
        Nei = copy.deepcopy(Node_set)
        for node in Node_set:
            Nei = Nei|set(nx.neighbors(G1, node))
        Nei = Nei.difference(Node_set)

        ###判断重边
        Nei_edges = []
        for nei in Nei:
            for node in list(nx.neighbors(G1, nei)):
                edge = {nei,node}
                if node in Node_set:
                    Nei_edges.append(edge)

        ###找出最小的边和下一次搜寻的点
        Edge_set = {}
        for edge in Nei_edges:
            edge = list(edge)
            w = G1.get_edge_data(edge[0], edge[1])['weight']
            Edge_set[(edge[0],edge[1])] = w  ###添加边的权重
            tup = min(zip(Edge_set.values(),Edge_set.keys()))###最小权重的点
        for node in list(tup[1]):
            if node not in Node_set:
                next_node = node
        tmp_d[next_node] = tup[0]

        ###添加判断后的边和点
        for edge in Nei_edges:   ###list(nx.neighbors(G1, next_node)):
            edge = list(edge)
            if G1.get_edge_data(edge[0], edge[1])['weight'] == tup[0]:
                edge = {edge[0],edge[1]}
                Check_edge.append(edge)
        Node_set.add(next_node)
        return(Check_edge,tmp_d)

results = prim_function(Check_edge, Node_set, 10, tmp_d)
