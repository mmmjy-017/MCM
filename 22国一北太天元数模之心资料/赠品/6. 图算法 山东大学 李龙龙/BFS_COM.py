#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:38:20 2021

@author: longlee
"""

import numpy as np
import networkx as nx
import scipy.sparse as sp
import copy

G = nx.DiGraph()


e_0 = time.time()

G.add_edge(0, 1)
G.add_edge(0, 4)
G.add_edge(0, 7)
G.add_edge(1, 2)  
G.add_edge(1, 6)
G.add_edge(1, 8)
G.add_edge(2, 0)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(4, 1)
G.add_edge(5, 3)
G.add_edge(7, 8)
G.add_edge(8, 7)


rows = [0,0,0,1,1,1,2,2,2,2,3,4,5,7,8]
cols = [1,4,7,2,6,8,0,1,3,5,4,1,3,8,7]
vals = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

n = 9


A = sp.coo_matrix((vals, (rows,cols)),shape = (n, n))

I = np.identity(n)
A = A + I
b = np.ones(n)
D = A.dot(b)
D = D.tolist()
D = D[0]

###
def BFS_M(M,Checked,V,Adj,tmp,Scc,Node):

    Flag = True
    while Flag == True:
        bfs_tmp = []
        
        # # V = np.dot(M, V)
        v_c = np.zeros((n,1))
        for i in list(Adj[tmp]):
            v_c = v_c + M[:,i]
        V = v_c
        
        Res = set(Node)-Checked

        for i in Res:
            if V[i] != 0 :
                Checked.add(i)

                bfs_tmp.append(i)

        if len(bfs_tmp) != 0:
            tmp = tmp +1
            Adj[tmp] = bfs_tmp
            Flag = True
        else:
            Flag = False
    
    return(Checked)




def Com_M(A, V_list, N):
    Com = {}
    SSC = set()
    tmp = 0
    while len(V_list) !=0:
        
        ini_node = D.index(max(D)) #V_list[0]
        v = np.zeros((N,1))
        v[ini_node] = 1
        Adj1 = {}
        Adj1[0] = [ini_node]
        v1 = np.zeros((N,1))
        v1[ini_node] = 1
        Check1 = set()
        Check1.add(ini_node)
        Check2 = set()
        Check2.add(ini_node)
        Adj2 = {}
        Adj2[0] = [ini_node]
        
        GT_bfs = BFS_M(A.T,Check1,v,Adj1,tmp = 0,Scc = SSC,Node = V_list)

        G_bfs = BFS_M(A,Check2,v1,Adj2,tmp = 0,Scc = SSC,Node = V_list)
        
        com = GT_bfs.intersection(G_bfs)
        
        for ide in com:
            D[ide] = 0
            
        SSC = SSC|com
        Com[tmp] = com
        tmp = tmp + 1
        V_list = set(V_list)-com
        
    return(Com,tmp)

t1 = time.time()
V_l = set(np.arange(n))#创建点列表
TT = Com_M(A,V_l,n)
Com_1 = TT[0]

Com_3= list(nx.kosaraju_strongly_connected_components(G))

Com_4 = list(nx.strongly_connected_components(G))
