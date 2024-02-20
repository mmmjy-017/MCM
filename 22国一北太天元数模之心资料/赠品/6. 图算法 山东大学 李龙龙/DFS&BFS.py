#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:27:07 2021

@author: longlee
"""
import networkx as nx
import numpy as np


###DFS
def DFS_1_Graph(G1,node_start, max_step):
    dfs = []
    cur_step = 1
    visited = {}
    stack_list = []
    visited[node_start] = '0'
    stack_list.append(node_start)
    while len(stack_list) > 0:
        cur_node = stack_list[-1]
        next_nodes = G1[cur_node].keys()  ###list(nx.neighbors(G1, node))
        if len(next_nodes) == 0: ###叶子节点要返回
            stack_list.pop()
            cur_step = cur_step - 1
        else:
            if (len(set(next_nodes)-set(visited.keys())) == 0 or cur_step > max_step):
                ###如果点都被访问过，或者迭代次数超过最大次数
                stack_list.pop()
                cur_step = cur_step - 1
            else:
                for nei in next_nodes:
                    dfs.append(nei)
                    if nei not in visited:
                        visited[nei] = cur_step
                        stack_list.append(nei)
                        cur_step = cur_step + 1
                        break
    return(dfs, visited)


def DFS_2_Graph(G1,start_node):
    DFS = []
    stack = []
    stack.append(start_node)
    seen = set()
    seen.add(start_node)
    while (len(stack) > 0):
        node = stack.pop()
        DFS.append(node)
        next_nodes = list(nx.neighbors(G1, node))
        for nei in next_nodes:
            if nei not in seen:
                stack.append(nei)
                seen.add(nei)
    return(DFS)

def BFS_Graph(G1,start_node):
    BFS = []
    queue = []
    queue.append(start_node)
    seen = set()
    seen.add(start_node)
    while (len(queue) > 0):
        node = queue.pop(0)
        BFS.append(node)
        next_nodes = G1[node]
        for nei in next_nodes:
            if nei not in seen:
                queue.append(nei)
                seen.add(nei)
    return(BFS)

##test
G_t = nx.Graph()
G_t.add_edge(0,1)
G_t.add_edge(0,2)
G_t.add_edge(1,2)
G_t.add_edge(1,3)
G_t.add_edge(2,4)
G_t.add_edge(2,3)
G_t.add_edge(3,4)
G_t.add_edge(3,5)

results_3 = DFS_1_Graph(G_t, 0, 10)
results_4 = DFS_2_Graph(G_t, 0)
result_5 = BFS_Graph(G_t,0)
